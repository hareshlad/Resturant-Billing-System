from tkinter import *
from tkinter import messagebox
import sqlite3
import re
import time
import random
import datetime

window = Tk()
counter1 = IntVar()
counter2 = IntVar()
counter3 = IntVar()
counter4 = IntVar()
counter5 = IntVar()
counter6 = IntVar()
counter7 = IntVar()
totalx=IntVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%y%H:%M:%S"))

ReceiptCal_F = Frame(window,bg='orange',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=BOTTOM)
Receipt_Ref = StringVar()
Receipt_F=Frame(ReceiptCal_F,bg='orange',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)
def onClick1(event=None):
		counter1.set(counter1.get() + 1)
		c1=counter1.get()
		c1s=str(c1)
		print(c1s)
def onClick2(event=None):
		counter2.set(counter2.get() + 1)
		c2=counter2.get()
		c1s=str(c2)
		print(c1s)
    
def onClick3(event=None):
		counter3.set(counter3.get() + 1)
	   
		c3=counter3.get()
		c1s=str(c3)
		print(c1s)
def onClick4(event=None):
		counter4.set(counter4.get() + 1)
		c4=counter4.get()
		c1s=str(c4)
		print(c1s)
    
def onClick5(event=None):
		counter5.set(counter5.get() + 1)
		c5=counter5.get()
		c1s=str(c5)
		print(c1s)

def onClick6(event=None):
		counter6.set(counter6.get() + 1)
		c6=counter6.get()
		c1s=str(c6)
		print(c1s)
def onClick7(event=None):
		counter7.set(counter7.get() + 1)
		c7=counter7.get()
		c1s=str(c7)
		print(c1s)
            
def total():
    o1=e1.get()
    o2=e2.get()
    o3=e3.get()
    o4=e4.get()
    o5=e5.get()
    o6=e6.get()
    o7=e7.get()
    o1r=int(o1)
    o2r=int(o2)
    o3r=int(o3)
    o4r=int(o4)
    o5r=int(o5)
    o6r=int(o6)
    o7r=int(o7)
    r1=o1r*250
    r2=o2r*199
    r3=o3r*350
    r4=o4r*450
    r5=o5r*150
    r6=o6r*50
    r7=o7r*130
    totalx.set(r1+r2+r3+r4+r5+r6+r7)




def message():
					
					scr1=Tk()
					L=Label(scr1,text="BILL")
					
					DateofOrder = StringVar()
					DateofOrder.set(time.strftime("%d/%m/%y%H:%M:%S"))
					
					ReceiptCal_F = Frame(scr1,bg='orange',bd=5,relief=RIDGE)
					ReceiptCal_F.pack(side=BOTTOM)
					Receipt_Ref = StringVar()
					Receipt_F=Frame(ReceiptCal_F,bg='orange',bd=10,relief=RIDGE)
					Receipt_F.pack(side=BOTTOM)
					
					def total():
							o1=e1.get()
							o2=e2.get()
							o3=e3.get()
							o4=e4.get()
							o5=e5.get()
							o6=e6.get()
							o7=e7.get()
							
							o1r=int(o1)
							o2r=int(o2)
							o3r=int(o3)
							o4r=int(o4)
							o5r=int(o5)
							o6r=int(o6)
							o7r=int(o7)
							r1=o1r*250
							r2=o2r*199
							r3=o3r*350
							r4=o4r*450
							r5=o5r*150
							r6=o6r*50
							r7=o7r*130
							totalx.set(r1+r2+r3+r4+r5+r6+r7)
					def bill():
					
							txtReceipt.delete("1.0",END)
							x=random.randint(10,20)
							randomRef= str(x)
							Receipt_Ref.set("Bill"+ randomRef)
							

						
							txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get()+'\n')
							txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
							txtReceipt.insert(END,'Loaded Chicken:\t\t\t\t\t' + e1.get() +'\n')
							txtReceipt.insert(END,'Deluxe:\t\t\t\t\t'+ e2.get()+'\n')
							txtReceipt.insert(END,'Extravaganza:\t\t\t\t\t'+ e3.get()+'\n')
							txtReceipt.insert(END,'Extravaganza:\t\t\t\t\t'+ e4.get()+'\n')
							txtReceipt.insert(END,'Chicken Tikka:\t\t\t\t\t'+ e5.get()+'\n')
							txtReceipt.insert(END,'Water:\t\t\t\t\t'+ e6.get()+'\n')
							txtReceipt.insert(END,'Coke:\t\t\t\t\t'+ e7.get()+'\n')
							
					
							txtReceipt.insert(END,'Total cost'+str(totalx.get())+"\n")
							txtReceipt.insert(END,'Name:\t\t\t'+text1.get())
							
					txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
					txtReceipt.grid(row=0,column=0)
					
					txtReceipt.delete("1.0",END)
					x=random.randint(10908,500876)
					randomRef= str(x)
					Receipt_Ref.set("Bill"+ randomRef)

						
					txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
					txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
					txtReceipt.insert(END,'Sprite:\t\t\t\t\t' + e1.get() +'\n')
					txtReceipt.insert(END,'Pepsi:\t\t\t\t\t'+ e2.get()+'\n')
					txtReceipt.insert(END,'DietCoke:\t\t\t\t\t'+ e3.get()+'\n')
					txtReceipt.insert(END,'Mojito:\t\t\t\t\t'+ e4.get()+'\n')
					txtReceipt.insert(END,'Cappuccino:\t\t\t\t\t'+ e5.get()+'\n')
					txtReceipt.insert(END,'Fanta:\t\t\t\t\t'+ e6.get()+'\n')
					txtReceipt.insert(END,'CocaCola:\t\t\t\t\t'+ e7.get()+'\n')
					txtReceipt.insert(END,'Total cost'+str(totalx.get())+"\n")
					txtReceipt.insert(END,'Name:\t'+text1.get()+'\n')
					txtReceipt.insert(END,'Mobile:\t'+text2.get())
					
					
					
					L.pack()
					
					scr1.mainloop()
							
					
					
		
	
		

