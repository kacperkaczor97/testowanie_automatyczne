from selenium import webdriver

import logging



logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Firefox(executable_path='C:\Drivers\geckodriver.exe)

logger.info('Przejscie na stronę Plan Zajęć PJATK')
driver.get('https://planzajec.pjwstk.edu.pl/')
logger.info('Przejscie do logowanie')
temp = driver.find_element_by_link_text('Twój plan zajęć')
temp.click()
logger.info('Wprowadzenie Danych')
temp = driver.find_element_by_name('ctl00$ContentPlaceHolder1$Login1$UserName').send_keys('s16587')
temp = driver.find_element_by_name('ctl00$ContentPlaceHolder1$Login1$Password').send_keys('Haslo123')
logger.info('Zatwierdzenie')
temp = driver.find_element_by_name('ctl00$ContentPlaceHolder1$Login1$LoginButton')
temp.click()
# nie chce podawac Panu moich danych logowanie, ale jeżeli poda sie właściwe to działa

driver.close()