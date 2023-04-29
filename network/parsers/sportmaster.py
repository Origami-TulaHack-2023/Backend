import cfscrape
from bs4 import BeautifulSoup

import requests
import re


def format_str(string: str) -> str:
    string = re.sub(r"[\n\t\s]", " ", string)
    return re.sub(" +", " ", string)[1:-1]


AUTH_TOKEN = "56fa337b8ddf870c76021a5f"


def get_data(vendor_code: str):
    total_feedbacks = []
    n = 10
    for i in range(1, n):
        session = requests.Session()
        scraper = cfscrape.create_scraper(sess=session)
        url = f"https://w-api2.aplaut.io/widgets/{AUTH_TOKEN}/v3/product/{vendor_code}/product-reviews.html?hostname=sportmaster.ru&page={i}"
        page = scraper.get(url)

        if page.status_code != 200:
            break

        soup = BeautifulSoup(page.text, features="html.parser")
        reviews = soup.select(".sp-review")
        n = int(soup.select(".sp-pagination-item")[-2].text)

        page_feedbacks = []
        for review in reviews:
            feedback = {}
            feedback["name"] = format_str(review.select_one("[itemprop=author]").text)
            feedback["datetime"] = review.select_one(".sp-review-header-date").get(
                "datetime"
            )
            feedback["text"] = " ".join(
                format_str(review.select_one(".sp-review-body").text).split(" ")[1:]
            )
            feedback["market_place"] = "sportmaster"
            feedback["rating"] = float(
                (
                    review.select_one(".sp-review-header-rating")
                    .select_one("meta[itemprop=ratingValue]")
                    .get("content")
                )
            )
            page_feedbacks.append(feedback)
        total_feedbacks.extend(page_feedbacks)
    return total_feedbacks
