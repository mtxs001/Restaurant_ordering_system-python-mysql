import tkinter
import tkinter.messagebox
from tkinter import ttk
import sql_control
import parameter



# class 名称frame(tkinter.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         此处填写变量
#         self.create_page()
#     def create_page(self):
#         此处填写框架并打包（pack\grid\place）
#         self.show_data_frame()#刷新，得到数据
#     def show_data_frame(self):
#         此处填写功能

#饭店的页面

#菜谱页面
class menusframe(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.status=tkinter.StringVar()

        self.create_page()

    def create_page(self):
        self.fr1=tkinter.Frame(self)
        self.fr1.grid(row=1, column=1,rowspan=3,sticky="n")

        tkinter.Button(self.fr1,text="刷新数据",command=self.show_data_frame,font=parameter.botton_font).grid(row=3,column=1,sticky="e")
        tkinter.Label(self, textvariable=self.status,font=parameter.label_font).grid(row=2, column=2)

        tkinter.Label(self.fr1, text="菜谱操作：",font=parameter.label_font).grid(row=1, column=1)

        self.con_menusframe=con_menusframe(self.fr1,self.status,self)
        self.con_menusframe.grid(row=2, column=1)

        self.show_data_frame()

    def show_data_frame(self):
        columns = ("M_id", "M_name", "M_original_price", "M_discount", "M_present_price", "M_class")
        columns_cn = ("序列号", "菜名", "原价", "折扣", "现价", "分类")
        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        for i in columns:
            self.tree_view.column(i, width=140, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=1, column=2, pady=5, padx=5,sticky="nw")

        for _ in map(self.tree_view.delete,self.tree_view.get_children("")):
            pass

        sql = "select * from menus"
        menus_data=sql_control.sql_control(sql).result

        index=0
        for dish in menus_data:
            self.tree_view.insert(parent='',index=index+1,values=dish)
            index = index + 1

        self.con_menusframe.status.set("刷新成功！")

class con_menusframe(tkinter.Frame):
    def __init__(self, root,status,fr1):
        super().__init__(root)
        self.fr1=fr1

        self.M_ID=tkinter.StringVar()
        self.M_name=tkinter.StringVar()
        self.M_original_price=tkinter.StringVar()
        self.M_discount=tkinter.StringVar()
        self.M_discount.set('1')
        self.M_class=tkinter.StringVar()
        self.delete_data = tkinter.StringVar()

        self.status=status
        self.create_page()

    def create_page(self):
        tkinter.Label(self, text="序列号：", font=parameter.label_font).grid(row=1, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.delete_data, font=parameter.enter_font).grid(row=1, column=2)

        tkinter.Label(self, text="菜   名：",font=parameter.label_font).grid(row=2, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.M_name,font=parameter.enter_font).grid(row=2, column=2)

        tkinter.Label(self, text="原    价：",font=parameter.label_font).grid(row=3, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.M_original_price,font=parameter.enter_font).grid(row=3, column=2)

        tkinter.Label(self, text="折    扣：", font=parameter.label_font).grid(row=4, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.M_discount, font=parameter.enter_font).grid(row=4, column=2)

        tkinter.Label(self, text="分   类：",font=parameter.label_font).grid(row=5, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.M_class,font=parameter.enter_font).grid(row=5, column=2)

        tkinter.Button(self, text="插入数据", command=self.insert_data,font=parameter.botton_font).grid(row=6, column=2, sticky=tkinter.E)
        tkinter.Button(self, text="修改数据", command=self.update_data, font=parameter.botton_font).grid(row=7, column=2, sticky=tkinter.E)
        tkinter.Button(self, text="删除数据", command=self.delete_data_frame, font=parameter.botton_font).grid(row=8, column=2, sticky=tkinter.E)
        tkinter.Button(self, text="查看套餐", command=self.group_menus_data, font=parameter.botton_font).grid(row=9, column=2, sticky=tkinter.E)
        tkinter.Button(self, text="添加套餐", command=self.add_group_menus_data, font=parameter.botton_font).grid(row=10, column=2, sticky=tkinter.E)
        tkinter.Button(self, text="删除套餐", command=self.delete_group_menus_data, font=parameter.botton_font).grid(row=11, column=2, sticky=tkinter.E)

    def group_menus_data(self):
        columns = ('Men_M_id','M_id','M_name','M_original_price','M_discount','M_present_price','M_class')
        columns_cn = ("套餐序列", "菜品序列","菜名","原价","折扣", "现价", "分类")
        self.tree_view = ttk.Treeview(self.fr1, show="headings", columns=columns)
        for i in columns:
            self.tree_view.column(i, width=120, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=3, column=2,pady=5,padx=5,sticky="w")

        for _ in map(self.tree_view.delete,self.tree_view.get_children("")):
            pass
        if len(self.delete_data.get())!=0:
            sql = "select * from `套餐菜单`where  Men_M_id=%s"%self.delete_data.get()
            menus_data=sql_control.sql_control(sql).result
            index=0
            for dish in menus_data:
                self.tree_view.insert(parent='',index=index+1,values=dish)
            self.Men = self.delete_data.get()
        else:
            self.status.set("你好像什么都没填！")
    def add_group_menus_data(self):
        print(self.Men,1)
        print(self.delete_data.get(),2)
        if len(self.delete_data.get())==0:
            self.status.set("你好像什么都没填！")

        elif self.Men!=self.delete_data.get():
            sql="insert into group_menus_content values ('%s','%s')"%(self.Men,self.delete_data.get())
            sql_control.sql_control(sql)
            self.status.set("添加套餐成功!")
        else:
            self.status.set("错误！")
        self.delete_data.set(self.Men)
        self.group_menus_data()
    def delete_group_menus_data(self):
        if len(self.delete_data.get())==0:
            self.status.set("你好像什么都没填！")
        elif self.Men!=self.delete_data.get():
            sql="delete from group_menus_content where Men_M_id=%s and M_id=%s"%(self.Men,self.delete_data.get())
            sql_control.sql_control(sql)
            self.status.set("删除套餐成功!")
        else:
            self.status.set("错误！")
        self.delete_data.set(self.Men)
        self.group_menus_data()
    def insert_data(self):
        if len(self.M_name.get()) == 0 or len(self.M_original_price.get()) == 0 or len(self.M_class.get()) == 0:
            self.status.set("你好像有什么没填！")
        else:
            sql = 'insert into menus2(M_name,M_original_price,M_discount,M_class) values ("%s","%s","%s","%s")'%(self.M_name.get(),self.M_original_price.get(),self.M_discount.get(),self.M_class.get())
            sql_control.sql_control(sql)

            self.status.set("插入成功!")
            self.M_ID.set('')
            self.M_name.set('')
            self.M_original_price.set('')
            self.M_discount.set('1')
            self.M_class.set('')

    def delete_data_frame(self):
        if len(self.delete_data.get())==0:
            self.status.set("你好像什么都没填！")
        else:
            sql="delete from menus2 where M_id='%s'"%self.delete_data.get()
            print(sql)
            sql_control.sql_control(sql)
            self.delete_data.set('')
            self.status.set("删除成功!")

    def update_data(self):
        if len(self.M_original_price.get())!=0:
            sql ="update menus2 set M_original_price=%s where M_id=%s"%(self.M_original_price.get(),self.delete_data.get())
            sql_control.sql_control(sql)
        if len(self.M_discount.get())!=0:
            sql ="update menus2 set M_discount=%s where M_id=%s"%(self.M_discount.get(),self.delete_data.get())
            sql_control.sql_control(sql)
        self.status.set("更新成功!")
        self.M_ID.set('')
        self.M_name.set('')
        self.M_original_price.set('')
        self.M_discount.set('1')
        self.M_class.set('')


#关于页面
class aboutframe(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)

        tkinter.Label(self, text="作者：漫天星沙\n说明").pack()

#订单页面
class orderframe(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.flag1=1

        self.create_page()


    def create_page(self):
        self.fr1 = tkinter.Frame(self)
        self.fr1.grid(row=2, column=1, sticky="n")

        tkinter.Label(self.fr1, text="订单操作：",font=parameter.label_font).grid(row=1, column=1)
        tkinter.Button(self.fr1, text="详细页面", command=self.detail_data,font=parameter.botton_font).grid(row=3 , column=1)
        tkinter.Button(self.fr1, text="省略页面", command=self.omit_data, font=parameter.botton_font).grid(row=4 , column=1)

        self.updateorderframe=updateorderframe(self.fr1,self)
        self.updateorderframe.grid(row=2, column=1)

        self.show_data_frame()
    def show_data_frame(self):

        self.updateorderframe.update_status.set('')


        if self.flag1==1:
            columns=('O_id','O_time','O_commit','O_delete_status','O_make_status','O_eat_status')
            columns_cn = ('O_id','O_time','O_commit','O_delete_status','O_make_status','O_eat_status')
        else:
            columns = ('O_id','O_time','C_name','C_phone','T_name','T_status','O_delete_status','O_commit','O_make_status','R_name','R_phone','O_eat_status')
            columns_cn =  ('O_id','O_time','C_name','C_phone','T_name','T_status','O_delete_status','O_commit','O_make_status','R_name','R_phone','O_eat_status')
        self.tree_view=ttk.Treeview(self,show="headings",columns=columns)
        for i in columns:
            self.tree_view.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=2,column=2,pady=5,padx=5)

        for _ in map(self.tree_view.delete,self.tree_view.get_children("")):
            pass

        if self.flag1==1:
            sql = "select * from `订单`"
        else:
            sql = "select * from `订单2`"
        order_data = sql_control.sql_control(sql).result

        index=0
        for order in order_data:
            self.tree_view.insert(parent='',index=index+1,values=order)
            index=index+1
    def detail_data(self):
        self.flag1=0
        self.tree_view.grid_forget()
        self.show_data_frame()

    def omit_data(self):
        self.flag1=1
        self.tree_view.grid_forget()
        self.show_data_frame()

class updateorderframe(tkinter.Frame):

    def __init__(self, root,fr1):
        super().__init__(root)

        self.update_data = tkinter.StringVar()
        self.update_status = tkinter.StringVar()
        self.fr1=fr1
        self.create_page()

    def create_page(self):

        tkinter.Label(self, text="序列号").grid(row=0, column=1)
        tkinter.Entry(self, textvariable=self.update_data).grid(row=1, column=1)
        tkinter.Button(self, text="完成订单", command=self.delete_data_frame, font=parameter.botton_font).grid(row=3, column=1)
        tkinter.Button(self, text="订单详情", command=self.ordering_menus_date, font=parameter.botton_font).grid(row=2, column=1)
        tkinter.Label(self.fr1, textvariable=self.update_status).grid(row=3, column=1)

    def ordering_menus_date(self):

        columns=('O_id','M_name','M_original_price','M_discount','M_present_price')
        columns_cn =('O_id','M_name','M_original_price','M_discount','M_present_price')
        self.tree_view=ttk.Treeview(self.fr1,show="headings",columns=columns)
        for i in columns:
            self.tree_view.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=3, column=2,pady=5,padx=5,sticky='w')

        for _ in map(self.tree_view.delete,self.tree_view.get_children("")):
            pass

        sql = "select * from `订单菜谱`where O_id='%s'"%self.update_data.get()
        order_data = sql_control.sql_control(sql).result

        index=0
        for order in order_data:
            self.tree_view.insert(parent='',index=index+1,values=order)
            index=index+1

    def delete_data_frame(self):
        if len(self.update_data.get())==0:
            self.update_status.set("你好像什么都没填！")
        else:
            sql="select O_eat_status from ordering where O_id='%s'"%self.update_data.get()
            O_eat_status=sql_control.sql_control(sql).result
            O_eat_status='%s'%O_eat_status[-1]

            if O_eat_status=='未取餐':
                sql = "update ordering set O_delete_status='无法撤销',O_make_status='制作完成',O_eat_status='就餐中' where O_id='%s'" % self.update_data.get()
            else:
                sql="update ordering set O_delete_status='无法撤销',O_make_status='制作完成' where O_id='%s'"%self.update_data.get()

            sql_control.sql_control(sql)
            self.update_data.set('')
            self.update_status.set("更新成功!")

