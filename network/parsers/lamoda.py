from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from django.conf import settings
from django.http import HttpResponse

from xvfbwrapper import Xvfb

import time, os, json


def get_feedbacks_lamoda(vendor_code: int):
	vdisplay = Xvfb()
	vdisplay.start()
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome(executable_path=os.path.join(settings.BASE_DIR, 'chromedriver'), options=chrome_options)
	driver.get('https://www.lamoda.ru/p/mp002xw0byit/shoes-salamander-botinki/#reviews-and-questions')
	print('hello1')
	time.sleep(4)
	driver.execute_script("window.scrollTo(0, 1800)") 
	driver.find_element('xpath', "//span[@aria-label='Отзывы']").click()
	time.sleep(2)
	driver.execute_script("window.scrollTo(0, 2000)") 
	a = True
	х = 2000
	while a:
		x = 2000
		driver.execute_script(f"window.scrollTo(0, {x+500})") 
		try:
			driver.find_element('xpath', '//div[@class="icon icon_collapse-arrow icon_direction-down icon_24 _arrow_10ljn_14 _active_10ljn_19"]').click()
		except:
			try:
				driver.find_element('xpath', '//div[@class="icon icon_collapse-arrow icon_direction-up icon_24 _arrow_10ljn_14"]').click()
				a = False
			except:
				pass

	element_div = driver.find_elements('xpath', '//div[@class="_author_1ufmy_11"]')
	element_date = driver.find_elements('xpath', '//span[@class="_date_1ufmy_16"]')
	element_description = driver.find_elements('xpath', '//div[@class="_description_1ufmy_21"]')

	result_json = []

	for i in element_div:
		my_dict = {"name": i.text, "text": "", "rating": 4, "datetime": "", "market_place": "lamoda"}
		result_json.append(my_dict)

	j = 0

	for i in element_date:
		result_json[j]["datetime"] = i.text
		j += 1

	p = 0

	for i in element_description:
		result_json[p]["text"] = i.text
		p += 1

	driver.execute_script("window.scrollTo(0, 0)") 
	driver.quit()
	vdisplay.stop()
	
	return result_json
