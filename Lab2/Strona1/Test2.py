

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
    fh = logging.FileHandler('Test2ChromeLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')

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
    fh = logging.FileHandler('Test2FirefoxLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Firefox(executable_path='C:\Drivers\geckodriver.exe')

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

else:
    print("Zła podana wartość")