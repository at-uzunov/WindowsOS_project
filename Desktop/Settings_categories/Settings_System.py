from tkinter import *


class SystemSettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background='#F3F3F3'

        self.run()

    def run(self):
        self.test_frame()
        sys_category = SystemCategory(self)

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background=self.background)
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)


class SystemCategory(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.run()

    def run(self):
        self.category_title()
        self.second_frame()
        self.desktop_picture()
        self.microsoft365()
        self.windows_update()
        self.categories()

    def category_title(self):
        label = Label(self.parent, text='System',
                      font=('Segoe Ui',19,'bold'),
                      anchor='w',
                      bg=self.parent.background)
        label.grid(row=1, column=2, columnspan=2, sticky='new')

    def second_frame(self):
        self.content_frame = Frame(self.parent, background=self.parent.background)
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')
        for i in range(14):
            self.content_frame.rowconfigure(i, minsize=64)
            self.content_frame.columnconfigure(i, minsize=64)


    def desktop_picture(self):
        desk_img = PhotoImage(file='Desktop/Images/background.png')
        desk_img = desk_img.subsample(x=13, y=13)
        desktop_pic_frame = Frame(self.content_frame, highlightbackground='black', highlightthickness=3)
        desktop_pic_frame.grid(row=0, column=0, columnspan=2)

        pic = Label(desktop_pic_frame, image=desk_img)
        pic.grid(row=0, column=0)
        pic.image = desk_img

        text_frame = Frame(self.content_frame, background=self.parent.background)
        text_frame.grid_propagate(False)
        text_frame.grid(row=0, column=2, columnspan=2, sticky='news')

        user_label = Label(text_frame, text='User', font=('Segoe Ui',14,'bold'), anchor='w', width=6,
                           bg=self.parent.background)
        user_label.grid(row=0, column=0, pady=(5, 0),padx=10, columnspan=10,sticky='w')

        pc_name = Label(text_frame, text='Python 3.10', font=('Segoe Ui',10), anchor='nw', width=10,
                        bg=self.parent.background)
        pc_name.grid(row=1, column=0, padx=10,columnspan=10,sticky='nw')

        rename_label = Label(text_frame, text='Rename', font=('Segoe Ui',10), anchor='nw', width=10,
                             bg=self.parent.background,fg='blue')
        rename_label.grid(row=2, column=0, columnspan=10,padx=10,sticky='nw')

    def microsoft365(self):
        desk_img = PhotoImage(file='Desktop/Images/middle_frame/microsoft.png')
        desk_img = desk_img.subsample(x=2, y=2)
        desktop_pic_frame = Frame(self.content_frame, background=self.parent.background)
        desktop_pic_frame.grid(row=0, column=5, columnspan=2, sticky='w')

        pic = Label(desktop_pic_frame, image=desk_img,bg=self.parent.background)
        pic.grid(row=0, column=0, rowspan=3,sticky='nsew')
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='Microsoft 365', font=('Segoe Ui',10,'bold'), anchor='w',
                           bg=self.parent.background)
        user_label.grid(row=0, column=1, sticky='nsew',padx=10)

        pc_name = Label(desktop_pic_frame, text='View benefits', font=('Segoe Ui',9), anchor='w',
                        bg=self.parent.background)
        pc_name.grid(row=1, column=1, sticky='nwes',padx=10)

        desktop_pic_frame.bind("<Enter>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_enter0(e, frame, image_label, text_label,
                                                                                    text_label2))
        desktop_pic_frame.bind("<Leave>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_leave0(e, frame, image_label, text_label,
                                                                                    text_label2))

    def windows_update(self):
        desk_img = PhotoImage(file='Desktop/Images/left_frame/update.png')
        desk_img = desk_img.subsample(x=2,y=2)
        desktop_pic_frame = Frame(self.content_frame, background=self.parent.background)
        desktop_pic_frame.grid(row=0, column=7, columnspan=4, sticky='w', padx=(20, 0))

        pic = Label(desktop_pic_frame, image=desk_img,bg=self.parent.background)
        pic.grid(row=0, column=0, rowspan=2,sticky='nsew')
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='Windows Update', font=('Segoe Ui',10,'bold'), anchor='w',
                           bg=self.parent.background)
        user_label.grid(row=0, column=1, sticky='nsew',padx=10)

        pc_name = Label(desktop_pic_frame, text='Last checked: 9 hours ago', font=('Segoe Ui',9), anchor='w',
                        bg=self.parent.background)
        pc_name.grid(row=1, column=1, sticky='nwes',padx=10,columnspan=4)

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
        path = 'Desktop/Images/middle_frame'
        content = {f'{path}/laptop.png': 'Display',
                   f'{path}/sound.png': 'Sound',
                   f'{path}/notifications.png': 'Notifications',
                   f'{path}/focus.png': 'Focus',
                   f'{path}/power.png': 'Power',
                   f'{path}/storage.png': 'Storage',
                   f'{path}/share.png': 'Nearby sharing',
                   f'{path}/multitask.png': 'Multitasking',
                   }
        text_containt = ['Monitors, brightness, night light, display profile', 'Volume levels, output, sound devices',
                         'Alerts from apps and system, do not disturb', 'Reduce distractions',
                         'Screen and sleep, power mode',
                         'Storage space, drivers, configure rules', 'Discoverability, received files location',
                         'Snap windows, desktops, task switching']
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame, bg='white')
            frame.grid(row=index + 2, columnspan=11, sticky='nsew', pady=(0, 7))
            for i in range(2):
                frame.grid_rowconfigure(i, minsize=40)
            for i in range(17):
                frame.grid_columnconfigure(i, minsize=40)
            self.category_content.append(frame)

            image_label = Label(frame, image=img,bg='white')
            image_label.grid(row=0, column=0, rowspan=2,padx=(10,0))
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
            next_img.grid(row=0,rowspan=2,column=18,sticky='news',padx=(10,0))
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


