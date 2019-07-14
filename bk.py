#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import datetime
import argparse
import threading
import os
import platform

from typing import List
from typing import Union

def select_radio(browser: webdriver, id: int):
    elem = browser.find_element_by_xpath("(//*[@class='radioSimpleInput'])[{}]".format(id))
    elem.click()


def select_checkbox(browser: webdriver, id: int):
    elem = browser.find_element_by_xpath("(//*[@class='checkboxSimpleInput'])[{}]".format(id))
    elem.click()


def select_column_radio(browser: webdriver, id: int, nb_cols: int, nb_rows: int):
    for i in range(nb_rows):
        select_radio(browser, id + i * nb_cols)


def next_page(browser: webdriver):
    elem = browser.find_element_by_id('NextButton')  # Find the button
    elem.click()

def completion_process(n: int, quit: bool, driver_web: webdriver) -> Union[str, None]:

    browser = driver_web()
    
    for _ in range(n):
        browser.get("https://www.bk-feedback-uk.com")
    
        elem = browser.find_element_by_id('NextButton')  # Find the button
        elem.click()
    
        elem = browser.find_element_by_id('SurveyCode')
        elem.send_keys('23745')
    
        #we fill the date
        time = datetime.datetime.now()
        time = time - datetime.timedelta(days=7)
    
        select = Select(browser.find_element_by_id("InputDay"))
        select.select_by_value("{:02}".format(time.day))
    
        select = Select(browser.find_element_by_id("InputMonth"))
        select.select_by_value("{:02}".format(time.month))
    
        select = Select(browser.find_element_by_id("InputHour"))
        select.select_by_value('12')
    
        select = Select(browser.find_element_by_id("InputMinute"))
        select.select_by_value('{:02}'.format(time.minute))
    
        select = Select(browser.find_element_by_id("InputMeridian"))
        select.select_by_value("AM")
    
        next_page(browser)
        next_page(browser)
        next_page(browser)
    
        select_radio(browser, 2)
        next_page(browser)
    
        select_radio(browser, 3)
        next_page(browser)
    
        select_radio(browser, 4)
        next_page(browser)
    
        select_radio(browser, 2)
        next_page(browser)
    
        select_radio(browser, 1)
        next_page(browser)
    
        select_column_radio(browser, 1, 5, 5)
        next_page(browser)
    
        select_column_radio(browser, 1, 5, 5)
        next_page(browser)
    
        #select_column_radio(browser, 1, 5, 2)
        #next_page(browser)
    
        select_radio(browser, 1)
        # il y a des fois deux des fois une seule
        try:
            select_radio(browser, 6)
        except NoSuchElementException:
            pass
        next_page(browser)
    
        select_column_radio(browser, 1, 6, 2)
        next_page(browser)
    
        select_radio(browser, 2)
        next_page(browser)
    
        select_column_radio(browser, 1, 5, 2)
        next_page(browser)
    
        next_page(browser)
    
        #select_checkbox(browser, 18)
        elem = browser.find_element_by_id("FNSR000091").find_element_by_class_name("checkboxSimpleInput")
        elem.click()
        next_page(browser)
    
        select_checkbox(browser, 11)
        next_page(browser)
    
        # we establish a delay because the page takes too long to load
        # we wait for the radioSimpleInput to appear on the page
        try:
            elem = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'radioSimpleInput')))
        except TimeoutException:
            print("The page takes too long to load")
    
        select_radio(browser, 1)
        next_page(browser)
    
        select_radio(browser, 2)
        next_page(browser)
    
        select_radio(browser, 1)
        next_page(browser)
    
        try:
            select_radio(browser, 1)
            next_page(browser)
        except NoSuchElementException:
            pass
    
        select = Select(browser.find_element_by_id("R069000"))
        select.select_by_value('9')
        select = Select(browser.find_element_by_id("R070000"))
        select.select_by_value('9')
        select = Select(browser.find_element_by_id("R074000"))
        select.select_by_value('9')
        next_page(browser)
    
        #select = Select(browser.find_element_by_id("R074000"))
        #select.select_by_value('9')
        #next_page(browser)
    
        elem = browser.find_element_by_id('S076000')
        elem.send_keys('69000')
        next_page(browser)
    
        try: 
            elem = browser.find_element_by_class_name('ValCode')
            return elem.text
            #print(elem.text)
        except NoSuchElementException:
            print("\u001b[31mValidation Code FAILED\u001b[0m")
            return None

    if quit:
        browser.quit()


def completion_normal(n: int, quit: bool, driver_web: webdriver, codes: List[str]):
    result = completion_process(n, quit, driver_web)
    if result is not None:
        codes.append(result)


def completion_assured(n: int, quit: bool, driver_web: webdriver, codes: List[str]):
    result = completion_process(n, quit, driver_web)
    while (result is None) or result in codes:
        result = completion_process(n, quit, driver_web)
    
    codes.append(result)


def main():
    # We add the browser drivers to the PATH
    system = platform.system()
    if system == "Windows":
        subdir = "win64"
    elif system == "Linux":
        subdir = "lnx64"
    else:
        print("The system ", system, "is not supported")

    drivers_path = os.path.join(os.getcwd(), "drivers", subdir)
    os.environ["PATH"] += os.pathsep + drivers_path

    # Gestion et parsing des arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--quit', help='Quit when the program is finished.', action="store_true")
    parser.add_argument('-N', '--Niterations', help='The number of iterations of the script in one browser.', type=int)
    parser.add_argument('-Np', '--NParaIterations', help='The number of iterations in parallel aka the number of browsers in parallel.', type=int)
    parser.add_argument('-Nc', '--NCodes', help='The number of unqiue codes that the user wants at the end. Relaunches the script until this number is reached. This option is incompatible with -N and -Np', type=int)
    parser.add_argument('-c', '--chrome', help="Launch the script with the chrome browser", action="store_true")
    parser.add_argument('-f', '--firefox', help="Launch the script with the firefox browser", action="store_true")
    parser.add_argument('-o', '--opera', help="Launch the script with the opera browser", action="store_true")
    args = parser.parse_args()

    if args.NCodes is not None and ((args.Niterations is not None) or (args.NParaIterations is not None)):
        print("The Nc option is incompatible with N or Np")
        exit()

    N = args.Niterations if args.Niterations is not None else 1
    Np = args.NParaIterations if args.NParaIterations is not None else (args.NCodes if args.NCodes is not None else 1)

    if args.chrome:
        driver_web = webdriver.Chrome
    elif args.opera:
        driver_web = webdriver.Opera
    elif args.firefox:
        driver_web = webdriver.Firefox
    else:
        driver_web = webdriver.Firefox 
    
    threads = []
    codes = []
    for _ in range(Np):
        if args.NCodes is not None:
            thread = threading.Thread(target=completion_assured, args=(N, args.quit, driver_web, codes))
        else:
            thread = threading.Thread(target=completion_normal, args=(N, args.quit, driver_web, codes))
        threads.append(thread)
        thread.start()

    for j in range(Np):
        threads[j].join()

    for c in codes:
        print(c)

if __name__ == "__main__":
    main()
    if platform.system() == "Windows":
       os.system("pause")