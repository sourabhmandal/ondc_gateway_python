import json
import os

import requests
from django.http import JsonResponse

from ondc import auth


def health(request):
    bap_pub_key = os.getenv("BAP_PUBLIC_KEY")
    bap_prv_key = os.getenv("BAP_PRIVATE_KEY")
    # print(bap_pub_key, bap_prv_key)

    auth_header = auth.create_authorisation_header(request.body.decode('UTF-8'), bap_prv_key)

    r = requests.post(
            'https://pilot-gateway-1.beckn.nsdl.co.in/search', 
            json=json.dumps(request.body.decode('UTF-8'))
        )
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    r.headers["Authorization"] = auth_header
    data = r.json()

    print(r.headers)
    return JsonResponse(data)
