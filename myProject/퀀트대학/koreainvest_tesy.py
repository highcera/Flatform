import requests
import json
import keyring
import pandas as pd
import time
import numpy as np
import datetime
from datetime import timedelta
import schedule

# key

# 종합계좌
keyring.set_password('real_app_key', 'highcera', 'PSF4OaxrCHka4LbSMy1PIaIu71lLSWwc9gfu')
keyring.set_password('real_app_secret', 'highcera', 'r4pZyak/rMiRdH+d4u3rVahdyOFWeOsBr9YnYekyhkWDPnt+zY9RtVrF6o39ab00QHQSNC+fmVih2jzR5kauqW5GECUjx4rzzqtvL2QvdcfF7c6njITnl6ewn33PYGjZfT8d6QCTEJZRY+S7pE3KaZG1KdEbuM9c8uwM8HSplo066JOLh9s=')

# 모의계좌
keyring.set_password('mock_app_key', 'highcera', 'PSgHVNUekFYy1kOhmxyQp5TXPVgFdqM65TAk')
keyring.set_password('mock_app_secret', 'highcera', 'iILX9aLiZykbi/l3nkv6kJVk/FDm+mg9mscO7KvS2BvUGMSy/JTdv4ZEykQocERZVkl1BP9WwCaZulcU40sknzDDIJyLAKocvjA+RcDsTlh5F7KrKQwdMrFsHx9g8BK2bsIsplyzx/BD3aum5znCY90mJ2ehDeOBUPyNgGA5SxszHbZRyu0=')

app_key = keyring.get_password('mock_app_key', 'highcera')
app_secret = keyring.get_password('mock_app_secret', 'highcera')

# base url
url_base = "https://openapivts.koreainvestment.com:29443" # 모의투자

# information
headers = {"content-type": "application/json"}
path = "oauth2/tokenP"
body = {
    "grant_type": "client_credentials",
    "appkey": app_key,
    "appsecret": app_secret
}

url = f"{url_base}/{path}"

res = requests.post(url, headers=headers, data=json.dumps(body))
access_token = res.json()['access_token']

def hashkey(datas):
    path = "uapi/hashkey"
    url = f"{url_base}/{path}"
    headers = {
        'content-Type': 'application/json',
        'appKey': app_key,
        'appSecret': app_secret,
    }
    res = requests.post(url, headers=headers, data=json.dumps(datas))
    hashkey = res.json()["HASH"]

    return hashkey


# 현재가 구하기
def get_price(ticker):
    path = "uapi/domestic-stock/v1/quotations/inquire-price"
    url = f"{url_base}/{path}"

    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {access_token}",
        "appKey": app_key,
        "appSecret": app_secret,
        "tr_id": "FHKST01010100"
    }

    params = {"fid_cond_mrkt_div_code": "J", "fid_input_iscd": ticker}

    res = requests.get(url, headers=headers, params=params)
    price = res.json()['output']['stck_prpr']
    price = int(price)
    time.sleep(0.2)

    return price

# 주문
def trading(ticker, tr_id):

    path = "/uapi/domestic-stock/v1/trading/order-cash"
    url = f"{url_base}/{path}"

    data = {
        "CANO": "50093079", # 계좌번호 앞 8지리
        "ACNT_PRDT_CD": "01",
        "PDNO": ticker,
        "ORD_DVSN": "03",
        "ORD_QTY": "1",
        "ORD_UNPR": "0",
    }

    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {access_token}",
        "appKey": app_key,
        "appSecret": app_secret,
        "tr_id": tr_id,
        "custtype": "P",
        "hashkey": hashkey(data)
    }

    res = requests.post(url, headers=headers, data=json.dumps(data)) 


