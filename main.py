from tkinter import *
import smtplib


HomePage=Tk()
HomePage.title("App")
HomePage.geometry('600x600')

Homelab=Label(HomePage,text='Email Generator',background='#34A2FE')
Homelab.pack()


emailLabel=Label(HomePage,text='Email')
emailLabel.place(x=80,y=130)

inemail=Entry(HomePage,width=30)
inemail.place(x=240,y=130)

passwordlabel=Label(HomePage,text='Password')
passwordlabel.place(x=80,y=180)

inpassword=Entry(HomePage,width=30,show='*')
inpassword.place(x=240,y=180)

email2=Label(HomePage,text="Send Email")
email2.place(x=80,y=229)

inemail2=Entry(HomePage,width=30)
inemail2.place(x=240,y=229)

text=Label(HomePage,text="Message")
text.place(x=80,y=279)

intext=Entry(HomePage,width=30)
intext.place(x=240,y=279)

No=Label(HomePage,text="No of Email")
No.place(x=75,y=330)

Noin=Entry(HomePage,width=30)
Noin.place(x=240,y=330)


def Send():
    d=CollectAllData()
    size=int(Noin.get())
    my_email=d.get('Email')
    sender_email=d.get('Email2')
    MSG=d.get('MSG')
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()

    connection.login(user=my_email, password=d.get('Password'))

    for i in range(size):
        connection.sendmail(from_addr=my_email, to_addrs=sender_email, msg=MSG)
    connection.close()

button=Button(HomePage,text='Send Email',command=Send)
button.place(x=289,y=390)

def CollectAllData():
    Email=inemail.get()
    password=inpassword.get()
    Email2=inemail2.get()
    TextMSG=intext.get()
    Data={
        'Email':Email,
        'Password':password,
        'Email2':Email2,
        'MSG':TextMSG
    }
    return Data


if __name__ == '__main__':
    mainloop()

















