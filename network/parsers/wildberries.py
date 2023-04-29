import requests, json


def get_imt_id(vendor_code: str) -> int:
    vol = vendor_code[:3]
    part = vendor_code[:5]
    for i in range(1, 12):
        basket = f"0{i}" if i < 10 else i
        url = f"https://basket-{basket}.wb.ru/vol{vol}/part{part}/{vendor_code}/info/ru/card.json"
        response = requests.get(url)
        if response.status_code != 404:
            json_data = response.json()
            imt_id = json_data.get("imt_id")
            if imt_id is not None:
                return imt_id


def transform_feedbacks(feedbacks):
    transformed = []
    for feedback in feedbacks:
        temp = {
            "name": feedback["wbUserDetails"]["name"],
            "text": feedback["text"],
            "rating": feedback["productValuation"],
            "datetime": feedback["createdDate"][:10],
            "market_place": "wildberries",
        }
        transformed.append(temp)
    return transformed


def get_feedbacks(vendor_code: int):
    imt_id = get_imt_id(vendor_code)
    feedbacks = []
    for i in range(1, 3):
        url = f"https://feedbacks{i}.wb.ru/feedbacks/v1/{imt_id}"
        response = requests.get(url)
        json_data = response.json()
        feedbacks = json_data.get("feedbacks")
        if feedbacks is not None:
            return transform_feedbacks(feedbacks)
