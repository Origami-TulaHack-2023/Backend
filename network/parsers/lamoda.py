import time

from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager


def get_feedbacks_lamoda(vendor_code: int):
	options = webdriver.FirefoxOptions()
	options.add_argument('--mute-audio')
	options.add_argument('--disable-infobars')
	options.add_argument('--disable-popup-blocking')
	options.add_argument('--disable-dev-shm-usage')
	options.set_preference('intl.accept_languages', 'en,en-US')
	browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

	browser.get('https://www.lamoda.ru/p/mp002xw0byit/shoes-salamander-botinki/#reviews-and-questions')

	time.sleep(4)
	browser.execute_script("window.scrollTo(0, 900)") 
	element = browser.find_element('xpath', '//span[@aria-label="Отзывы"]').click()
	time.sleep(2)
	browser.execute_script("window.scrollTo(0, 1400)") 
	a = True
	х = 1400
	while a:
		x = 1400
		browser.execute_script(f"window.scrollTo(0, {x+500})") 
		try:
			browser.find_element('xpath', '//div[@class="icon icon_collapse-arrow icon_direction-down icon_24 _arrow_10ljn_14 _active_10ljn_19"]').click()
		except:
			browser.find_element('xpath', '//div[@class="icon icon_collapse-arrow icon_direction-up icon_24 _arrow_10ljn_14"]').click()
			a = False

	element_div = browser.find_elements('xpath', '//div[@class="_author_1ufmy_11"]')
	element_date = browser.find_elements('xpath', '//span[@class="_date_1ufmy_16"]')
	element_description = browser.find_elements('xpath', '//div[@class="_description_1ufmy_21"]')

	result_json = []

	for i in element_div:
		
		my_dict = {"name": i.text, "text": "", "rating": "", "datetime": "", "market_place": "lamoda"}
		# Добавляем словарь в массив
		result_json.append(my_dict)

	j = 0

	for i in element_date:
		result_json[j]["datetime"] = i.text
		j += 1

	p = 0

	for i in element_description:
		result_json[p]["text"] = i.text
		p += 1

	browser.quit()
	print(result_json)

	return result_json
