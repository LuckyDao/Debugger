
#TODO:  180617_10 make browser options choosable
#TODO:  180618_15 figure out how to set headless for Chrome
#TODO:  180618_17 Should handle SSL certificates gracefully at some point - will need to find my certificates on the computer - requests package looks like it can handle this well
    #https://stackoverflow.com/questions/18061640/ignore-certificate-validation-with-urllib3  Could switch between HTTPSConnectionPool and PoolManager
    #HACK:  https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho
#TODO:  180623_19 get chrome to work
#TODO:  180623_20 Rather than try except, for non critical errors, I could log them
#TODO:  180623_21 Replace sleep with wait http://selenium-python.readthedocs.io/waits.html
#TODO:  180624_23 add a way to check values through a data layer (like tealium on Belk)
    #updating s_code check - if it finds utag.js, have to go into the utag code itself?  Not sure
#TODO:  180624_24 Should I use the htmlUnit driver rather than FF or Chrome default? https://www.seleniumhq.org/docs/03_webdriver.jsp#selenium-webdriver-s-
#TODO:  180630_28 Sometimes I receive a 504 or 304 error, and my URL if returns a "STATUS OK"  this is incorrect
#TODO:  180630_29 print my evars/props, but also pass them into arrays
#TODO:  180630_30 Randomize the sleep amount, but use implicit wait (todo 21)

#TODO: 180705_32 check if an instance of the browser is already open, if so, don't open a new one
#TODO:  180705_33 LANDSEND DOESN"T WORK - it has a popup modal - must kill the popup modal
#TODO:  180705_34 LANDSEND USES DTM - must figure out how to defeat it -- put in a check for _satelite
#TODO:  180705_35 OLD NAVY:  https://oldnavy.gap.com will this work?

#TODO:  180713_36:  I need to learn more about the geckodriver and how selenium/webdriver talks to it - what is doing the translation of "general.useragent.override"


print("**ACTUAL CODE...Last Commit:  7/29/2018 14:12PM")

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options as Options #allows for some browser options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #allows for some browser options
from time import sleep #allows for waiting w/ promise
import requests #used for URL functions and validity
import urllib3 #used to kill Insecure https request warnings- should solve properly for this

print("...Import complete...")

#CREATE OPTIONS AND CAPABILITIES OBJECTS
ops = Options()
caps = DesiredCapabilities.FIREFOX.copy()
profile = webdriver.FirefoxProfile()
prof = webdriver.FirefoxProfile()

#MODIFY OPTIONS AND CAPABILITIES TO BE HEADLESS AND EAGER LOAD STRATEGY, ATTEMPTING TO ADD IN UA
caps.update({'pageLoadStrategy':'eager'})
ops.headless=True
prof.set_preference("general.useragent.override", "Android 4.4; Mobile;")


#SET TARGET URLs AND BROWSER
URLArray = [""]
URLCount = 0
TargetURL = URLArray[URLCount]
####

browser = webdriver.Firefox(executable_path="C:\\Python36\\Env\\PacketSniffer\\geckodriver.exe",options=ops, capabilities=caps)
print("...Globals are set...")




def URLTest():
    # TEST URL FOR ERRORS
    try:
        #hard disable SSL warning
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        r = requests.head(TargetURL, verify=False)
        #URL Status ok?
        if r.status_code == 200 or 301 or 302:
            print("\nURL STATUS OK:  "+str(r.status_code))
        else:
            print("URL STATUS NOT 200:  " + str(r.status_code))
            return quit()
    except requests.exceptions.RequestException as e:
        print("GET ENCOUNTERED A FAILURE"+str(e)), quit()


def StandardCodeChecks():
    # TEST FOR ADOBE COOKIE AND S_CODE
    #check for cookie, if not, quit.  Should build if cookie changes page to page as well
    if browser.get_cookie("") is not None:
        InitialVisitorCookie = browser.get_cookie("")
        #FUTURE STATE:  if CurrentCookie == NULL Then Continue else if Initial Visitor Cookie != CurrentCookie throw error
        print("...Cookie Was Found...")
        sleep(2)
        if ScriptExecution("marketingCloudVisitorID",False) is None or ScriptExecution("marketingCloudVisitorID",False)=="":
            print("MCID NOT SET!")
            quit()
        else:
            print("...MCID Was Set...")
    else:
        print("COOKIE OR ORG ID NOT FOUND!")
        quit()


    # check for presence of s_code.js, (this only works without data layer or DTM update later)
    if len(browser.find_elements_by_xpath("//script[contains(@src, 's_code.js')]"))>0:
        print("...s_code exists...")
    else:
        print("s_code does not exist!...")
        return quit()

#put in a printit argument to print results or not
def ScriptExecution(SVarStr,PrintMe=True):
    #put a check for _sattelite
    SVarVal = browser.execute_script("return ("+"s."+SVarStr+");")
    if SVarVal is None:
        nothing=0
    elif SVarVal == "" and PrintMe==True:
        print(str(SVarStr)+":"+"  ---")
    elif PrintMe==True:
        print(str(SVarStr)+":"+"  "+str(SVarVal))
    return SVarVal

def PullData():
    browser.get(TargetURL)
    print("...Getting URL...")
    sleep(1)

    #RUN STANDARD CHECKS FOR ADOBE CODE
    StandardCodeChecks()

    try:
        #print("********ScriptExecution*******")
        print("**************")
        ScriptExecution("pageName")
        print("**************")
        ScriptExecution("marketingCloudVisitorID")
        ScriptExecution("products")
        for i in range(0, 25, 1):
            ScriptExecution("prop"+str(i))
            ScriptExecution("eVar" + str(i))

    except WebDriverException as e:
        print("WebDriver Exception on {}".format(TargetURL))
        print("\n"+str(e))



for m in range(0, len(URLArray)):
    TargetURL = URLArray[URLCount]
    URLTest()
    PullData()
    m += 1
    URLCount = URLCount + 1
else:
    browser.quit()

print("\nEND OF CODE")