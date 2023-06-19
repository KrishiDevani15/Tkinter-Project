from tkinter import *
from PIL import Image,ImageTk

from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'nitish@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy','Login Successful')
    else:
        messagebox.showerror('Error','Login Failed')



root = Tk()

# Window
root.title("Login Form")
root.iconbitmap('favicon.ico')

root.geometry("350x500")
root.resizable(False,False)

root.config(background='#0096DC')

# Image
img = Image.open('image1.png')
resize_img = img.resize((70,70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

# Text
text_label = Label(root,text='Flipkart',bg='#0096DC',fg='white',font=('verdana',24))
text_label.pack()

# Email
email_label = Label(root,text='Enter Email',bg='#0096DC',fg='white',font=('verdana',12))
email_label.pack(pady =(20,5))

# Input Email
email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15)) 
#Password
password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC',font=('verdana',12))
password_label.pack(pady=(20,5))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

#Button
login_btn = Button(root,text='Login Here',bg='white',fg='black',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))
root.mainloop()

