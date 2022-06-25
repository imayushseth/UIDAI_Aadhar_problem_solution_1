import random
import math
from tkinter import *
from tkinter import messagebox
from twilio.rest import Client
import smtplib

# IN THIS PROJECT I FIRST SEPARATED EVERY GUI PAGE,
# AFTER THAT I MERGED ALL IN ONE .. YES I COULD HAVE ADDED THEM IN CLASSES AND
# HAVE BEEN LESSER AMOUNT, IT WAS MY FIRST PROJECT :)

# ALL OTP SERVER ARE NOW NULL AND VOID
# DUE TO PRIVACY REASONS AND TERMS OF CONDITIONS


# BUT YOU STILL CAN RUN ALL THE GUI


dark_blue = '#28118f'
light_blue = '#23c3eb'

data = '0987654321qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
length = len(data)
captcha = ''
for i in range(6):
    captcha += data[math.floor(random.random() * length)]

otp1 = random.randint(100000, 999999)

# SENDING OTP via EMAIL


def send_otp():
    try:
        account_sid = "AC027b5927043dd3843068d66b750e488a"
        auth_token = "d0269842108730faad0bfba488628e57"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body='Hi,\n'
                 'Your OTP for Login to myAadhaar is:\n'
                 f'{otp1}\n'
                 f'It is Valid for 10 minutes only. Do not share your OTP.',
            from_='+18508093563',
            to=f'+91{int(num_tf.get())}'

            # Enter your phone number here that is verified with twilio,
            # If you don't want to verify, No problem.
            # I will show how it works in the video linked with my mail.
            # Here now you can proceed with the OTP sent to your email
        )

        print(message.sid)

    except:

        messagebox.showerror(title="Can't send OTP to phone number or Email",
                             message=f"Due to end of Subscription and Secutity/Privacy purpose, "
                                     f"OTP can't be send but still, you can go further."
                                     f"Your login OTP is {otp1}")

    entered_email = email_tf.get()

    sender = "aadhaartest.by.ayush@gmail.com"
    receiver = f"{entered_email}"
    password = "password1234#ayush"  # sender's email password here
    subject = 'Login OTP is here'
    body = f"Hi there," \
           "" \
           f"Your login OTP is: {otp1} " \
           "It is valid for 10 minutes. Don't share with anyone."

    message = f''' From: Ayush Seth {sender}
    To: Beast {receiver}
    Subject = {subject}\n
    {body}'''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        print('Logged in...')
        server.sendmail(sender, receiver, message)
        print('Email has been sent!')
    except smtplib.SMTPAuthenticationError:
        print('Unable to sign in ')


# CHECKING

