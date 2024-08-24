from tkinter import *

class SystemSettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background='#F3F3F3'

        self.run()

    def run(self):
        sys_category = SystemCategory(self)
        self.test_frame()

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background='blue')
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)

        for i in range(25):
            label1 = Label(self, text='', highlightbackground='black', highlightthickness=1)
            label1.grid(row=0, column=i, sticky='nsew')
            label2 = Label(self, text='', highlightbackground='black', highlightthickness=1)
            label2.grid(row=i, column=0, sticky='nsew')


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
        label = Label(self.parent, text='System', font=('Segoe Ui',19,'bold'),anchor='w')
        label.grid(row=1, column=2, columnspan=2, sticky='nsew')

    def second_frame(self):
        self.content_frame = Frame(self.parent, background='white')
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')
        for i in range(14):
            self.content_frame.rowconfigure(i, minsize=64)
            self.content_frame.columnconfigure(i, minsize=64)

            label = Label(self.content_frame, text='', highlightbackground='black', highlightthickness=1,
                          bg='darkorange')
            label.grid(row=i, column=12, sticky='nwes')

            label2 = Label(self.content_frame, text='', highlightbackground='black', highlightthickness=1,
                           bg='darkorange')
            label2.grid(row=8, column=i, sticky='nwes')

    def desktop_picture(self):
        desk_img = PhotoImage(file='../Images/background.png')
        desk_img = desk_img.subsample(x=13, y=13)
        desktop_pic_frame = Frame(self.content_frame, highlightbackground='black', highlightthickness=3)
        desktop_pic_frame.grid(row=0, column=0, columnspan=2)

        pic = Label(desktop_pic_frame, image=desk_img)
        pic.grid(row=0, column=0)
        pic.image = desk_img

        text_frame = Frame(self.content_frame, background='red')
        text_frame.grid_propagate(False)
        text_frame.grid(row=0, column=2, columnspan=2, sticky='news')

        user_label = Label(text_frame, text='User', font=('Segoe Ui',14,'bold'), anchor='w', width=6)
        user_label.grid(row=0, column=0, pady=(5, 0), columnspan=10,sticky='w')

        pc_name = Label(text_frame, text='Python10', font=('Segoe Ui',10), anchor='w', width=10)
        pc_name.grid(row=1, column=0, pady=(5, 0), columnspan=10)

        rename_label = Label(text_frame, text='Rename', font=('Segoe Ui',10), anchor='w', width=10)
        rename_label.grid(row=2, column=0, columnspan=10)

    def microsoft365(self):
        desk_img = PhotoImage(file='../Images/middle_frame/microsoft.png')
        desk_img = desk_img.subsample(x=2, y=2)
        desktop_pic_frame = Frame(self.content_frame, background='red')
        desktop_pic_frame.grid(row=0, column=6, columnspan=2, sticky='w')

        pic = Label(desktop_pic_frame, image=desk_img)
        pic.grid(row=0, column=0, rowspan=2,sticky='nsew')
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='Microsoft 365', font=('Segoe Ui',11,'bold'), anchor='w')
        user_label.grid(row=0, column=1, sticky='nsew')

        pc_name = Label(desktop_pic_frame, text='view benefits', font=('Segoe Ui',10), anchor='w')
        pc_name.grid(row=1, column=1, sticky='nwes')

        desktop_pic_frame.bind("<Enter>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_enter(e, frame, image_label, text_label,
                                                                                    text_label2))
        desktop_pic_frame.bind("<Leave>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_leave(e, frame, image_label, text_label,
                                                                                    text_label2))

    def windows_update(self):
        desk_img = PhotoImage(file='../Images/left_frame/update.png')
        desk_img = desk_img.subsample(x=11, y=11)
        desktop_pic_frame = Frame(self.content_frame, background='red')
        desktop_pic_frame.grid(row=0, column=8, columnspan=3, sticky='w', padx=(20, 0))

        pic = Label(desktop_pic_frame, image=desk_img)
        pic.grid(row=0, column=0, rowspan=2,sticky='nsew')
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='Windows Update', font=('Segoe Ui',11,'bold'), anchor='w')
        user_label.grid(row=0, column=1,sticky='nsew')

        pc_name = Label(desktop_pic_frame, text='Last checked: 9 hours ago', font=('Segoe Ui',8), anchor='w')
        pc_name.grid(row=1, column=1, sticky='nwes')

        desktop_pic_frame.bind("<Enter>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_enter(e, frame, image_label, text_label,
                                                                                    text_label2))
        desktop_pic_frame.bind("<Leave>", lambda e, frame=desktop_pic_frame,
                                                 image_label=pic, text_label=user_label,
                                                 text_label2=pc_name: self.on_leave(e, frame, image_label, text_label,
                                                                                    text_label2))

    def categories(self):
        self.category_content = []
        content = {'Images/middle_frame/laptop.png': 'Display', 'Images/middle_frame/sound.png': 'Sound',
                   'Images/middle_frame/notifications.png': 'Notifications', 'Images/middle_frame/focus.png': 'Focus',
                   'Images/middle_frame/power.png': 'Power', 'Images/middle_frame/storage.png': 'Storage',
                   'Images/middle_frame/share.png': 'Nearby sharing',
                   'Images/middle_frame/multitask.png': 'Multitasking',
                   }
        text_containt = ['Monitors, brightness, night light, display profile', 'Volume levels, output, sound devices',
                         'Alerts from apps and system, do not disturb', 'Reduce distractions',
                         'Screen and sleep, power mode',
                         'Storage space, drivers, configure rules', 'Discoverability, received files location',
                         'Snap windows, desktops, task switching']
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame, bg='red')
            frame.grid(row=index + 2, columnspan=11, sticky='nsew', pady=(0, 5))
            for i in range(2):
                frame.grid_rowconfigure(i, minsize=40)
            for i in range(17):
                frame.grid_columnconfigure(i, minsize=40)
            self.category_content.append(frame)

            image_label = Label(frame, image=img)
            image_label.grid(row=0, column=0, rowspan=2)
            image_label.image = img
            self.category_content.append(image_label)

            text_label = Label(frame, text=content[text], anchor='w', font=('Segoe Ui',11))
            text_label.grid(row=0, column=1, sticky='swe', padx=10, columnspan=17)
            self.category_content.append(text_label)

            text_label2 = Label(frame, text=text_containt[index], anchor='w', font=('Segoe Ui',9))
            text_label2.grid(row=1, column=1, sticky='nwe', padx=10, columnspan=17)
            self.category_content.append(text_label2)

            img_next = PhotoImage(file='../Images/middle_frame/next.png')
            img_next = img_next.subsample(x=2,y=2)
            next_img = Label(frame,image=img_next)
            next_img.grid(row=0,rowspan=2,column=18,sticky='news')
            next_img.image = img_next



            frame.bind("<Enter>", lambda e, frame=frame, image_label=image_label, text_label=text_label,
                                         text_label2=text_label2,next_img = next_img: self.on_enter(e, frame, image_label, text_label,
                                                                                text_label2,next_img))
            frame.bind("<Leave>", lambda e, frame=frame, image_label=image_label, text_label=text_label,
                                         text_label2=text_label2,next_img=next_img: self.on_leave(e, frame, image_label, text_label,
                                                                                text_label2,next_img))

    def on_enter(self, event, *args):
        for i in args:
            i.configure(bg='blue')

    def on_leave(self, event, *args):
        for i in args:
            i.configure(bg='white')
