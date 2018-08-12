
#Note:  GLOBAL means "global to the file" not the package

#TODO:  180729_8 VLG right frame should contain output of current execution or some sort of indicator
#TODO:  180729_9 LG in the Adobe org ID, check if it is URL encoded or not and adjust  (script prefers URL encoded)
#TODO:  180729_8 SM sort all widget grid and creation top to bottom, left to right
#TODO:  180729_10 MD no need to disable widgets while running, should give user feedback that it is not just hung
#TODO:  180729_14 SM outpath should be toggled as 1:  file output or 2:  driver location  (yup w/ lambda)
#TODO:  180730_17 MD put in Entry boxes that display default selections (driver and output path should have default values)
#TODO:  180730_18 SM from todo17 in scraping script:  put path selection for SSL certificate location
#TODO:  180808_19 Need to set up the output pane -
    #Pane for output
    #connect log and print statements to output pane
    #pass errors to output pane
    #Create "loading" animation with a for loop


#TODO:  180808_21 add helpful hints

#TODOCOMPLETE:  180808_21 remove url count, is not used
#TODOCOMPLETE:  180730_19 SM attach Adobe Org ID
#TODOCOMPLETE:  180730_20 OP since I'm importing Scrape into Interface, I could make a "browser" class with methods and such --NOT NEEDED
#TODOCOMPLETE:  180808_22 Add a check for any empty boxes
#TODOCOMPLETE:  180729_11 SM attach namespace entry box
#TODOCOMPLETE:  180808_20 add a check for the Adobe ID before it loads pages

    #Colors:
        # #224587 Bright Blu
        # #bcbdc0 Light Grey
        # #565857 Dark Grey
        # #8a8d91 Med Grey
        # #5e77a7 Light Blue


print("ACTUAL CODE:  Last upload 8/4/18 1:15PM")


from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import re
import globals
import ScrapingScript as SS

print ("***import complete***")

#TOP LVL FXS
def DeleteEntry(event):
    if OrgIDEnt.get() == "Enter your Adobe Org ID":
        OrgIDEnt.delete(0,END)
    else:
        x=0

def GetInputBoxes():
    #get and format the input box
    patterns = [" ", "\n", "\t"]
    BoxData = InputBox.get("1.0",END)
    for i in range(len(patterns)):
        BoxData = re.sub(patterns[i],"",BoxData)

    BoxData = re.split(",",BoxData)
    globals.URLArray = BoxData
    globals.TargetURL= globals.URLArray[0]

    #get the org ID
    globals.OrgID = OrgIDEnt.get()

    #get the Namespace
    globals.AdobeNamespace = NamespaceEnt.get()

    if globals.AdobeNamespace=="" or globals.OrgID =="" or globals.URLArray==[""]:
        print("Namespace, OrgID or Array not set!!")
    else:
        SS.KesselRun()

def QuitIt():
    SS.browser.stop_client()
    SS.browser.quit()
    root.destroy()

def SetOutputPath(param):
    if param is "output":
        globals.OutputPath = filedialog.askdirectory()
        print("output:  "+str(globals.OutputPath))
    else:
        globals.DriverPath = filedialog.askdirectory()
        print("driver:  "+str(globals.DriverPath))





#SET ROOT WINDOW AND CONFIGURE
root = Tk()

root.configure(bg="#565857")
root.geometry("1250x765")
root.resizable(width=False, height=False)

#CREATE 1ST LEVEL WIDGETS (FRAMES)
TopFrame=Frame(root)
LeftFrame=Frame(root, bg= "#5e77a7")
RightFrame=Frame(root,bg="#8a8d91")
BottomFrame=Frame(root)

#PLACE 1ST LEVEL WIDGETS
TopFrame.grid(row=0, column=0,padx=5, pady=5, sticky = "NWE")
BottomFrame.grid(row=2, column = 0, padx=5, pady=5,sticky="EW")
LeftFrame.grid(row=1, column=0,padx=5, pady=5, sticky = "W")
RightFrame.grid(row=1, column=1, padx=5, pady=5, sticky = "NE")

#CREATE 2ND LEVEL WIDGETS (BUTTONS AND INPUT FIELDS)
InputBox = scrolledtext.ScrolledText(LeftFrame, wrap = WORD)
RunButton = Button(BottomFrame, text="Run Script", width=12, command = GetInputBoxes, bg="#5e77a7")
QuitButton = Button(BottomFrame, text ="Quit", width =12, command = QuitIt)
OutputButton = Button(BottomFrame, text = "Save To...", width = 12, command = lambda: SetOutputPath("output"))
DriverButton = Button(BottomFrame, text = "Driver Path...", width = 12, command = lambda: SetOutputPath("driver"))

RadioVar = IntVar() #required for radio button
DeviceRadioDT = Radiobutton(BottomFrame, text = "Desktop", variable = RadioVar, value=1)
DeviceRadioTB = Radiobutton(BottomFrame, text = "Tablet", variable = RadioVar, value=2)
DeviceRadioSP = Radiobutton(BottomFrame, text = "Smartphone", variable = RadioVar, value=3)
RadioVar.set(1) #default DT

OrgIDDefText = StringVar()
OrgIDDefText.set("Enter your Adobe Org ID")
OrgIDEnt = Entry(TopFrame, textvariable=OrgIDDefText, fg="#8a8d91", width=30)
OrgIDEnt.bind("<Button-1>", DeleteEntry)

NamespaceEnt = Entry(TopFrame, fg = "#8a8d91", width=30)

#PLACE 2ND LEVEL WIDGETS
InputBox.grid(row=0, column=0, padx=5, pady=5)

RunButton.grid(row=1, column=0, padx=5, pady=5)
QuitButton.grid(row=2, column=0, padx=5, pady=5)
OutputButton.grid(row=3, column=0, padx=5, pady=5)
DriverButton.grid(row=4, column=0, padx=5, pady=5)

DeviceRadioDT.grid(row=1, column=1, padx=5, pady=5, sticky = "W")
DeviceRadioSP.grid(row=2, column=1, padx=5, pady=5, sticky = "W")
DeviceRadioTB.grid(row=3, column=1, padx=5, pady=5, sticky = "W")

OrgIDEnt.grid(row=0,column =1, padx=5, pady=5, sticky = "W")
NamespaceEnt.grid(row = 1, column=1, padx=5, pady=5, sticky = "W")

#CREATE 2ND LEVEL LABELS
DeviceLab = Label(BottomFrame, text = "Select Device",fg = "#224587")
RunLab = Label(BottomFrame, text = "Begin Script",fg = "#224587")
OrgIDLab = Label(TopFrame,text = "Org ID:  ", fg ="#224587")
NamespaceLab = Label(TopFrame, text= "Var Namespace:  ", fg="#224587")

#PLACE 2ND LEVEL LABELS
RunLab.grid(row=0,column =0, padx=5, pady=5, sticky = "")
DeviceLab.grid(row=0,column =1, padx=5, pady=5, sticky = "W")
OrgIDLab.grid(row=0,column =0, padx=5, pady=5, sticky = "W")
NamespaceLab.grid(row=1,column =0, padx=5, pady=5, sticky = "W")

#FINAL RUN
root.mainloop()