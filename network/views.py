from django.http import HttpResponse

from .parsers.wildberries import get_feedbacks
from .parsers.ozon import get_review
from .parsers.sportmaster import get_data
from .parsers.lamoda import get_feedbacks_lamoda

import json


def my_view(request):
    if request.method == "POST":
        body = request.body

        my_string = body.decode("utf-8")

        my_json_body = json.loads(my_string)
        feedbacks = []

        for vender in my_json_body:
            if vender["market_place"] == "wildberries":
                feedbacks.extend(get_feedbacks(str(vender["vendor_code"])))
            elif vender["market_place"] == "ozon":
                feedbacks.extend(get_review(str(vender["vendor_code"])))
            elif vender["market_place"] == "sportmaster":
                feedbacks.extend(get_data(str(vender["vendor_code"])))
            elif vender["market_place"] == "lamoda":
                feedbacks.extend(get_feedbacks_lamoda(str(vender["vendor_code"])))

        return HttpResponse(json.dumps(feedbacks, ensure_ascii=False))