def submit():
    entered_otp = int(otp_tf.get())
    check_num()
    check_captcha()

    # IF OTP IS CORRECT PROCEED

    if entered_otp == otp1:
        messagebox.showinfo(title='Validated', message='OTP IS Correct')
        w7.destroy()

        def sample_one():
            messagebox.showinfo(title='Unavailable',
                                message="Sorry,\nYou can't use this\n feature right now.")

        def sample_two():
            messagebox.showinfo(title='Unavailable',
                                message="Sorry,\nYou can't use this\n feature right now.")

        def update_aadhaar():

            # DELETING PREVIOUS WINDOW

            window.destroy()

            def proceed():
                if x.get() == 4:
                    w6.destroy()

                    def click1(event):
                        entry1.config(state=NORMAL)
                        entry1.delete(0, END)

                    def click2(event):
                        entry2.config(state=NORMAL)
                        entry2.delete(0, END)

                    def click3(event):
                        entry3.config(state=NORMAL)
                        entry3.delete(0, END)

                    def click4(event):
                        entry4.config(state=NORMAL)
                        entry4.delete(0, END)

                    def click5(event):
                        entry5.config(state=NORMAL)
                        entry5.delete(0, END)

                    def click6(event):
                        entry6.config(state=NORMAL)
                        entry6.delete(0, END)

                    def click7(event):
                        entry7.config(state=NORMAL)
                        entry7.delete(0, END)

                    def click8(event):
                        entry8.config(state=NORMAL)
                        entry8.delete(0, END)

                    def click9(event):
                        entry9.config(state=NORMAL)
                        entry9.delete(0, END)

                    def next1():
                        messagebox.showerror(title='Sorry', message="You can't use this feature"
                                                                    " \nClick on you don't reside here")

                    def other():
                        w4.destroy()

                        def check():
                            if y.get():
                                leng = len(number2.get())
                                if leng == 10:
                                    Label(w3, text='Number looks Good !', fg='green', width=30,
                                          font=("Abel", 10)).place(x=480, y=410)
                                else:
                                    ll = Label(w3, text='Something Wrong with given Number !', fg='red',
                                               font=("Abel", 10))
                                    ll.place(x=480, y=410)
                                return True
                            else:
                                return False

                        def submit4():
                            if check():
                                w3.destroy()
                                otp2 = random.randint(100000, 999999)

                                def go_otp2():
                                    print(otp2)
                                    try:
                                        account2_sid = "AC26b5fe091d1cf2752ad30306e0652018"
                                        auth2_token = "d63d8c974501570cf6ee39acdccce24b"
                                        client = Client(account2_sid, auth2_token)

                                        message2 = client.messages.create(
                                            body='Hi there!,\n'
                                                 'Ayush here, testing messages part 1'  # change body, landlords part
                                                 'A person linked with the phone number +917044559343\n'
                                                 'Wanna use your Aadhaar Address to Update there Aadhaar.\n'
                                                 'Here is the OTP you can share with them,'
                                                 f'{otp2}\n'
                                                 f'It is Valid for 10 minutes only. Do not share with anyone else except '
                                                 f'them.\n '
                                                 f'Or else click on the below link, We will send them Secure OTP\n'
                                                 f'Link is not Available Right Now',
                                            from_='+13343731610',
                                            to=f'+917003314974'     # {number2.get()}
                                        )

                                        print(message2.sid)
                                    except:

                                        messagebox.showerror(title="Can't Proceed",
                                                             message="Similar reason can't send OTP..."
                                                                     "Don't worry OTP is just at TOP LEFT corner of window.")

                                go_otp2()

                                def click_o(event):
                                    otp2_tf.config(state=NORMAL)
                                    otp2_tf.delete(0, END)

                                def done2():
                                    entered_otp2 = int(otp2_tf.get())
                                    if otp2 == entered_otp2:
                                        messagebox.showinfo(title='Validated',
                                                            message='OTP is coreect. You are being Approved.')
                                        w.destroy()

                                        def let_go():
                                            agree()

                                        def agree():
                                            if z.get():
                                                win.destroy()

                                                def update():
                                                    hno = entry1.get()
                                                    floor = entry2.get()
                                                    land = entry5.get()
                                                    messagebox.showinfo(title='Updated',
                                                                        message='Your Aadhaar has been Updated Successfully!\n'
                                                                                'New Address is:\n'
                                                                                f'{hno}, {floor}, South Royal City, DumDum Road, {land} ,'
                                                                                f' 123456, Kolkata, West Bengal')
                                                    w1.destroy()

                                                def click1(event):
                                                    entry1.config(state=NORMAL)
                                                    entry1.delete(0, END)

                                                def click2(event):
                                                    entry2.config(state=NORMAL)
                                                    entry2.delete(0, END)

                                                def click5(event):
                                                    entry5.config(state=NORMAL)
                                                    entry5.delete(0, END)

                                                w1 = Tk()
                                                w1.attributes('-fullscreen', True)

                                                Label(w1,
                                                      text='Last Process for Updation',
                                                      font=('Arial', 30, 'bold'),
                                                      padx=10,
                                                      pady=20,
                                                      fg='white',
                                                      bg=dark_blue
                                                      ).pack(fill=BOTH)

                                                frame2 = Frame(w1,
                                                               bg='white',
                                                               height=550,
                                                               bd=4,
                                                               relief=SUNKEN,
                                                               width=700)
                                                frame2.pack(pady=15)
                                                frame2.pack_propagate(False)
                                                Label(frame2,
                                                      text="Using Landlord's Address",
                                                      font=('Arial', 15, 'bold'),
                                                      fg='white',
                                                      bg=light_blue).pack(fill=BOTH)
                                                entry1 = Entry(frame2,
                                                               font=('Arial', 18),
                                                               fg='black',
                                                               width=30, bd=1,
                                                               bg='white')
                                                entry1.insert(0, 'Apartment No.12-A')
                                                entry1.config(state=DISABLED)
                                                entry1.bind("<Button-1>", click1)
                                                entry1.place(x=149, y=50)

                                                entry2 = Entry(frame2,
                                                               font=('Arial', 18),
                                                               fg='black',
                                                               width=30, bd=1,
                                                               bg='white')
                                                entry2.insert(0, '5th Floor')
                                                entry2.config(state=DISABLED)
                                                entry2.bind("<Button-1>", click2)
                                                entry2.place(x=149, y=110)

                                                entry3 = Entry(frame2,
                                                               font=('Arial', 18),
                                                               fg='black',
                                                               width=30, bd=1,
                                                               bg='white')
                                                entry3.insert(0, 'South Royal Society')
                                                entry3.config(state=DISABLED)
                                                entry3.place(x=149, y=170)

                                                entry4 = Entry(frame2,
                                                               font=('Arial', 18),
                                                               fg='black',
                                                               width=30, bd=1,
                                                               bg='white')
                                                entry4.insert(0, 'DumDum Road')
                                                entry4.config(state=DISABLED)
                                                entry4.place(x=149, y=230)

                                                entry5 = Entry(frame2,
                                                               font=('Arial', 18),
                                                               fg='black',
                                                               width=30, bd=1,
                                                               bg='white')
                                                entry5.insert(0, 'Landmark')
                                                entry5.config(state=DISABLED)
                                                entry5.bind("<Button-1>", click5)
                                                entry5.place(x=149, y=290)

                                                entry6 = Entry(frame2,
                                                               font=('Arial', 18),
                                                               fg='black',
                                                               width=30, bd=1,
                                                               bg='white')
                                                entry6.insert(0, '123456')
                                                entry6.config(state=DISABLED)
                                                entry6.place(x=149, y=350)

                                                entry7 = Entry(frame2,
                                                               font=('Arial', 18),
                                                               fg='black',
                                                               width=30, bd=1,
                                                               bg='white')
                                                entry7.insert(0, 'Kolkata')
                                                entry7.config(state=DISABLED)
                                                entry7.place(x=149, y=410)

                                                entry9 = Entry(frame2,
                                                               font=('Arial', 18),
                                                               fg='black',
                                                               width=30, bd=1,
                                                               bg='white')
                                                entry9.insert(0, 'West Bengal')
                                                entry9.config(state=DISABLED)
                                                entry9.place(x=149, y=470)

                                                Label(frame2, text='State?', fg='red', bg='white',
                                                      font=('Cambridge', 8, 'italic')
                                                      ).place(x=149, y=502)
                                                Label(frame2, text='City?', fg='red', bg='white',
                                                      font=('Cambridge', 8, 'italic')
                                                      ).place(x=149, y=442)
                                                Label(frame2, text='PinCode?', fg='red', bg='white',
                                                      font=('Cambridge', 8, 'italic')
                                                      ).place(x=149, y=382)
                                                Label(frame2, text='Landmark?', fg='red', bg='white',
                                                      font=('Cambridge', 8, 'italic')
                                                      ).place(x=149, y=322)
                                                Label(frame2, text='Area/Street/Road?', fg='red', bg='white',
                                                      font=('Cambridge', 8, 'italic')
                                                      ).place(x=149, y=262)
                                                Label(frame2, text='Locality/Flat/Sector?', fg='red', bg='white',
                                                      font=('Cambridge', 8, 'italic')
                                                      ).place(x=149, y=202)
                                                Label(frame2, text='Floor/Apartment/Building?', fg='red', bg='white',
                                                      font=('Cambridge', 8, 'italic')
                                                      ).place(x=149, y=142)
                                                Label(frame2, text='House No./Flat No.?', fg='red', bg='white',
                                                      font=('Cambridge', 8, 'italic')
                                                      ).place(x=149, y=82)

                                                Button(w1,
                                                       text='UPDATE',
                                                       font=('Helvetica', 20),
                                                       bg=dark_blue,
                                                       fg='white',
                                                       padx=3, pady=3,
                                                       command=update
                                                       ).pack()
                                                w1.mainloop()

                                            else:
                                                messagebox.showwarning(title='Warning',
                                                                       message="Click Checkbox otherwise you can't proceed")

                                        win = Tk()
                                        win.attributes('-fullscreen', True)

                                        Label(win,
                                              text='myAadhaar',
                                              font=('Arial', 30, 'bold'),
                                              padx=10,
                                              pady=20,
                                              fg='white',
                                              bg=dark_blue
                                              ).pack(fill=BOTH)

                                        frame5 = Frame(win,
                                                       bg='white',
                                                       bd=2,
                                                       relief=SOLID,
                                                       height=480,
                                                       width=480)
                                        frame5.place(x=275, y=150)
                                        frame5.pack_propagate(False)
                                        Label(frame5,
                                              text="Terms & Conditions\n"
                                                   "You won't be able to change details in address like\n"
                                                   "State, City, Pincode, etc.\n"
                                                   "Only minute changes are applicable.",
                                              font=("Arial", 15),
                                              bg=light_blue,
                                              fg='black'
                                              ).pack(fill=BOTH, expand=True)
                                        Label(frame5, bg='white',
                                              text="Landlord's Address is:\n"
                                                   "Apartment No. 12-A, 5th Floor, South Royal Society\n"
                                                   "DumDum Road, Kolkata, West Bengal, 123456",
                                              font=('Helvetica', 14, 'bold'),
                                              fg='red').pack(fill=BOTH, expand=True)
                                        z = BooleanVar()

                                        Checkbutton(frame5,
                                                    text='I agree to Terms & Conditions.',
                                                    font=('Arial', 20, 'italic'),
                                                    onvalue=True,
                                                    offvalue=False,
                                                    variable=z,
                                                    fg='black', bg=light_blue,
                                                    activeforeground='black',
                                                    activebackground=light_blue,
                                                    ).pack(fill=BOTH, expand=True)
                                        Button(win,
                                               text='Next',
                                               font=('Arial', 15),
                                               bg=dark_blue,
                                               fg='white',
                                               activeforeground='white', padx=5, pady=5,
                                               activebackground=dark_blue,
                                               command=let_go).place(x=475, y=650)

                                        win.mainloop()

                                    else:
                                        messagebox.showerror(title='Invalid', message='Incorrect OTP')

                                w = Tk()
                                w.attributes('-fullscreen', True)

                                Label(w,
                                      text='myAadhaar Verification',
                                      font=('Arial', 30, 'bold'),
                                      padx=10,
                                      pady=20,
                                      fg='white',
                                      bg=dark_blue
                                      ).pack(fill=BOTH)

                                frame9 = Frame(w,
                                               bg='white',
                                               bd=2,
                                               relief=SOLID,
                                               height=480,
                                               width=480)
                                frame9.place(x=275, y=150)
                                frame9.pack_propagate(False)
                                Label(frame9,
                                      text="Check your Mail for OTP",
                                      font=("Arial", 20),
                                      fg='white',
                                      bg=dark_blue,
                                      pady=7
                                      ).pack(fill=BOTH)
                                Label(frame9,
                                      text='Wait for the Response of your Landlord.\n '
                                           'Once he Agree, You will get OTP',
                                      font=("Arial", 15),
                                      fg='black',
                                      bg='white',
                                      pady=10
                                      ).pack(fill=BOTH, expand=True)
                                otp2_tf = Entry(frame9,
                                                font=('Arial', 28),
                                                fg='black',
                                                justify=CENTER,
                                                width=20, bd=3,
                                                bg='white')
                                otp2_tf.insert(0, 'Enter OTP')
                                otp2_tf.config(state=DISABLED)
                                otp2_tf.bind("<Button-1>", click_o)
                                otp2_tf.pack(expand=True)
                                Button(frame9, text='Submit', fg='white', bg=dark_blue,
                                       font=('Arial', 15),
                                       activeforeground='white',
                                       activebackground=dark_blue,
                                       command=done2
                                       ).pack(expand=True)

                                Label(w, text=otp2, font=('Arial', 20, 'italic'),
                                      fg='black',
                                      bg='white',
                                      width=5).place(x=2, y=2)
                                w.mainloop()

                            else:
                                messagebox.showwarning(title='Warning', message='Click Checkbox')

                        w3 = Tk()
                        w3.attributes('-fullscreen', True)
                        Label(w3,
                              text='Enter Details of \n Landlord / Address Holder',
                              font=('Helvetica', 20, 'bold'),
                              bg=dark_blue,
                              fg='white',
                              width=50,
                              pady=20).place(x=87, y=100)

                        Label(w3,
                              text='Name: ',
                              font=('Cambridge', 20, 'underline', 'bold'),
                              fg='black', anchor=W,
                              width=20, padx=10, pady=10).place(x=200, y=250)

                        Label(w3,
                              text='Phone Number: ',
                              font=('Cambridge', 20, 'underline', 'bold'),
                              fg='black', anchor=W,
                              width=20, padx=10, pady=10).place(x=200, y=350)

                        Label(w3,
                              text='Relation: ',
                              font=('Cambridge', 20, 'underline', 'bold'),
                              fg='black', anchor=W,
                              width=20, padx=10, pady=10).place(x=200, y=450)

                        name = Entry(w3,
                                     font=('Cambridge', 30, 'bold'),
                                     fg='black', justify=CENTER,
                                     width=20
                                     )
                        name.place(x=480, y=253)

                        number2 = Entry(w3,
                                        font=('Cambridge', 30, 'bold'),
                                        fg='black',
                                        width=20, justify=CENTER
                                        )
                        number2.place(x=480, y=353)
                        Entry(w3,
                              font=('Cambridge', 30, 'bold'),
                              fg='black',
                              width=20, justify=CENTER
                              ).place(x=480, y=453)

                        y = BooleanVar()

                        Checkbutton(w3,
                                    text='I am not a Robot.',
                                    font=('Arial', 25, 'italic'),
                                    onvalue=True,
                                    offvalue=False,
                                    variable=y,
                                    fg='black', bd=5,
                                    activeforeground='black',
                                    width=30, relief=RAISED,
                                    command=check).place(x=225, y=553)

                        Button(w3,
                               text='Submit',
                               font=('Helvetica', 20, 'bold'),
                               fg='white',
                               bg=dark_blue,
                               width=8,
                               pady=5,
                               padx=5,
                               command=submit4).place(x=425, y=653)

                        w3.mainloop()

                    w4 = Tk()
                    w4.attributes('-fullscreen', True)

                    Label(w4,
                          text='Update Address',
                          font=('Arial', 30, 'bold'),
                          padx=10,
                          pady=20,
                          fg='white',
                          bg=dark_blue
                          ).pack(fill=BOTH)

                    frame1 = Frame(w4,
                                   bg='white',
                                   height=120,
                                   bd=4,
                                   relief=SUNKEN,
                                   width=500)
                    frame1.place(x=262, y=100)
                    frame1.pack_propagate(False)
                    Label(frame1,
                          text='Current Details',
                          font=('Arial', 11, 'bold'),
                          fg=dark_blue,
                          bg='white').place(x=1, y=9)
                    Label(frame1,
                          text='Current Address:',
                          font=('Arial', 8),
                          fg='black',
                          bg='white').place(x=1, y=40)
                    Label(frame1,
                          text="S/O: (Father's name here), H.No.50-C, Martin Royal, Canal Street,",
                          font=('Arial', 11),
                          fg='green',
                          bg='white').place(x=0, y=60)
                    Label(frame1,
                          text="North 24 Parganas, Kolkata, West Bengal, 123456",
                          font=('Arial', 11),
                          fg='green',
                          bg='white').place(x=0, y=81)
                    frame2 = Frame(w4,
                                   bg='white',
                                   height=460,
                                   bd=4,
                                   relief=SUNKEN,
                                   width=500)
                    frame2.place(x=262, y=245)
                    frame2.pack_propagate(False)
                    Label(frame2,
                          text='Details to be Updated',
                          font=('Arial', 11, 'bold'),
                          fg=dark_blue,
                          bg='white').place(x=1, y=5)
                    entry1 = Entry(frame2,
                                   font=('Arial', 18),
                                   fg='black',
                                   width=30, bd=1,
                                   bg='white')
                    entry1.insert(0, 'Care of')
                    entry1.config(state=DISABLED)
                    entry1.bind("<Button-1>", click1)
                    entry1.place(x=20, y=50)

                    entry2 = Entry(frame2,
                                   font=('Arial', 18),
                                   fg='black',
                                   width=30, bd=1,
                                   bg='white')
                    entry2.insert(0, 'House/Building/Apartment')
                    entry2.config(state=DISABLED)
                    entry2.bind("<Button-1>", click2)
                    entry2.place(x=20, y=95)

                    entry3 = Entry(frame2,
                                   font=('Arial', 18),
                                   fg='black',
                                   width=30, bd=1,
                                   bg='white')
                    entry3.insert(0, 'Street/Road/Lane')
                    entry3.config(state=DISABLED)
                    entry3.bind("<Button-1>", click3)
                    entry3.place(x=20, y=140)

                    entry4 = Entry(frame2,
                                   font=('Arial', 18),
                                   fg='black',
                                   width=30, bd=1,
                                   bg='white')
                    entry4.insert(0, 'Area/Locality/Sector')
                    entry4.config(state=DISABLED)
                    entry4.bind("<Button-1>", click4)
                    entry4.place(x=20, y=185)

                    entry5 = Entry(frame2,
                                   font=('Arial', 18),
                                   fg='black',
                                   width=30, bd=1,
                                   bg='white')
                    entry5.insert(0, 'Landmark')
                    entry5.config(state=DISABLED)
                    entry5.bind("<Button-1>", click5)
                    entry5.place(x=20, y=230)

                    entry6 = Entry(frame2,
                                   font=('Arial', 18),
                                   fg='black',
                                   width=30, bd=1,
                                   bg='white')
                    entry6.insert(0, 'Pincode')
                    entry6.config(state=DISABLED)
                    entry6.bind("<Button-1>", click6)
                    entry6.place(x=20, y=275)

                    entry7 = Entry(frame2,
                                   font=('Arial', 18),
                                   fg='black',
                                   width=30, bd=1,
                                   bg='white')
                    entry7.insert(0, 'Village/Town/City')
                    entry7.config(state=DISABLED)
                    entry7.bind("<Button-1>", click7)
                    entry7.place(x=20, y=320)

                    entry8 = Entry(frame2,
                                   font=('Arial', 18),
                                   fg='black',
                                   width=30, bd=1,
                                   bg='white')
                    entry8.insert(0, 'District')
                    entry8.config(state=DISABLED)
                    entry8.bind("<Button-1>", click8)
                    entry8.place(x=20, y=365)

                    entry9 = Entry(frame2,
                                   font=('Arial', 18),
                                   fg='black',
                                   width=30, bd=1,
                                   bg='white')
                    entry9.insert(0, 'State')
                    entry9.config(state=DISABLED)
                    entry9.bind("<Button-1>", click9)
                    entry9.place(x=20, y=410)

                    Button(w4,
                           text='Next',
                           font=('Arial', 12),
                           bg=dark_blue,
                           fg='white',
                           activeforeground='white',
                           activebackground=dark_blue,
                           command=next1
                           ).place(x=717, y=710)
                    Button(w4,
                           text="You don't reside here? Click to use Other's Address",
                           font=('Arial', 12),
                           bg=dark_blue,
                           fg='white',
                           activeforeground='white',
                           activebackground=dark_blue,
                           command=other
                           ).place(x=262, y=710)
                    w4.mainloop()

                else:
                    messagebox.askretrycancel(title='Invalid', message='Select one option before clicking.')

            def order():
                if x.get() == 0:
                    messagebox.showinfo(title='Unavailable',
                                        message='I only understand English language.')
                elif x.get() == 1:
                    messagebox.showinfo(title='Unavailable',
                                        message="I can't help you with this right now.")
                elif x.get() == 2:
                    messagebox.showinfo(title='Unavailable',
                                        message="I can't help you with this right now.")
                elif x.get() == 3:
                    messagebox.showinfo(title='Unavailable',
                                        message='Are you not sure about your Gender huh?')

            w6 = Tk()
            w6.attributes('-fullscreen', True)

            Label(w6,
                  text='Select any of the following Aadhaar data field to update.',
                  font=('Helvetica', 15),
                  fg='black',
                  pady=50).pack()

            frame = Frame(w6, height=600, width=500, bg='white')
            frame.place(x=300, y=100)

            avail = ['Language', 'Name', 'Date of Birth', 'Gender', 'Address']
            x = IntVar()

            for i in range(len(avail)):
                radiobutton = Radiobutton(frame,
                                          text=avail[i],
                                          variable=x,
                                          value=i,
                                          font=('Helvetica', 10, 'bold'),
                                          fg=dark_blue,
                                          activebackground=light_blue,
                                          activeforeground=dark_blue,
                                          width=50,
                                          indicatoron=0,
                                          height=5,
                                          command=order)
                radiobutton.pack()

            Label(w6,
                  text='Keep Valid Documents related to PoI / PoB for Uploading.',
                  font=('Helvetica', 10),
                  width=60,
                  fg=dark_blue).place(x=265, y=570)

            Button(w6,
                   text='Proceed to Update Aadhaar',
                   font=('Helvetica', 15),
                   bg=dark_blue,
                   fg='white',
                   width=50,
                   pady=10,
                   command=proceed).place(x=215, y=610)
            w6.mainloop()

        window = Tk()
        window.attributes('-fullscreen', True)

        Label(window, text='myAadhaar \n One portal for all online services',
              font=('Helvetica', 35),
              fg='white',
              bg=dark_blue,
              width=50,
              pady=20
              ).pack()

        Label(window,
              text='Get Aadhaar \n Aadhaar is for every resident of India.',
              font=('Helvetica', 20, 'bold'),
              fg='white',
              bg=light_blue,
              padx=40,
              pady=40,
              width=30).place(x=60, y=180)

        Label(window,
              text='Update Aadhaar \n Keep your Aadhaar details up-to-date.',
              font=('Helvetica', 20, 'bold'),
              fg='white',
              bg=light_blue,
              padx=40,
              pady=40,
              width=30).place(x=60, y=380)

        Label(window,
              text='Aadhaar Services \n An array of services for Aadhaar holders.',
              font=('Helvetica', 20, 'bold'),
              fg='white',
              bg=light_blue,
              padx=40,
              pady=40,
              width=30).place(x=60, y=580)

        Button(window,
               text='Click here ',
               font=('Helvetica', 15, 'italic'),
               fg='white',
               bg=dark_blue,
               padx=40,
               pady=40,
               width=10, relief=SUNKEN,
               command=sample_one,
               ).place(x=750, y=195)

        Button(window,
               text='Click here ',
               font=('Helvetica', 15, 'italic'),
               fg='white',
               bg=dark_blue,
               padx=40,
               pady=40, relief=SUNKEN,
               width=10,
               command=update_aadhaar
               ).place(x=750, y=395)

        Button(window,
               text='Click here ',
               font=('Helvetica', 15, 'italic'),
               fg='white',
               bg=dark_blue,
               padx=40,
               pady=40,
               width=10, relief=SUNKEN,
               command=sample_two
               ).place(x=750, y=595)
        window.mainloop()

    else:
        messagebox.showwarning(title='Invalid', message='OTP is Incorrect.')


