import base64
import json
from datetime import datetime

import requests
from pip._vendor.requests.auth import HTTPBasicAuth


class MpesaC2bCredential:
    consumer_key = '08D8DOOqB9hMUkajAAzZpl4WaQ92peAoCGTEUGuhd6stKeGM'
    consumer_secret = '7lk21ELNDXCpGZ9DJ2F3advtAEItdBb7WB3ycf9WIkvVcbuMv3GT4eZX7d5EToUN'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')