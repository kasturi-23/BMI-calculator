#Bmi = (weight in kg)/(height in mtr)*2
import xlsxwriter as xw
import mysql.connector as mq
from tkinter.ttk import *
from tkinter import ttk
import datetime
import mysql.connector
from tkinter import *
from tkinter.messagebox import *
from time import strftime
def f1():
	root.withdraw()
	win.deiconify()
def f2():
	win.withdraw()
	bmical.deiconify()

def f3():
	bmical.withdraw()
	win.deiconify()

def f4():
	bmical.withdraw()
	convert.deiconify()
def f5():
	bmical.deiconify()
	convert.withdraw()
def convert1():
	try:
		s1=entfeet.get()
		s2=entinches.get()
		if (s1.isdigit())==True and (s2.isdigit())==True:
			if int(s1)>0 and int(s1)<=7:
				if int(s2)>=0 and int(s2)<=11:
					meter= 0.305* float(s1)+ 0.0254* float(s2)
					mter=round(meter,4)
					msg= "Height in feets to meter is"  +str(mter)+" meters"
					showinfo("Height ",msg)
				else:
					showerror("error","Inches can be only between 1 to 11")
			else:
				showerror("error","Feets can be only between 1 to 07")
		
		elif((s1.isalpha()==True) or (s2.isalpha()==True)):
			showerror("Error","invalid height")
		elif(s1.isalpha()==True):
			showerror("Error","invalid height")
		elif(s2.isalpha()==True):
			showerror("Error","invalid height")
		else:
			Showerror("Enter valid height")
	except ValueError :
		showerror("Error","Enter digits Only")
	except NameError:
		showerror("Error","Enter valid height")

def f6():
	win.withdraw()
	view_st.deiconify()
	my_connect = mysql.connector.connect(host= 'localhost', user= 'root',password = 'ABC456')
	cur = my_connect.cursor()					# connnection is done
	cur.execute("use BMI")
	cur.execute("select * from bmical2")
#cur.execute("select * from bmical2")
	v=Scrollbar(view_st)
	v.pack(side=RIGHT,fill=Y)
	tree= Treeview(view_st)  			
	tree['show']='headings'

	s=ttk.Style(view_st)
	s.theme_use("clam")
	
	tree["columns"] =("Name","Age","Phone_Number","Gender","Height","Weight","BMI","status")  # DEFINES NUMBER OF COLUMNS
	# assign width to the columns
	tree.column("Name",width=100,minwidth=50,anchor=CENTER)
	tree.column("Age",width=71,minwidth=50,anchor=CENTER)
	tree.column("Phone_Number",width=100,minwidth=50,anchor=CENTER)
	tree.column("Gender",width=71,minwidth=50,anchor=CENTER)
	tree.column("Height",width=71,minwidth=50,anchor=CENTER)
	tree.column("Weight",width=71,minwidth=50,anchor=CENTER)
	tree.column("BMI",width=90,minwidth=50,anchor=CENTER)
	tree.column("status",width=90,minwidth=50,anchor=CENTER)

	# Assign the heading names to yhe respective column
	tree.heading("Name",text="Name",anchor=CENTER)
	tree.heading("Age",text="Age",anchor=CENTER)
	tree.heading("Phone_Number",text="Phone Number",anchor=CENTER)
	tree.heading("Gender",text="Gender",anchor=CENTER)
	tree.heading("Height",text="Height",anchor=CENTER)
	tree.heading("Weight",text="Weight",anchor=CENTER)
	tree.heading("BMI",text="BMI",anchor=CENTER)
	tree.heading("status",text="Status",anchor=CENTER)
	i=0
	for ro in  cur:
		tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7]))
		i=i+1
	tree.pack()
	#data= cur.fetchall()
	#info = ""	
	my_connect.commit()
	my_connect.close()
	
	tree.config(yscrollcommand=v.set)
	v.config(command=tree.yview)
	#yscrollbar=ttk.Scrollbar(view_st,orient="vertical",command=tree.yview)			# scrollbar is created and  displayed vertically
	#yscrollbar.pack(side=RIGHT,fill='x')							# displays the scrollbar to the right
	btnback2=Button(view_st,text="Back",width=15,font=('arial', 14, 'bold'),command=f7)
	btnback2.pack(pady=10)

def f7():
	win.deiconify()
	view_st.withdraw()
def f8():
	win.deiconify()
	bmical.withdraw()

def sel():
	selection = "You selected the option " + str(var.get())
