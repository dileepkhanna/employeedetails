import tkinter.messagebox
from tkinter import *
import mysql.connector

access = Tk()
access.geometry('700x600')
access.title('emp_details')
access.configure(bg='light grey')
Label(access, text='EMPOYLEE DETAILS', font=('calibri', 25),bg='black', fg='grey').place(x=250, y=10)

db=mysql.connector.connect(host='localhost', user='root',password='9948318650',db='employee')
cursor=db.cursor()

def ctc():
    Empolyee_ctc.set(Empolyee_salary.get()*12)

def add():
    Id=Empolyee_id.get()
    name=Empolyee_name.get()
    desg=Empolyee_desg.get()
    salary=Empolyee_salary.get()
    ctc=Empolyee_ctc.get()
    cursor.execute('insert into main values(%s,%s,%s,%s,%s)', [Id,name,desg,salary,ctc] )
    db.commit()
    tkinter.messagebox.showinfo('emp_details','details added')

def view():
    Id=Empolyee_id.get()
    cursor.execute('select*from main where EmpId=%s',[Id])
    data=cursor.fetchone()
    if data is not None:
        Empolyee_name.set(data[1])
        Empolyee_desg.set(data[2])
        Empolyee_salary.set(data[3])
        Empolyee_ctc.set(data[4])
    else:
        tkinter.messagebox.showwarning('emp_details', 'no data')

def clear():
    Empolyee_id.set('')
    Empolyee_name.set('')
    Empolyee_desg.set('')
    Empolyee_salary.set('')
    Empolyee_ctc.set('')

def update():
    Id = Empolyee_id.get()
    name = Empolyee_name.get()
    desigination = Empolyee_desg.get()
    salary = Empolyee_salary.get()
    ctc = Empolyee_ctc.get()
    cursor.execute('update main set EmpName=%s, EmpDesigination=%s, EmpSalary=%s, EmpCTC=%s where EmpId=%s',
                   [name, desigination, salary, ctc, Id])
    db.commit()
    tkinter.messagebox.showinfo('emp_details','data update')

def delete():
    Id = Empolyee_id.get()
    name = Empolyee_name.get()
    desigination = Empolyee_desg.get()
    salary = Empolyee_salary.get()
    ctc = Empolyee_ctc.get()
    cursor.execute('delete from main where EmpId=%s',[Id])
    db.commit()
    tkinter.messagebox.showinfo('emp_details','data deleted')

def overall():
   view=Toplevel(access)
   view.geometry('1000x600')
   view.configure(bg='lightgreen')
   view.title('employee details')
   cursor.execute('select*from main')
   data=cursor.fetchall()
   rows=len(data)
   cols=len(data[0])
   Label(view, text='Emp Id', font=('calibri', 20, 'bold'),bg='lightgreen').grid(row=0,column=0)
   Label(view, text='Emp Name', font=('calibri', 20, 'bold'), bg='lightgreen').grid(row=0,column=1)
   Label(view, text='Emp Desigination', font=('calibri', 20, 'bold'), bg='lightgreen').grid(row=0,column=2)
   Label(view, text='Emp Salary', font=('calibri', 20, 'bold'), bg='lightgreen').grid(row=0,column=3)
   Label(view, text='Emp CTC', font=('calibri', 20, 'bold'), bg='lightgreen').grid(row=0,column=4)
   for i in range(rows):
       for j in range(cols):
           s = Entry(view,font=('TimesNewRoman'))
           s.grid(row=i+1,column=j)
           s.insert(END, data[i][j])




Label(access,text='Empolyee Id', font=('timer new roman',16),bg='light grey').place(x=100,y=100)
Empolyee_id = StringVar()
Entry(access,textvariable=Empolyee_id, font=('calibri',16),bg='white').place(x=350,y=100)
Label(access,text='Empolyee Name', font=('timer new roman',16),bg='light grey').place(x=100,y=150)
Empolyee_name= StringVar()
Entry(access,textvariable=Empolyee_name, font=('calibri',16),bg='white').place(x=350,y=150)
Label(access,text='Empolyee Desigination', font=('timer new roman',16),bg='light grey').place(x=100,y=200)
Empolyee_desg= StringVar()
Entry(access,textvariable=Empolyee_desg, font=('calibri',16),bg='white').place(x=350,y=200)
Label(access,text='Empolyee Salary', font=('timer new roman',16),bg='light grey').place(x=100,y=250)
Empolyee_salary= IntVar()
Entry(access,textvariable=Empolyee_salary, font=('calibri',16),bg='white',).place(x=350,y=250)
Label(access,text='Empolyee CTC', font=('timer new roman',16),bg='light grey').place(x=100,y=300)
Empolyee_ctc= IntVar()
Entry(access,textvariable=Empolyee_ctc, font=('calibri',16),bg='white',).place(x=350,y=300)
Button(access,text='Calculate', font=('calibri',8),bg='black',fg='lightgrey',height=1,width=6, command=ctc).place(x=600,y=270)


Button(access,text='Add', font=('calibri',10),bg='black',fg='lightgrey',height=2,width=5,command=add).place(x=100,y=400)
Button(access,text='View', font=('calibri',10),bg='black',fg='lightgrey',height=2,width=5, command=view).place(x=200,y=400)
Button(access,text='Clear', font=('calibri',10),bg='black',fg='lightgrey',height=2,width=5, command=clear).place(x=300,y=400)
Button(access,text='Update', font=('calibri',10),bg='black',fg='lightgrey',height=2,width=5, command=update).place(x=100,y=450)
Button(access,text='Delete', font=('calibri',10),bg='black',fg='lightgrey',height=2,width=5, command=delete).place(x=200,y=450)
Button(access,text='Overall', font=('calibri',10),bg='black',fg='lightgrey',height=2,width=5, command=overall).place(x=300,y=450)
access.mainloop()