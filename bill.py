import os
from tkinter import *
from tkinter import messagebox
import random
import tempfile

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", font=("times new roman", 30, "bold"), padx=15, pady=5, border=5, relief=GROOVE, bg=bg_color,fg="white" )
        title.pack(fill=X)

        #Variable Initialize
        # for Cosmetics
        self.soap_name=IntVar()
        self.cream_name=IntVar()
        self.face_wash_name=IntVar()
        self.hair_spr_name=IntVar()
        self.hg_name=IntVar()
        self.lotion_name=IntVar()
        # for Grocery
        self.rice=DoubleVar()
        self.foodOil=DoubleVar()
        self.daal=DoubleVar()
        self.sugar=DoubleVar()
        self.tea=DoubleVar()
        self.wheat=DoubleVar()

        # for cold drinks
        self.maza=IntVar()
        self.coke=IntVar()
        self.dew=IntVar()
        self.pepsi=IntVar()
        self.slice=IntVar()
        self.thumsup=IntVar()
        self.sprite=IntVar()



        #variable for total price
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.coldDrink_price=StringVar()

        #variable for total tax
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.coldDrink_tax=StringVar()

        #Variable for customer detail
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.c_bill_no=StringVar()
        self.bill_no()
        # x=random.randint(1000,9999)        
        # self.c_bill_no.set(str(x))
        self.c_serach=StringVar() 

        #Costumer Detail frame
        f1 =LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"), bg=bg_color,
                       fg="yellow", border=5, relief=GROOVE)
        f1.place(x=0, y=80,relwidth=1)
        cname_lable = Label(f1, text="Customer Name:", font=("times new roman", 15, "bold"), fg="white", bg=bg_color,
                            padx=20).grid(row=0, column=0,pady=5, padx=10)
        cname_entry= Entry(f1,textvariable=self.c_name,border= 5,relief=SUNKEN,width=30 ).grid(row=0, column=1, pady=5, padx=10)

        cph_lable= Label(f1, text="Phone No.:", font=("times new roman" ,15,"bold"),fg= "white",bg=bg_color,padx=20).grid(row=0, column=2,pady=5, padx=10)
        cph_entry= Entry(f1,textvariable=self.c_phone,border= 5,relief=SUNKEN,width=25 ).grid(row=0, column=3, pady=5, padx=10)

        cbill_lable= Label(f1, text="Bill No.:", font=("times new roman" ,15,"bold"),fg= "white",bg=bg_color,padx=20).grid(row=0, column=4,pady=5, padx=10)
        cbill_entry= Entry(f1,textvariable=self.c_serach,border= 5,relief=SUNKEN,width=20 ).grid(row=0, column=5, pady=5, padx=10)

        Button(f1, text="Search",command=self.find_bill,width= 5,font=("times new roman" ,15,"bold"),padx=20).grid(row=0, column=6, pady=5, padx=30)

        #Frame for cosmetics
        f2 =LabelFrame(self.root, text="Cosmetics", font=("times new roman" ,15,"bold"),bg=bg_color,fg="yellow",border= 5,relief=GROOVE)
        f2.place(x=0, y=165,height=380)

        item1_label= Label(f2, text="Bath Soap:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=0, column=0,pady=5, padx=10)
        item2_entry= Entry(f2,textvariable=self.soap_name,border= 5,relief=SUNKEN ).grid(row=0, column=1, pady=5, padx=10)
        item1_label= Label(f2, text="Face Cream:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=1, column=0,pady=5, padx=10)
        item2_entry= Entry(f2,textvariable=self.cream_name,border= 5,relief=SUNKEN ).grid(row=1, column=1, pady=5, padx=10)

        item3_label= Label(f2, text="Face Wash:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=2, column=0,pady=5, padx=10)
        item3_entry= Entry(f2,textvariable=self.face_wash_name,border= 5,relief=SUNKEN ).grid(row=2, column=1, pady=5, padx=10)

        item4_label= Label(f2, text="Hair Spray:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=3, column=0,pady=5, padx=10)
        item4_entry= Entry(f2,textvariable=self.hair_spr_name,border= 5,relief=SUNKEN ).grid(row=3, column=1, pady=5, padx=10)

        item5_label= Label(f2, text="Hair Gel:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=4, column=0,pady=5, padx=10)
        item5_entry= Entry(f2,textvariable=self.hg_name,border= 5,relief=SUNKEN ).grid(row=4, column=1, pady=5, padx=10)

        item6_label= Label(f2, text="Body Lotion:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=5, column=0,pady=5, padx=10)
        item6_entry= Entry(f2,textvariable=self.lotion_name,border= 5,relief=SUNKEN ).grid(row=5, column=1, pady=5, padx=10)


        #Frame for Grocery
        f3 =LabelFrame(self.root, text="Grocery", font=("times new roman" ,15,"bold"),bg=bg_color,fg="yellow",border= 5,relief=GROOVE)
        f3.place(x=300, y=165,height=380)

        item1_label= Label(f3, text="Rice:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=0, column=0,pady=5, padx=10)
        item2_entry= Entry(f3,textvariable=self.rice,border= 5,relief=SUNKEN ).grid(row=0, column=1, pady=5, padx=10)

        item1_label= Label(f3, text="Food Oil:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=1, column=0,pady=5, padx=10)
        item2_entry= Entry(f3,textvariable=self.foodOil,border= 5,relief=SUNKEN ).grid(row=1, column=1, pady=5, padx=10)

        item3_label= Label(f3, text="Daal:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=2, column=0,pady=5, padx=10)
        item3_entry= Entry(f3,textvariable=self.daal,border= 5,relief=SUNKEN ).grid(row=2, column=1, pady=5, padx=10)

        item4_label= Label(f3, text="Sugar:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=3, column=0,pady=5, padx=10)
        item4_entry= Entry(f3,textvariable=self.sugar,border= 5,relief=SUNKEN ).grid(row=3, column=1, pady=5, padx=10)

        item5_label= Label(f3, text="Tea:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=4, column=0,pady=5, padx=10)
        item5_entry= Entry(f3,textvariable=self.tea,border= 5,relief=SUNKEN ).grid(row=4, column=1, pady=5, padx=10)

        item6_label= Label(f3, text="Wheat:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=5, column=0,pady=5, padx=10)
        item6_entry= Entry(f3,textvariable=self.wheat,border= 5,relief=SUNKEN ).grid(row=5, column=1, pady=5, padx=10)

    

        #Frame for Cold Drinks
        f4 =LabelFrame(self.root, text="Cold Drink", font=("times new roman" ,15,"bold"),bg=bg_color,fg="yellow",border= 5,relief=GROOVE)
        f4.place(x=600, y=165,height=380)

        item1_label= Label(f4, text="Maza:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=0, column=0,pady=5, padx=10)
        item2_entry= Entry(f4,textvariable=self.maza,border= 5,relief=SUNKEN ).grid(row=0, column=1, pady=5, padx=10)

        item1_label= Label(f4, text="Coke:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=1, column=0,pady=5, padx=10)
        item2_entry= Entry(f4,textvariable=self.coke,border=5, relief=SUNKEN ).grid(row=1, column=1, pady=5, padx=10)

        item3_label= Label(f4, text="Dew:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=2, column=0,pady=5, padx=10)
        item3_entry= Entry(f4,textvariable=self.dew, border=5, relief=SUNKEN ).grid(row=2, column=1, pady=5, padx=10)

        item4_label= Label(f4, text="Pepsi:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=3, column=0,pady=5, padx=10)
        item4_entry= Entry(f4,textvariable=self.pepsi, border=5, relief=SUNKEN ).grid(row=3, column=1, pady=5, padx=10)

        item5_label= Label(f4, text="Slice:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=4, column=0,pady=5, padx=10)
        item5_entry= Entry(f4,textvariable=self.slice, border=5, relief=SUNKEN ).grid(row=4, column=1, pady=5, padx=10)

        item6_label= Label(f4, text="ThumpsUp:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=5, column=0,pady=5, padx=10)
        item6_entry= Entry(f4,textvariable=self.thumsup, border=5, relief=SUNKEN ).grid(row=5, column=1, pady=5, padx=10)

        item7_label= Label(f4, text="Sprite:", font=("times new roman" ,15),fg= "white",bg=bg_color,padx=20).grid(row=6, column=0,pady=5, padx=10)
        item7_entry= Entry(f4,textvariable=self.sprite, border=5, relief=SUNKEN ).grid(row=6, column=1, pady=5, padx=10)

        # $$$$$ Bill Area
        f5 = Frame(self.root, border=5, relief=GROOVE, bg="red")
        bill_area = Label(f5, text="Bill_Area",font="lucida 15 bold", bd=5, relief=GROOVE).pack(fill=X)

        # Adding scrollbar
        scrolbar = Scrollbar(f5,orient=VERTICAL)
        scrolbar.pack(side=RIGHT, fill=Y)
        self.txtarea = Text(f5,yscrollcommand=scrolbar.set)
        scrolbar.config(command=self.txtarea.yview)
        self.txtarea.pack()
        f5.place(x=920, y=165, width=400,height=380)

        #Adding Bill Menu
        f6 = LabelFrame(self.root, text="Bill Summary", font=("times new roman", 15, "bold"), bg=bg_color, fg="yellow", border=5, relief=GROOVE)
        f6.place(x=0, y=550, relwidth=1, height=140)
        l1 = Label(f6, text="Total Cosmetic Amount", font=("times new roman", 15, "bold"),bg=bg_color).grid(row=0, column=0)
        t1 = Entry(f6,textvariable=self.cosmetic_price, border=5, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        l2 = Label(f6, text="Total Grocery Amount", font=("times new roman", 15, "bold"), bg=bg_color).grid(row=1, column=0)
        t2 = Entry(f6,textvariable=self.grocery_price, border=5, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10)
        l3 = Label(f6, text="Total Cold Drinks Amount", font=("times new roman", 15, "bold"), bg=bg_color).grid(row=2, column=0)
        t3 = Entry(f6,textvariable=self.coldDrink_price, border=5, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10)

        taxl1 = Label(f6, text="Tax on Cosmetic", font=("times new roman", 15, "bold"), bg=bg_color).grid(row=0, column=3)
        taxt1 = Entry(f6,textvariable=self.cosmetic_tax, border=5, relief=SUNKEN).grid(row=0, column=4, pady=5, padx=10)

        taxl2 = Label(f6, text="Tax on Grocery", font=("times new roman", 15, "bold"), bg=bg_color).grid(row=1, column=3)
        taxt2 = Entry(f6,textvariable=self.grocery_tax, border=5, relief=SUNKEN).grid(row=1, column=4, pady=5, padx=10)

        taxl3 = Label(f6, text="Tax on Cold Drinks", font=("times new roman", 15, "bold"), bg=bg_color).grid(row=2, column=3)
        taxt3 = Entry(f6,textvariable=self.coldDrink_tax, border=5, relief=SUNKEN).grid(row=2, column=4, pady=5, padx=10)

        btn_f = Frame(f6, bd=7, relief=GROOVE)
        btn_f.place(x=700, y=5, width=630, height=100)

        total_btn=Button(btn_f, command=self.total_amount ,text="Total",font="arial 15 bold",bg="cadetblue",width=10, bd=4, relief=GROOVE,padx=5,pady=6).grid(row=0,column=0,padx=7, pady=15)
        BG_btn = Button(btn_f, text="Generate Bill",command=self.bill_area, font="arial 15 bold", bg="cadetblue", width=10, bd=4, relief=GROOVE, padx=5, pady=6).grid(row=0, column=1, padx=5, pady=15)
        Print_btn = Button(btn_f, command=self.print_bill,text="Print", font="arial 15 bold", bg="cadetblue", width=10, bd=4, relief=GROOVE, padx=5, pady=6).grid(row=0, column=2, padx=5, pady=15)
        Clear_btn = Button(btn_f, command=self.clear_btn,text="Clear", font="arial 15 bold", bg="cadetblue", width=10, bd=4, relief=GROOVE, padx=5, pady=6).grid(row=0, column=3, padx=5, pady=15)
        self.welcome_bill()

    def bill_no(self):
        x=random.randint(1000,9999)
        if f"{x}.txt" not in os.listdir("bills/"):
            self.c_bill_no.set(x)
        else:
            self.bill_no()
            

    def total_amount(self):
        #total cosmetic value 
        self.c_s_price=self.soap_name.get()*40
        self.c_c_price=self.cream_name.get()*35
        self.c_fw_price=self.face_wash_name.get()*60
        self.c_hr_price=self.hair_spr_name.get()*120
        self.c_hg_price=self.hg_name.get()*45
        self.c_l_price=self.lotion_name.get()*32
        self.cosmetic_price.set(str(float(self.c_s_price+self.c_c_price+self.c_fw_price+self.c_hr_price+self.c_hg_price+self.c_l_price)))


        self.taxableCos=float(self.cosmetic_price.get())

        self.cosmetic_tax.set(str(round(self.taxableCos*(18/100),2)))

        #total total grocery value 

        self.g_r_price=self.rice.get()*40
        self.g_fo_price=self.foodOil.get()*98
        self.g_d_price=self.daal.get()*98
        self.g_s_price=self.sugar.get()*40
        self.g_t_price=self.tea.get()*102
        self.g_w_price=self.wheat.get()*25


        self.grocery_price.set(str(float(self.g_r_price+self.g_fo_price+self.g_d_price+self.g_s_price+self.g_t_price+self.g_w_price)))

        self.taxablegros=float(self.grocery_price.get())

        self.grocery_tax.set(str(round(self.taxablegros*(18/100),2)))

        #total cold drink value 

        self.co_m_price=self.maza.get()*95
        self.co_c_price=self.coke.get()*90
        self.co_d_price=self.dew.get()*85
        self.co_p_price=self.pepsi.get()*111
        self.co_s_price=self.slice.get()*105
        self.co_t_price=self.thumsup.get()*92
        self.co_sp_price=self.sprite.get()*40

        self.coldDrink_price.set(str(float(self.co_m_price+self.co_c_price+self.co_d_price+self.co_p_price+self.co_s_price+self.co_t_price+self.co_sp_price)))

        self.taxablecold=float(self.coldDrink_price.get())

        self.coldDrink_tax.set(str(round(self.taxablecold*(18/100),2)))

        self.total_Bill=round(float(self.cosmetic_price.get())+float(self.cosmetic_tax.get())+float(self.grocery_price.get())+float(self.grocery_tax.get())+float(self.coldDrink_price.get())+float(self.coldDrink_tax.get()),2)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome CHANDAN's Retail")
        self.txtarea.insert(END,f"\n\n Bill Number: {self.c_bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END,"\n==============================================")
        self.txtarea.insert(END,"\nProduct Name\t\t\tQTY\t\tPrice")
        self.txtarea.insert(END,"\n==============================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Add customer details")

        elif self.cosmetic_price.get()=="0.0" and self.grocery_price.get()=="0.0" and self.coldDrink_price.get()=="0.0":
            messagebox.showerror("Error","Add product to cart")

        else:
            self.welcome_bill()
            #for Cosmetics
            
            if self.soap_name.get()!=0:
                self.txtarea.insert(END,f"\nBath Soap\t\t\t{self.soap_name.get()}\t\t{self.c_s_price}")
            if  self.cream_name.get()!=0:
                self.txtarea.insert(END,f"\nFace Cream\t\t\t{self.cream_name.get()}\t\t{self.c_c_price}")
            if  self.face_wash_name.get()!=0:
                self.txtarea.insert(END,f"\nFace Wash\t\t\t{self.face_wash_name.get()}\t\t{self.c_fw_price}")
            if  self.hair_spr_name.get()!=0:
                self.txtarea.insert(END,f"\nHair Spray\t\t\t{self.hair_spr_name.get()}\t\t{self.c_hr_price}")
            if  self.hg_name.get()!=0:
                self.txtarea.insert(END,f"\nHair Gel\t\t\t{self.hg_name.get()}\t\t{self.c_hg_price}")
            if  self.lotion_name.get()!=0:
                self.txtarea.insert(END,f"\nBody Lotion\t\t\t{self.lotion_name.get()}\t\t{self.c_l_price}")
            # for Grocery
            if  self.rice.get()!=0:
                self.txtarea.insert(END,f"\nRice\t\t\t{self.rice.get()}\t\t{self.g_r_price}")
            if  self.foodOil.get()!=0:
                self.txtarea.insert(END,f"\nFood Oil\t\t\t{self.foodOil.get()}\t\t{self.g_fo_price}")
            if  self.daal.get()!=0:
                self.txtarea.insert(END,f"\nDaal\t\t\t{self.daal.get()}\t\t{self.g_d_price}")
            if  self.sugar.get()!=0:
                self.txtarea.insert(END,f"\nSugar\t\t\t{self.sugar.get()}\t\t{self.g_s_price}")
            if  self.tea.get()!=0:
                self.txtarea.insert(END,f"\nTea\t\t\t{self.tea.get()}\t\t{self.g_t_price}")
            if  self.wheat.get()!=0:
                self.txtarea.insert(END,f"\nWheat\t\t\t{self.wheat.get()}\t\t{self.g_w_price}")

            # for cold drinks
            if  self.maza.get()!=0:
                self.txtarea.insert(END,f"\nMaza\t\t\t{self.maza.get()}\t\t{self.co_m_price}")
            if  self.coke.get()!=0:
                self.txtarea.insert(END,f"\nCoke\t\t\t{self.coke.get()}\t\t{self.co_c_price}")
            if  self.dew.get()!=0:
                self.txtarea.insert(END,f"\nDew\t\t\t{self.dew.get()}\t\t{self.co_d_price}")
            if  self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\nPepsi\t\t\t{self.pepsi.get()}\t\t{self.co_p_price}")
            if  self.slice.get()!=0:
                self.txtarea.insert(END,f"\nSlice\t\t\t{self.slice.get()}\t\t{self.co_s_price}")
            if  self.thumsup.get()!=0:
                self.txtarea.insert(END,f"\nThums UP\t\t\t{self.thumsup.get()}\t\t{self.co_t_price}")
            if  self.sprite.get()!=0:
                self.txtarea.insert(END,f"\nSprite\t\t\t{self.sprite.get()}\t\t{self.co_sp_price}")


            self.txtarea.insert(END,"\n==============================================")
            if self.cosmetic_tax.get()!="0.0":
                self.txtarea.insert(END,f"\nCosmetic Amount:{self.cosmetic_price.get()}\t\t\tCosmetic Tax:{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="0.0":
                self.txtarea.insert(END,f"\nGrocery Amount:{self.grocery_price.get()}\t\t\tGrocery Tax:{self.grocery_tax.get()}")

            if self.coldDrink_tax.get()!="0.0":
                self.txtarea.insert(END,f"\nCold Drink Amount:{self.coldDrink_price.get()}\tCold Drint Tax:{self.coldDrink_tax.get()}")

            self.txtarea.insert(END,f"\n\nTotal Bill Amount:  Rs. {self.total_Bill}")
            self.txtarea.insert(END,"\n==============================================")

            self.txtarea.insert(END,"\n\n\tThank you for shopping with us")
            self.txtarea.insert(END,"\n\t     Have a nice day!.")
            self.save_bill()

    def save_bill(self):
        save=messagebox.askyesno("Bill Save","Do you want to save the bill?")
        if save:
            self.bill_data=self.txtarea.get('1.0',END)
            f= open(f"bills/{str(self.c_bill_no.get())}.txt","w")
            f.write(self.bill_data)
            f.close()
            messagebox.showinfo("Bill Saved",f"Bill No. {self.c_bill_no.get()} saved Successfully.")

        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0] ==self.c_serach.get():
                f1= open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                
                for d in f1:
                    self.txtarea.insert(END,d)
                    
                f1.close()
                present="yes"

        if present=="no":
            messagebox.showerror("Error","Bill no is not generated yet.")

    def clear_btn(self):
        ans=messagebox.askyesno("Clear Data", "Do you really want to clear the data?")
        if ans:
            
            # for Cosmetics
            self.soap_name.set(0)
            self.cream_name.set(0)
            self.face_wash_name.set(0)
            self.hair_spr_name.set(0)
            self.hg_name.set(0)
            self.lotion_name.set(0)
            # for Grocery
            self.rice.set(0)
            self.foodOil.set(0)
            self.daal.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            self.wheat.set(0)

            # for cold drinks
            self.maza.set(0)
            self.coke.set(0)
            self.dew.set(0)
            self.pepsi.set(0)
            self.slice.set(0)
            self.thumsup.set(0)
            self.sprite.set(0)

            #variable for total price
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.coldDrink_price.set("")

            #variable for total tax
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.coldDrink_tax.set("")

            #Variable for customer detail
            self.c_name.set("")
            self.c_phone.set("")
            self.c_bill_no.set("")
            # x=random.randint(1000,9999)
            # self.c_bill_no.set(str(x))
            self.c_serach.set("")
            self.bill_no()
            self.welcome_bill()

    def print_bill(self):
        bprint=messagebox.askyesno("Bill print","Do you want to print this bill?")
        if bprint:
            temp_file=tempfile.mktemp('.txt')
            open (temp_file,"w").write(self.txtarea.get('1.0',END))
            os.startfile(temp_file,'print')

            


        
root = Tk()
obj = Bill_App(root)
root.mainloop()