import tkinter as tk
import pgen
from tkinter import messagebox
import pyperclip
import json
pop1=None
window=tk.Tk()

window.title("Password Manager")
window.minsize(height=450,width=500)
window.config(bg="#0E46A3")
canvas=tk.Canvas(height=200,width=250)

canvas.pack()
canvas.config(bg="#0E46A3",highlightthickness=0)
def copier():
    pyperclip.copy(psw)
def genert():
    newr=pgen.password()
    newp=newr.genp()
    text3.delete("0","end")
    text3.insert("end",newp)

def ag():
    global pop1
    pop1.destroy()
def saver():
    global pop1
    global psw
    pop1.destroy()
    web=text1.get().title()
    user=text2.get().lower()
    psw=text3.get().lower()
    copier()
    latdata={web:{"Email":user,"password":psw}}
    with open ("psword.json","r") as cr:
        data=json.load(cr)
        data.update(latdata)

 

    with open ("psword.json","w") as pr:
        json.dump(data,pr,indent=4)
    text1.delete("0","end")
    text3.delete("0","end")
def conf():

    global pop1

    web=text1.get().lower()
    user=text2.get().lower()
    psw=text3.get().lower()
    if(len(web)>0 and len(user)>0 and len(psw)>0):
   
        pop1=tk.Tk()
        pop1.title("Appbrewery")
        pop1.minsize(width=500,height=200)
        pop1.config(bg="#1E0342")
        pop3=tk.Label(pop1,text="Website : "+web,font=("Arial",8,"bold"))
        pop3.pack()
        pop1.config(pady=10,padx=10)
        pop2=tk.Label(pop1,text="User : "+user,font=("Arial",8,"bold"))
        pop2.pack()
        pop2=tk.Label(pop1,text="Password : "+psw,font=("Arial",8,"bold"))
        pop2.pack()
        confirm=tk.Button(pop1,text="Confirm",font=("Arial",8,"bold"),command=saver)
        no=tk.Button(pop1,text="Reconsider",font=("Arial",8,"bold"),command=ag)
        confirm.pack(side="left",padx=150,pady=15)
        no.pack(side="right",padx=150,pady=15)
        pop1.mainloop()
    else :
        tk.messagebox.showinfo(title="oops",message="Please make sure u didnt leave any fields empty!!")
def searcher():
    web=text1.get().title()
    
    with open ("psword.json","r") as k:
      
        datar=json.load(k)
       
        #user=datar[web]["Email"]
        #psw=datar[web]["password"]
        
        if web in datar:
            user=datar[web]["Email"]
            psw=datar[web]["password"]
            tk.messagebox.showinfo(title=web,message=f"Email : {user}\nPassword : {psw}",icon="info")
        if web not in datar:
            tk.messagebox.showinfo(title=web,message=f"No password found ")
photo=tk.PhotoImage(file="logo.png")
canvas.create_image(125,120,image=photo)
web=tk.Label(text="Website",font=("Arial",15,"bold"))
web.pack(side="left")
web.config(padx=25)
text1=tk.Entry(width=40)
text1.place(x=170,y=315)
email=tk.Label(text="Username",font=("Arial",15,"bold"))
email.place(x=0,y=350)
text2=tk.Entry(width=40)
text2.place(x=170,y=353)
email.config(padx=15)
password=tk.Label(text="Password",font=("Arial",15,"bold"))
password.place(x=0,y=390)
password.config(padx=16)
text3=tk.Entry(width=20)
text3.place(x=170,y=394)
genp=tk.Button(text="Generate Password",command=genert,font=("Arial",7,"bold"))
search=tk.Button(text="Search",font=("Arial",7,"bold"),command=searcher,height=1)
search.place(x=425,y=315)

genp.place(x=300,y=394)
save=tk.Button(text="Add",font=("Arial",7,"bold"),command=conf)
save.place(x=235,y=420)

window.mainloop()