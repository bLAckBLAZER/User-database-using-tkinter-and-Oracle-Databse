from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import cx_Oracle
import pygame.mixer


pygame.mixer.init()
pygame.mixer.music.load("Attention (Charlie Puth) 320Kbps-(ProMp3.In).mp3")
pygame.mixer.music.play()

root=Tk()
root.title("Student Management System")
root.geometry("300x300+400+200")
root.configure(background="orange")

def sound():
	sound.counter+=1
	if(not(sound.counter%2==0)):
		pygame.mixer.music.pause()
	else:
		pygame.mixer.music.unpause()
sound.counter=0
	


btnSoundRoot=Button(root,text="On/Off",command=sound)
btnSoundRoot.place(y=270,x=250)
lblSoundRoot= Label(root,text="Music:")
lblSoundRoot.place(y=270,x=195)

lblSignRoot = Label(root,text="-By Omkar Jadhav")
lblSignRoot.place(x=150,y=200)

vist=Toplevel(root)
vist.title("View Student")
vist.geometry("300x300+400+200")
vist.withdraw()

stData= scrolledtext.ScrolledText(vist,width=30,height=15)

def f4():
	root.deiconify()
	vist.withdraw()
	stData.delete("1.0",END)
btnBackVuew= Button(vist,text="Back",command=f4)
stData.pack()
btnBackVuew.pack()

adst=Toplevel(root)
adst.title("Add Student")
adst.geometry("300x300+400+200")
adst.withdraw()

lblRnoAdd= Label(adst,text="Rno")
entRnoAdd= Entry(adst,bd=5)
lblNameAdd= Label(adst,text="Name")
entNameAdd= Entry(adst,bd=5)

def f5():
	con = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor= con.cursor()
		s1 = entRnoAdd.get()
		if(s1==""):
			messagebox.showerror("incomplete","rno is empty")
			entRnoAdd.focus()
			return
		s2= entNameAdd.get()
		if(s2==""):
			messagebox.showerror("incomplete","Name is empty")
			entNameAdd.focus()
			return

		rno=int(entRnoAdd.get())
		name=entNameAdd.get()
		sql="insert into student values('%d','%s')"
		args=(rno,name)
		cursor.execute(sql%args)
		con.commit()
		msg= str(cursor.rowcount)+"rows inserted"
		messagebox.showinfo("Success",msg)



	except cx_Oracle.DatabaseError as e:
		msg="issue"+str(e)
		messagebox.showerror("issue",msg)
		con.rollback()
	finally:
		cursor.close()
		if con is not None:
			con.close()
	entRnoAdd.delete(0,END)
	entNameAdd.delete(0,END)
	entRnoAdd.focus()

btnSaveAdd= Button(adst,text="Save", command=f5)

def f2():
	root.deiconify()
	adst.withdraw()

btnBackAdd=Button(adst,text="Back", command=f2)

lblRnoAdd.pack(pady=5)
entRnoAdd.pack(pady=5)
lblNameAdd.pack(pady=5)
entNameAdd.pack(pady=5)
btnSaveAdd.pack(pady=5)
btnBackAdd.pack(pady=5)

def f1():
	adst.deiconify()
	root.withdraw()

btnAddRoot=Button(root,text="Add",width=10,command=f1)

def f3():
	vist.deiconify()
	root.withdraw()
	con=None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor= con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		rows=cursor.fetchall()
		data=""
		for r in rows:
			rno=r[0]
			name=r[1]
			data=data+"Rno "+str(rno)+" " + "Name " +name+"\n"
		stData.insert(INSERT,data)

	except cx_Oracle.DatabaseError as e:
		msg = "issue" + str(e)
		messagebox.showerror("Error",msg)

	finally:
		cursor.close()
		if con is not None:
			con.close()

btnViewRoot = Button(root,text="View",width=10,command= f3)

upst= Toplevel(root)
upst.title("Update")
upst.geometry("300x300+400+200")
upst.withdraw()

def f10():
	root.withdraw()
	upst.deiconify()
	
