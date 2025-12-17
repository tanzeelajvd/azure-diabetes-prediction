from tkinter import *
from tkinter import messagebox as tkMessageBox
import urllib.request
import json,ctypes
#===============================#
def hello(event):
    entryname9.delete(0, "end")
def hello1(event):
    entryname8.delete(0, "end")
def hello2(event):
    entryname7.delete(0, "end")
def hello3(event):
    entryname6.delete(0, "end")  
def hello4(event):
    entryname1.delete(0, "end")
#===============================#    
#=================================Button Click=======================================#   
def button_click_function():
    
    p1=entryname1.get()
    if p1=="":
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Your Age", "ERROR", 0)
        return
    try:
        if(int(p1)<0 or int(p1)>150):
            ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Age", "ERROR", 0)
            return
    except:
        
            ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Age", "ERROR", 0)
            return
        
    p2=entryname2.get()
    if(p2=="....Select...."):
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Gender", "ERROR", 0)
        return      
    if(p2=="Male"):
        p2="1"
    else:
        p2="0"


        
    p3=entryname3.get()
    if(p3=="....Select...."):
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Yes or NO", "ERROR", 0)
        return
    if(p3=="Yes"):
        p3="1"
    else:
        p3="0"


        
    p4=entryname4.get()
    if(p4=="....Select...."):
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Yes or NO", "ERROR", 0)
        return
    if(p4=="Yes"):
        p4="1"
    else:
        p4="0"


        
    p5=entryname5.get()
    if(p5=="....Select...."):
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Yes or NO", "ERROR", 0)
        return
    if(p5=="Yes"):
        p5="1"
    else:
        p5="0"


        
    p6=entryname6.get()
    if p6=="":
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Frequency of Thirst", "ERROR", 0)
        return
    try:
        if(int(p6)<0 or int(p6)>20):
            ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Frequency", "ERROR", 0)
            return
    except:
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Frequency", "ERROR", 0)
        return


   
    p7=entryname7.get()
    if p7=="":
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Frequency of Urination", "ERROR", 0)
        return
    try:
        if(int(p7)<0 or int(p7)>30):
            ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Frequency", "ERROR", 0)
            return
    except:
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Frequency", "ERROR", 0)
        return


        
    p8=entryname8.get()
    if p8=="":
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Height", "ERROR", 0)
        return
    try:
        if(int(p8)<10 or int(p8)>250):
            ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Height", "ERROR", 0)
            return
    except:
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Height", "ERROR", 0)
        return



        
    p9=entryname9.get()
    if p9=="":
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Weight", "ERROR", 0)
        return
    try:
        if(int(p9)<10 or int(p8)>250):
            ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Weight", "ERROR", 0)
            return
    except:
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Valid Weight", "ERROR", 0)
        return


        
    p10=entryname10.get()
    if(p10=="....Select...."):
        ctypes.windll.user32.MessageBoxW(0, "Please Enter Yes or No", "ERROR", 0)
        return
    if(p10=="Yes"):
        p10="1"
    else:
        p10="0"



        
    data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Age': p1,   
                            'Gender': p2,   
                            'Family History': p3,   
                            'Smoking': p4,   
                            'Drinking': p5,   
                            'Thirst': p6,   
                            'Urination': p7,   
                            'Height': p8,   
                            'Weight': p9,   
                            'Fatigue': p10,   
                    }
                ],
        },

        
    "GlobalParameters":  {
        }
    }
    
    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/40c5ee4ebb4e49e09445cd805c332920/services/03f545c8310b468894d278623b1b7505/execute?api-version=2.0&format=swagger'
    api_key = "<YOUR_AZURE_API_KEY>"    # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        
        response = urllib.request.urlopen(req)
        result = response.read()
        results=json.loads(result.decode('utf-8'))
       # print(results)
        
        if(results['Results']['output1'][0]['Scored Labels']=="1"):
            lbl13 = Label(window , text ="You are diabetic",font=("Book Antiqua",15,"bold"),fg="white",bg="black")
            lbl13.grid(row=17,column=0,sticky="w",padx=(390,0),columnspan=2)

        else:
            lbl14 = Label(window , text ="You are not diabetic",font=("Book Antiqua",15,"bold"),fg="white",bg="black")
            lbl14.grid(row=17,column=0,sticky="w",padx=(370,0),columnspan=2)

        
        t=results['Results']['output1'][0]['Scored Probabilities']
        t=float(t[0:4])*100
        lbl15 = Label(window , text = "Chances that you are diabetic is "+str(t)[0:4]+"%",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
        lbl15.grid(row=18,column=0,sticky="w",padx=(320,0),columnspan=2)

 
    except urllib.request.HTTPError:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(json.loads(error.read()))
    



global entryname1,entryname2,entryname3,entryname4,entryname5,entryname6,entryname7,entryname8,entryname9,entryname10

global window    
window = Tk()

window.configure(background='black')
window.geometry("900x900")
window.title("DIABETES DIAGONOSTIC SOFTWARE")
window.resizable(width=False, height= False)

#====================================================================Labels Heading============================================================================#

lbllinfo = Label(window, font=("Book Antiqua",40,"bold"),text="Diabetes Test",fg="white", bg="black", bd=10,anchor="w")
lbllinfo.grid(row=0,column=0,sticky="w",padx=(280,0),columnspan=2)

lbllinfo1 = Label(window, font=("Book Antiqua",12),text="Change Begins With Just One Click",fg="white", bg="black", bd=10,anchor="w")
lbllinfo1.grid(row=1,column=0,sticky="w",padx=(320,0),columnspan=2)


lbllinfo2 = Label(window, font=("Book Antiqua",20,"bold"),text="Enter your Details",fg="white", bg="black", bd=10,anchor="w")
lbllinfo2.grid(row=2,column=0,sticky="w",padx=(335,0),columnspan=2)

#===========================================Enter Details=================================================#
lbl1 = Label(window , text = "Age ", font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl1.grid(row=4,column=0,padx=(130, 100),pady=(0,10),sticky="w")

entryname1 = Entry(window, fg="grey")
entryname1.config(font=("Book Antiqua",10))
entryname1.grid(row=4,column=1,padx=(0, 100),pady=(0,10),sticky="w")
entryname1.insert(0,"             In Years")
entryname1.bind('<Button-1>', hello4)




lbl2 = Label(window , text = "Gender ",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl2.grid(row=5,column=0,padx=(130, 100),pady=(0,10),sticky="w")

gender_list=["Male","Female"]
entryname2=StringVar(window)
entryname2.set("....Select....")
gender_option=OptionMenu(window,entryname2,*gender_list)
gender_option.config(bg="white",fg="black",width="17")
gender_option.grid(row=5,column=1,padx=(0, 100),pady=(0,10),sticky="w")




lbl3 = Label(window , text = "Family History of being Diabetic ",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl3.grid(row=6,column=0,padx=(130, 100),pady=(0,10),sticky="w")

answer=["Yes","No"]
entryname3=StringVar(window)
entryname3.set("....Select....")
history_option=OptionMenu(window,entryname3,*answer)
history_option.config(bg="white",fg="black",width="17")
history_option.grid(row=6,column=1,padx=(0, 100),pady=(0,10),sticky="w")




lbl4 = Label(window , text = "Do you smoke ? ",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl4.grid(row=7,column=0,padx=(130, 100),pady=(0,10),sticky="w")

answer1=["Yes","No"]
entryname4=StringVar(window)
entryname4.set("....Select....")
smoke_option1=OptionMenu(window,entryname4,*answer1)
smoke_option1.config(bg="white",fg="black",width="17")
smoke_option1.grid(row=7,column=1,padx=(0, 100),pady=(0,10),sticky="w")



lbl5 = Label(window , text = "Do you drink ? ",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl5.grid(row=8,column=0,padx=(130, 100),pady=(0,10),sticky="w")

answer2=["Yes","No"]
entryname5=StringVar(window)
entryname5.set("....Select....")
drink_option=OptionMenu(window,entryname5,*answer2)
drink_option.config(bg="white",fg="black",width="17")
drink_option.grid(row=8,column=1,padx=(0, 100),pady=(0,10),sticky="w")




lbl6 = Label(window , text = "Frequency of Thirst ",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl6.grid(row=9,column=0,padx=(130, 100),pady=(0,10),sticky="w")

entryname6 = Entry(window,fg="grey")
entryname6.config(font=("Book Antiqua",10))
entryname6.grid(row=9,column=1,padx=(0, 100),pady=(0,10),sticky="w")
entryname6.insert(0,"     No of times per day")
entryname6.bind('<Button-1>', hello3)




lbl7 = Label(window , text = "Frequency of Urination ",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl7.grid(row=10,column=0,padx=(130, 100),pady=(0,10),sticky="w")

entryname7 = Entry(window,fg="grey")
entryname7.config(font=("Book Antiqua",10))
entryname7.grid(row=10,column=1,padx=(0, 100),pady=(0,10),sticky="w")
entryname7.insert(0,"      No of times per day")
entryname7.bind('<Button-1>', hello2)




lbl8 = Label(window , text = "Height ",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl8.grid(row=11,column=0,padx=(130, 100),pady=(0,10),sticky="w")

entryname8 = Entry(window,fg="grey")
entryname8.config(font=("Book Antiqua",10))
entryname8.grid(row=11,column=1,padx=(0, 100),pady=(0,10),sticky="w")
entryname8.insert(0,"          In Centimeters")
entryname8.bind('<Button-1>', hello1)




lbl9 = Label(window , text = "Weight",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl9.grid(row=12,column=0,padx=(130, 100),pady=(0,10),sticky="w")

entryname9 = Entry(window,fg="grey")
entryname9.config(font=("Book Antiqua",10))
entryname9.insert(0,"            In Kilograms")
entryname9.grid(row=12,column=1,padx=(0, 100),pady=(0,10),sticky="w")
entryname9.bind('<Button-1>', hello)




lbl10 = Label(window , text = "Fatigue ",font=("Book Antiqua",13,"bold"),fg="white",bg="black")
lbl10.grid(row=13,column=0,padx=(130, 100),pady=(0,10),sticky="w")

answer56=["Yes","No"]
entryname10=StringVar(window)
entryname10.set("....Select....")
history_option56=OptionMenu(window,entryname10,*answer56)
history_option56.config(bg="white",fg="black",width="17")
history_option56.grid(row=13,column=1,padx=(0, 100),pady=(0,10),sticky="w")




btnshow = Button(window , text = "Show Results",font=("Book Antiqua",13,"bold"),fg="white",bg="black",command=button_click_function)
btnshow.grid(row=15,column=0,padx=(40, 100),pady=(0,10),columnspan=2)




#creating an empty label to display the output
ty="............................................................................................................RESULT............................................................................................................................"
lbl23 = Label(window , text =ty,fg="white",bg="black",font="bold")
lbl23.grid(row=16,column=0,columnspan=2)


#render the window
window.mainloop()
