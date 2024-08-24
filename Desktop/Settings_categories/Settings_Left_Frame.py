from tkinter import *

class LeftFrame(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.left_frame_hold()

    def left_frame_hold(self):
        self.update()
        self.configure(height=self.parent.winfo_height(), width=self.parent.winfo_width() / 7,
                       background='#F3F3F3')
        self.grid_propagate(False)

        self.grid(row=0, column=0, rowspan=14, columnspan=5, sticky='new')
        for i in range(25):
            self.rowconfigure(i, minsize=32, weight=1)
            self.columnconfigure(i, minsize=32, weight=1)

        usr_frame = UserFrame(self)
        icons = LeftFrameButtons(self)


class UserFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.user_frame_items = []
        self.enter_color = '#E3E3E3'
        self.leave_color = '#F3F3F3'
        self.parent.parent.middle_frame = 0

        self.user_frame_hold()

    def user_frame_hold(self):
        self.update()
        self.configure(height=50, width=int(self.parent.winfo_width() * 0.6),
                       background=self.leave_color)
        self.grid_propagate(False)
        self.grid(row=1, column=0, columnspan=25, sticky='news', rowspan=3)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        for i in range(25):
            self.grid_rowconfigure(i, minsize=15, weight=1)
            self.grid_columnconfigure(i, minsize=15, weight=1)

        self.user_frame_items.append(self)

        self.user_frame_picture()
        self.account_name()

        for i in self.user_frame_items:
            i.bind('<Button-1>', self.place_label)

    def account_name(self):
        self.acc_name = Label(self, text='Default User', bg=self.leave_color, font=('Segoe UI',11,'bold'))
        self.acc_name.grid(row=2, column=4, sticky='sw', columnspan=4,padx=(10,0))

        self.acc_mail = Label(self, text='account_email@gmail.com', bg=self.leave_color, font=('Segoe Ui',10))
        self.acc_mail.grid(row=3, column=4, sticky='nw', columnspan=4, rowspan=2,padx=(10,0))

        self.user_frame_items.append(self.acc_name)
        self.user_frame_items.append(self.acc_mail)

    def user_frame_picture(self):
        account_image = PhotoImage(file='Desktop/Images/default-avatar.png')
        self.image_holder = Label(self, image=account_image, background=self.leave_color)
        self.image_holder.grid(row=0, column=0, rowspan=10, columnspan=6, sticky='nw',padx=(20,0))
        self.image_holder.image = account_image

        self.user_frame_items.append(self.image_holder)

    def on_enter(self, e):
        if e.widget.winfo_toplevel() == self.parent.winfo_toplevel():
            self.configure(bg=self.enter_color)
            self.image_holder.configure(bg=self.enter_color)
            self.acc_name.configure(bg=self.enter_color)
            self.acc_mail.configure(bg=self.enter_color)

    def on_leave(self, e):
        if e.widget.winfo_toplevel() == self.parent.winfo_toplevel():
            self.configure(bg=self.leave_color)
            self.image_holder.configure(bg=self.leave_color)
            self.acc_name.configure(bg=self.leave_color)
            self.acc_mail.configure(bg=self.leave_color)

    def place_label(self, e):
        label = Label(self.parent, text='test')
        label.grid(row=3, column=0)


class LeftFrameButtons:
    def __init__(self, parent):
        self.parent = parent
        self.parent.update()

        self.enter_color = '#E3E3E3'
        self.leave_color = '#F3F3F3'

        self.search()
        self.labels()

    def labels(self):
        self.labels_holder = []
        path = 'Desktop/Images/left_frame'
        self.buttons_text = {f'{path}/System.png': '    System',
                             f'{path}/Bluetooth.png': '    Bluetooth & devices',
                             f'{path}/Wifi-1-icon.png': '    Network & internet',
                             f'{path}/personalization.png': '    Personalization',
                             f'{path}/apps.png': '    Apps',
                             'Desktop/Images/Accounts.png': '    Accounts',
                             f'{path}/Time_Zone.png': '    Time & language',
                             f'{path}/Accessibility.png': '    Accessibility',
                             f'{path}/privacy.png': '    Privacy & security',
                             f'{path}/update.png': '    Windows Update',
                             'Desktop/Images/middle_frame/Hello/linkedin.png': '    LinkedIn'}
        for i, text in enumerate(self.buttons_text):
            image = PhotoImage(file=text)
            if i == 2:
                image = image.subsample(x=4,y=4)
            elif i == 9 or i == 10:
                image = image.subsample(x=2,y=2)
            else:
                image = image.subsample(x=12, y=12)
            label = Label(self.parent, image=image, text=self.buttons_text[text],
                          compound='left', anchor='w', bg=self.leave_color, font=('Segoe Ui',11))
            label.bind('<Enter>', lambda e, label=label: self.on_enter(e, label))
            label.bind('<Leave>', lambda e, label=label: self.on_leave(e, label))
            label.grid(row=i + 7, column=1, sticky='nsew', columnspan=25)
            label.image = image
            self.labels_holder.append(label)
            if i == 0:
                label.configure(background=self.enter_color)
                label.bind('<Leave>', self.mark_selected)
            label.bind('<Button-1>', lambda e, number=i: self.selected_category(e, number))


    def selected_category(self, e, number):
        self.labels_holder[number].bind('<Leave>', self.mark_selected)
        self.middle_frame_init(number)
        for index in self.labels_holder:
            if index != self.labels_holder[number]:
                index.configure(bg=self.leave_color)
                index.bind('<Leave>', lambda e, label=index: self.on_leave(e, label))

    def mark_selected(self, e):
        e.widget.configure(background=self.enter_color)

    def on_enter(self, e, label):
        label.configure(bg=self.enter_color)

    def on_leave(self, e, label):
        label.configure(bg=self.leave_color)

    # Test might delete later
    def middle_frame_init(self, number):
        self.parent.parent.middle_frame = number
        self.parent.parent.system_settings()


    def search(self):
        image = PhotoImage(file='Desktop/Images/search_icon.png')
        image = image.subsample(x=3, y=3)

        search_frame = Frame(self.parent, bg='white', highlightcolor='white', highlightthickness=2,highlightbackground='white')
        search_frame.grid(row=5, column=1,columnspan=9, sticky='new')

        bg_frame = Frame(self.parent, bg='black', highlightcolor='black', highlightthickness=4,highlightbackground='black')
        bg_frame.grid(row=5, column=1,columnspan=9, sticky='sew')

        for i in range(30):
            if i == 27:
                search_frame.grid_columnconfigure(27,minsize=0)
            else:
                search_frame.grid_columnconfigure(i,minsize=10)

        search_entry = Entry(search_frame,highlightbackground='white',highlightthickness=3,highlightcolor='white')
        search_entry.grid(row=0,column=0, sticky='news',columnspan=25)

        label = Label(search_frame, image=image, bg='white',anchor='e')
        label.grid(row=0, column=26,sticky='news')
        label.image = image