def check_num():
    num = str(num_tf.get())
    if len(num) == 10:
        messagebox.showinfo(title='Validated', message='Number is correct.')
    else:
        messagebox.showwarning(title='Invalid', message='Number is Incorrect.')


def check_captcha():
    entered_captcha = captcha_tf.get()
    if entered_captcha == captcha:
        messagebox.showinfo(message='Correct Captcha')

    else:
        messagebox.showerror(message='Incorrect Captcha')


w7 = Tk()
w7.geometry('1180x1000')
w7.attributes('-fullscreen', True)

Label(w7,
      text='Welcome to myAadhaar',
      font=('Arial', 30, 'bold'),
      padx=10,
      pady=20,
      fg='white',
      bg=dark_blue
      ).pack(fill=BOTH)

Label(w7,
      text='LOGIN',
      font=('Helvetica', 30, 'bold'),
      width=10,
      padx=10,
      pady=10,
      fg='white',
      bg=dark_blue
      ).place(x=375, y=110)

Label(w7,
      text='Enter Phone Number',
      font=('Helvetica', 20, 'bold'),
      width=20,
      padx=10,
      pady=10,
      fg='black',
      bg=light_blue
      ).place(x=130, y=210)
Label(w7,
      text='Enter Captcha',
      font=('Helvetica', 20, 'bold'),
      width=20,
      padx=10,
      pady=10,
      fg='black',
      bg=light_blue
      ).place(x=130, y=467)