def f11():
	upst.deiconify()
	root.withdraw()
	con=None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor= con.cursor()
		s1 = entRnoUpdate.get()
		if(s1==""):
			messagebox.showerror("incomplete","rno is empty")
			entRnoUpdate.focus()
			return
		s2= entNameUpdate.get()
		if(s2==""):
			messagebox.showerror("incomplete","Name is empty")
			entNameUpdate.focus()
			return
		rno=int(entRnoUpdate.get())
		name=entNameUpdate.get()
		sql="update student set name='%s' where rno='%d'"
		args=(name,rno)
		cursor.execute(sql%args)
		con.commit()
		if(cursor.rowcount==0):
			messagebox.showerror("Error","rno does not exist")
			entRnoUpdate.delete(0,END)
			entNameUpdate.delete(0,END)
			entRnoUpdate.focus()
			return

		msg= str(cursor.rowcount)+"rows updated"
		messagebox.showinfo("Success",msg)


	except (cx_Oracle.DatabaseError,ValueError) as e:
		msg = "issue" + str(e)
		messagebox.showerror("Error",msg)


	finally:
		cursor.close()
		if con is not None:
			con.close()
	entRnoUpdate.delete(0,END)
	entNameUpdate.delete(0,END)
	entRnoUpdate.focus()



def f12():
	root.deiconify()
	upst.withdraw()



lblRnoUpdate= Label(upst,text="Enter Roll no")
entRnoUpdate= Entry(upst,bd=5)
lblNameUpdate= Label(upst,text="Enter new name")
entNameUpdate= Entry(upst,bd=5)
btnUpdateUpdate= Button(upst,text="Update",width=10,command=f11)
btnBackUpdate=Button(upst,text="Back",width=10,command=f12)


lblRnoUpdate.pack(pady=5)
entRnoUpdate.pack(pady=5)
lblNameUpdate.pack(pady=5)
entNameUpdate.pack(pady=5)
btnUpdateUpdate.pack(pady=5)
btnBackUpdate.pack(pady=5)


btnUpdateRoot = Button(root,text="Update",width=10, command=f10)

delst=Toplevel(root)
delst.title("Delete Student")
delst.geometry("300x300+400+200")
delst.withdraw()


def f8():
	root.deiconify()
	delst.withdraw()

def f9():
	con = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor= con.cursor()
		s1 = entRnoDelete.get()
		if(s1==""):
			messagebox.showerror("incomplete","rno is empty")
			entRnoDelete.focus()
			return
		
		rollno=int(entRnoDelete.get())
		sql = "delete from student where rno='%d'"
		args=(rollno)
		cursor.execute(sql%rollno)
		con.commit()
		if (cursor.rowcount==0):
			messagebox.showerror("Error", "Entered rollno does not exist")
			
		else:
			messagebox.showinfo("Deleted",str(cursor.rowcount)+" rows deleted")
		entRnoDelete.delete(0,END)
		entRnoDelete.focus()
		return


	except cx_Oracle.DatabaseError as e:
		msg = "issue" + str(e)
		messagebox.showerror("Error",msg)

	finally:
		cursor.close()
		if con is not None:
			con.close()
        

lblRnoDelete= Label(delst,text="Enter Roll no")
entRnoDelete= Entry(delst,bd=5)
btnBackDelete= Button(delst,text="Back",width=10,command=f8)
btnRemoveDelete= Button(delst,text="Delete",width=10,command=f9)


lblRnoDelete.pack(pady=5)
entRnoDelete.pack(pady=5)
btnRemoveDelete.pack(pady=5)
btnBackDelete.pack(pady=5)

def f7():
	delst.deiconify()
	root.withdraw()


btnDeleteRoot=Button(root,text="Delete",width=10,command=f7)
btnAddRoot.pack(pady=10)
btnViewRoot.pack(pady=10)
btnUpdateRoot.pack(pady=10)
btnDeleteRoot.pack(pady=10)

def f6():
	 ans= messagebox.askyesno("Exit","tusi jaa rahe ho?")
	 if ans:
	 	import sys
	 	sys.exit()

root.protocol("WM_DELETE_WINDOW",f6)
root.mainloop()