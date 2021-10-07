from tkinter import *
import os
root =Tk()

def wrt():
	if(not os.path.exists("log.txt")):
		with open("log.txt","w") as f:
			f.write(f"the name of the user is {userval.get()}\n"
			f"the number of the user is {phnval.get()}\n"
			f"the city of the user is {cityval.get()}\n"
			f"the email id of the user is {idval.get()}\n"
			f"the disability of the user is {disval.get()}\n\n")
	else:
		with open("log.txt","a") as f:
			f.write(f"the name of the user is {userval.get()}\n"
			f"the number of the user is {phnval.get()}\n"
			f"the city of the user is {cityval.get()}\n"
			f"the email id of the user is {idval.get()}\n"
			f"the disability of the user is {disval.get()}\n\n")



root.geometry("900x600")
Label(root,text="Welcome to fill your form",font ="aries 12 bold",pady = 8).grid(row=0,column=3)

#creating the names and packing them
User = Label(root,text="Name:").grid(row=1,column=2)
phn = Label(root,text="Number:").grid(row=2,column=2)
city = Label(root,text="city:").grid(row=3,column=2)
mail = Label(root,text="E-Mail ID:").grid(row=4,column=2)

#craeting variables for entry
userval = StringVar()
phnval = StringVar()
cityval = StringVar()
idval = StringVar()
disval = IntVar()

#creating entry widgets and packing the entries
userentry = Entry(root,textvariable=userval).grid(row=1,column=3)
phmentry = Entry(root,textvariable=phnval).grid(row=2,column=3)
cityentry = Entry(root,textvariable=cityval).grid(row=3,column=3)
identry = Entry(root,textvariable=idval).grid(row=4,column=3)

#creating checkbox
disserv = Checkbutton(text="Do you have any disability?",variable = disval).grid(row=5,column =3)

#crdating button
submit = Button(root,text ="SUBMIT",bg ="green",borderwidth = 3,command= wrt).grid(row=6,column =3)


root.mainloop()