# 계좌 잔고 조회
def check_account():

    output1 = []
    output2 = []
    CTX_AREA_NK100 = ''

    while True:

        path = "/uapi/domestic-stock/v1/trading/inquire-balance"
        url = f"{url_base}/{path}"

        headers = {
            "Content-Type": "application/json",
            "authorization": f"Bearer {access_token}",
            "appKey": app_key,
            "appSecret": app_secret,
            "tr_id": "VTTC8434R"
        }

        params = {
            "CANO": "50093079", # 계좌번호 앞 8지리 730 / 907
            "ACNT_PRDT_CD": "01",
            "AFHR_FLPR_YN": "N",
            "UNPR_DVSN": "01",
            "FUND_STTL_ICLD_YN": "N",
            "FNCG_AMT_AUTO_RDPT_YN": "N",
            "OFL_YN": "",
            "INQR_DVSN": "01",
            "PRCS_DVSN": "00",
            "CTX_AREA_FK100": '',
            "CTX_AREA_NK100": CTX_AREA_NK100
        }

        res = requests.get(url, headers=headers, params=params)
        output1.append(pd.DataFrame.from_records(res.json()['output1']))

        CTX_AREA_NK100 = res.json()['ctx_area_nk100'].strip()

        if CTX_AREA_NK100 == '':
            output2.append(res.json()['output2'][0])
            break

    if not output1[0].empty:
        res1 = pd.concat(output1)[['pdno',
                                   'hldg_qty']].rename(columns={
                                       'pdno': '종목코드',
                                       'hldg_qty': '보유수량'
                                   }).reset_index(drop=True)
    else:
        res1 = pd.DataFrame(columns=['종목코드', '보유수량'])

    res2 = output2[0]
    return [res1, res2]

# 모델 포트폴리오
mp = pd.DataFrame({
    '종목코드': [
        '005930',  # 삼성전자
        '373220',  # LG에너지솔루션
        '000660',  # SK하이닉스
        '207940',  # 삼성바이오로직스
        '051910',  # LG화학
        '035420',  # NAVER
        '005380',  # 현대차
        '006400',  # 삼성SDI,
        '035720',  # 카카오
        '105560',  #KB금융
    ]
})

################################################################################
# 화일 종목 불러오기 - 위 mp 주석처리 후 아래 mp2-> mp로 수정 후 실행
df = pd.read_csv("C:/Users/highc/OneDrive/문서/주식론 검증/래리하이트_4주연속 신고가_230826.csv")
mp2 = df['종목코드'].apply(lambda x : x[1:]).to_frame(name='종목코드')

# for i in range(20):
#     print(get_price(mp2['종목코드'][i]))
#################################################################################

# 보유 종목과 aum 불러오기
ap, account = check_account()
# print(type(ap), ap, account)

# # 주당 투자 금액
invest_per_stock = int(account['tot_evlu_amt']) * 0.98 / len(mp2)

# 매매 구성
# target = pd.DataFrame()
target = mp2.merge(ap, on='종목코드', how='outer')
target['보유수량'] = target['보유수량'].fillna(0).apply(pd.to_numeric)

# 현재가 확인
target['현재가'] = target.apply(lambda x: get_price(x.종목코드), axis=1)
target['현재가'] = target['종목코드'].apply(lambda x: get_price(x))

# 목표수량 및 투자수량 입력
target['목표수량'] = np.where(target['종목코드'].isin(mp2['종목코드'].tolist()),
                          round(invest_per_stock / target['현재가']), 0)

target['투자수량'] = target['목표수량'] - target['보유수량']
print(target)

# 시간 분할
startDt1 = datetime.datetime.now() + timedelta(minutes=1)
startDt2 = datetime.datetime.now().replace(hour=9,minute=10,second=0,microsecond=0)
startDt = max(startDt1, startDt2)
endDt = datetime.datetime.now().replace(hour=15,minute=0,second=0,microsecond=0)

# 스케줄 초기화
schedule.clear()

# 스케줄 등록
for t in range(target.shape[0]) :
    
    n = target.loc[t, '투자수량']
    position = 'VTTC0802U' if n > 0 else 'VTTC0801U'
    ticker = target.loc[t, '종목코드']    
    
    time_list = pd.date_range(startDt, endDt, periods = abs(n))    
    time_list = time_list.round(freq = 's').tolist()    
    time_list_sec = [s.strftime('%H:%M:%S') for s in time_list]                 

    for i in time_list_sec:
        schedule.every().day.at(i).do(trading, ticker, position) 

# 스케줄 실행
try:
    while True:
        schedule.run_pending()    
        if datetime.datetime.now() > endDt :
            print('거래가 완료되었습니다.')        
            schedule.clear()
            break

except Exception as e:
    # send_message(f"[오류 발생]{e}")
    time.sleep(1)

