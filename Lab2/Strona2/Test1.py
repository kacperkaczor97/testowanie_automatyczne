

print("Aby uruchomić Test w Chrome wybierz 1")
print("Aby uruchomić Test w Firefox wybierz 2")
print("Aby uruchomić Test w Opera wybierz 3")

web = input("Podaj którą przeglądarke chcesz wybrać: ")
print(f"Wybrales {web}".format(web=web))

if web == "1":

    from selenium import webdriver
    import logging

    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fh = logging.FileHandler('Test1ChromeLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')

    logger.info('Przejscie na stronę OLX')
    driver.get('https://www.olx.pl/')
    logger.info('Akceptacja Cookie')
    temp = driver.find_element_by_id('onetrust-accept-btn-handler')
    temp.click()
    logger.info('Przejscie do okna logowania')
    temp = driver.find_element_by_id('topLoginLink')
    temp.click()
    logger.info('Wpisz dane logowania')
    temp = driver.find_element_by_id('userEmail').send_keys('willena6@yiustrange.com')
    temp = driver.find_element_by_id('userPass').send_keys('Haslo!23$')
    logger.info('Zatwierdz logowanie')
    temp = driver.find_element_by_id('se_userLogin')
    temp.click()
    logger.info('Jestes zalogowany')

    driver.close()

elif web == "2":
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

    logger.info('Przejscie na stronę OLX')
    driver.get('https://www.olx.pl/')
    logger.info('Akceptacja Cookie')
    temp = driver.find_element_by_id('onetrust-accept-btn-handler')
    temp.click()
    logger.info('Przejscie do okna logowania')
    temp = driver.find_element_by_id('topLoginLink')
    temp.click()
    logger.info('Wpisz dane logowania')
    temp = driver.find_element_by_id('userEmail').send_keys('willena6@yiustrange.com')
    temp = driver.find_element_by_id('userPass').send_keys('Haslo!23$')
    logger.info('Zatwierdz logowanie')
    temp = driver.find_element_by_id('se_userLogin')
    temp.click()
    logger.info('Jestes zalogowany')

    driver.close()

elif web == "3":
    from selenium import webdriver
    import logging

    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fh = logging.FileHandler('Test1OperaLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Opera(executable_path='C:\Drivers\operadriver.exe')

    logger.info('Przejscie na stronę OLX')
    driver.get('https://www.olx.pl/')
    logger.info('Akceptacja Cookie')
    temp = driver.find_element_by_id('onetrust-accept-btn-handler')
    temp.click()
    logger.info('Przejscie do okna logowania')
    temp = driver.find_element_by_id('topLoginLink')
    temp.click()
    logger.info('Wpisz dane logowania')
    temp = driver.find_element_by_id('userEmail').send_keys('willena6@yiustrange.com')
    temp = driver.find_element_by_id('userPass').send_keys('Haslo!23$')
    logger.info('Zatwierdz logowanie')
    temp = driver.find_element_by_id('se_userLogin')
    temp.click()
    logger.info('Jestes zalogowany')

    driver.close()
else:
    print("Zła podana wartość")