#员工页面
class employeeframe(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.create_page()

    def create_page(self):

        columns=('W_id','W_name','W_sex','W_age','W_phone','W_work_status','W_health_status')
        columns_cn =('W_id','W_name','W_sex','W_age','W_phone','W_work_status','W_health_status')
        self.tree_view=ttk.Treeview(self,show="headings",columns=columns)
        for i in columns:
            self.tree_view.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=1, column=2,pady=5,padx=5)

        self.fr1=tkinter.Frame(self)
        self.fr1.grid(row=1, column=1,sticky="n")
        tkinter.Label(self.fr1, text="员工操作:", font=parameter.label_font).grid(row=1, columns=1)
        tkinter.Button(self.fr1,text="刷新数据",command=self.show_data_frame,font=parameter.botton_font).grid(row=3, sticky=tkinter.E)

        self.insertemployeeframe = insertemployeeframe(self.fr1)
        self.insertemployeeframe.grid(row=2, columns=1)

        self.show_data_frame()
    def show_data_frame(self):

        self.insertemployeeframe.status.set('')
        for _ in map(self.tree_view.delete,self.tree_view.get_children("")):
            pass

        sql ='''
       select * from waiter
        '''
        order_data=sql_control.sql_control(sql).result

        index=0
        for order in order_data:
            self.tree_view.insert(parent='',index=index+1,values=order)
            index = index + 1

