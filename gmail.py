from tkinter import *
import smtplib
from tkinter import messagebox

root = Tk()

root.title("Gmail")

root.geometry('1080x400')

root.resizable(0,0)
root.config(bg="teal")


def hello():
  try:
       email = Email.get()
       password = Pass.get()
       if(len(email) > 0 and len(password) >0):
           print(email,password)
           mail = smtplib.SMTP('smtp.gmail.com',587)
           mail.starttls()
           isLogined=mail.login(email,password)
           print(type(isLogined))
           if(isLogined[0]==235):
               loginBtn.config(text="logout")
               secondWindow = Toplevel()
               secondWindow.geometry('540x400')
               revlabel = Label(secondWindow,text="Reciver Email").place(x=50,y=50)
               rev = Entry(secondWindow,width="20")
               rev.place(x=100,y=50)
               messageBox = Text(secondWindow,width="50",height="10").place(x=80,y=100)
               secondWindow.mainloop()

  except smtplib.SMTPException as e:
      print(e)
      messagebox.showwarning("Authentication Error","User Login Data is Incorrect")
  except:
      print("Error occured")
      messagebox.showwarning("Internet Error","Internet Error")

EmailLable = Label(root,text="Enter Email")
EmailLable.place(x=150,y=150)

Email = Entry(root,width="50")
Email.place(x=250,y=150)



passLabel = Label(root,text="Enter Password")
passLabel.place(x=150,y=200)

Pass = Entry(root,width="50",show="*")
Pass.place(x=250,y=200)


loginBtn = Button(root,text="Login",padx="100",pady="5",command=hello)
loginBtn.place(x=280,y=250)

root.mainloop()