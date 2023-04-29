import requests, json


def get_review(name_product: str):
    reviews = []

    url = f"https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=%2Fproduct%2Fproteinovye-batonchiki-bez-sahara-rexy-night-mini-assorti-40g-9sht-838196715%2F%3FcampaignId%3D226%26layout_container%3DpdpReviews%26layout_page_index%3D2%26sh%3DwcfpHL-axw"

    # response = requests.get(url, auth=(token))
    response = requests.get(url)
    print(response)
    json_data = response.json()
    reviews = json_data.get("reviews")

    if reviews is not None:
        return transform_feedbacks(reviews)