class insertemployeeframe(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.E_ID = tkinter.StringVar()
        self.E_name = tkinter.StringVar()
        self.E_sex = tkinter.StringVar()
        self.E_age = tkinter.StringVar()
        self.E_phone = tkinter.StringVar()

        self.delete_data = tkinter.StringVar()

        self.status = tkinter.StringVar()

        self.create_page()

    def create_page(self):
        tkinter.Label(self, text="员工序号：", font=parameter.label_font).grid(row=0, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.delete_data,font=parameter.enter_font).grid(row=0, column=2)
        tkinter.Label(self, text="员工姓名：", font=parameter.label_font).grid(row=1, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.E_name,font=parameter.enter_font).grid(row=1, column=2)
        tkinter.Label(self, text="员工性别：", font=parameter.label_font).grid(row=2, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.E_sex,font=parameter.enter_font).grid(row=2, column=2)
        tkinter.Label(self, text="员工年龄：", font=parameter.label_font).grid(row=3, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.E_age,font=parameter.enter_font).grid(row=3, column=2)
        tkinter.Label(self, text="联系电话：", font=parameter.label_font).grid(row=4, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.E_phone,font=parameter.enter_font).grid(row=4, column=2)

        tkinter.Label(self, textvariable=self.status).grid(row=5, column=1)
        tkinter.Button(self, text="插入数据", command=self.insert_data,font=parameter.botton_font).grid(row=5, column=2, sticky=tkinter.E)

        tkinter.Button(self, text="删除数据", command=self.delete_data_frame,font=parameter.botton_font).grid(row=6, column=2, sticky=tkinter.E)


    def insert_data(self):
        if len(self.E_name.get())!=0:
            sql = 'insert into waiter(W_name,W_sex,W_age,W_phone) values ("%s","%s","%s","%s")' % (self.E_name.get(), self.E_sex.get(), self.E_age.get(),self.E_phone.get())
            sql_control.sql_control(sql)
            self.status.set("插入成功!")
        else:
            self.status.set("插入失败!")
        self.E_name.set('')
        self.E_sex.set('')
        self.E_age.set('')
        self.E_phone.set('')
    def delete_data_frame(self):

        if len(self.delete_data.get())==0:
            self.status.set("你好像什么都没填！")
        else:
            sql="delete from waiter where W_id=%s"%self.delete_data.get()
            print(sql)
            sql_control.sql_control(sql)
            self.delete_data.set('')
            self.status.set("删除成功!")

#餐桌页面
class tableframe(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.create_page()

    def create_page(self):

        columns=('T_id','T_name','T_content','T_status')
        columns_cn =('T_id','T_name','T_content','T_status')
        self.tree_view=ttk.Treeview(self,show="headings",columns=columns)
        for i in columns:
            self.tree_view.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=1, column=2,pady=5,padx=5)

        self.fr1=tkinter.Frame(self)
        self.fr1.grid(row=1, column=1,sticky="n")
        tkinter.Label(self.fr1, text="餐桌操作:", font=parameter.label_font).grid(row=1, columns=1)
        tkinter.Button(self.fr1,text="刷新数据",command=self.show_data_frame,font=parameter.botton_font).grid(row=3, sticky=tkinter.E)

        self.insertemployeeframe = inserttableframe(self.fr1)
        self.insertemployeeframe.grid(row=2, columns=1)

        self.show_data_frame()
    def show_data_frame(self):

        self.insertemployeeframe.status.set('')
        for _ in map(self.tree_view.delete,self.tree_view.get_children("")):
            pass

        sql ='''
       select * from food_table
        '''
        order_data=sql_control.sql_control(sql).result

        index=0
        for order in order_data:
            self.tree_view.insert(parent='',index=index+1,values=order)

class inserttableframe(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.E_ID = tkinter.StringVar()
        self.E_name = tkinter.StringVar()
        self.E_sex = tkinter.StringVar()
        self.E_age = tkinter.StringVar()

        self.delete_data = tkinter.StringVar()

        self.status = tkinter.StringVar()

        self.create_page()

    def create_page(self):
        tkinter.Label(self, text="餐桌序号：", font=parameter.label_font).grid(row=0, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.delete_data,font=parameter.enter_font).grid(row=0, column=2)
        tkinter.Label(self, text="餐桌名称：", font=parameter.label_font).grid(row=1, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.E_name,font=parameter.enter_font).grid(row=1, column=2)
        tkinter.Label(self, text="餐桌容量：", font=parameter.label_font).grid(row=2, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.E_sex,font=parameter.enter_font).grid(row=2, column=2)
        tkinter.Label(self, text="餐桌状态：", font=parameter.label_font).grid(row=3, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.E_age,font=parameter.enter_font).grid(row=3, column=2)


        tkinter.Label(self, textvariable=self.status).grid(row=5, column=1)
        tkinter.Button(self, text="插入数据", command=self.insert_data,font=parameter.botton_font).grid(row=5, column=2, sticky=tkinter.E)

        tkinter.Button(self, text="删除数据", command=self.delete_data_frame,font=parameter.botton_font).grid(row=6, column=2, sticky=tkinter.E)


    def insert_data(self):
        if len(self.E_name.get())!=0:
            sql = 'insert into food_table(T_name,T_content,T_status) values ("%s","%s","%s")' % (self.E_name.get(), self.E_sex.get(), self.E_age.get())
            sql_control.sql_control(sql)
            self.status.set("插入成功!")
        else:
            self.status.set("插入失败!")
        self.E_name.set('')
        self.E_sex.set('')
        self.E_age.set('')

    def delete_data_frame(self):

        if len(self.delete_data.get())==0:
            self.status.set("你好像什么都没填！")
        else:
            sql="delete from food_table where T_id=%s"%self.delete_data.get()
            print(sql)
            sql_control.sql_control(sql)
            self.delete_data.set('')
            self.status.set("删除成功!")

#统计界面
class countframe(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)

        # 此处填写变量
        self.create_page()
    def create_page(self):
        # 此处填写框架并打包（pack\grid\place）


        self.flag1 = tkinter.Label(self, text="订单利润")
        self.flag1.grid(row=2, column=2)
        columns = ('O_id','O_time','M_sum_profit','O_make_status')
        columns_cn = ("序列号", "时间", "总价格","状态")
        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        for i in columns:
            self.tree_view.column(i, width=150, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=3, column=2, pady=5, padx=5, sticky="nw")


        self.flag2 = tkinter.Label(self, text="销量统计")
        self.flag2.grid(row=4, column=2)
        columns = ('M_id','M_name','M_original_price','M_sum_number','M_sum_price')
        columns_cn = ("序列号", "菜名", "原价", "销量", "总价")
        self.tree_view1 = ttk.Treeview(self, show="headings", columns=columns)
        for i in columns:
            self.tree_view1.column(i, width=120, anchor="center")
        for i in range(len(columns)):
            self.tree_view1.heading(columns[i], text=columns_cn[i])
        self.tree_view1.grid(row=5, column=2, pady=5, padx=5, sticky="nw")

        tkinter.Label(self, text="总销售价格").grid(row=6, column=2,sticky='w')
        sql = "SELECT `总毛利润`.gross_profit FROM `总毛利润`"
        self.status = sql_control.sql_control(sql).result
        self.status = '%s' % (self.status[0])
        print(self.status)
        tkinter.Label(self, text='%s'%self.status, font=parameter.label_font).grid(row=6, column=2,sticky='e')

        self.show_data_frame()
    def show_data_frame(self):
        # 此处填写功能

        for _ in map(self.tree_view1.delete,self.tree_view1.get_children("")):
            pass
        sql = "select * from `统计2`"
        menus_data=sql_control.sql_control(sql).result
        index=0
        for dish in menus_data:
            self.tree_view1.insert(parent='',index=index+1,values=dish)

        for _ in map(self.tree_view.delete,self.tree_view.get_children("")):
            pass

        sql = "select * from `统计1`"
        menus_data=sql_control.sql_control(sql).result

        index=0
        for dish in menus_data:
            self.tree_view.insert(parent='',index=index+1,values=dish)

#顾客订餐的页面
class c_menusframe(tkinter.Frame):


    def __init__(self, root,username):
        super().__init__(root)
        self.fr1 = tkinter.Frame(self)
        self.fr2 = tkinter.Frame(self)

        self.create_page(username)
    def create_page(self,username):

        self.fr1.grid(row=1, column=1, sticky="n")
        self.fr2.grid(row=2, column=1, sticky="wn")
        tkinter.Label(self.fr1, text="订餐页").grid(row=2,column=2)
        columns = ("M_id", "M_name", "M_original_price", "M_discount", "M_present_price", "M_class","M_sum_number")
        columns_cn = ("序列号", "菜名", "原价", "折扣", "现价", "分类","累计销量")
        self.tree_view = ttk.Treeview(self.fr1, show="headings", columns=columns)
        for i in columns:
            self.tree_view.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=3,column=2)

        tkinter.Label(self.fr1, text="套餐页").grid(row=2,column=3)
        columns = ("M_id", "M_name", "M_original_price", "M_discount", "M_present_price", "M_class", "M_sum_number")
        columns_cn = ("序列号", "菜名", "原价", "折扣", "现价", "分类", "累计销量")
        self.tree_view1 = ttk.Treeview(self.fr1, show="headings", columns=columns)
        for i in columns:
            self.tree_view1.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view1.heading(columns[i], text=columns_cn[i])
        self.tree_view1.grid(row=3,column=3)



        tkinter.Button(self.fr1,text="刷新数据",command=self.show_data_frame).grid(row=4,column=2,sticky="w",pady=5)
        self.ordermenusframe=ordermenusframe(self.fr2,username)
        self.ordermenusframe.grid(row=1)

        self.show_data_frame()

    def show_data_frame(self):
        self.ordermenusframe.order_status.set('')

        for _ in map(self.tree_view.delete,self.tree_view.get_children("")):
            pass

        sql = "select * from `菜谱`"
        menus_data=sql_control.sql_control(sql).result

        index=0
        for dish in menus_data:
            self.tree_view.insert(parent='',index=index+1,values=dish)
            index = index + 1
        for _ in map(self.tree_view1.delete,self.tree_view1.get_children("")):
            pass

        sql = "select * from `套餐`"
        menus_data=sql_control.sql_control(sql).result

        index=0
        for dish in menus_data:
            self.tree_view1.insert(parent='',index=index+1,values=dish)

class ordermenusframe(tkinter.Frame):
    def __init__(self, root,username):
        super().__init__(root)
        #此处填写变量
        self.flag1=1
        self.fr2 = tkinter.Frame(self)
        self.index = 0

        self.order=[]

        self.order_id=tkinter.StringVar()
        self.order_number=tkinter.StringVar()
        self.order_status=tkinter.StringVar()
        self.order_employee=tkinter.StringVar()
        self.order_TD_id=tkinter.StringVar()
        self.order_commit=tkinter.StringVar()
        self.username=username

        self.create_page()
    def create_page(self):
        # 此处填写框架并打包（pack\grid\place）
        self.fr2.grid(row=1, column=1, sticky="n")
        tkinter.Label(self.fr2, text="请输入菜谱序列号：").grid(row=1, column=1)
        tkinter.Entry(self.fr2, textvariable=self.order_id).grid(row=1, column=2)
        tkinter.Label(self.fr2, text="请输入菜谱数量：").grid(row=2, column=1)
        tkinter.Entry(self.fr2, textvariable=self.order_number).grid(row=2, column=2)
        tkinter.Label(self.fr2, text="请输入餐桌序号：").grid(row=4, column=1)
        tkinter.Entry(self.fr2, textvariable=self.order_TD_id).grid(row=4, column=2)
        tkinter.Label(self.fr2, text="请输入备注：").grid(row=5, column=1)
        tkinter.Entry(self.fr2, textvariable=self.order_commit).grid(row=5, column=2)
        tkinter.Label(self.fr2,textvariable=self.order_status).grid(row=6, column=1)

        tkinter.Button(self.fr2, text="何处就餐", command=self.table_data).grid(row=6, column=2)
        tkinter.Button(self.fr2, text="查看套餐", command=self.group_menus_data).grid(row=7, column=2)
        tkinter.Button(self.fr2, text="添加餐品", command=self.add_menus_data).grid(row=8, column=2)
        tkinter.Button(self.fr2, text="清空餐品", command=self.end_menus_data).grid(row=9, column=2)
        tkinter.Button(self.fr2, text="删除餐品", command=self.delete_menus_data).grid(row=10, column=2)
        tkinter.Button(self.fr2, text="完成订单", command=self.over_order).grid(row=11, column=2)

        self.text2=tkinter.Label(self, text="我的订单")
        self.text2.grid(row=0, column=2)
        columns = ("M_id", "M_name", "M_original_price", "M_discount", "M_present_price", "M_class", "M_sum_number")
        columns_cn = ("序列号", "菜名", "原价", "折扣", "现价", "分类", "累计销量")
        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        for i in columns:
            self.tree_view.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=1, column=2)

        self.text1 = tkinter.Label(self, text="套餐详情")
        columns = ("M_id", "M_name", "M_original_price", "M_discount", "M_present_price", "M_class", "M_sum_number")
        columns_cn = ("序列号", "菜名", "原价", "折扣", "现价", "分类", "累计销量")
        self.tree_view1 = ttk.Treeview(self, show="headings", columns=columns)
        for i in columns:
            self.tree_view1.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view1.heading(columns[i], text=columns_cn[i])

        self.text3 = tkinter.Label(self, text="套餐详情")
        columns = ('T_id', 'T_name', 'T_content', 'T_status')
        columns_cn = ('T_id', 'T_name', 'T_content', 'T_status')
        self.tree_view3 = ttk.Treeview(self, show="headings", columns=columns)
        for i in columns:
            self.tree_view3.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view3.heading(columns[i], text=columns_cn[i])

    def table_data(self):
        self.tree_view.grid_forget()
        self.text2.grid_forget()
        self.tree_view1.grid_forget()
        self.text1.grid_forget()
        self.text3.grid(row=0, column=2)
        self.tree_view3.grid(row=1, column=2)
        for _ in map(self.tree_view3.delete, self.tree_view3.get_children("")):
            pass
        sql = '''
               select * from food_table
                '''
        order_data = sql_control.sql_control(sql).result
        index = 0
        for order in order_data:
            self.tree_view3.insert(parent='', index=index + 1, values=order)

    def over_order(self):
        sql = "select now()"
        time=sql_control.sql_control(sql).result
        time = '%s' % (time[0])
        if len(self.order_TD_id.get())!=0 and len(self.order_commit.get())!=0:
            if eval(self.order_TD_id.get())==3:
                sql = 'insert into ordering(C_id,T_id,R_id,O_time,O_commit,O_delete_status,O_make_status,O_eat_status) values (%s,%s,0,"%s",%s,"可撤销","未完成","未运送")'% (self.username,self.order_TD_id.get(),time,self.order_commit.get())
            else:
                sql = 'insert into ordering(C_id,T_id,R_id,O_time,O_commit,O_delete_status,O_make_status,O_eat_status) values (%s,%s,0,"%s",%s,"可撤销","未完成","未取餐")' % (self.username, self.order_TD_id.get(), time, self.order_commit.get())

            sql_control.sql_control(sql)
            sql = 'select O_id from ordering where  O_time="%s"' %time
            menus_data = '%s'%sql_control.sql_control(sql).result[0]
            for i in self.order:
                print((menus_data,i))
                sql = "insert into order_menus values (%s,%s)" % (menus_data,i)
                sql_control.sql_control(sql)
            sql = "select * from count"
            sql_control.sql_control(sql)
            time = sql_control.sql_control(sql).result
            for i in time:
                time2 = '%s' % (i[0])
                time1 = '%s' % (i[1])
                sql ="update menus2 set M_sum_number='%s' where M_id='%s'" %(time1,time2)
                sql_control.sql_control(sql)

            self.order_status.set("订餐成功!")
        else:
            self.order_status.set("订餐失败!")

    def delete_menus_data(self):

        if not self.tree_view.selection():
            tkinter.messagebox.showerror("未选中")
        for item in self.tree_view.selection():
            self.order.remove(eval(self.tree_view.item(item,'values')[0]))
            self.tree_view.delete(item)

    def group_menus_data(self):
        self.tree_view.grid_forget()
        self.text2.grid_forget()
        self.tree_view3.grid_forget()
        self.text3.grid_forget()
        self.text1.grid(row=0, column=2)
        self.tree_view1.grid(row=1, column=2)

        for _ in map(self.tree_view1.delete, self.tree_view1.get_children("")):
            pass
        if len(self.order_id.get()) != 0:
            sql = "select * from `套餐菜单`where  Men_M_id=%s" % self.order_id.get()
            menus_data = sql_control.sql_control(sql).result
            index = 0
            for dish in menus_data:
                self.tree_view1.insert(parent='', index=index + 1, values=dish)
                index = index + 1
            self.Men = self.order_id.get()
        else:
            self.order_status.set("你好像什么都没填！")

    def end_menus_data(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children("")):
            pass

    def add_menus_data(self):
        self.tree_view3.grid_forget()
        self.text3.grid_forget()
        self.tree_view1.grid_forget()
        self.text1.grid_forget()
        self.text2.grid(row=0, column=2)
        self.tree_view.grid(row=1, column=2)
        if len(self.order_number.get())!=0:
            times=eval(self.order_number.get())
            print(times)
            for i in range(times):
                if len(self.order_id.get()) != 0:
                    if self.flag1 == 1:
                        self.index = 0
                        self.flag1 = 0
                    sql = "select * from menus where  M_id=%s" % self.order_id.get()
                    self.order = self.order + [eval(self.order_id.get())]

                    menus_data = sql_control.sql_control(sql).result

                    for dish in menus_data:
                        self.tree_view.insert(parent='', index=self.index + 1, values=dish)
                        self.index = self.index + 1
                    self.Men = self.order_id.get()
                else:
                    self.order_status.set("你好像什么都没填！")

        else:
            if len(self.order_id.get()) != 0:
                if self.flag1==1:
                    self.index = 0
                    self.flag1=0
                sql = "select * from menus where  M_id=%s" % self.order_id.get()
                self.order=self.order+[eval(self.order_id.get())]

                menus_data = sql_control.sql_control(sql).result

                for dish in menus_data:
                    self.tree_view.insert(parent='', index=self.index + 1, values=dish)
                    self.index = self.index + 1
                self.Men = self.order_id.get()
            else:
                self.order_status.set("你好像什么都没填！")
        self.text2.grid(row=0, column=2)
        self.tree_view.grid(row=1, column=2)

