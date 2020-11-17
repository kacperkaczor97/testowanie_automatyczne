from selenium import webdriver
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
fh = logging.FileHandler('Test1FirefoxLog.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

driver = webdriver.Firefox(executable_path='C:\Drivers\geckodriver.exe')

logger.info('Przejscie na stronę Plan Zajęć PJATK')
driver.get('https://planzajec.pjwstk.edu.pl/')
logger.info('Przejscie do planu ogólnego')
temp = driver.find_element_by_link_text('Ogólny plan zajęć')
temp.click()
logger.info('Otwarcie listy miast')
temp = driver.find_element_by_id('WydzialComboBox_Arrow')
temp.click()
logger.info('Wybranie Gdańska')
temp = driver.find_element_by_class_name('rcbItem')
temp.click()

driver.close()