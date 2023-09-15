import tkinter
import tkinter.messagebox
import sql_control
import restaurant_page
import customer_page
import rider_page
import views
import parameter

class login_page:

        #容器制作
        #图标root.iconbitmap("")
        #背景色root.config(bg="blue")

    def __init__(self,master):
        self.root=master
        self.root.title("餐厅订餐系统")
        self.root.geometry("600x400")

        self.fr1= tkinter.Frame(root)
        self.fr1.pack(expand=True)

        self.r2 = views.C_register_frame(self.fr1)
        self.r1 = views.R_register_frame(self.fr1)


        self.username=tkinter.StringVar()
        self.password=tkinter.StringVar()

        self.page1=tkinter.Frame(self.fr1)
        self.page1.grid()

        self.user=tkinter.StringVar()
        self.user.set('n')
        tkinter.Radiobutton(self.page1, text="我是餐厅", variable=self.user, value='r',font=parameter.label_font).grid(row=4, column=2,sticky='w')
        tkinter.Radiobutton(self.page1,text="我是顾客",variable=self.user,value='C',font=parameter.label_font).grid(row=5,column=2,sticky='w')
        tkinter.Radiobutton(self.page1, text="我是骑手", variable=self.user, value='R',font=parameter.label_font).grid(row=6, column=2,sticky='w')

        tkinter.Label(self.page1, text="XX饭店平台",font=parameter.label_font).grid(row=0, column=1,columnspan=2)
        tkinter.Label(self.page1,text="账号",font=parameter.label_font).grid(row=1,column=1, pady=10)
        tkinter.Entry(self.page1,textvariable=self.username).grid(row=1, column=2)

        tkinter.Label(self.page1,text="密码",font=parameter.label_font).grid(row=2,column=1,pady=10)
        tkinter.Entry(self.page1,textvariable=self.password).grid(row=2, column=2)

        tkinter.Button(self.page1, text="注册", command=self.注册, font=parameter.botton_font).grid(row=3, column=1, pady=10)
        tkinter.Button(self.page1, text="登录",command=self.登录, font=parameter.botton_font).grid(row=3, column=2,pady=10,sticky='w')
        tkinter.Button(self.page1, text="退出",command=self.page1.quit, font=parameter.botton_font).grid(row=3, column=2,sticky='e')


    def 登录(self):

        if self.user.get()=='r' and self.验证(1):
            self.fr1.destroy()
            restaurant_page.restaurant_page(self.root)
            print("登录成功")
        elif self.user.get()=='C' and self.验证(2):
            self.fr1.destroy()
            customer_page.customer_page(self.root,self.username.get())
            print("登录成功")
        elif self.user.get()=='R' and self.验证(3):
            self.fr1.destroy()
            rider_page.rider_page(self.root,self.username.get())
            print("登录成功")
        else:
            tkinter.messagebox.showwarning(title='警告',message='登录失败')
    def 验证(self,user):
        sql="select C_id,C_password from customer"
        date1=sql_control.sql_control(sql).result
        sql = "select R_id,R_password from rider"
        date2 = sql_control.sql_control(sql).result
        print(date1)

        if user==1 and self.username.get()=='admin' and self.password.get()=='123456':
            return True
        if user==2 and (eval(self.username.get()),self.password.get()) in date1:
            return True
        if user == 3 and (eval(self.username.get()), self.password.get()) in date2:
            return True

    def 注册(self):
        if self.user.get()== 'R':
            self.page1.grid_forget()

            self.r1 .grid(row=1, column=1)
            self.r3=tkinter.Button(self.fr1, text="注册", command=self.qiut, font=parameter.botton_font)
            self.r3.grid(row=2, column=1, sticky=tkinter.E)

        elif self.user.get() == 'C':
            self.page1.grid_forget()
            self.r2.grid(row=1, column=1)
            self.r3=tkinter.Button(self.fr1, text="退出", command=self.qiut, font=parameter.botton_font)
            self.r3.grid(row=2, column=1, sticky=tkinter.E)
        else:
            tkinter.messagebox.showwarning(title='警告',message='请选择顾客或骑手')

    def qiut(self):
            self.r1.grid_forget()
            self.r2.grid_forget()
            self.r3.grid_forget()
            self.page1.grid()






if __name__=="__main__":
    root = tkinter.Tk()
    login_page(master=root)
    root.mainloop()