class c_orderframe(tkinter.Frame):
    def __init__(self, root,username):
        super().__init__(root)
        #此处填写变量
        self.status=tkinter.StringVar()
        self.username=username
        self.fr2 = tkinter.Frame(self)
        self.create_page()
    def create_page(self):
        self.fr2.grid(row=2, column=1)
        tkinter.Label(self.fr2, text="订单操作：").grid(row=2, column=1)
        columns = ('O_id', 'O_time', 'C_phone', 'T_name', 'T_status', 'O_delete_status', 'O_commit', 'O_make_status', 'R_name', 'R_phone', 'O_eat_status')
        columns_cn = ('O_id', 'O_time', 'C_phone', 'T_name', 'T_status', 'O_delete_status', 'O_commit', 'O_make_status', 'R_name', 'R_phone', 'O_eat_status')
        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        for i in columns:
            self.tree_view.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=2, column=2, pady=5, padx=5)
        tkinter.Button(self.fr2, text="刷新数据", command=self.show_data_frame, font=parameter.botton_font).grid(row=3, column=1)
        tkinter.Button(self.fr2, text="撤销订单", command=self.delete_order, font=parameter.botton_font).grid(row=4, column=1)
        tkinter.Button(self.fr2, text="已经领取", command=self.over_order, font=parameter.botton_font).grid(row=5, column=1)
        tkinter.Label(self.fr2, textvariable=self.status, font=parameter.label_font).grid(row=6, column=1)
        self.show_data_frame()
    def show_data_frame(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children("")):
            pass
        sql = "select * from `订单3`where C_id=%s"%self.username
        order_data = sql_control.sql_control(sql).result
        index = 0
        for order in order_data:
            self.tree_view.insert(parent='', index=index + 1, values=order)
            index = index + 1

    def over_order(self):
        if not self.tree_view.selection():
            tkinter.messagebox.showerror("未选中")
        for item in self.tree_view.selection():
            print(self.tree_view.item(item, 'values'))
            if self.tree_view.item(item, 'values')[-3]=='运送中' or self.tree_view.item(item, 'values')[-3]=='就餐中':
                sql="update `订单3` set O_eat_status='已完成' where O_id=%s"%eval(self.tree_view.item(item, 'values')[0])
                sql_control.sql_control(sql)
                self.show_data_frame()
                self.status.set("已确认")

            else:
                self.status.set("未运送或已完成")

    def delete_order(self):
        if not self.tree_view.selection():
            tkinter.messagebox.showerror(message="未选中")
        else:
            for item in self.tree_view.selection():
                if self.tree_view.item(item, 'values')[5] == '可撤销':

                    sql = "delete from order_menus where O_id=%s" % self.tree_view.item(item, 'values')[0]
                    sql_control.sql_control(sql)
                    sql = "delete from ordering where O_id=%s" % eval(self.tree_view.item(item, 'values')[0])
                    sql_control.sql_control(sql)
                    sql = "select * from count"
                    sql_control.sql_control(sql)
                    time = sql_control.sql_control(sql).result
                    for i in time:
                        time2 = '%s' % (i[0])
                        time1 = '%s' % (i[1])
                        sql = "update menus2 set M_sum_number='%s' where M_id='%s'" % (time1, time2)
                        sql_control.sql_control(sql)
                    self.show_data_frame()
                    self.status.set("撤销成功")
                else:
                    self.status.set("错误")

