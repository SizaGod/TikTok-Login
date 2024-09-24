from SizaGod.dictionary import *
import requests

def xor(string: str) -> str:
    return "".join([hex(ord(_) ^ 5)[2:] for _ in string]) 
    
enc_em=input("Enter Your E-mail : ")
enc_ps=input("Enter Your  Password : ")
email=xor(enc_em) 
password=xor(enc_ps)

def Login():
    url = "https://api16-normal-c-alisg.tiktokv.com/passport/user/login/"
    headers = killman()
    payload = f"password={password}&account_sdk_source=app&multi_login=1&email={email}&mix_mode=1"
    params = base_params()
    response = requests.post(url, params=params, data=payload, headers=headers)
    print(response.text)
    
Login()
    