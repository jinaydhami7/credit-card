# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:32:12 2022

@author: Nirav
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox 

root=Tk()
root.title("Credit Card Authentication")
root.geometry("600x400")

root.configure(background="gold")

input_box = Entry()
input_box.place(relx=0.5, rely=0.3, anchor = CENTER)

img=ImageTk.PhotoImage(Image.open ("credit.jpg"))
label = Label(root, image=img)

pin = 1234
def authentication():
   
          try: 
               input_value = int(input_box.get())
               if(pin == input_value):
                   messagebox.showinfo("Alert","Credit card accepted.")
          except:
                messagebox.showinfo("Alert","Credit card not accepted.")
             
btn = Button(root, text = "check credit card", command = authentication)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)
label.place(relx=0.5, rely=0.7, anchor = CENTER)

root.mainloop()