class C_mineframe(tkinter.Frame):
    def __init__(self, root, username):
        super().__init__(root)
        self.R_ID = tkinter.StringVar()
        self.R_ID.set(username)
        self.R_password = tkinter.StringVar()
        self.R_name = tkinter.StringVar()
        self.R_sex = tkinter.StringVar()
        self.R_phone = tkinter.StringVar()
        self.R_health_status = tkinter.StringVar()
        self.status= tkinter.StringVar()
        self.value1 = (self.R_ID,self.R_password, self.R_name, self.R_sex, self.R_phone, self.R_health_status)
        self.create_page()
    def create_page(self):
        tkinter.Label(self, text="信息操作").grid(row=0, column=1)
        tkinter.Label(self, text="顾客账号：", font=parameter.label_font).grid(row=1, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_ID,state="readonly" ,font=parameter.enter_font).grid(row=1, column=2)
        tkinter.Label(self, text="顾客密码：", font=parameter.label_font).grid(row=2, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_password, font=parameter.enter_font).grid(row=2, column=2)
        tkinter.Label(self, text="顾客姓名：", font=parameter.label_font).grid(row=3, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_name, font=parameter.enter_font).grid(row=3, column=2)
        tkinter.Label(self, text="顾客性别：", font=parameter.label_font).grid(row=4, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_sex, font=parameter.enter_font).grid(row=4, column=2)
        tkinter.Label(self, text="联系电话：", font=parameter.label_font).grid(row=5, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_phone, font=parameter.enter_font).grid(row=5, column=2)
        tkinter.Label(self, text="顾客地址：", font=parameter.label_font).grid(row=6, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_health_status, font=parameter.enter_font).grid(row=6, column=2)
        tkinter.Button(self, text="更改数据", command=self.insert_data, font=parameter.botton_font).grid(row=7, column=2, sticky=tkinter.E)
        tkinter.Label(self, textvariable=self.status).grid(row=8, column=2)
        self.show_data_frame()#刷新，得到数据
    def show_data_frame(self):
        sql="select * from customer where C_id=%s" % self.R_ID.get()
        date1=sql_control.sql_control(sql).result
        for date in date1:
            for i in range(len(date)):
                self.value1[i].set(date[i])
    def insert_data(self):
        if len(self.R_password.get())!=0 and len(self.R_name.get())!=0 and len(self.R_phone.get())==11 and len(self.R_health_status.get())!=0:
            if len(self.R_sex.get()) != 0:
                self.value = (self.R_password.get(), self.R_name.get(), self.R_sex.get(), self.R_phone.get(), self.R_health_status.get(), self.R_ID.get())
                sql = 'update customer set customer.C_password="%s",customer.C_name="%s",customer.C_sex="%s",customer.C_phone="%s",customer.C_address="%s" where C_id="%s"' % self.value
            else:
                self.value1 = (self.R_password.get(), self.R_name.get(),  self.R_phone.get(), self.R_health_status.get(), self.R_ID.get())
                sql = 'update customer set customer.C_password="%s",customer.C_name="%s",customer.C_sex=null,customer.C_phone="%s",customer.C_address="%s" where C_id="%s"' % self.value1
            sql_control.sql_control(sql)
            self.status.set("更新成功！")
        else:
            self.status.set("更新失败！")
        self.show_data_frame()


