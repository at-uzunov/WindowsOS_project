from tkinter import *


class WinUpdateSettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background = '#F3F3F3'

        self.run()

    def run(self):
        sys_category = WinUpdateCategory(self)
        self.test_frame()

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background=self.background)
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)


class WinUpdateCategory(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.run()

    def run(self):
        self.category_title()
        self.second_frame()
        self.desktop_picture()
        self.categories()

    def category_title(self):
        label = Label(self.parent, text='Windows Update', font=('Segoe Ui', 22, 'bold'), anchor='w',
                      bg=self.parent.background)
        label.grid(row=1, column=2, columnspan=4, sticky='nsew')

    def second_frame(self):
        self.content_frame = Frame(self.parent, bg=self.parent.background)
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')
        for i in range(14):
            self.content_frame.rowconfigure(i, minsize=64)
            self.content_frame.columnconfigure(i, minsize=64)

    def desktop_picture(self):
        desk_img = PhotoImage(file='Desktop/Images/middle_frame/WinUpdate/update.png')
        desktop_pic_frame = Frame(self.content_frame, bg=self.parent.background)
        desktop_pic_frame.grid(row=0, column=0, columnspan=2)

        pic = Label(desktop_pic_frame, image=desk_img, bg=self.parent.background)
        pic.grid(row=0, column=0)
        pic.image = desk_img

        text_frame = Frame(self.content_frame, background=self.parent.background)
        text_frame.grid_propagate(False)
        text_frame.grid(row=0, column=2, columnspan=4, sticky='nsew')

        user_label = Label(text_frame, text="You're up to date", font=('Segoe Ui', 14, 'bold'), anchor='w',
                           bg=self.parent.background)
        user_label.grid(row=0, column=0, pady=(20, 0), columnspan=10, sticky='w')

        pc_name = Label(text_frame, text='Last checked: Today, 12:35 PM', font=('Segoe Ui', 10), anchor='w',
                        bg=self.parent.background)
        pc_name.grid(row=1, column=0, pady=(5, 0), columnspan=10)

        check_for_update = Label(self.content_frame, text=' Check for update ', bg='blue', fg='white', height=2,
                                 font=('Segoe Ui', 10, 'bold'))
        check_for_update.grid(row=0, column=9, rowspan=2, sticky='ew', columnspan=2)

        preview_update = Frame(self.content_frame, bg='#F4F4F4', highlightbackground='black', highlightthickness=1)
        preview_update.grid(row=1, columnspan=11, sticky='nsew', pady=(20, 5), rowspan=2)
        for i in range(2):
            preview_update.grid_rowconfigure(i, minsize=40)

        picture = PhotoImage(file='Desktop/Images/middle_frame/WinUpdate/info.png')
        picture = picture.subsample(x=2, y=2)
        picture_label = Label(preview_update, image=picture, bg='#F4F4F4')
        picture_label.image = picture
        picture_label.grid(row=0, column=0, padx=10)
        preview_update_info = Label(preview_update, text='2023-09 Cumulative Update Preview for Windows 11 version 22'
                                                         'H2 is available.',
                                    font=('Segoe Ui', 10, 'bold'), bg='#F4F4F4')
        preview_update_info.grid(row=0, column=1, columnspan=10, sticky='w', padx=(10, 0))

        download_label = Label(preview_update, text=' Download & install ', height=2, width=20, font=('Segoe Ui', 10),
                               bg='gray92')
        download_label.grid(row=1, column=1, columnspan=10, sticky='w', padx=(10, 0), pady=(10))

        more_options = Label(self.content_frame, text='More options', font=("Segoe Ui", 10, 'bold'), anchor='w',
                             bg='#F4F4F4')
        more_options.grid(row=3, column=0, sticky='sew', columnspan=2, pady=(10))

    def categories(self):
        self.category_content = []
        path = 'Desktop/Images/middle_frame/WinUpdate'
        content = {f'{path}/latest.png': "Get the latest updates as soon as they're available",
                   f'{path}/pause.png': 'Pause updates',
                   f'{path}/history.png': 'Update history',
                   f'{path}/settings.png': 'Advanced options',
                   f'{path}/insider.png': 'Windows Insider Program',
                   'Desktop/Images/middle_frame/storage.png': 'Storage',
                   }
        text_containt = ['Monitors, brightness, night light, display profile',
                         '',
                         '',
                         'Reduce distractions',
                         'Screen and sleep, power mode',
                         'Storage space, drivers, configure rules', ]
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame, bg='white')
            frame.grid(row=index + 4, columnspan=11, sticky='nsew', pady=(0, 5))
            for i in range(2):
                frame.grid_rowconfigure(i, minsize=40)
            for i in range(17):
                frame.grid_columnconfigure(i, minsize=40)
            self.category_content.append(frame)

            image_label = Label(frame, image=img, bg='white')
            image_label.grid(row=0, column=0, rowspan=2)
            image_label.image = img
            self.category_content.append(image_label)

            if index == 1 or index == 2:
                self.text_label = Label(frame, text=content[text], anchor='w', font=('Segoe Ui', 11), height=1,
                                        bg='white')
                self.text_label.grid(row=0, column=1, sticky='we', padx=10, columnspan=17, rowspan=2)
                self.text_label2 = Label(frame, text='', anchor='w', bg='white')
                self.text_label2.grid(row=1, column=1)
            else:
                self.text_label = Label(frame, text=content[text], anchor='w', font=('Segoe Ui', 11), bg='white')
                self.text_label.grid(row=0, column=1, sticky='swe', padx=10, columnspan=17)
                self.text_label2 = Label(frame, text=text_containt[index], anchor='w', font=('Segoe Ui', 9), bg='white')
                self.text_label2.grid(row=1, column=1, sticky='nwe', padx=10, columnspan=17)
            self.category_content.append(self.text_label2)
            self.category_content.append(self.text_label)

            img_next = PhotoImage(file='Desktop/Images/middle_frame/next.png')
            img_next = img_next.subsample(x=2, y=2)
            next_img = Label(frame, image=img_next, bg='white')
            next_img.grid(row=0, rowspan=2, column=18, sticky='news', padx=(5, 20))
            next_img.image = img_next

            frame.bind("<Enter>", lambda e, frame=frame, image_label=image_label, text_label=self.text_label,
                                         text_label2=self.text_label2, next_img=next_img: self.on_enter(e, frame,
                                                                                                        image_label,
                                                                                                        text_label,
                                                                                                        text_label2,
                                                                                                        next_img))
            frame.bind("<Leave>", lambda e, frame=frame, image_label=image_label, text_label=self.text_label,
                                         text_label2=self.text_label2, next_img=next_img: self.on_leave(e, frame,
                                                                                                        image_label,
                                                                                                        text_label,
                                                                                                        text_label2,
                                                                                                        next_img))

    def on_enter(self, event, *args):
        for i in args:
            i.configure(bg='#E3E3E3')

    def on_leave(self, event, *args):
        for i in args:
            i.configure(bg='white')
