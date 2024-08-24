from tkinter import *

class NetworkSettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background='#F3F3F3'
        self.run()

    def run(self):
        sys_category = NetworkCategory(self)
        self.test_frame()

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background=self.background)
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)


class NetworkCategory(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.run()

    def run(self):
        self.category_title()
        self.second_frame()
        self.desktop_picture()
        self.properties()
        self.data_usage()
        self.categories()

    def category_title(self):
        label = Label(self.parent, text='Network & internet', font=('Segoe Ui',19,'bold'),anchor='w',bg=self.parent.background)
        label.grid(row=1, column=2, columnspan=4, sticky='new')

    def second_frame(self):
        self.content_frame = Frame(self.parent,bg=self.parent.background)
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')
        for i in range(14):
            self.content_frame.rowconfigure(i, minsize=64)
            self.content_frame.columnconfigure(i, minsize=64)

    def desktop_picture(self):
        desk_img = PhotoImage(file='Desktop/Images/middle_frame/Network/Ethernet0.png')
        desktop_pic_frame = Frame(self.content_frame,bg=self.parent.background)
        desktop_pic_frame.grid(row=0, column=0, columnspan=2,rowspan=2,sticky='n')

        pic = Label(desktop_pic_frame, image=desk_img,bg=self.parent.background)
        pic.grid(row=0, column=0)
        pic.image = desk_img

        text_frame = Frame(self.content_frame,bg=self.parent.background)
        text_frame.grid_propagate(False)
        text_frame.grid(row=0, column=2, columnspan=2, sticky='news',pady=(10,0))

        user_label = Label(text_frame, text='Ethernet0', font=('Segoe Ui',14,'bold'), anchor='w', width=10,bg=self.parent.background)
        user_label.grid(row=1, column=0, columnspan=10,sticky='w',rowspan=5)

        pc_name = Label(text_frame, text='Connected', font=('Segoe Ui',10), anchor='w', width=10,bg=self.parent.background)
        pc_name.grid(row=6, column=0, columnspan=10,sticky='w')



    def properties(self):
        desk_img = PhotoImage(file='Desktop/Images/middle_frame/Network/info.png')
        desk_img = desk_img.subsample(x=2,y=2)
        desktop_pic_frame = Frame(self.content_frame,bg=self.parent.background)
        desktop_pic_frame.grid(row=0, column=6, columnspan=2, sticky='w')

        pic = Label(desktop_pic_frame, image=desk_img, bg=self.parent.background)
        pic.grid(row=0, column=0, rowspan=2,sticky='nsew')
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='Properties', font=('Segoe Ui',10,'bold'), anchor='w',bg=self.parent.background)
        user_label.grid(row=0, column=1, sticky='nsew',padx=10)

        pc_name = Label(desktop_pic_frame, text='Public network', font=('Segoe Ui',9), anchor='w',bg=self.parent.background)
        pc_name.grid(row=1, column=1, sticky='nwes',padx=10)

        desktop_pic_frame.bind("<Enter>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_enter0(e, frame, image_label, text_label,
                                                                                    text_label2))
        desktop_pic_frame.bind("<Leave>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_leave0(e, frame, image_label, text_label,
                                                                                    text_label2))

    def data_usage(self):
        desk_img = PhotoImage(file='Desktop/Images/middle_frame/Network/data.png')
        desk_img = desk_img.subsample(x=2,y=2)
        desktop_pic_frame = Frame(self.content_frame,bg=self.parent.background)
        desktop_pic_frame.grid(row=0, column=8, columnspan=3, sticky='w', padx=(20, 0))

        pic = Label(desktop_pic_frame, image=desk_img,bg=self.parent.background)
        pic.grid(row=0, column=0, rowspan=2,sticky='nsew')
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='Data usage', font=('Segoe Ui',10,'bold'), anchor='w',bg=self.parent.background)
        user_label.grid(row=0, column=1,sticky='nsew',padx=10)

        pc_name = Label(desktop_pic_frame, text='520 MB, last 30 days', font=('Segoe Ui',9), anchor='w',bg=self.parent.background)
        pc_name.grid(row=1, column=1, sticky='nwes',padx=10)

        desktop_pic_frame.bind("<Enter>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_enter0(e, frame, image_label, text_label,
                                                                                     text_label2))
        desktop_pic_frame.bind("<Leave>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_leave0(e, frame, image_label, text_label,
                                                                                     text_label2))

    def categories(self):
        self.category_content = []
        path = 'Desktop/Images/middle_frame/Network'
        content = {f'{path}/ethernet.png': 'Ethernet', f'{path}/vpn.png': 'VPN',
                   f'{path}/proxy.png': 'Proxy', f'{path}/dial.png': 'Dial-up',
                   f'{path}/advanced.png': 'Advanced network settings',
                   }
        text_containt = ['Authentication, IP and DNS settings, metered network', 'Add, connect, manage',
                         'Proxy server for Wi-Fi and Ethernet connections',
                         'Set up a dial-up internet connection',
                         'View all network adapters, network reset']
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame,bg='white')
            frame.grid(row=index + 2, columnspan=11, sticky='nsew', pady=(0, 5))
            for i in range(2):
                frame.grid_rowconfigure(i, minsize=40)
            for i in range(17):
                frame.grid_columnconfigure(i, minsize=40)
            self.category_content.append(frame)

            image_label = Label(frame, image=img,bg='white')
            image_label.grid(row=0, column=0, rowspan=2)
            image_label.image = img
            self.category_content.append(image_label)

            text_label = Label(frame, text=content[text], anchor='w', font=('Segoe Ui',11),bg='white')
            text_label.grid(row=0, column=1, sticky='swe', padx=10, columnspan=17)
            self.category_content.append(text_label)

            text_label2 = Label(frame, text=text_containt[index], anchor='w', font=('Segoe Ui',9),bg='white')
            text_label2.grid(row=1, column=1, sticky='nwe', padx=10, columnspan=17)
            self.category_content.append(text_label2)

            img_next = PhotoImage(file='Desktop/Images/middle_frame/next.png')
            img_next = img_next.subsample(x=2,y=2)
            next_img = Label(frame,image=img_next,bg='white')
            next_img.grid(row=0,rowspan=2,column=18,sticky='news',padx=(5,20))
            next_img.image = img_next



            frame.bind("<Enter>", lambda e, frame=frame, image_label=image_label, text_label=text_label,
                                         text_label2=text_label2,next_img = next_img: self.on_enter(e, frame, image_label, text_label,
                                                                                text_label2,next_img))
            frame.bind("<Leave>", lambda e, frame=frame, image_label=image_label, text_label=text_label,
                                         text_label2=text_label2,next_img=next_img: self.on_leave(e, frame, image_label, text_label,
                                                                                text_label2,next_img))

    def on_enter0(self, event, *args):
        for i in args:
            i.configure(bg='#E3E3E3')

    def on_leave0(self, event, *args):
        for i in args:
            i.configure(bg=self.parent.background)

    def on_enter(self, event, *args):
        for i in args:
            i.configure(bg='#E3E3E3')

    def on_leave(self, event, *args):
        for i in args:
            i.configure(bg='white')
