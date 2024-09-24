import uuid
import random
import requests

def GetCookies():
    new_uuid = str(uuid.uuid4()).replace('-', '')    
    sid_tt = f"sid_tt={new_uuid[:16]}; "
    sessionid = f"sessionid={new_uuid}; "
    sessionid_ss = f"sessionid_ss={new_uuid}; "    
    url =f'https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=19&iid='+str(random.randint(30000, 79999))+'&device_id='+str(random.randint(30000, 79999))+'&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=310503&version_name=31.5.3&device_platform=android&os=android&ab_version=31.5.3&ssmix=a&device_type=Infinix+X6816&device_brand=Infinix&language=ar&os_api=30&os_version=11&openudid=3293d1a6e9361cb7&manifest_version_code=2023105030&resolution=720*1568&dpi=303&update_version_code='+str(random.randint(80, 99))+'&_rticket=1722418820230&is_pad=0&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi5g&uoo=0&op_region=IQ&timezone_offset=10800&build_number=31.5.3&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=ar%2C&ts=1722418819&cdid=556d8162-2721-4760-a509-a92b3cf27738&support_webview=1&cronet_version=2fdb62f9_2023-09-06&ttnet_version=4.2.152.11-tiktok&use_store_region_cookie=1'    
    try:
        cookies = requests.get(url).cookies.get_dict()
        msToken = cookies.get('msToken', '')
        odin_tt = cookies.get('odin_tt', '92f5b95e015f0a43017b79d61e45d094887adf0450dbfb3e0ce465874c190014bbebf5500449add10f44a7247ef20abf6828dcdd5e38e5ca376af4262d9f822e8ab9dc2c22ec4cabbf631e709864c794')
        store_idc = cookies.get('store-idc', '')
        tt_target_idc = cookies.get('tt-target-idc', '')
        
        responses = requests.get('https://www.tiktok.com/login')
        coo = responses.cookies.get_dict()
        tt_csrf_token = coo.get('tt_csrf_token', 'Not found')
        ttwid = coo.get('ttwid', 'Not found')
    except Exception as e:
        print(e)
        print("Turn VPN")
        return {}
    
    return {
        "Cookie": 
        "passport_csrf_token=" + tt_csrf_token + ";" +
        "passport_csrf_token_default=" + tt_csrf_token + ";" +
        sid_tt +
        sessionid +
        sessionid_ss +
        "msToken=" + msToken + "; " +
        "odin_tt=" + odin_tt + "; " +
        "store-idc=" + store_idc + "; " +
        "tt-target-idc=" + tt_target_idc + "; " +
        "ttwid=" + ttwid + "; " +
        sessionid_ss,
    }
