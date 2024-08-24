from tkinter import *

class BluetoothSettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background='#F3F3F3'

        self.run()

    def run(self):
        sys_category = BluetoothCategory(self)
        self.test_frame()

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background=self.background)
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)



class BluetoothCategory(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.run()

    def run(self):
        self.category_title()
        self.second_frame()
        self.categories()

    def category_title(self):
        label = Label(self.parent,
                      text='Bluetooth & devices',
                      font=('Segoe Ui',19,'bold'),
                      anchor='w',
                      bg=self.parent.background
                      )
        label.grid(row=1, column=2, columnspan=5, sticky='new')

    def second_frame(self):
        self.content_frame = Frame(self.parent,bg=self.parent.background)
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')

        for i in range(14):
            self.content_frame.rowconfigure(i, minsize=64)
            self.content_frame.columnconfigure(i, minsize=64)

    def categories(self):
        self.category_content = []
        path = 'Desktop/Images/middle_frame/Bluetooth'
        content = {f'{path}/devices.png': 'Devices',
                   f'{path}/printers.png': 'Printers & scanners',
                   f'{path}/phone.png': 'Phone Link',
                   f'{path}/mouse.png': 'Mouse',
                   f'{path}/pen.png': 'Pen & Windows Ink',
                   f'{path}/autoplay.png': 'AutoPlay',
                   f'{path}/usb.png': 'USB',
                   }
        text_containt = ['Mouse, keyboard, pen, audio, display and docks, other devices',
                         'Preferences, troubleshoot',
                         "Instantly access your Android device's photos, text, and more",
                         'Buttons, mouse pointer speed, scrolling',
                         'Right-handed or left-handed, pen button shortcuts, handwriting',
                         'Defaults for removable drivers and memory cards',
                         'Notifications, USb battery saver',]
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame,bg='white')
            frame.grid(row=index, columnspan=11, sticky='nsew', pady=(0, 7))
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
            if index == 0:
                label = Label(frame,text='Add device',background='blue',fg='white', font=('Segoe Ui',10),height=2,width=15)
                label.grid(row=0,column=13,rowspan=3,columnspan=4)
            if index == 2:
                label = Label(frame,text='Open Phone Link',background='white',fg='black', font=('Segoe Ui',9),height=1,width=15,
                              highlightthickness=1,highlightcolor='black')
                label.grid(row=0,column=13,rowspan=3,columnspan=4)
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

    def on_enter(self, event, *args):
        for i in args:
            i.configure(bg='#E3E3E3')

    def on_leave(self, event, *args):
        for i in args:
            i.configure(bg='white')
