#TODOCOMPLETE:  18061601 Goal is to take learnings from first tutorial and read in something, print to console
#TODOCOMPLETE:  18061602 "TypeError: must be str, not NoneType", occurs when several vars are pulled
    #https://stackoverflow.com/questions/43566543/typeerror-must-be-str-not-nonetype
    #TypeError: must be str, not NoneType
    #solved with def CheckforNone
#TODOCOMPLETE:  18061705 what is browser.get, browser.execute_script? - THESE RUN FROM THE GECKODRIVERS
#TODOCOMPLETE:  18061708 Dynamically populate vars and props

#TODO:  18061703 evar9 returns as none on HP why?  it should be "homepage" - this is prev.page, so browser doesn't take into account the s.do functions
#TODO:  18061704 pull all evars and see what returns, set function to loop through this part
#TODO:  18061706 should use some error handling for lack of internet connection, should test connectivity, etc.
#TODO:  18061707 learn more on what I can do with the drivers
#TODO:  18061709 create case for different types of code (pageName vs. s.prop17 vs. mid)
#TODO:  18061710 make browser dynamic
#TODO:  18061711 in pagehits Fx, should do a on DOM COMPLETE check before running other functions
#TODO:  18061712 Make a loop for the props and vars
#TODO:  18061713 In for loop under pagehits, should have a mechanism to check if the prop exists.  i.e. there's no prop0, but it returns blank... differentiate from NOT PRESENT and ACTUAL BLANK


print("**ACTUAL CODE")

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
from time import sleep
print("Import complete...")

#setglobals
target_url = 'https://www.kohls.com'
global HTML_string
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options,executable_path="C:\\Python36\\Env\\PacketSniffer\\geckodriver.exe", timeout=5)
print("Globals are set...")




def ScriptExecution(SVarStr):
    SVarVal = browser.execute_script("return ("+"s."+SVarStr+");")
    if SVarVal == None:
        print(SVarStr+":"+"  blank")
    else:
        print(SVarStr+":"+"  "+SVarVal)
    return SVarVal

def pagehits(url):
    browser.get(url)
    print("URL has been gotten")
    sleep(1)
    print("Site is loading... ")

    try:
        print("ScriptExecution in pagehits Fx...")

        ##Current Edits
        #begin loop
        for i in range(0, 256, 1):
            ScriptExecution("prop"+str(i))
            continue

        ##End of Edits
        # ScriptExecution("prop1")
        # ScriptExecution("prop3")
        # ScriptExecution("prop5")
        # ScriptExecution("prop9")
        # ScriptExecution("prop15")
        # ScriptExecution("prop17")
    except WebDriverException:
        print("Exception on {}".format(url))
    browser.quit()

pagehits(target_url)
print("END OF CODE")
