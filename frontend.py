from database_helper_insert import backend
from database_helper_retrieve import backend2
from tkinter import *
from tkinter import Menu
from tkinter import ttk

class frontend:

    def __init__(self):
        self.root=Tk()
        self.root.resizable(0,0)
        self.ob1=backend()
        self.ob2=backend2()
        self.initial2()
        self.first_page()
        self.root.mainloop()

    def quit(self):
        self.canvas.destroy()
        self.root.quit()
        self.root.destroy()
        exit()

    def initial2(self):
        self.canvas=Canvas(self.root, width=1200, height=700)
        self.my_image=PhotoImage(file=r'C:\Users\Spoorthi S\Desktop\uni.png')
        self.canvas.create_image(220,0,anchor=NW,image=self.my_image)
        self.canvas.grid()
        self.root.title("UNICARD SYSTEM")

    def first_page(self):
        self.canvas.destroy()
        self.initial2()
        self.button2=Button(self.root,text="Admin",anchor='center',width=15,command=self.admin_login)
        self.button2_window=self.canvas.create_window(380,280,anchor='nw',window=self.button2)
        self.button2=Button(self.root,text="User",anchor='center',width=15)
        self.button2_window=self.canvas.create_window(680,280,anchor='nw',window=self.button2)
        self.button2=Button(self.root,text="Exit",anchor='center',width=15,command=self.quit)
        self.button2_window=self.canvas.create_window(550,480,anchor='nw',window=self.button2)

    def admin_login(self):
        self.canvas.destroy()
        self.initial2()
        self.txt2=self.canvas.create_text(370,200,text="User name:",font=("arial",15),fill="black")
        self.e3=Entry(self.canvas)
        self.canvas.create_window(600,200,window=self.e3)
        
        self.txt3=self.canvas.create_text(360,300,text="Password:",font=("arial",15),fill="black")
        self.e4=Entry(self.canvas,show="*")
        self.canvas.create_window(600,300,window=self.e4)

        self.button2=Button(self.root,text="Login",anchor='center',width=15,command=self.login_db)
        self.button2_window=self.canvas.create_window(680,380,anchor='nw',window=self.button2)


    def login_db(self):
        admin_id=self.e3.get()
        password=self.e4.get()
        self.login_admin(admin_id,password)
    def login_admin(self,admin_id,password):
        i=0
        j=0
        conn,cursor=self.ob1.connectt()
        cursor.execute("SELECT username FROM admin WHERE username= %s",(admin_id,))
        for row in cursor:
            i=i+1
            if(i==1):
                cursor.execute("SELECT password FROM admin WHERE password= %s AND username =%s",(password,admin_id))
                for row in cursor:
                    j=j+1
                    if(j==1):
                        self.canvas.destroy()
                        self.initial2()
                        self.admin_page()
        if(i==0):
            self.admin_login()
            self.txt4=self.canvas.create_text(500,500,text="Invalid User Name",font=("arial",15),fill="red")
        elif(i==1 and j==0):
            self.admin_login()
            self.txt4=self.canvas.create_text(500,500,text="Invalid password",font=("arial",15),fill="red")
        self.ob1.close(cursor,conn)

    def admin_page(self):
        self.canvas.destroy()
        self.initial2()
        self.button2=Button(self.root,text="Insert",anchor='center',width=15,command=self.Insert)
        self.button2_window=self.canvas.create_window(300,280,anchor='nw',window=self.button2)
        self.button2=Button(self.root,text="Update",anchor='center',width=15,command=self.Update)
        self.button2_window=self.canvas.create_window(500,280,anchor='nw',window=self.button2)
        self.button2=Button(self.root,text="Delete",anchor='center',width=15,command=self.Delete)
        self.button2_window=self.canvas.create_window(700,280,anchor='nw',window=self.button2)

    def Insert(self):
        self.canvas.destroy()
        self.initial2()
        self.op=self.canvas.create_text(300,100,text="Select the options which has to be inserted:",font=("arial",10),fill="black")
        
        self.c1=IntVar()
        self.ch1=Checkbutton(self.root,text="Person",variable=self.c1,onvalue=1,offvalue=0,height=5,width=10,fg="black")
        self.ch1_window=self.canvas.create_window(300,150,anchor='nw',window=self.ch1)
        
        self.c2=IntVar()
        self.ch2=Checkbutton(self.root,text="Ration",variable=self.c2,onvalue=1,offvalue=0,height=5,width=10,fg="black")
        self.ch2_window=self.canvas.create_window(300,200,anchor='nw',window=self.ch2)
        
        self.c3=IntVar()
        self.ch3=Checkbutton(self.root,text="Pan",variable=self.c3,onvalue=1,offvalue=0,height=5,width=10,fg="black")
        self.ch3_window=self.canvas.create_window(300,250,anchor='nw',window=self.ch3)
        
        self.c4=IntVar()
        self.ch4=Checkbutton(self.root,text="Buspass",variable=self.c4,onvalue=1,offvalue=0,height=5,width=10,fg="black")
        self.ch4_window=self.canvas.create_window(300,300,anchor='nw',window=self.ch4)
        
        self.c5=IntVar()
        self.ch5=Checkbutton(self.root,text="licence",variable=self.c5,onvalue=1,offvalue=0,height=5,width=10,fg="black")
        self.ch5_window=self.canvas.create_window(300,350,anchor='nw',window=self.ch5)
        
        self.c6=IntVar()
        self.ch6=Checkbutton(self.root,text="lpg",variable=self.c6,onvalue=1,offvalue=0,height=5,width=10,fg="black")
        self.ch6_window=self.canvas.create_window(300,400,anchor='nw',window=self.ch6)
        
        self.c7=IntVar()
        self.ch7=Checkbutton(self.root,text="Health",variable=self.c7,onvalue=1,offvalue=0,height=5,width=10,fg="black")
        self.ch7_window=self.canvas.create_window(300,450,anchor='nw',window=self.ch7)

        self.button2=Button(self.root,text="Insert",anchor='center',width=15,command=self.insert_values)
        self.button2_window=self.canvas.create_window(300,550,anchor='nw',window=self.button2)

    def insert_values(self):
        self.n1=self.c1.get()
        self.n2=self.c2.get()
        self.n3=self.c3.get()
        self.n4=self.c4.get()
        self.n5=self.c5.get()
        self.n6=self.c6.get()
        self.n7=self.c7.get()
        self.canvas.destroy()
        self.initial2()

        self.button2=Button(self.root,text="Insert",anchor='center',width=15)
        self.button2_window=self.canvas.create_window(300,550,anchor='nw',window=self.button2)

    def Update(self):
        self.canvas.destroy()
        self.initial2()
        self.button2=Button(self.root,text="Update address",anchor='center',width=15,command=self.updatea)
        self.button2_window=self.canvas.create_window(380,280,anchor='nw',window=self.button2)
        self.button3=Button(self.root,text="Update phone number",anchor='center',width=20,command=self.updatep)
        self.button3_window=self.canvas.create_window(680,280,anchor='nw',window=self.button3)

    def updatea(self):
        self.canvas.destroy()
        self.initial2()
        self.op=self.canvas.create_text(300,100,text="Enter the following information:",font=("arial",10),fill="black")

        self.txt2=self.canvas.create_text(300,150,text="House Number and Street:",font=("arial",15),fill="black")
        self.e3=Entry(self.canvas)
        self.canvas.create_window(500,150,window=self.e3)
        
        self.txt3=self.canvas.create_text(300,200,text="City:",font=("arial",15),fill="black")
        self.e4=Entry(self.canvas)
        self.canvas.create_window(500,200,window=self.e4)

        self.txt3=self.canvas.create_text(300,250,text="State:",font=("arial",15),fill="black")
        self.e5=Entry(self.canvas)
        self.canvas.create_window(500,250,window=self.e5)

        self.txt3=self.canvas.create_text(300,300,text="pin:",font=("arial",15),fill="black")
        self.e6=Entry(self.canvas)
        self.canvas.create_window(500,300,window=self.e6)

        self.txt3=self.canvas.create_text(300,350,text="Uid:",font=("arial",15),fill="black")
        self.e7=Entry(self.canvas)
        self.canvas.create_window(500,350,window=self.e7)

        self.button2=Button(self.root,text="update",anchor='center',width=15,command=self.upa)
        self.button2_window=self.canvas.create_window(500,480,anchor='nw',window=self.button2)

        
    def upa(self):
        ads=self.e3.get()
        adc=self.e4.get()
        adst=self.e5.get()
        adp=self.e6.get()
        ui=self.e7.get()
        self.ob1.update_person_add(ads,adc,adst,adp,ui)
        
        self.op=self.canvas.create_text(500,580,text="Value Changed",font=("arial",10),fill="black")
        self.button2=Button(self.root,text="Exit",anchor='center',width=15,command=self.quit)
        self.button2_window=self.canvas.create_window(800,580,anchor='nw',window=self.button2)
    

    def updatep(self):
        self.canvas.destroy()
        self.initial2()
        self.op=self.canvas.create_text(300,100,text="Enter the following information:",font=("arial",10),fill="black")

        self.txt2=self.canvas.create_text(300,150,text="phone",font=("arial",15),fill="black")
        self.e3=Entry(self.canvas)
        self.canvas.create_window(500,150,window=self.e3)
        
        self.txt3=self.canvas.create_text(300,200,text="uid",font=("arial",15),fill="black")
        self.e4=Entry(self.canvas)
        self.canvas.create_window(500,200,window=self.e4)

        self.button2=Button(self.root,text="update",anchor='center',width=15,command=self.upp)
        self.button2_window=self.canvas.create_window(500,300,anchor='nw',window=self.button2)
        

    def upp(self):
        self.ob1.update_person_ph(self.e3.get(),self.e4.get())
        self.op=self.canvas.create_text(500,400,text="Value Changed",font=("arial",10),fill="black")
        self.button2=Button(self.root,text="Exit",anchor='center',width=15,command=self.quit)
        self.button2_window=self.canvas.create_window(800,580,anchor='nw',window=self.button2)
        
        
    def Delete(self):
        self.canvas.destroy()
        self.initial2()
        self.op=self.canvas.create_text(300,100,text="Enter uid number",font=("arial",10),fill="black")

        self.txt2=self.canvas.create_text(300,150,text="uid",font=("arial",15),fill="black")
        self.e3=Entry(self.canvas)
        self.canvas.create_window(500,150,window=self.e3)
        
        self.button2=Button(self.root,text="Delete",anchor='center',width=15,command=self.dell)
        self.button2_window=self.canvas.create_window(300,350,anchor='nw',window=self.button2)

        

    def dell(self):
        self.ob1.delete(self.e3.get())
        self.op=self.canvas.create_text(500,450,text="Deleted",font=("arial",10),fill="black")
        self.button2=Button(self.root,text="Exit",anchor='center',width=15,command=self.quit)
        self.button2_window=self.canvas.create_window(800,450,anchor='nw',window=self.button2)
        
        
        

ob=frontend()
