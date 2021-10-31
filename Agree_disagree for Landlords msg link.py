# I explained everything about this module in the video
# Please check it out its must
# If you guys liked my project then i will work on this backend part
# I just gave you the idea that
# A message will be sent to landlord with a link
# Once he clicked on it he will redirect to this page
# If he agreed OTP will be sent back to us via email
# That we can use in our main project as verication agreement and login#

from tkinter import *
from tkinter import messagebox

dark_blue = '#28118f'
light_blue = '#23c3eb'


def agree():
    messagebox.showinfo(title='Agreed', message='OTP is Sent to them through Email.')
    pass


def disagree():
    messagebox.showinfo(title='Disagreed', message='You disagreed.')
    w9.destroy()


w9 = Tk()
w9.attributes('-fullscreen', True)
Label(w9,
      text='myAadhaar',
      font=('Arial', 30, 'bold'),
      padx=10,
      pady=20,
      fg='white',
      bg=dark_blue
      ).pack(fill=BOTH)
Label(w9, text='Do you want to Allow?\n To use your Address for Updation',
      font=('Arial', 30, 'bold'),
      padx=5,
      pady=50,
      fg='black'
      ).pack()
Button(w9, text='Agree', font=('Arial', 30, 'bold'),
       padx=5,
       pady=5,
       fg='white', width=10, command=agree,
       bg=light_blue).place(x=200, y=300)

Button(w9, text='Disagree', font=('Arial', 30, 'bold'),
       padx=5,
       pady=5,
       fg='white', width=10, command=disagree,
       bg=light_blue).place(x=600, y=300)
w9.mainloop()