def bmi():
	try:
		my_connect = mysql.connector.connect(host= 'localhost', user= 'root',password = 'ABC456')
		cur = my_connect.cursor()					# connnection is done
		print("connected")
		cur.execute("Create database if not exists BMI")
		cur.execute("use BMI")
		print("Database created")
		cur.execute("create table if not exists bmical2( name char(40) not null,age int(3) not null,phoneno char(12) not null,gender char(8) not null, height float(10) not null,weight float(10) not null,bmi float(10) not null,status char(20) not null)")
		print("table created")
		a1= entname.get()
		a2= entage.get()
		a3 = entphone.get()
		a4= var.get()
		a5=entheight.get()
		a6=entweight.get()
		s1=entheight.get()
		s2=entweight.get()
		a=getdouble(s1)
		b= getdouble(s2)
		pno=str(a3)
		pno1=list(pno)
		p=len(pno1)
		name=list(a1)
		namelen=len(name)
		height=float(a5)
		weight=float(a6)
		str1="!@#$%^&*()_+-={}[]|';\/.,<>?|"
		ss1=list(str1)
		for ab in name:
			for ac in ss1:
				if(ab==ac):
					showerror("Error","Name should not contain special characters")
					break
				else:
					continue
		if(a1.isalpha())==True:
			if (namelen>=2)==True:
				if (a2.isdigit() and int(a2)>0)==True:
					if p == 10:
						if height>0.0 :
							if weight>0.0:
								bmi1 = b/(a**2)
								b=round(bmi1,4)
								bb=float(b)
								if bb<18.5:
									msg= "The bmi is " +format(b)+'\n'+"Underweight"
									x=str('underweight')
									cur.execute("insert into bmical2(name , age, phoneno,gender,height,weight,bmi,status) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(a1,a2,pno,a4,a5,a6,bmi1,x))
									showinfo("BMI",msg)
								elif bb>=18.5 and bb<=24.9:
									msg= "The bmi is " +format(b)+'\n'+"Normal"
									x=str('Normal')
									cur.execute("insert into bmical2(name , age, phoneno,gender,height,weight,bmi,status) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(a1,a2,pno,a4,a5,a6,bmi1,x))
									showinfo("BMI",msg)
								elif bb>25 and bb<=29.9:
									msg= "The bmi is " +format(b)+'\n'+"Overweight"
									x=str('Overweight')
									cur.execute("insert into bmical2(name , age, phoneno,gender,height,weight,bmi,status) values('{}','{}','{}','{}','{}','{}','{},'{}')".format(a1,a2,pno,a4,a5,a6,bmi1,x))
									showinfo("BMI",msg)
								
							else:
								showerror("Error","Weight cannot be negative")
						else:
							showerror("Error","Height cannot be negative")
					else:
						showwarning("Warning","Enter a valid phone number")
				else:
					showwarning("Warning","Age can be in digits only")
			else:
				showwarning("Error","Invalid name")
		elif(a1.isdigit())==True:
			show("Error","Name cannot be a digit")	
		
	except ValueError:
		showerror("Error","Enter appropriate data")
	except NameError:
		showerror("Error","Enter a valid data  ")
	finally:
		
		#cur.execute("insert into bmical2(name , age, phoneno,gender,height,weight,bmi) values('{}','{}','{}','{}','{}','{}','{}')".format(a1,a2,a3,a4,a5,a6,bmi1))
		#print("user data entered in table")
		my_connect.commit()
		my_connect.close()
def export():
	wb=xw.Workbook("Final.xlsx")
	sh= wb.add_worksheet("stud_list")
	conn=mq.connect(host="localhost",user="root",passwd="ABC456",database="bmi")
	cur=conn.cursor()
	query="select * from bmical2"
	cur.execute(query)
	res=cur.fetchall()
	row=0
	for k in res:
		for q in range(len(k)):
			sh.write(row,q,k[q])
		row=row+1
		msg="Count="+str(row)
	text2=Text(win,height=2,width=18,font=('arial',15,'bold'))
	text2.place(x=250,y=380)
	
	text2.insert(END,msg)
	text2.configure(state='disabled')
	showinfo("Exported","Data Exported")
	conn.close()
	wb.close()
	
def my_time():
	time_string=strftime('%H:%M:%S %p\n %A ')
	L1.config(text=time_string)
	L1.after(1000,my_time)

root = Tk()
root.title("Welcome")
root.geometry("700x400+300+200")


b1= Button(root,text="BMI Calculator",height=12,width=41,font=("arial",20,'bold'),command=f1)
b1.pack(pady=10)


win = Toplevel(root)
win.title("BMI Calculator")
win.geometry("700x600+300+100")

dt = datetime.datetime.now()
print(dt)
datee=dt.date()
print(datee)
datee1=str(datee)
h= dt.hour


if 6 <= h <= 11:
	msg ="              Good Morning             "+"\n          Date: "+datee1+"\n"
elif 12<= h  <16:
	msg = "            Good Afternoon           "+"\n         Date: "+datee1+"\n"
else:
	msg ="             Good Evening               " "\n           Date: "+datee1+"\n"
print(msg)
text1=Text(win,height=2,width=30,font=('arial',15,'bold'))
text1.pack(pady=10)
text1.insert(END,msg)
text1.configure(state='disabled')

L1=Label(win, width=15, font=('arial', 14, 'bold'))
L1.place(x=250,y=100)
my_time()
btn1 = Button(win, text="BMI Calculator", width=15,bg='#ADD8E6', font=('arial', 14, 'bold'),command=f2)
btn1.place(x=250,y=170)

btn2 = Button(win, text="View History", width=15,bg='#ADD8E6', font=('arial', 14, 'bold'),command=f6)
btn2.place(x=250,y=240)

btn3 = Button(win, text="Export data", width=15,bg='#ADD8E6', font=('arial', 14, 'bold'),command=export)
btn3.place(x=250,y=310)

win.withdraw() 
	
		
bmical= Toplevel(win)
bmical.title("BMI Calculator")
bmical.geometry("700x650+100+10")
label_name= Label(bmical, text="Enter name ",font=('arial', 14, 'bold' ))
label_name.place(x=20,y=10)
entname = Entry(bmical, bd=5, font=('arial', 18, 'bold' ))
entname.pack(pady=10)

label_age= Label(bmical, text="Enter age",font=('arial', 14, 'bold' ))
label_age.place(x=20,y=70)
entage = Entry(bmical, bd=5, font=('arial', 18, 'bold' ))
entage.pack(pady=10)

label_phoneno= Label(bmical, text="Enter phone ",font=('arial', 14, 'bold' ))
label_phoneno.place(x=20,y=130)
entphone = Entry(bmical, bd=5, font=('arial', 18, 'bold' ))
entphone.pack(pady=10)

var= StringVar()
label_gender= Label(bmical, text="Gender ",font=('arial', 14, 'bold' ))
label_gender.place(x=20,y=190)
r1= Radiobutton(bmical,text="Male",variable= var,value="Male",font=('arial',14,'bold'),command=sel)
r1.place(x=200,y= 190)
r2= Radiobutton(bmical,text="Female",variable= var,value="Female",font=('arial',14,'bold'),command=sel)
r2.place(x=380,y= 190)

label_height_in_mtr= Label(bmical, text="Enter height in mtr ",font=('arial', 14, 'bold' ))
label_height_in_mtr.place(x=20,y=250)
entheight = Entry(bmical, bd=5, font=('arial', 18, 'bold' ))
entheight.place(x=210,y=250)

label_weight_in_kg= Label(bmical, text="Enter weight in kg ",font=('arial', 14, 'bold' ))
label_weight_in_kg.place(x=20,y=310)
entweight = Entry(bmical, bd=5, font=('arial', 18, 'bold' ))
entweight.place(x=210,y=310)

btncal = Button(bmical, text="calculate", width=15,bg='#ADD8E6', font=('arial', 14, 'bold'),command=bmi)
btncal.place(x=170,y=370)

btnconvert = Button(bmical, text="convert", width=15,bg='#ADD8E6', font=('arial', 14, 'bold'),command=f4)
btnconvert.place(x=500,y=250)

btnback1=Button(bmical,text="Back",width=15,bg='#ADD8E6',font=('arial', 14, 'bold'),command=f8)
btnback1.place(x=450,y=370)

bmical.withdraw()

convert = Toplevel(bmical)
convert.title("Height coversion")
convert.geometry("700x650+100+10")
label_enter_your_height=Label(convert, text="Enter  your height ",font=('arial', 14, 'bold' ))
label_enter_your_height.pack(pady=10)
label_feet= Label(convert, text="Enter height in feet ",font=('arial', 14, 'bold' ))
label_feet.pack(pady=10)
entfeet = Entry(convert, bd=5, font=('arial', 18, 'bold'))
entfeet.pack(pady=10)
label_inches= Label(convert, text="Enter height in inches ",font=('arial', 14, 'bold' ))
label_inches.pack(pady=10)
entinches = Entry(convert, bd=5, font=('arial', 18, 'bold' ))
entinches.pack(pady=10)
btnconvert = Button(convert, text="convert", width=15,bg='#ADD8E6', font=('arial', 14, 'bold'),command=convert1)
btnconvert.pack(pady=10)
btnback=Button(convert,text="Back",width=15,bg='#ADD8E6',font=('arial', 14, 'bold'),command=f5)
btnback.pack(pady=10)
convert.withdraw()


view_st=Tk()
view_st.title("View student")
view_st.geometry("800x300")
view_st.configure(bg='light blue')
	
view_st.withdraw()
root.mainloop()