#快递取餐的页面
class riderframe(tkinter.Frame):
    def __init__(self, root,username):
        super().__init__(root)
        self.status = tkinter.StringVar()
        self.fr2 = tkinter.Frame(self)
        self.username=username
        #此处填写变量
        self.create_page()
    def create_page(self):
        #此处填写框架并打包（pack\grid\place）
        self.fr2.grid(row=1, column=1,sticky='n')
        tkinter.Label(self.fr2, text="订单操作：", font=parameter.label_font).grid(row=1, column=1)
        tkinter.Button(self.fr2, text="刷新数据", command=self.show_data_frame, font=parameter.botton_font).grid(row=2, column=1)
        tkinter.Button(self.fr2, text="领取订单", command=self.over_order, font=parameter.botton_font).grid(row=3, column=1)
        columns = ('O_id','O_time','C_address','C_name','C_phone','O_commit','O_delete_status','O_make_status','O_eat_status','R_id','R_name')
        columns_cn =  ('O_id','O_time','C_address','C_name','C_phone','O_commit','O_delete_status','O_make_status','O_eat_status','R_id','R_name')
        self.tree_view=ttk.Treeview(self,show="headings",columns=columns)
        for i in columns:
            self.tree_view.column(i, width=80, anchor="center")
        for i in range(len(columns)):
            self.tree_view.heading(columns[i], text=columns_cn[i])
        self.tree_view.grid(row=1,column=2,pady=5,padx=5)
        tkinter.Label(self.fr2, textvariable=self.status, font=parameter.label_font).grid(row=4, column=1)


        self.show_data_frame()#刷新，得到数据
    def show_data_frame(self):

            for _ in map(self.tree_view.delete, self.tree_view.get_children("")):
                pass

            sql = "select * from `快递订单`"
            menus_data = sql_control.sql_control(sql).result

            index = 0
            for dish in menus_data:
                self.tree_view.insert(parent='', index=index + 1, values=dish)

    def over_order(self):
        if not self.tree_view.selection():
            tkinter.messagebox.showerror("未选中")
        for item in self.tree_view.selection():
            if self.tree_view.item(item, 'values')[-5] == '制作完成' and self.tree_view.item(item, 'values')[-4] == '未运送':
                sql="update `快递订单` set O_eat_status='运送中',R_id=%s where O_id=%s"%(self.username,eval(self.tree_view.item(item, 'values')[0]))
                sql_control.sql_control(sql)
                self.show_data_frame()
                self.status.set("领取成功")
            else:
                self.status.set("错误")

