import mysql.connector as mc
from tkinter import *
import tkinter as tk
class backend2:
    def connectt(self):
        mydb=mc.connect(host="localhost",user="root",passwd="",database="unicard")
        mycursor=mydb.cursor()
        return mydb,mycursor
        

    def person_retrive(self,uid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from person where uid=%s",(uid,))
        record=list(mycursor.fetchall())
        return record
        
    def ration_retrive(self,huid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from ration where huid=%s",(huid,))
        record=list(mycursor.fetchall())
        mycursor.execute("select * from person p join ration r on p.p_ration_id=r.ration_id where r.huid=%s",(huid,))
        record1=list(mycursor.fetchall())
        return record,record1

    def food_grains_retrive(self,huid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from food_grains where f_ration_id=(select ration_id  from ration where huid=%s)",(huid,))
        record=list(mycursor.fetchall())
        return record

    def print_data(self,r,r1,huid):
        for i in r1:
            if (i[0]==huid):
                print(i)

        print(r)
                
        for i in r1:
            if (i[0]!=huid):
                print(i)
                
        if(len(r)==0):
            print("information does not exsits")
        

    def transport_retrive(self,uid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from transport where uid=%s",(uid,))
        record=list(mycursor.fetchall())
        return record

    def licence_retrive(self,uid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from licence where uid=%s",(uid,))
        record=mycursor.fetchall()
        mycursor.execute("select * from vehicle where licence_num=(select licence_num from licence where uid=%s)",(uid,))
        record1=list(mycursor.fetchall())
        return record,record1

    def health_retrive(self,huid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from health where huid=%s",(huid,))
        record=list(mycursor.fetchall())
        mycursor.execute("select * from person p join health h on p.p_health_id=h.health_id where h.huid=%s",(huid,))
        record1=list(mycursor.fetchall())
        return record,record1

    def lpg_retrive(self,huid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from lpg where huid=%s",(huid,))
        record=list(mycursor.fetchall())
        mycursor.execute("select * from person p join lpg l on p.p_lpg_id=l.lpg_id where l.huid=%s",(huid,))
        record1=list(mycursor.fetchall())
        return record,record1

    def lpg_record_retrive(self,huid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from lpg_record where lpg_id=(select lpg_id from lpg where huid=%s)",(huid,))
        record=list(mycursor.fetchall())
        return record

    def pan_retrive(self,uid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from pan_card where uid=%s",(uid,))
        record=list(mycursor.fetchall())
        return record


    def income_tax(self,uid):
        mydb,mycursor=self.connectt()
        mycursor.execute("select * from income_tax where pan_num=(select pan_num from pan_card where uid=%s)",(uid,))
        record=list(mycursor.fetchall())
        return record
        
        
    
    

        
