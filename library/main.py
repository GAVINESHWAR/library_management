#############################sql codess###############%%%%%%%%%%%%%%%%%%%%%
from datetime import date
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Avisql007@",
    database="library_management"
)
mycursor = mydb.cursor()
mycursor.execute("show tables")
l=[]
for i in mycursor:
    l.append(i)
if ("book",) and ("book_id",) and ("student",) not in l:
    mycursor.execute("CREATE TABLE book (book_id INT PRIMARY KEY,book_name VARCHAR(50), subject VARCHAR(20))")
    mycursor.execute("CREATE TABLE student (student_id varchar(10) PRIMARY KEY,first_name VARCHAR(20), last_name VARCHAR(20))")
    mycursor.execute("create table book_id (book_value int)")
mycursor.execute("select * from book_id")
for x in mycursor:
    book_id=x[0]
##registration function data enter to the sql tables;
def registration(st_id,f_name,l_name):
    flag=False
    for i in st_id:
        if i.isalpha():
            flag=True
    if flag:
        try:
            mycursor.execute("insert into student values(%s,%s,%s,0)",(st_id,f_name,l_name))
            mydb.commit()
            table="create table if not exists "+st_id+" (book_id int,book_name VARCHAR(50), subject VARCHAR(20),issued_date date,return_date date)"
            mycursor.execute(table) 
            mydb.commit()
            return 1
        except:
            #pop up message
            messagebox.showwarning("Duplicate entry","student is already registered")
            return -1
    else:
        #show pop up message
        messagebox.showerror("Invalid","enter valid student id")
        #go back to registration page
        return -1

##front end code
from tkinter import *
from tkinter import messagebox
from time import sleep
from tkinter import ttk
import ast 
screen=Tk()
screen.title("JNTUACEA")
#screen.geometry("925x500+300+200")
p1=PhotoImage(file="bg21.png")
Label(screen,image=p1,bg="white").pack(expand=True)
####registration code column signup###########
def sign_up():
    window=Toplevel(screen)
    window.title("Registration")
    window.geometry("925x500+300+200")
    window.config(bg="#fff")
    window.resizable(False,False)
###signup function
    def signup():
        admissionno=user.get()
        firstname=code.get()
        lastname=conform_code.get()
        a=registration(admissionno,firstname,lastname)
        if a==-1:
            window.destroy()
            sign_up()
        messagebox.showinfo("Registration","sucessfully sign up") 
        window.destroy()
#sign funtion to if havving account
    #def sign():
     #   window.destroy()
    img=PhotoImage(file="signup.png")
    Label(window,image=img,border=0,bg="white").place(x=50,y=90)
#function for user input
    def on_enter(e):
        user.delete(0,"end")
    def on_leave(e):
        if code.get()=="":
            code.inser(0,"Password")
    frame=Frame(window,width=350,height=390,bg="white")
    frame.place(x=520,y=50)
#heading 
    heading=Label(frame,text="Registration",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
    heading.place(x=100,y=5)
######=======#######

#input data 1user
    user=Entry(frame,width=25,fg="black",border=2,bg="white",font=("Microsoft Yahei UI Light",11))
    user.place(x=75,y=80)
    user.insert(0,"Admission no")
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg="black").place(x=35,y=105)

#password 2
    def on_enter(e):
        code.delete(0,"end")
    def on_leave(e):
        if code.get()=="":
            code.insert(0,"Firstname")
    code=Entry(frame,width=25,fg="black",border=2,bg="white",font=("Microsoft Yahei UI Light",11))
    code.place(x=75,y=140)
    code.insert(0,"Firstname")
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg="black").place(x=35,y=165)