class R_mineframe(tkinter.Frame):
    def __init__(self, root, username):
        super().__init__(root)
        self.R_ID = tkinter.StringVar()
        self.R_ID.set(username)
        self.R_password = tkinter.StringVar()
        self.R_name = tkinter.StringVar()
        self.R_sex = tkinter.StringVar()
        self.R_phone = tkinter.StringVar()
        self.R_health_status = tkinter.StringVar()
        self.status= tkinter.StringVar()
        self.value1 = (self.R_ID,self.R_password, self.R_name, self.R_sex, self.R_phone, self.R_health_status)
        self.create_page()
    def create_page(self):
        tkinter.Label(self, text="信息操作").grid(row=0, column=1)
        tkinter.Label(self, text="骑手账号：", font=parameter.label_font).grid(row=1, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_ID,state="readonly" ,font=parameter.enter_font).grid(row=1, column=2)
        tkinter.Label(self, text="骑手密码：", font=parameter.label_font).grid(row=2, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_password, font=parameter.enter_font).grid(row=2, column=2)
        tkinter.Label(self, text="骑手姓名：", font=parameter.label_font).grid(row=3, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_name, font=parameter.enter_font).grid(row=3, column=2)
        tkinter.Label(self, text="骑手性别：", font=parameter.label_font).grid(row=4, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_sex, font=parameter.enter_font).grid(row=4, column=2)
        tkinter.Label(self, text="联系电话：", font=parameter.label_font).grid(row=5, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_phone, font=parameter.enter_font).grid(row=5, column=2)
        tkinter.Label(self, text="健康状况：", font=parameter.label_font).grid(row=6, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_health_status, font=parameter.enter_font).grid(row=6, column=2)
        tkinter.Button(self, text="更改数据", command=self.insert_data, font=parameter.botton_font).grid(row=7, column=2, sticky=tkinter.E)
        tkinter.Label(self, textvariable=self.status).grid(row=8, column=2)
        self.show_data_frame()#刷新，得到数据
    def show_data_frame(self):
        sql="select * from rider where R_id=%s" % self.R_ID.get()
        date1=sql_control.sql_control(sql).result
        for date in date1:
            for i in range(len(date)):
                self.value1[i].set(date[i])
    def insert_data(self):
        if len(self.R_password.get())!=0 and len(self.R_name.get())!=0 and len(self.R_phone.get())==11 and len(self.R_health_status.get())!=0:
            if len(self.R_sex.get()) != 0:
                self.value = (self.R_password.get(), self.R_name.get(), self.R_sex.get(), self.R_phone.get(), self.R_health_status.get(), self.R_ID.get())
                sql = 'update rider set rider.R_password="%s",rider.R_name="%s",rider.R_sex="%s",rider.R_phone="%s",rider.R_health_status="%s" where R_id="%s"' % self.value
            else:
                self.value1 = (self.R_password.get(), self.R_name.get(),  self.R_phone.get(), self.R_health_status.get(), self.R_ID.get())
                sql = 'update rider set rider.R_password="%s",rider.R_name="%s",rider.R_sex=null,rider.R_phone="%s",rider.R_health_status="%s" where R_id="%s"' % self.value1
            sql_control.sql_control(sql)
            self.status.set("更新成功！")
        else:
            self.status.set("更新失败！")
        self.show_data_frame()

