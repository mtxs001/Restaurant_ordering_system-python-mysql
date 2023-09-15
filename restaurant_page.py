import tkinter
import tkinter.messagebox
import views



class restaurant_page:
    def __init__(self,master:tkinter.Tk):
        self.root=master
        self.root.title("餐厅订餐系统 饭店版")
        self.root.geometry("600x400")
        self.creat_page()

    def creat_page(self):

        self.about_frame =views.aboutframe(self.root)
        self.menus_frame = views.menusframe(self.root)
        self.order_frame = views.orderframe(self.root)
        self.employee_frame = views.employeeframe(self.root)
        self.table_frame = views.tableframe(self.root)
        self.count_frame = views.countframe(self.root)


        menubar=tkinter.Menu(self.root)
        menubar.add_command(label="查找菜单", command=self.show_menus)
        menubar.add_command(label="查找订单", command=self.show_order)
        menubar.add_command(label="员工信息",command=self.show_employee)
        menubar.add_command(label="餐桌信息", command=self.show_table)
        menubar.add_command(label="统计", command=self.show_count)
        menubar.add_command(label="关于",command=self.show_about)
        self.root["menu"]=menubar


    def show_table(self):
        self.root.geometry("600x280")
        self.table_frame.pack(expand=True)
        self.count_frame.pack_forget()
        self.employee_frame.pack_forget()
        self.order_frame.pack_forget()
        self.about_frame.pack_forget()
        self.menus_frame.pack_forget()


    def show_count(self):
        self.root.geometry("650x600")
        self.table_frame.pack_forget()
        self.count_frame.pack(expand=True)
        self.employee_frame.pack_forget()
        self.order_frame.pack_forget()
        self.about_frame.pack_forget()
        self.menus_frame.pack_forget()

    def show_employee(self):
        self.root.geometry("850x300")
        self.table_frame.pack_forget()
        self.employee_frame.pack(expand=True)
        self.order_frame.pack_forget()
        self.about_frame.pack_forget()
        self.menus_frame.pack_forget()
        self.count_frame.pack_forget()

    def show_order(self):
        self.root.geometry("1100x500")
        self.table_frame.pack_forget()
        self.employee_frame.pack_forget()
        self.order_frame.pack(anchor='nw')
        self.about_frame.pack_forget()
        self.menus_frame.pack_forget()
        self.count_frame.pack_forget()


    def show_about(self):
        self.root.geometry("500x300")
        self.table_frame.pack_forget()

        self.employee_frame.pack_forget()
        self.order_frame.pack_forget()
        self.about_frame.pack()
        self.menus_frame.pack_forget()
        self.count_frame.pack_forget()



    def show_menus(self):
        self.root.geometry("1100x500")
        self.table_frame.pack_forget()
        self.employee_frame.pack_forget()
        self.order_frame.pack_forget()
        self.about_frame.pack_forget()
        self.menus_frame.pack(expand=True)
        self.count_frame.pack_forget()

