# Installation
# python -m pip install requests

# Request
import requests

url = "https://api-sbox.dnlsrv.com/cigateway/id/v1/phoneIdUrl"

payload = {
    "merchantId": "02200013919FB4",
    "consentId": "9783471AFDB69NH34",
    "consentTimeStamp": "2020-08-20T12:00:57+00:00",
    "consumerMdn": "+14085040458",
    "correlationId": "244464DFCB537E56",
    "consumerDeviceIP": "213.27.12.111",
    "consumerDeviceUA": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "air": False,
    "redirectUrl": "https://MerchantSite/Redirect"
}
headers = {
    "Authorization": "sha512-OrXJ9cUS2ZeapEbLBiONVK/eQtBwF1Mi7z2Zg9jNB9g71zvGSBXHqqhwfrfTD9WiNT+FIKOPvjToU/nhjml6Mw==?E5No",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "RequestTime": "2022-08-01T09:33:43+00:00"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