class R_register_frame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.R_password = tkinter.StringVar()
        self.R_name = tkinter.StringVar()
        self.R_sex = tkinter.StringVar()
        self.R_phone = tkinter.StringVar()
        self.R_health_status = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.value1 = (self.R_password, self.R_name, self.R_sex, self.R_phone, self.R_health_status)
        self.create_page()

    def create_page(self):
        tkinter.Label(self, text="注册操作").grid(row=0, column=1)
        tkinter.Label(self, text="骑手密码：", font=parameter.label_font).grid(row=2, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_password, font=parameter.enter_font).grid(row=2, column=2)
        tkinter.Label(self, text="骑手姓名：", font=parameter.label_font).grid(row=3, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_name, font=parameter.enter_font).grid(row=3, column=2)
        tkinter.Label(self, text="骑手性别：", font=parameter.label_font).grid(row=4, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_sex, font=parameter.enter_font).grid(row=4, column=2)
        tkinter.Label(self, text="联系电话：", font=parameter.label_font).grid(row=5, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_phone, font=parameter.enter_font).grid(row=5, column=2)
        tkinter.Label(self, text="健康状况：", font=parameter.label_font).grid(row=6, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_health_status, font=parameter.enter_font).grid(row=6, column=2)
        tkinter.Button(self, text="注册", command=self.insert_data, font=parameter.botton_font).grid(row=7, column=2, sticky=tkinter.E)
        tkinter.Label(self, textvariable=self.status).grid(row=8, column=2)

    def insert_data(self):

        if len(self.R_password.get()) != 0 and len(self.R_name.get()) != 0 and len(self.R_phone.get()) == 11 and len(self.R_health_status.get()) != 0:
            if len(self.R_sex.get()) != 0:
                self.value = (self.R_password.get(), self.R_name.get(), self.R_sex.get(), self.R_phone.get(), self.R_health_status.get())
                sql = 'insert into rider(R_password,R_name, R_sex,R_phone, R_health_status) values ("%s","%s","%s","%s","%s")' % self.value
            else:
                self.value1 = (self.R_password.get(), self.R_name.get(), self.R_phone.get(), self.R_health_status.get())
                sql = 'insert into rider(R_password,R_name, R_sex,R_phone, R_health_status) values ("%s","%s",null,"%s","%s")' % self.value1
            date = '%s' % sql_control.sql_control(sql).last_insert_id[0]
            self.status.set("注册成功！")
            tkinter.messagebox.showwarning(title='注意', message='你的账号是%s，\n你的账号是%s。' % (date, self.R_password.get()))
        else:
            self.status.set("注册失败！")

class C_register_frame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.R_password = tkinter.StringVar()
        self.R_name = tkinter.StringVar()
        self.R_sex = tkinter.StringVar()
        self.R_phone = tkinter.StringVar()
        self.R_health_status = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.value1 = (self.R_password, self.R_name, self.R_sex, self.R_phone, self.R_health_status)
        self.create_page()

    def create_page(self):
        tkinter.Label(self, text="注册操作").grid(row=0, column=1)
        tkinter.Label(self, text="顾客密码：", font=parameter.label_font).grid(row=2, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_password, font=parameter.enter_font).grid(row=2, column=2)
        tkinter.Label(self, text="顾客姓名：", font=parameter.label_font).grid(row=3, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_name, font=parameter.enter_font).grid(row=3, column=2)
        tkinter.Label(self, text="顾客性别：", font=parameter.label_font).grid(row=4, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_sex, font=parameter.enter_font).grid(row=4, column=2)
        tkinter.Label(self, text="联系电话：", font=parameter.label_font).grid(row=5, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_phone, font=parameter.enter_font).grid(row=5, column=2)
        tkinter.Label(self, text="顾客地址：", font=parameter.label_font).grid(row=6, column=1, pady=5)
        tkinter.Entry(self, textvariable=self.R_health_status, font=parameter.enter_font).grid(row=6, column=2)

        tkinter.Button(self, text="注册", command=self.insert_data, font=parameter.botton_font).grid(row=7, column=2, sticky=tkinter.E)
        tkinter.Label(self, textvariable=self.status).grid(row=8, column=2)

    def insert_data(self):
        if len(self.R_password.get()) != 0 and len(self.R_name.get()) != 0 and len(self.R_phone.get()) == 11 and len(self.R_health_status.get()) != 0:
            if len(self.R_sex.get()) != 0:
                self.value = (self.R_password.get(), self.R_name.get(), self.R_sex.get(), self.R_phone.get(), self.R_health_status.get())
                sql = 'insert into customer(C_password,C_name, C_sex,C_phone, C_address) values ("%s","%s","%s","%s","%s")' % self.value
            else:
                self.value1 = (self.R_password.get(), self.R_name.get(), self.R_phone.get(), self.R_health_status.get())
                sql = 'insert into customer(C_password,C_name, C_sex,C_phone, C_address) values ("%s","%s",null,"%s","%s")' % self.value1
            date ='%s'%sql_control.sql_control(sql).last_insert_id[0]
            self.status.set("注册成功！")
            tkinter.messagebox.showwarning(title='注意', message='你的账号是%s，\n你的账号是%s。' % (date, self.R_password.get()))
        else:
            self.status.set("注册失败！")





        #此处填写功能
#
# class 名称frame(tkinter.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         #此处填写变量
#         self.create_page()
#     def create_page(self):
#         #此处填写框架并打包（pack\grid\place）
#         self.show_data_frame()#刷新，得到数据
#     def show_data_frame(self):
#         #此处填写功能