def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''    

def clrbut():
     textin.set('')

     
def Clear():
		
		text1.delete(0,END)
		text2.delete(0,END)
		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)
		e5.delete(0,END)
		e6.delete(0,END)
		e7.delete(0,END)
		


def Submit():
    
		
		Name1=text1.get()
		Name1=str(Name1)
		Contact1=text2.get()
		Contact1=str(Contact1)
		
		conn = sqlite3.connect('customer.db')
		with conn:
			cursor=conn.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS Form(Name TEXT,Contact TEXT,ordertime DATETIME 
     
    )''')
		cursor.execute("INSERT INTO form VALUES('%s','%s', CURRENT_TIMESTAMP)"%(text1.get(),text2.get()))
		conn.commit()
		if len(Contact1)!= 10 or (not Name1.isdigit()):
   
			messagebox.showinfo("Welcome","Data is entered sucessfully ")

photo = PhotoImage(file =r"no-LoadedL.png") 
Button(window, text = 'Click Me !', image = photo,command=onClick1).place(x=20,y=350)
Label3=Label(window,text="Loaded Chicken",fg='black',font=("Times New roman",10,"bold"),width=15)
Label3.place(x=25,y=480)
e1 = Entry(window, bd =1  , bg = "white",width=3,textvariable=counter1,font=('ariel' ,10))
e1.place(x = 70, y =500)






photo1 = PhotoImage(file =r"deluxe.png") 
Button(window, text = 'Click Me !', image = photo1,command=onClick2).place(x=150,y=350)
Label4=Label(window,text="Deluxe",fg='black',font=("Times New roman",10,"bold"),width=15)
Label4.place(x=150,y=480)

e2 = Entry(window, bd =1  , bg = "white",width=3,textvariable=counter2,font=('ariel' ,10))
e2.place(x = 190, y =500)


photo2 = PhotoImage(file =r"extravaganza.png") 
Button(window, text = 'Click Me !', image = photo2,command=onClick3).place(x=280,y=350)
Label5=Label(window,text="Extravaganza",fg='black',font=("Times New roman",10,"bold"),width=15)
Label5.place(x=285,y=480)
e3 = Entry(window, bd =1  , bg = "white",width=3,textvariable=counter3,font=('ariel' ,10))
e3.place(x = 330, y =500)

photo3 = PhotoImage(file =r"Non-Veg_Supreme.png") 
Button(window, text = 'Click Me !', image = photo3,command=onClick4).place(x=20,y=530)
Label8=Label(window,text="Non-veg Supreme",fg='black',font=("Times New roman",10,"bold"),width=15)
Label8.place(x=25,y=650)
e4 = Entry(window, bd =1  , bg = "white",width=3,textvariable=counter4,font=('ariel' ,10))
e4.place(x = 70, y =680)

photo4 = PhotoImage(file =r"nonChicken_Tikka.png") 
Button(window, text = 'Click Me !', image = photo4,command=onClick5).place(x=150,y=530)
Label9=Label(window,text="Chicken Tikka",fg='black',font=("Times New roman",10,"bold"),width=15)
Label9.place(x=150,y=650)
e5 = Entry(window, bd =1  , bg = "white",width=3,textvariable=counter5,font=('ariel' ,10))
e5.place(x = 190, y =680)

photo5 = PhotoImage(file =r"water.png") 
Button(window, text = 'Click Me !', image = photo5,command=onClick6).place(x=430,y=350)
Label6=Label(window,text="Water",fg='black',font=("Times New roman",10,"bold"),width=15)
Label6.place(x=420,y=480)
e6 = Entry(window, bd =1  , bg = "white",width=3,textvariable=counter6,font=('ariel' ,10))
e6.place(x = 460, y =500)

photo6 = PhotoImage(file =r"coke.png") 
Button(window, text = 'Click Me !', image = photo6,command=onClick7).place(x=550 ,y=350)


Label7=Label(window,text="Coke",fg='black',font=("Times New roman",10,"bold"),width=15)
Label7.place(x=550,y=480)
e7 = Entry(window, bd =1  , bg = "white",width=3,textvariable=counter7,font=('ariel' ,10))
e7.place(x = 590, y =500)

Total=Button(window,text="Total",fg='white',bg='Brown',width=20,command=total)
Total.place(x=450,y=600)
L1 = Entry(window , bd = 1  , bg = "white",width=5,textvariable=totalx,font=('ariel' ,10,))
L1.place(x = 650, y =600)


textin=StringVar()
operator=""



	

window.geometry('1200x800')


window.title("Welcome to Pappi Pet")

Name=StringVar()
Contact = StringVar()

Label0 =Label(window, text = 'Pappi Pet', font = ('Comic Sans MS',40),
 bg = 'firebrick', fg = 'white',width=40)
Label0.place(x=0,y=0)



Label1=Label(window,text="Name:",fg='blue',font=("Times New roman",14,"bold"),width=10)
Label1.place(x=50,y=100)

text1=Entry(window,font=("Times New Roman",20,"bold"),width=20)
text1.place(x=300,y=100)







Label2=Label(window,text="Phone Number:",fg='blue',font=("Times New roman",14,"bold"),width=14)
Label2.place(x=50,y=200)
text2=Entry(window,font=("Times New Roman",20,"bold"),width=20)
text2.place(x=300,y=200)

Submit=Button(window,text="Submit",fg='white',bg='Brown',width=20,command=Submit)
Submit.place(x=300,y=300)

windowtext=Entry(window,font=("Courier New",12,'bold'),textvar=textin,width=32,bd=5,bg='powder blue')
windowtext.place(x=800,y=70)

but1=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=800,y=100)

but2=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=800,y=170)

but3=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=800,y=240)

but4=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=865,y=100)

but5=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=865,y=170)

but6=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=865,y=240)

but7=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=930,y=100)

but8=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=930,y=170)

but9=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=930,y=240)

but0=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=800,y=310)

butdot=Button(window,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=865,y=310)

butpl=Button(window,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=995,y=100)

butsub=Button(window,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=995,y=170)

butml=Button(window,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butml.place(x=995,y=240)

butdiv=Button(window,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=995,y=310)

butclear=Button(window,padx=14,pady=119,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=1057,y=100)

butequal=Button(window,padx=151,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=800,y=380)


    
Bill=Button(window,text="Bill",fg='white',bg='Brown',width=20,command=message)
Bill.place(x=800,y=600)


Clear=Button(window,text="Clear",fg='white',bg='Brown',width=20,command=Clear)
Clear.place(x=980,y=600) 




window.mainloop()
