from SizaGod.Gorgon import Gorgon
from SizaGod.Argus import Argus
from SizaGod.Ladon import Ladon
from urllib.parse import urlencode
import time
from SizaGod.tiktok import device_register
import requests
import time
import random
from SizaGod.TikTokAg import UserAgent
from binascii import hexlify
from random import randbytes
from uuid import uuid4
from SizaGod.CookiesTik import GetCookies

Mahos = UserAgent()
agent = Mahos['User-Agent']
brand = Mahos['brand']
type = Mahos['type']

    
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "v04.04.05-ov-android", sdk_version: int = 134744640, platform: int = 0, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix: unix = int(time.time())
    
        return Gorgon(params, unix, payload, cookie).get_value() | { 
            "x-ladon"   : Ladon.encrypt(unix, license_id, aid),
            "x-argus"   : Argus.get_sign(params, x_ss_stub, unix,
                platform        = platform,
                aid             = aid,
                license_id      = license_id,
                sec_device_id   = sec_device_id,
                sdk_version     = sdk_version_str, 
                sdk_version_int = sdk_version
            )
        }
        




def base_params():
    tim = '{:.0f}'.format(time.time() * 1000)
    data = device_register()
    try:
      did = data['device_id']
    except:
      did = '73' + ''.join(random.choices('0123456789', k=16)),
    try:
      iid = data['install_id']
    except:
      iid = '73' + ''.join(random.choices('0123456789', k=16)),
    try:
      udid = data['openudid']
    except:
      udid = hexlify(randbytes(8)).decode()
    try:
      cdid = data['cdid']
    except:
      cdid = str(uuid4())
    
    
    
    return {
        
  'passport-sdk-version': "19",
  'iid': iid,
  'device_id': did,
  'ac': "mobile",
  'channel': "googleplay",
  'aid': "1233",
  'app_name': "musical_ly",
  'version_code': "310503",
  'version_name': "31.5.3",
  'device_platform': "android",
  'os': "android",
  'ab_version': "31.5.3",
  'ssmix': "a",
  'device_type': type,
  'device_brand': brand,
  'language': "ar",
  'os_api': "30",
  'os_version': "11",
  'openudid': udid,
  'manifest_version_code': "2023105030",
  'resolution': "1080*2220",
  'dpi': "440",
  'update_version_code': "2023105030",
  '_rticket': tim,
  'is_pad': "0",
  'app_type': "normal",
  'sys_region': "CA",
  'mcc_mnc': "42103",
  'timezone_name': "Asia/Aden",
  'app_language': "en",
  'carrier_region': "CA",
  'ac2': "lte",
  'uoo': "1",
  'op_region': "CA",
  'timezone_offset': "10800",
  'build_number': "31.5.3",
  'host_abi': "arm64-v8a",
  'locale': "en",
  'region': "CA",
  'ts': str(int(time.time())),
  'cdid': cdid,
  'support_webview': "1",
  'cronet_version': "2fdb62f9_2023-09-06",
  'ttnet_version': "4.2.152.11-tiktok",
  'use_store_region_cookie': "1"

    }
     



def killman():    
    headers = {
        'User-Agent': agent,
        'sdk-version': "2",
        'passport-sdk-version': "19",
        'x-tt-dm-status': "login=0;ct=0;rt=7",
        'x-vc-bdturing-sdk-version': "2.3.3.i18n",
        'x-tt-store-region': "ye",
        'x-tt-store-region-src': "did",
        'x-ss-dp': "1233",
        'x-khronos': str(int(time.time())),
        'Cookie': GetCookies()['Cookie'],
    }   
    headers.update(sign(urlencode(base_params())))

    return headers



