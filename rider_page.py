import tkinter
import tkinter.messagebox
import views



class rider_page:
    def __init__(self,master:tkinter.Tk,username):
        self.root=master
        self.root.title("餐厅订餐系统 骑手版")
        self.root.geometry("600x400")
        self.creat_page(username)

    def creat_page(self,username):

        self.about_frame =views.aboutframe(self.root)
        self.rider_frame = views.riderframe(self.root,username)
        self.mine_frame = views.R_mineframe(self.root, username)

        menubar=tkinter.Menu(self.root)
        menubar.add_command(label="领取订单", command=self.show_rider)
        menubar.add_command(label="我的资料", command=self.show_mine)
        menubar.add_command(label="关于",command=self.show_about)
        self.root["menu"]=menubar

    def show_about(self):
        self.root.geometry("500x300")
        self.about_frame.pack()
        self.rider_frame.pack_forget()
        self.mine_frame.pack_forget()

    def show_rider(self):
        self.root.geometry("1000x250")
        self.about_frame.pack_forget()
        self.rider_frame.pack(expand=True)
        self.mine_frame.pack_forget()

    def show_mine(self):
        self.root.geometry("300x300")
        self.mine_frame.pack(expand=True)
        self.about_frame.pack_forget()
        self.rider_frame.pack_forget()
