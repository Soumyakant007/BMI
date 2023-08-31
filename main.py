from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root=Tk()
root.title("BMI calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")
root.attributes('-fullscreen',True)


def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)
    if bmi<=18.5:
        label2.config(text="Underweight!")
        label3.config(text="You have lower weight than normal!")
    elif bmi>18.5 and bmi<=25:
        label2.config(text="Normal!")
        label3.config(text="It indicates that you are healthy!")
    elif bmi>25 and bmi<=30:
        label2.config(text="OverWeight!")
        label3.config(text="It indicates that a person is \n slightly overweight! \n A doctor may advise to lose some weight \n for health resons!")
    else:
        label2.config(text="Obese!")
        label3.config(text="Health may be at risk \n if they do not lose weight!")

#icon
image_icon=PhotoImage (file="Images/icon.png")
root.iconphoto (False,image_icon)


new_width=root.winfo_screenwidth()

#top
top=Image.open("Images/download.png")

top=top.resize((1920,310),Image.LANCZOS)
top_image=ImageTk.PhotoImage(top)
top_image_lab=Label(root, image=top_image, background="#f0f1f5")
top_image_lab.place(x=-10,y=-10)

#bottom box
Label (root, width=72,height=50, bg="lightblue",borderwidth=8,relief="groove").place(x=10,y=311)
#two boxes
box=Image.open("Images/box.png")
box_tk=ImageTk.PhotoImage(box)
Label(root,image=box_tk).place(x=650,y=500)
Label (root, image=box_tk). place(x=1200,y=500)
#scale
scale=Image.open("Images/scale .png")
scale_tk=ImageTk.PhotoImage(scale)
Label(root, image=scale_tk, bg="lightblue").place(x=20,y=330)

#######Slider1##### ######


current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed (event):
    Height.set(get_current_value())
    size=int(float(get_current_value()))
    img= (Image.open("Images/man.png"))
    resized_image=img.resize((200,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=200, y=710-size)
    secondimage.image=photo2
#Command to chnage background color of scale
style= ttk.Style()
style.configure("TScale", background="white")
slider=ttk.Scale(root, from_=0, to=390, orient='horizontal', style="TScale",
                command=slider_changed, variable=current_value,length=300)
slider.place(x=775, y=700)



#########Slider2########

current_value2= tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())
    
#Command to chnage background color of scale
style2= ttk.Style()
style2.configure("TScale", background="white")
slider2=ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale",
                command=slider_changed2, variable=current_value2, length=300)
slider2.place(x=1325, y=700)

#Entry box
Height=StringVar()
Weight=StringVar()
#height label
Label(root,text="Height", font='georgia 20', bg="#fff",fg="#000",bd=0, justify=CENTER).place(x=860,y=540)
height=Entry(root,textvariable=Height, width=5, font='georgia 45', bg="#fff",fg="#000",bd=0, justify=CENTER) #to align text 
height.place(x=800, y=600)
Height.set(get_current_value())

Label(root,text="Weight", font='georgia 20', bg="#fff",fg="#000",bd=0, justify=CENTER).place(x=1410,y=540)
weight=Entry(root, textvariable=Weight, width=5, font='georgia 45', bg="#fff",fg="#000",bd=0, justify=CENTER) #to align text 
weight.place(x=1350,y=600)
Weight.set(get_current_value2())

#manimg

secondimage = Label(root, bg="lightblue")
secondimage.place(x=200,y=530)



Button(root,text="View Report",width=20,height=4,font="georgia 15 bold",bg="#1f6e68",fg="white",command=BMI,borderwidth=6,relief="raised").place(x=1020,y=800)



label1=Label(root, font="georgia 70 bold", bg="lightblue",fg="#fff")
label1.place(x=150, y=735)
label2=Label (root, font="georgia 35 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=120, y=900)
label3=Label(root,font="georgia 15 bold",bg="lightblue")
label3.place(x=100,y=1000)

root.mainloop()