Label(w7,
      text='Enter Email',
      font=('Helvetica', 20, 'bold'),
      width=20,
      padx=10,
      pady=10,
      fg='black',
      bg=light_blue
      ).place(x=130, y=337)

Label(w7,
      text='Enter OTP',
      font=('Helvetica', 20, 'bold'),
      width=20,
      padx=10,
      pady=10,
      fg='black',
      bg=light_blue
      ).place(x=130, y=600)
num_tf = Entry(w7,
               font=('Arial', 30, 'bold'),
               width=15, relief=RAISED,
               fg='black',
               justify=CENTER
               )
num_tf.place(x=510, y=213)
email_tf = Entry(w7,
                 font=('Arial', 10, 'bold'),
                 width=47, relief=RAISED,
                 fg='black',
                 justify=CENTER
                 )
email_tf.place(x=510, y=355)

captcha_tf = Entry(w7,
                   font=('Arial', 30, 'bold'),
                   width=15, relief=RAISED,
                   fg='black', )
captcha_tf.place(x=510, y=468)
otp_tf = Entry(w7,
               font=('Arial', 30, 'bold'),
               width=15, relief=RAISED,
               fg='black',
               justify=CENTER
               )
otp_tf.place(x=510, y=602)
captcha_built = Label(w7,
                      text=captcha,
                      font=('Helvetica', 20, 'italic'),
                      width=8,
                      padx=10,
                      pady=7, relief=RAISED,
                      fg='white',
                      bg=dark_blue)
captcha_built.place(x=691, y=468)
Button(w7,
       text='Submit',
       font=('Helvetica', 25),
       fg='white',
       bg=dark_blue,
       activeforeground='white',
       activebackground=dark_blue,
       width=10,
       padx=3,
       pady=3,
       command=submit).place(x=405, y=680)
Button(w7,
       text='Check Number',
       font=('Helvetica', 15),
       fg='black',
       activeforeground='black',
       width=15,
       padx=3,
       pady=3,
       command=check_num).place(x=665, y=270)
Button(w7,
       text='Check Captcha',
       font=('Helvetica', 15),
       fg='black',
       activeforeground='black',
       width=15,
       padx=3,
       pady=3,
       command=check_captcha).place(x=665, y=525)
Button(w7,
       text='Send OTP',
       font=('Helvetica', 15),
       fg='black',
       activeforeground='black',
       width=15,
       padx=3,
       pady=3,
       command=send_otp).place(x=665, y=658)

