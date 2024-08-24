from tkinter import *

class PrivacySettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background='#F3F3F3'

        self.run()

    def run(self):
        sys_category = PrivacyCategory(self)
        self.test_frame()

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background=self.background)
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)


class PrivacyCategory(Frame):
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
        label = Label(self.parent, text='Privacy & security', font=('Segoe Ui',19,'bold'),anchor='w',bg=self.parent.background)
        label.grid(row=1, column=2, columnspan=4, sticky='nsew')

    def second_frame(self):
        self.content_frame = Frame(self.parent, background=self.parent.background)
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')
        for i in range(14):
            self.content_frame.rowconfigure(i, minsize=64)
            self.content_frame.columnconfigure(i, minsize=64)

    def desktop_picture(self):
        text_frame = Frame(self.content_frame, background=self.parent.background)
        text_frame.grid_propagate(False)
        text_frame.grid(row=0, column=0, columnspan=2, sticky='news')

        user_label = Label(text_frame, text='Security', font=('Segoe Ui',10,'bold'), anchor='w',
                           background=self.parent.background)
        user_label.grid(row=0, column=0, columnspan=1,sticky='w')

        text_frame2 = Frame(self.content_frame, background=self.parent.background)
        text_frame2.grid_propagate(False)
        text_frame2.grid(row=3, column=0, columnspan=3, sticky='news')
        user_label = Label(text_frame2, text='Windows permissions', font=('Segoe Ui',10,'bold'), anchor='sw',
                           background=self.parent.background)
        user_label.grid(row=0, column=0, columnspan=3,sticky='w',pady=(10,0))

    def categories(self):
        self.category_content = []
        path = 'Desktop/Images/middle_frame/Privacy'
        content = {f'{path}/windows.png': 'Windows Security',
                   f'{path}/find.png': 'Find my device',
                   f'{path}/troubleshoot.png': 'For developers',
                   f'{path}/general.png': 'General',
                   f'{path}/speech.png': 'Speech',
                   f'{path}/inking.png': 'Inking & typing personalization',
                   f'{path}/diagnostics.png': 'Diagnostics & feedback',
                   f'{path}/history.png': 'Activity history',
                   }
        text_containt = ['Antivirus, browsers, firewall, and network protection for your device',
                         "Track your device if you think you've lost it",
                         'These settings are intended for development use only',
                         'Advertising ID, local content, app launches, settings suggestions, productivity tools',
                         'Online speech recognition for dictation and other voice-based interactions',
                         'Custom dictionary, words in your dictionary',
                         'Diagnostic data, inking and typing data, tailored experience, feedback frequency',
                         'Options for getting more from your activity history across devices and accounts']
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame, bg='white')
            if index == 0:
                frame.grid(row=index, columnspan=11, sticky='nsew', pady=(30, 5))
            elif index == 3:
                frame.grid(row=index, columnspan=11, sticky='nsew', pady=(40, 5))
            else:
                frame.grid(row=index, columnspan=11, sticky='nsew', pady=(0, 5))
            for i in range(2):
                frame.grid_rowconfigure(i, minsize=40)
            for i in range(17):
                frame.grid_columnconfigure(i, minsize=40)
            self.category_content.append(frame)

            image_label = Label(frame, image=img, bg='white')
            image_label.grid(row=0, column=0, rowspan=2)
            image_label.image = img
            self.category_content.append(image_label)

            text_label = Label(frame, text=content[text], anchor='w', font=('Segoe Ui', 11), bg='white')
            text_label.grid(row=0, column=1, sticky='swe', padx=10, columnspan=17)
            self.category_content.append(text_label)

            text_label2 = Label(frame, text=text_containt[index], anchor='w', font=('Segoe Ui', 9), bg='white')
            text_label2.grid(row=1, column=1, sticky='nwe', padx=10, columnspan=17)
            self.category_content.append(text_label2)

            img_next = PhotoImage(file='Desktop/Images/middle_frame/next.png')
            img_next = img_next.subsample(x=2, y=2)
            next_img = Label(frame, image=img_next, bg='white')
            next_img.grid(row=0, rowspan=2, column=18, sticky='news', padx=(5, 20))
            next_img.image = img_next

            frame.bind("<Enter>", lambda e, frame=frame, image_label=image_label, text_label=text_label,
                                         text_label2=text_label2, next_img=next_img: self.on_enter(e, frame,
                                                                                                   image_label,
                                                                                                   text_label,
                                                                                                   text_label2,
                                                                                                   next_img))
            frame.bind("<Leave>", lambda e, frame=frame, image_label=image_label, text_label=text_label,
                                         text_label2=text_label2, next_img=next_img: self.on_leave(e, frame,
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
