from tkinter import *

class AccountsSettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background='#F3F3F3'

        self.run()

    def run(self):
        sys_category = AccountsCategory(self)
        self.test_frame()

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background=self.background)
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)


class AccountsCategory(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


        self.run()

    def run(self):
        self.category_title()
        self.second_frame()
        self.desktop_picture()
        self.rewards()
        self.one_drive()
        self.categories()

    def category_title(self):
        label = Label(self.parent, text='Accounts', font=('Segoe Ui',19,'bold'),anchor='w',bg=self.parent.background)
        label.grid(row=1, column=2, columnspan=2, sticky='new')

    def second_frame(self):
        self.content_frame = Frame(self.parent, background=self.parent.background)
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')
        for i in range(14):
            self.content_frame.rowconfigure(i, minsize=64)
            self.content_frame.columnconfigure(i, minsize=64)

    def desktop_picture(self):
        path = 'Desktop/Images'
        desk_img = PhotoImage(file=f'{path}/default-avatar.png')
        desktop_pic_frame = Frame(self.content_frame, background=self.parent.background)
        desktop_pic_frame.grid(row=0, column=0, columnspan=5,rowspan=2,sticky='nsew',pady=(0,15))
        for i in range(8):
            desktop_pic_frame.grid_columnconfigure(i,minsize=10)
        pic = Label(desktop_pic_frame, image=desk_img, background=self.parent.background)
        pic.grid(row=0, column=0,rowspan=5,columnspan=2)
        pic.image = desk_img

        user_label = Label(desktop_pic_frame,
                           text='Default User', font=('Segoe Ui',16),
                           anchor='w',
                           background=self.parent.background)
        user_label.grid(row=1, column=3,sticky='w',columnspan=5)

        pc_name = Label(desktop_pic_frame, text='account_email@gmail.com', font=('Segoe Ui',11),
                        anchor='sw',
                        background=self.parent.background)
        pc_name.grid(row=2, column=3,columnspan=5,sticky='nw')

        rename_label = Label(desktop_pic_frame, text='Administrator', font=('Segoe Ui',11),
                             anchor='nw',
                             background=self.parent.background)
        rename_label.grid(row=3, column=3,sticky='nw',columnspan=5)

    def rewards(self):
        path = 'Desktop/Images/middle_frame/Accounts'
        desk_img = PhotoImage(file=f'{path}/rewards.png')
        desk_img = desk_img.subsample(x=2, y=2)
        desktop_pic_frame = Frame(self.content_frame, background=self.parent.background)
        desktop_pic_frame.grid(row=0, column=6, columnspan=2, sticky='w')

        pic = Label(desktop_pic_frame, image=desk_img, background=self.parent.background)
        pic.grid(row=0, column=0, rowspan=2,sticky='nsew')
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='Rewards', font=('Segoe Ui',10,'bold'),
                           anchor='w',
                           background=self.parent.background)
        user_label.grid(row=0, column=1, sticky='nsew',padx=10)

        pc_name = Label(desktop_pic_frame, text='3 points', font=('Segoe Ui',9),
                        anchor='w',
                        background=self.parent.background)
        pc_name.grid(row=1, column=1, sticky='nwes',padx=10)

        desktop_pic_frame.bind("<Enter>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_enter0(e, frame, image_label, text_label,
                                                                                    text_label2))
        desktop_pic_frame.bind("<Leave>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_leave0(e, frame, image_label, text_label,
                                                                                    text_label2))

    def one_drive(self):
        path = 'Desktop/Images/middle_frame/Accounts'
        desk_img = PhotoImage(file=f'{path}/drive.png')
        desk_img = desk_img.subsample(x=2, y=2)
        desktop_pic_frame = Frame(self.content_frame, background=self.parent.background)
        desktop_pic_frame.grid(row=0, column=8, columnspan=3, sticky='w', padx=(20, 0))

        pic = Label(desktop_pic_frame, image=desk_img, background=self.parent.background)
        pic.grid(row=0, column=0, rowspan=2,sticky='nsew')
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='OneDrive', font=('Segoe Ui',10,'bold'),
                           anchor='w',
                           background=self.parent.background)
        user_label.grid(row=0, column=1,sticky='nsew',padx=10)

        pc_name = Label(desktop_pic_frame, text='Manage files', font=('Segoe Ui',9),
                        anchor='w',
                        background=self.parent.background)
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
        path = 'Desktop/Images'
        content = {f'{path}/middle_frame/microsoft.png': 'Microsoft 365 Family',
                   f'{path}/middle_frame/Accounts/xbox.png': 'PC Game Pass',
                   f'{path}/middle_frame/Accounts/info.png': 'Your info',}
        text_containt = ['Premium Office apps, OneDrive cloud storage, and more',
                         'Over 100 high-quality PC games, EA Play, and discounts on select games and add-ons',
                         'Profile photo']
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame, background='white')
            if index == 0:
                frame.grid(row=index + 2, columnspan=11, sticky='nsew', pady=(0, 5))
            elif index == 1:
                frame.grid(row=index + 5, columnspan=11, sticky='nsew', pady=(5, 5))

                account_settings = Label(self.content_frame,text='Account settings',bg=self.parent.background,
                                         font=('Segoe Ui',11))
                account_settings.grid(row=index + 6,columnspan=3,sticky='nw')
            elif index == 2:
                frame.grid(row=index + 5, columnspan=11, sticky='nsew', pady=(25, 5))
            else:
                frame.grid(row=index + 6, columnspan=11, sticky='nsew')
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

            text_label2 = Label(frame, text=text_containt[index], anchor='w', font=('Segoe Ui',10),bg='white')
            text_label2.grid(row=1, column=1, sticky='nwe', padx=10, columnspan=17)
            self.category_content.append(text_label2)

            img_next = PhotoImage(file=f'{path}/middle_frame/next.png')
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
        self.frame2_init()
        self.frame2_office()

    def frame2_init(self):
        self.frame2 = Frame(self.content_frame, bg='white')
        self.frame2.grid(row=3, column=0, sticky='news', rowspan=3,columnspan=11)

        for i in range(3):
            self.frame2.rowconfigure(i, minsize=32)
        for i in range(13):
            self.frame2.columnconfigure(i,minsize=32)

        title_label = Label(self.frame2, text='Try Microsoft 365 for free',bg='white', font=('Segoe Ui',10,'bold'))
        title_label.grid(row=0, column=0, columnspan=3, sticky='w',padx=(10,0))  # Adjust columnspan as needed

        description_label = Label(
            self.frame2,
            text='One convenient subscription to share with up to five other \n'
                 'Includes premium Office apps and up to 6 TB of cloud \n'
                 'storage (1 TB per person).', font=('Segoe Ui',10),

            anchor='w',justify='left',bg='white'
        )
        description_label.grid(row=1, column=0, columnspan=6, sticky='w',padx=(10,0))

        try_label = Label(self.frame2,text='Try for free',bg='blue',fg='white', font=('Segoe Ui',10),height=2,width=12)
        try_label.grid(row=2,column=0,padx=(10,0),columnspan=2,sticky='w')

        learn_more = Label(self.frame2,text='Learn more',fg='blue', font=('Segoe Ui',10),height=2,width=12,bg='white')
        learn_more.grid(row=2,column=2,columnspan=2,sticky='w')

    def frame2_office(self):
        path = 'Desktop/Images/middle_frame/Accounts'
        content = [f'{path}/01.png',
                   f'{path}/02.png',
                   f'{path}/03.png',
                   f'{path}/04.png',
                   f'{path}/05.png',
                   f'{path}/06.png']
        for index,content in enumerate(content):
            label_img = PhotoImage(file=content)

            if index< 3:
                label = Label(self.frame2,image=label_img,bg='white')
                label.image = label_img
                label.grid(row = 1,column=index+8,pady=(0,30),padx=(10,0))
            else:
                label = Label(self.frame2,image=label_img,bg='white')
                label.image = label_img
                label.grid(row = 2,column=index+5,pady=(0,30),padx=(10,0))

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
