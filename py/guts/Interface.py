#TODO:  180715_2 allow user to enter their org ID
#TODO:  180715_1 add interface that accepts an array of URLs
#TODO:  180722_3 Make interface prettier
#TODO:  180722_4 Need to be able to interact with other file variables
#TODO:  180724_5 clean input prior to passing
    #resources:
        #https://docs.python.org/3/library/tk.html
        #Best explanation so far:  https://www.python-course.eu/tkinter_labels.php
        #think structure is Tk is master of all, Frame is the window itself, you have to call "pack" to get widgets into the frame
        #Example TKinter I used https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=0s&index=2&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
        #http://effbot.org/tkinterbook/frame.htm  Great basics site
        #https://coolors.co/export/pdf/224587-bcbdc0-565857-8a8d91-5e77a7
        #https://docs.python.org/3/library/tkinter.ttk.html#widget
        # Good for sizing of windows:  https://smallguysit.com/index.php/2017/11/11/tkinter-entry-widget/
        #Full tkinter guide https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
    #Colors:
        # #224587 Bright Blu
        # #bcbdc0 Light Grey
        # #565857 Dark Grey
        # #8a8d91 Med Grey
        # #5e77a7 Light Blue

print("ACTUAL CODE:  Last upload 7/29/18 2:26PM")


from tkinter import *
from tkinter import scrolledtext
print ("***import complete***")

root = Tk()
root.focus_set()
root.configure(bg="#565857")
root.geometry("800x600")
root.resizable(width=False, height=False)


#TODO:  180724_5 clean input prior to passing
#need to clean values
# def myFunc():
#     data = box.get("1.0",END)
#     print("DATA:  "+data)
#     data.strip(" ")
#     print("STrippted:  "+data)
#     MyArray = data.split(",")
#     print(MyArray)
#     return MyArray

#Instantiate Frames
TopFrame=Frame(root)
LeftFrame=Frame(root, bg= "#5e77a7")
RightFrame=Frame(root,bg="#8a8d91")
BottomFrame=Frame(root)

#Frames options


#Grid frames
TopFrame.grid(row=0, column=0,padx=5, pady=5, sticky = "NWE")
BottomFrame.grid(row=2, padx=5, pady=5,sticky="EW")
LeftFrame.grid(row=1, column=0,padx=5, pady=5, sticky = "W")
RightFrame.grid(row=1, column=1, padx=5, pady=5, sticky = "NE")

#Large input text box
InputBox = scrolledtext.ScrolledText(LeftFrame, wrap = WORD)

#Buttons for passing values, quit, Device, and choosing output location
RadioVar = IntVar()
RunButton=Button(BottomFrame, text="Run Script", width=12)
DeviceButtonDT = Radiobutton(BottomFrame, text = "Desktop", variable = RadioVar, value=1)
DeviceButtonTB = Radiobutton(BottomFrame, text = "Tablet", variable = RadioVar, value=2)
DeviceButtonSP = Radiobutton(BottomFrame, text = "Smartphone", variable = RadioVar, value=3)

#button placement and inputs
InputBox.grid(row=0, column=0, padx=5, pady=5)
RunButton.grid(row=1, column=0, padx=10, pady=5)
DeviceButtonDT.grid(row=1, column=1, padx=5, pady=5, sticky = "W")
DeviceButtonSP.grid(row=2, column=1, padx=5, pady=5, sticky = "W")
DeviceButtonTB.grid(row=3, column=1, padx=5, pady=5, sticky = "W")

#Create Labels
DeviceLab = Label(BottomFrame, text = "Select Device",fg = "#224587")
RunLab = Label(BottomFrame, text = "Begin Script",fg = "#224587")
DeviceLab.grid(row=0,column =1, padx=5, pady=5, sticky = "W")
RunLab.grid(row=0,column =0, padx=5, pady=5)


#final Run
root.mainloop()