#confirm password
    def on_enter(e):
        conform_code.delete(0,"end")
    def on_leave(e):
        if conform_code.get()=="":
            conform_code.insert(0,"Lastname")
    conform_code=Entry(frame,width=25,fg="black",border=2,bg="white",font=("Microsoft Yahei UI Light",11))
    conform_code.place(x=75,y=200)
    conform_code.insert(0,"Lastname")
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg="black").place(x=35,y=225)
###################3---------------
#button
    Button(frame,width=39,pady=7,text="Register",bg="#57a1f8",fg="white",border=0,cursor="hand2",command=signup).place(x=35,y=280)
    label=Label(frame,text="I have an account",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
    label.place(x=90,y=340)
    #signin=Button(frame,width=6,text="Sign in",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=sign)
    #ignin.place(x=200,y=340)
    window.mainloop()
###################################################################donating a book function##############
######Sql code
def donate1(book_name,subject):
    try:
        global book_id
        book_id+=1
        mycursor.execute("update book_id set book_value=%s ",(book_id,))
        mycursor.execute("insert into book values(%s,%s,%s)",(book_id,book_name,subject))
        mydb.commit()
        return 1
    except:
        messagebox.showwarning("invalid","unexpected error occured")
        return 0
#########tkinter function
def donateIn():
    donate=Toplevel(screen)
    donate.title('Donating a book')
#donate.geometry('925x500+300+200')
    donate.configure(bg="#fff")
#donate.resizable(False,False)
# image variable
    img=PhotoImage(file="db1.png")
#img2=PhotoImage(file="p2.png")
#function of submission
    def donated():
        a=bookname.get()
        b=subject.get()
        result = donate1(a,b)
        if result==1:
            messagebox.showinfo("successful","book is added to library succesfully")
            sleep(1)
            messagebox.showinfo("congrats","thank you for donating books")
            donate.destroy()
    #donate.destroy()
# position of the image
    Label(donate,image=img,bg='white').pack(expand=True)
    frame =Frame(donate,width=350,height=350,bg="black")
    frame.place(x=525,y=200)

    heading1=Label(frame,text="Book Deatails" , fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
    heading1.place(x=65,y=5)
# INPUT
###############----------------------------------
    def on_enter1(e):
        bookname.delete(0,"end")
    def on_leave1(e):
        name=bookname.get()
        if name=="":
            bookname.insert(0,"Bookname")
    bookname = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    bookname.place(x=70,y=80)
    bookname.insert(0,"Book name")
    bookname.bind("<FocusIn>",on_enter1)
    bookname.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
##########################3-----------------------############################
#input2
    def on_enter1(e):
        subject.delete(0,"end")
    def on_leave1(e):
        name=subject.get()
        if name=="":
            subject.insert(0,"Subject")
    subject = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    subject.place(x=70,y=150)
    subject.insert(0,"Subject")
    subject.bind("<FocusIn>",on_enter1)
    subject.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
########################3---------------################
#Button
    Button(frame,pady=5,padx=70,text="Donate ",bg="#57a1f8",fg="white",cursor="hand2",border=2,font=(10),command=donated).place(x=65,y=210)
    donate.mainloop()

######issuing a book
#####sql code#####
#function to issue a book
def issue_a_book(student_id,book_id):
    mycursor.execute("select * from student where student_id=%s",(student_id,))
    res=mycursor.fetchall()
    if len(res)==0:
        #pop up message
        messagebox.showerror("not registried","student has  not registered or enter correct student id")
        return -1
        #front end  registration()
        #again open issue_a_book in front end
    mycursor.execute("select * from "+student_id+" where return_date is null")   
    res=mycursor.fetchall()
    if(len(res)>=3):
        messagebox.showwarning("Limit exceeded","you have already taken three books return books to take new books")
        messagebox.showinfo("submit","submit the previously taken books to take a book")
        #pop up message you have already taken a book
        return 0
    mycursor.execute("select * from book where book_id=%s",(book_id,))
    res=mycursor.fetchall()
    if(len(res)==0):
        messagebox.showinfo("invalid","there is no such book")
        #frontend
        return -1
    else:
        book_name=res[0][1]
        subject=res[0][2]
        today=date.today()
        mycursor.execute("insert into "+student_id+" values(%s,%s,%s,%s,null)",(book_id,book_name,subject,today,))
        mycursor.execute("delete from book where book_id="+str(book_id))
        mydb.commit()
        return 1
def issue_Book():
    take=Toplevel(screen)
    take.title('Taking Book')
    take.configure(bg="white")
#donate.geometry('925x500+300+200')
#take.configure(bg="#fff")
#donate.resizable(False,False)
# image variable
    img=PhotoImage(file="tab1.png")
# position of the image
    Label(take,image=img,bg='white').pack(expand=True)
#img2=PhotoImage(file="p2.png")
#function of submission
    def donated():
        a=Admission_no.get()
        b=book_id.get()
        e=issue_a_book(a,b)
        if e==0:
            take.destroy()
        elif e==-1:
            take.destroy()
            issue_Book()
        else:
            messagebox.showinfo("successful","book is alloted to student Sucessful")
            sleep(1)
            messagebox.showinfo("congrats","happy learning")
            take.destroy()
    #frame creation 
    frame =Frame(take,width=350,height=350,bg="black")
    frame.place(x=525,y=250)

    heading1=Label(frame,text="Issuing Book" , fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
    heading1.place(x=85,y=10)
# INPUT
###############----------------------------------
    def on_enter1(e):
        Admission_no.delete(0,"end")
    def on_leave1(e):
        name=Admission_no.get()
        if name=="":
            Admission_no.insert(0,"Admission no")
    Admission_no = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    Admission_no.place(x=70,y=80)
    Admission_no.insert(0,"Admission no")
    Admission_no.bind("<FocusIn>",on_enter1)
    Admission_no.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
##########################3-----------------------############################
#input2
    def on_enter1(e):
        book_id.delete(0,"end")
    def on_leave1(e):
        name=book_id.get()
        if name=="":
            book_id.insert(0,"Book ID")
    book_id = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    book_id.place(x=70,y=150)
    book_id.insert(0,"Book ID")
    book_id.bind("<FocusIn>",on_enter1)
    book_id.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
########################3---------------################
#Button
    Button(frame,pady=5,padx=70,text="Submit ",bg="#57a1f8",fg="white",cursor="hand2",border=2,font=(10),command=donated).place(x=65,y=210)
    take.mainloop()
###############################RETURNING A BOOK CODE
#####sql code
def return_book(student_id,book_id):
    mycursor.execute("select * from student where student_id=%s",(student_id,))
    res=mycursor.fetchall()
    if len(res)==0:
        #pop up message
        messagebox.showinfo("invalid","enter proper student id")
        return -1
    mycursor.execute("select * from "+student_id+" where book_id="+str(book_id)+" and return_date is null" )
    res=mycursor.fetchall()
    if(len(res)==0):
        messagebox.showerror("invalid","enter proper book id")
        return -1
         #pop up messsage
        #return frontend function call  ie return book page
    else:
        book_name=res[0][1]
        subject=res[0][2]
        issued_date=res[0][3]
        return_date=date.today()
        months=((return_date-issued_date).days)//30
        fine=months*10
        mycursor.execute("select * from student where student_id=%s",(student_id,))
        for x in mycursor:
                fine+=x[3]
    
        mycursor.execute("update student set fine=%s where student_id=%s",(fine,student_id))
        mydb.commit()
        mycursor.execute("insert into book values(%s,%s,%s)",(book_id,book_name,subject))
        mycursor.execute("update "+student_id+" set return_date= %s where book_id=%s and return_date is null",(str(return_date),book_id))
        mydb.commit()
        return 1
###tkinter code
def returning():
    return1=Toplevel(screen)
    return1.title('Book Return')
    return1.configure(bg="white")
#donate.geometry('925x500+300+200')
#take.configure(bg="#fff")
#donate.resizable(False,False)
# image variable
    img=PhotoImage(file="return.png")
# position of the image
    Label(return1,image=img,bg='white').pack(expand=True)
#img2=PhotoImage(file="p2.png")
#function of submission
    def returned():
        a=Admission_no.get()
        b=book_id.get()
        result=return_book(a,b)
        if result==-1:
            return1.destroy()
            returning()
        else:
            messagebox.showinfo("successfull","book is returned to Library sucessfully")
            sleep(1)
            messagebox.showinfo("GOOD","Thank you submission")
            return1.destroy()
    #frame creation 
    frame =Frame(return1,width=350,height=350,bg="black")
    frame.place(x=525,y=250)

    heading1=Label(frame,text="Returning book" , fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
    heading1.place(x=68,y=10)
# INPUT
###############----------------------------------
    def on_enter1(e):
        Admission_no.delete(0,"end")
    def on_leave1(e):
        name=Admission_no.get()
        if name=="":
            Admission_no.insert(0,"Admission no")
    Admission_no = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    Admission_no.place(x=70,y=80)
    Admission_no.insert(0,"Admission no")
    Admission_no.bind("<FocusIn>",on_enter1)
    Admission_no.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
##########################3-----------------------############################
#input2
    def on_enter1(e):
        book_id.delete(0,"end")
    def on_leave1(e):
        name=book_id.get()
        if name=="":
            book_id.insert(0,"Book ID")
    book_id = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    book_id.place(x=70,y=150)
    book_id.insert(0,"Book ID")
    book_id.bind("<FocusIn>",on_enter1)
    book_id.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
########################3---------------################
#Button
    Button(frame,pady=5,padx=70,text="Submit ",bg="#57a1f8",fg="white",cursor="hand2",border=2,font=(10),command=returned).place(x=65,y=210)
    return1.mainloop() 
############Display a book:
def display():
    r=Toplevel(screen)
    r.title("Book in our library")
    r.geometry("700x300")
    r.config(bg="green")
    #img=PhotoImage(file="return.png")
    #Label(r,image=img,bg='white').pack(expand=True
    mycursor.execute("select * from book order by subject")
    tree=ttk.Treeview(r)
    #changing the style and color and the borders
    s=ttk.Style(r)
    s.theme_use("clam")
    s.configure(".",font=("helvetica", 11))
    s.configure("Treeview.h=Heading",foreground="orange",font=("Helvetica", 11 ,"bold"))
    tree["show"]="headings"
    tree["columns"]=("student_id","book_name","subject")
    tree.column("student_id",width=200,minwidth=50, anchor=CENTER)
    tree.column("book_name",width=200,minwidth=50,anchor=CENTER)
    tree.column("subject",width=200,minwidth=50,anchor=CENTER)
    tree.heading("student_id",text="student_id",anchor=CENTER)
    tree.heading("book_name",text="book_name",anchor=CENTER)
    tree.heading("subject",text="subject",anchor=CENTER)
    i=0
    for ro in mycursor:
        tree.insert("",i,text=" ",values=(ro[0],ro[1],ro[2]))
        i=i+1
    hsb=ttk.Scrollbar(r,orient="vertical")

    hsb.configure(command=tree.yview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)
    tree.pack(expand=TRUE)
    r.mainloop()
####book lost ##########################
##sql code
def book_lost(student_id,book_id):
    result=return_book(student_id,book_id)
    if result==-1:
        return result
    else:

        fine=20
        mycursor.execute("select * from student where student_id=%s",(student_id,))
        for x in mycursor:
            fine+=x[3]
    
        mycursor.execute("update student set fine=%s where student_id=%s",(fine,student_id))
        mydb.commit()
####tkinter code
def losted():
    lost=Toplevel(screen)
    lost.title('Book Lost')
    lost.configure(bg="white")
#donate.geometry('925x500+300+200')
#take.configure(bg="#fff")
#donate.resizable(False,False)
# image variable
    img=PhotoImage(file="return.png")
# position of the image
    Label(lost,image=img,bg='white').pack(expand=True)
#img2=PhotoImage(file="p2.png")
#function of submission
    def losted1():
        a=Admission_no.get()
        b=book_id.get()
        result=book_lost(a,b)
        if result==-1:
            lost.destroy()
            losted()
        else:
            messagebox.showinfo("sucessfull","book is returned to Library sucessfully")
            sleep(1)
            messagebox.showwarning("Warning","Don't repeat the thing again")
            sleep(1)
            lost.destroy()
    #frame creation 
    frame =Frame(lost,width=350,height=350,bg="black")
    frame.place(x=525,y=250)

    heading1=Label(frame,text="Book lost" , fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
    heading1.place(x=68,y=10)
# INPUT
###############----------------------------------
    def on_enter1(e):
        Admission_no.delete(0,"end")
    def on_leave1(e):
        name=Admission_no.get()
        if name=="":
            Admission_no.insert(0,"Admission no")
    Admission_no = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    Admission_no.place(x=70,y=80)
    Admission_no.insert(0,"Admission no")
    Admission_no.bind("<FocusIn>",on_enter1)
    Admission_no.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
##########################-----------------------############################
#input2
    def on_enter1(e):
        book_id.delete(0,"end")
    def on_leave1(e):
        name=book_id.get()
        if name=="":
            book_id.insert(0,"Book ID")
    book_id = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    book_id.place(x=70,y=150)
    book_id.insert(0,"Book ID")
    book_id.bind("<FocusIn>",on_enter1)
    book_id.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
########################3---------------################
#Button
    Button(frame,pady=5,padx=70,text="Submit ",bg="#57a1f8",fg="white",cursor="hand2",border=2,font=(10),command=losted1).place(x=65,y=210)
    lost.mainloop()
##########pay ment of the fine#########
#####Sql code####
def fine_amount(student_id):
    
    mycursor.execute("select * from student where student_id=%s",(student_id,))
    res=mycursor.fetchall()
    if(len(res)==1):
        for x in res:
                fine=x[3]
        #("your fine amount is",fine)
        return (fine,1)
    else:
        messagebox.showinfo("invali","enter proper student id")
        return (0,0)
        #return to fine page
def fine():
    pay=Toplevel(screen)
    pay.title('Payment')
    pay.configure(bg="white")
#donate.geometry('925x500+300+200')
#take.configure(bg="#fff")
#donate.resizable(False,False)
# image variable
    img=PhotoImage(file="payment1.png")
    img2=PhotoImage(file="payment2.png")
# position of the image
    Label(pay,image=img,bg='white').pack(expand=True)
#img2=PhotoImage(file="p2.png")
#function of submission
    def complete():
        pay.destroy()
    def payment():
        a=Admission_no.get()
        result=fine_amount(a)
        if result[1]==0:
            pay.destroy()
            fine()
        else:
            messagebox.showinfo("sucessfull","to know amount to pay click ok")
            messagebox.showinfo("Payment",result[0])
            messagebox.showwarning("warning","try to avoid late submission")
            messagebox.showinfo("instruction","click below button to redirect to main page")
            pay.destroy()
#frame creations 
    frame =Frame(pay,width=350,height=250,bg="black")
    frame.place(x=250,y=275)
    frame2 =Frame(pay,width=539,height=477,bg="white")
    frame2.place(x=900,y=275)
    Label(frame2,image=img2,width=539,height=477).place(x=0,y=0)
    heading1=Label(frame,text="Payment" , fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
    heading1.place(x=100,y=10)
# INPUT
###############----------------------------------
    def on_enter1(e):
        Admission_no.delete(0,"end")
    def on_leave1(e):
        name=Admission_no.get()
        if name=="":
            Admission_no.insert(0,"Admission no")
    Admission_no = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    Admission_no.place(x=70,y=80)
    Admission_no.insert(0,"Admission no")
    Admission_no.bind("<FocusIn>",on_enter1)
    Admission_no.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=30,y=125)
##########################3-----------------------############################
########################3---------------################
#Button
    Button(frame,pady=5,padx=70,text="Submit ",bg="#57a1f8",cursor="hand2",fg="white",border=2,font=(10),command=payment).place(x=65,y=175)
    Button(pay,text="back",fg="white",bg="black",padx=30,pady=8,cursor="hand2",font=("Microsoft Yahei UI Light",20,"bold"),command=complete).place(x=700,y=600)
    pay.mainloop()
###############paying the feeeeee
########sql code
def payments(student_id,fee):
    mycursor.execute("select * from student where student_id=%s",(student_id,))
    res=mycursor.fetchall()
    if(len(res)==1):
        for x in res:
            fine=x[3]
        fine-=int(fee)
        mycursor.execute("update student set fine=%s where student_id=%s",(fine,student_id))
        mydb.commit()
        return (fine,1)
    else:
        messagebox.showinfo("invalid","enter proper student id")
        return (0,0)
        #return to payment page
#tkinter code
def payment1():
    pay=Toplevel(screen)
    pay.title('Payment')
    pay.configure(bg="white")
#donate.geometry('925x500+300+200')
#take.configure(bg="#fff")
#donate.resizable(False,False)
# image variable
    img=PhotoImage(file="payment1.png")
    img2=PhotoImage(file="payment2.png")
# position of the image
    Label(pay,image=img,bg='white').pack(expand=True)
#img2=PhotoImage(file="p2.png")
#function of submission
    def complete():
        pay.destroy()
    def payment():
        a=Admission_no.get()
        b=fee.get()
        result=payments(a,b)
        if result[1]==0:
            pay.destroy()
            payment1()
        else:
            messagebox.showinfo("sucessfull","remaining fine amount  $"+str(result[0]))
            pay.destroy()
    #frame creations 
    frame =Frame(pay,width=350,height=250,bg="black")
    frame.place(x=250,y=275)
    frame2 =Frame(pay,width=539,height=477,bg="white")
    frame2.place(x=900,y=275)
    Label(frame2,image=img2,width=539,height=477).place(x=0,y=0)
    heading1=Label(frame,text="Payment" , fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
    heading1.place(x=100,y=10)
    # INPUT
    ###############----------------------------------
    def on_enter1(e):
        Admission_no.delete(0,"end")
    def on_leave1(e):
        name=Admission_no.get()
        if name=="":
            Admission_no.insert(0,"Admission no")
    Admission_no = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    Admission_no.place(x=70,y=80)
    Admission_no.insert(0,"Admission no")
    Admission_no.bind("<FocusIn>",on_enter1)
    Admission_no.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=30,y=125)
    ##########################3-----------------------############################
    ###input 2
    def on_enter1(e):
        fee.delete(0,"end")
    def on_leave1(e):
        name=fee.get()
        if name=="":
            fee.insert(0,"fee")
    fee = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    fee.place(x=70,y=127)
    fee.insert(0,"fee")
    fee.bind("<FocusIn>",on_enter1)
    fee.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=30,y=125)
    ########################3---------------################
    #Button
    Button(frame,pady=5,padx=70,text="Submit ",bg="#57a1f8",fg="white",cursor="hand2",border=2,font=(10),command=payment).place(x=65,y=175)
    Button(pay,text="back",fg="white",bg="black",padx=30,pady=8,cursor="hand2",font=("Microsoft Yahei UI Light",20,"bold"),command=complete).place(x=700,y=600)
    pay.mainloop()
##################students details ###########################
def student12():
    r=Toplevel(screen)
    r.title("Student")
    r.geometry("800x300")
    r.config(bg="green")
    mycursor.execute("select * from student")
    tree=ttk.Treeview(r)
#changing the style and color and the borders
    s=ttk.Style(r)
    s.theme_use("clam")
    s.configure(".",font=("helvetica", 12))
    s.configure("Treeview.h=Heading",foreground="orange",font=("Helvetica", 11 ,"bold"))
    tree["show"]="headings"
    tree["columns"]=("Admission_no","firstname","lastname","fine")
    tree.column("Admission_no",width=200,minwidth=50, anchor=CENTER)
    tree.column("firstname",width=200,minwidth=50,anchor=CENTER)
    tree.column("lastname",width=200,minwidth=50,anchor=CENTER)
    tree.column("fine",width=200,minwidth=50,anchor=CENTER)
    tree.heading("Admission_no",text="Admission_no",anchor=CENTER)
    tree.heading("firstname",text="firstname",anchor=CENTER)
    tree.heading("lastname",text="lastname",anchor=CENTER)
    tree.heading("fine",text="fine",anchor=CENTER)
    i=0
    for ro in mycursor:
        tree.insert("",i,text=" ",values=(ro[0],ro[1],ro[2],ro[3]))
        i=i+1
    hsb=ttk.Scrollbar(r,orient="vertical")
    hsb1=ttk.Scrollbar(r,orient="horizontal")
    hsb.configure(command=tree.yview)
    hsb1.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    tree.configure(yscrollcommand=hsb1.set)
    hsb.pack(fill=Y,side=RIGHT)
    hsb1.pack(fill=X,side=BOTTOM)
    tree.pack(expand=TRUE)
    r.mainloop()
####################individual student details code##################
######sql code###########
def checked(student_id):
    mycursor.execute("select * from student where student_id=%s",(student_id,))
    res=mycursor.fetchall()
    if len(res)==0:
        messagebox.showerror("not registried","student has  not registered or enter correct student id")
        #pop up message
        #messagebox.showerror("not registried","student has  not registered or enter correct student id")
    else:
        return 1
def individual():
    ind=Toplevel(screen)
    ind.title('Individual student details')
    ind.configure(bg="white")
    #donate.geometry('925x500+300+200')
    #take.configure(bg="#fff")
    #donate.resizable(False,False)
    # image variable
    img=PhotoImage(file="return.png")
    # position of the image
    l=Label(ind,image=img,bg='white')
    l.pack(expand=TRUE)
    #img2=PhotoImage(file="p2.png")
    #function of submission
        #frame creation 
    frame =Frame(ind,width=350,height=350,bg="black")
    frame.place(x=525,y=250)
#######function for displayong student deatails
    def check():
        a=Admission_no.get()
        result=checked(a)
        if result==1:
            ind.destroy()
            ress=Toplevel(screen)
            ress.title('Individual student details')
            ress.geometry("1000x300")
            ress.configure(bg="green")
            mycursor=mydb.cursor()
            a="select * from "+a
            mycursor.execute(a)
            tree=ttk.Treeview(ress)
                #changing the style and color and the borders
            s=ttk.Style(ress)
            s.theme_use("clam")
            s.configure(".",font=("helvetica", 12))
            s.configure("Treeview.h=Heading",foreground="orange",font=("Helvetica", 11 ,"bold"))
            tree["show"]="headings"
            tree["columns"]=("book_id","book_name","subject","issued_date","return_date")
            tree.column("book_id",width=200,minwidth=50, anchor=CENTER)
            tree.column("book_name",width=200,minwidth=50,anchor=CENTER)
            tree.column("subject",width=200,minwidth=50,anchor=CENTER)
            tree.column("issued_date",width=200,minwidth=50,anchor=CENTER)
            tree.column("return_date",width=200,minwidth=50,anchor=CENTER)
            tree.heading("book_id",text="book_id",anchor=CENTER)
            tree.heading("book_name",text="book_name",anchor=CENTER)
            tree.heading("subject",text="subject",anchor=CENTER)
            tree.heading("issued_date",text="issue_date",anchor=CENTER)
            tree.heading("return_date",text="return_date",anchor=CENTER)
            i=0
            for ro in mycursor:
                tree.insert("",i,text=" ",values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
                i=i+1
            hsb=ttk.Scrollbar(ress,orient="vertical")
            hsb1=ttk.Scrollbar(ress,orient="horizontal")
            hsb.configure(command=tree.yview)
            hsb1.configure(command=tree.xview)
            tree.configure(xscrollcommand=hsb.set)
            tree.configure(yscrollcommand=hsb1.set)
            hsb.pack(fill=Y,side=RIGHT)
            hsb1.pack(fill=X,side=BOTTOM)
            tree.pack(expand=TRUE)
            ress.mainloop()

    heading1=Label(frame,text="individual student\n details" , fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
    heading1.place(x=50,y=8)
    # INPUT
    ###############----------------------------------
    def on_enter1(e):
        Admission_no.delete(0,"end")
    def on_leave1(e):
        name=Admission_no.get()
        if name=="":
            Admission_no.insert(0,"Admission no")
    Admission_no = Entry(frame,width=25,fg="black",border=3,bg="white",font=("Microsoft Yahei UI Light",11))
    Admission_no.place(x=70,y=130)
    Admission_no.insert(0,"Admission no")
    Admission_no.bind("<FocusIn>",on_enter1)
    Admission_no.bind("<FocusOut>",on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
    ########################3---------------################
    #Button
    Button(frame,pady=5,padx=70,text="Submit ",bg="#57a1f8",fg="white",border=2,font=(10),command=check).place(x=65,y=210)
    ind.mainloop()
#signing out of the application
def closing():
    screen.destroy()
###buttons
l1=Label(screen,text=" welocome   to   jntuacea   Library ",fg="black",bg="white",width=45,font=(10)).place(x=550,y=50)
b0=Button(screen,text="   registration  ",padx=100,pady=4,fg="orange",bg="black",cursor="hand2",border=2,borderwidth=3,font=(15),command=sign_up).place(x=200,y=300)
#b1=Button(screen,text="  add a book   ",pady=4,padx=100,bg="black",fg="orange",cursor="hand2",border=8,borderwidth=3,font=(15)).place(x=600,y=250)
b2=Button(screen,text=" return a book ",pady=4,padx=100,bg="black",fg="orange",cursor="hand2",border=3,borderwidth=3,font=(15),command=returning).place(x=200,y=355)
b3=Button(screen,text="  take a book  ",pady=4,padx=100,bg="black",fg="orange",cursor="hand2",border=3,borderwidth=3,font=(15),command=issue_Book).place(x=200,y=410)
b4=Button(screen,text="donate a book",pady=4,padx=100,bg="black",fg="orange",cursor="hand2",border=3,borderwidth=3,font=(15),command=donateIn).place(x=200,y=465)
b5=Button(screen,text=" display book  ",pady=4,padx=100,bg="black",fg="orange",cursor="hand2",border=3,borderwidth=3,font=(15),command=display).place(x=600,y=320)
b6=Button(screen,text="   book lost     ",padx=100,pady=4,fg="orange",bg="black",cursor="hand2",border=3,borderwidth=3,font=(15),command=losted).place(x=600,y=375)
b7=Button(screen,text="    check fine  ",pady=4,padx=100,fg="orange",bg="black",cursor="hand2",border=3,borderwidth=3,font=(15),command=fine).place(x=600,y=430)
b8=Button(screen,text="student deatails  ",pady=4,padx=100,fg="orange",bg="black",cursor="hand2",border=3,borderwidth=3,font=(15),command=student12).place(x=1000,y=300)
b9=Button(screen,text="individual student",pady=4,padx=100,fg="orange",bg="black",cursor="hand2",border=3,borderwidth=3,font=(15),command=individual).place(x=1000,y=355)
b8=Button(screen,text="    payment        ",pady=4,padx=100,fg="orange",bg="black",cursor="hand2",border=3,borderwidth=3,font=(15),command=payment1).place(x=1000,y=410)
b9=Button(screen,text="   log out            ",pady=4,padx=100,fg="orange",bg="black",cursor="hand2",border=3,borderwidth=3,font=(15),command=closing).place(x=1000,y=465)
screen.mainloop()