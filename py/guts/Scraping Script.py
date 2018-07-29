
#TODO:  180617_10 make browser dynamic
#TODO:  180617_11 in pagehits Fx, should do a on DOM COMPLETE check before running other functions
#TODO:  180617_13 In for loop under pagehits, should have a mechanism to check if the prop exists.  i.e. there's no prop0, but it returns blank... differentiate from NOT PRESENT and ACTUAL BLANK
    #might be able to do this using the Omniture API (what vars do you actually have active... etc.
#TODO:  180618_15 figure out how to set headless for Chrome
#TODO:  180617_14 POST requests time out - is this due to query string?  not reproducing thus far:  6/18/18
#TODO:  180618_17 Should handle SSL certificates gracefully at some point - will need to find my certificates on the computer - requests package looks like it can handle this well
    #https://stackoverflow.com/questions/18061640/ignore-certificate-validation-with-urllib3  Could switch between HTTPSConnectionPool and PoolManager
    #HACK:  https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho
#TODO:  180623_19 get chrome to work
#TODO:  180623_20 Rather than try except, for non critical errors, I could log them
#TODO:  180623_21 Replace sleep with wait http://selenium-python.readthedocs.io/waits.html
#TODO:  180624_23 add a way to check values through a data layer (like tealium on Belk)
    #updating s_code check - if it finds utag.js, have to go into the utag code itself?  Not sure
#TODO:  180624_24 Should I use the htmlUnit driver rather than FF or Chrome default? https://www.seleniumhq.org/docs/03_webdriver.jsp#selenium-webdriver-s-
#TODO:  180624_25 SCODE check fails, src is changing from page to page.
#TODO:  180624_26 This page takes FOREVER to load https://www.kohls.com/catalog.jsp?CN=Promotions:Sale&BL=y&icid=hpmf-sale
    #Timeouts might work, but sometimes the page never finishes loading because of Ajax?
    #work on 26:  can't get dirver capabilities to work - might be syntax


print("**ACTUAL CODE...Last Commit:  6/17/2018 12:40PM")

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options #used for ff... not sure if needed?
from time import sleep #allows for waiting w/ promise
import requests #used for URL functions and validity
import urllib3 #used to kill Insecure https request warnings- should solve properly for this

print("...Import complete...")


#SET GLOBALS

TargetURL = ""
#webdriver.DesiredCapabilities(pageLoadStrategy="eager")

browser = webdriver.Firefox(executable_path="C:\\Python36\\Env\\PacketSniffer\\geckodriver.exe")
browser.get(TargetURL)


print("...Globals are set...")

####URL Testing for Errors###
def URLTest(TargetURL):
    try:
        #hard disable SSL warning
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        r = requests.head(TargetURL, verify=False)
        #URL Status ok?
        if r.status_code ==200 or 301 or 302:
            print("STATUS OK:  "+str(r.status_code))
        else:
            print("STATUS NOT 200:  " + str(r.status_code))
            return quit()
    except requests.exceptions.RequestException as e:
        print("GET ENCOUNTERED A FAILURE\n"+str(e)), quit()


def StandardCodeChecks():
    #check for cookie, if not, quit.  Should build if cookie changes as well
        #maybe do this dynamically so cookie name doesn't have to be manually set?
    if browser.get_cookie("") !=None:
        VisitorCookie =browser.get_cookie("")
        print("...Cookie Was Found...")
    else:
        print("COOKIE NOT FOUND!\n")
        #quit()
    #check for presence of s_code.js, (this only works without data layer or DTM update later)
    #doesn't work on pages other than HP
    # if len(browser.find_elements_by_xpath("//script[@type='text/javascript' and @src='/snb/media/omniture/s_code.js']"))>0:
    #     print("ElementExists")
    # else:
    #     print("ElementDoesntExist")
    #     return
def ScriptExecution(SVarStr):
    SVarVal = browser.execute_script("return ("+"s."+SVarStr+");")
    if SVarVal == None:
        nothing=0
    elif SVarVal =="":
        print(SVarStr+":"+"    NotSetYet")
    else:
        print(SVarStr+":"+"  "+SVarVal)
    return SVarVal

def PullData(url):
    browser.get(url)
    sleep(1)
    print("...Site is loading... ")

    #RUN STANDARD CHECKS FOR ADOBE CODE
    StandardCodeChecks()

    try:
        print("********ScriptExecution*******")
        ScriptExecution("pageName")
        ScriptExecution("products")
        for i in range(0, 15, 1):
            ScriptExecution("prop"+str(i))
            ScriptExecution("eVar" + str(i))

    except WebDriverException:
        print("WebDriver Exception on {}".format(url))
    #browser.quit()


URLTest(TargetURL)
PullData(TargetURL)

print("\nEND OF CODE")
