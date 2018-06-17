#TODO:  6/17 Goal is to take learnings from first tutorial and read in something, print to console
#TODO:  6/17 mid is throwing this error:  "TypeError: must be str, not NoneType", was v22 before that throwing the erro
#TODO:  6/17 evar9 returns as none on HP why?  it should be "homepage" - this is prev.page, so browser doesn't take into account the s.do functions

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
from time import sleep
import requests, bs4

target_url = 'https://www.kohls.com'

def pagehits(url):
    global HTML_string
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(firefox_options=options,executable_path="C:\\Python36\\Env\\PacketSniffer\\geckodriver.exe",timeout=5)
    browser.get(url)
    print("URL has been got-te-t-ed")
    sleep(1)
    print("Sleeping... because our site is slow")

    try:
        pageName = browser.execute_script("return (s.pageName);")
        v9 = browser.execute_script("return (s.evar9);")
        p17 = browser.execute_script("return (s.prop17);")
        pageURL = browser.execute_script("return (s.pageURL);")
        p18 = browser.execute_script("return (s.prop18);")
        pageType = browser.execute_script("return(s.pageType);")
        print("PageName:" + "  " + pageName)
        print("PageType:" + "  " + pageType)
        print(v9)
        print(p17)
        print(pageURL)
        print("p18:" + "  " + p18)
    except WebDriverException:
        print("Exception on {}".format(url, pageName))
    browser.quit()

pagehits(target_url)
