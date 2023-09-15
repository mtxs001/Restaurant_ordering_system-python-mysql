import tkinter
import tkinter.messagebox
import views



class customer_page:
    def __init__(self,master:tkinter.Tk,username):
        self.root=master
        self.root.title("餐厅订餐系统 顾客版")
        self.root.geometry("600x400")
        self.creat_page(username)

    def creat_page(self,username):

        self.about_frame =views.aboutframe(self.root)
        self.c_order_frame = views.c_orderframe(self.root,username)
        self.c_menus_frame = views.c_menusframe(self.root,username)
        self.mine_frame = views.C_mineframe(self.root, username)

        menubar=tkinter.Menu(self.root)
        menubar.add_command(label="点餐", command=self.show_c_menus)
        menubar.add_command(label="我的订单", command=self.show_c_order)
        menubar.add_command(label="我的资料", command=self.show_mine)
        menubar.add_command(label="关于",command=self.show_about)
        self.root["menu"]=menubar

    def show_about(self):
        self.root.geometry("500x300")
        self.c_menus_frame.pack_forget()
        self.about_frame.pack()
        self.c_order_frame.pack_forget()
        self.mine_frame.pack_forget()

    def show_c_menus(self):
        self.root.geometry("1150x600")
        self.about_frame.pack_forget()
        self.c_menus_frame.pack(expand=True)
        self.c_order_frame.pack_forget()
        self.mine_frame.pack_forget()

    def show_c_order(self):
        self.root.geometry("1000x250")
        self.about_frame.pack_forget()
        self.c_menus_frame.pack_forget()
        self.c_order_frame.pack(expand=True)
        self.mine_frame.pack_forget()

    def show_mine(self):
        self.root.geometry("300x300")
        self.about_frame.pack_forget()
        self.c_menus_frame.pack_forget()
        self.c_order_frame.pack_forget()
        self.mine_frame.pack(expand=True)
