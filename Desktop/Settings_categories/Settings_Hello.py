from tkinter import *

class LinedInSettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background='#F3F3F3'

        self.run()

    def run(self):
        sys_category = LinkedInCategory(self)
        self.test_frame()

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background=self.background)
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)


class LinkedInCategory(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


        self.run()

    def run(self):
        self.category_title()
        self.second_frame()
        self.desktop_picture()
        self.python()
        self.categories()
        self.bio()

    def category_title(self):
        label = Label(self.parent, text='LinedIn', font=('Segoe Ui',19,'bold'),anchor='w',
                      bg=self.parent.background)
        label.grid(row=1, column=2, columnspan=2, sticky='nsew')

    def second_frame(self):
        self.content_frame = Frame(self.parent, background=self.parent.background)
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')
        for i in range(14):
            self.content_frame.rowconfigure(i, minsize=64)
            self.content_frame.columnconfigure(i, minsize=64)

    def desktop_picture(self):
        desk_img = PhotoImage(file='Desktop/Images/middle_frame/Hello/linkedinbig.png')
        desktop_pic_frame = Frame(self.content_frame,bg=self.parent.background)
        desktop_pic_frame.grid(row=0, column=0, columnspan=4,sticky='nw')

        pic = Label(desktop_pic_frame, image=desk_img,bg=self.parent.background)
        pic.grid(row=0, column=0,rowspan=2,columnspan=2)
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='Atanas Uzunov', font=('Segoe Ui',16,'bold'), anchor='w',
                           bg=self.parent.background)
        user_label.grid(row=0, column=2, pady=(5, 0), columnspan=10,sticky='sw')

        pc_name = Label(desktop_pic_frame, text='atanas-uzunov-40aa23266', font=('Segoe Ui',10), anchor='w',
                        bg=self.parent.background)
        pc_name.grid(row=1, column=2, columnspan=10,sticky='nw',padx=(0,20))


    def python(self):
        desk_img = PhotoImage(file='Desktop/Images/middle_frame/Hello/python.png')
        desk_img = desk_img.subsample(x=2, y=2)
        desktop_pic_frame = Frame(self.content_frame, background=self.parent.background)
        desktop_pic_frame.grid(row=0, column=9, columnspan=2, sticky='w')

        pic = Label(desktop_pic_frame, image=desk_img,bg=self.parent.background)
        pic.grid(row=0, column=0, rowspan=2,sticky='nsew')
        pic.image = desk_img

        user_label = Label(desktop_pic_frame, text='Pyton 3.10', font=('Segoe Ui',11,'bold'), anchor='w',
                           bg=self.parent.background)
        user_label.grid(row=0, column=1, sticky='nsew',padx=(10,0))

        pc_name = Label(desktop_pic_frame, text='Tkinter', font=('Segoe Ui',10), anchor='w',bg=self.parent.background)
        pc_name.grid(row=1, column=1, sticky='nwes',padx=(10,0))

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
        path = 'Desktop/Images/middle_frame/Hello'
        content = {f'{path}/like.png': 'Like',
                   f'{path}/friend.png': 'Follow',
                   f'{path}/share.png': 'Share'
                   }
        text_containt = ['If you enjoyed',
                         'I am always open for a good friendship : )',
                         'For other']
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame, bg='white')
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
            next_img.grid(row=0,rowspan=2,column=18,sticky='news')
            next_img.image = img_next



            frame.bind("<Enter>", lambda e, frame=frame, image_label=image_label, text_label=text_label,
                                         text_label2=text_label2,next_img = next_img: self.on_enter(e, frame, image_label, text_label,
                                                                                text_label2,next_img))
            frame.bind("<Leave>", lambda e, frame=frame, image_label=image_label, text_label=text_label,
                                         text_label2=text_label2,next_img=next_img: self.on_leave(e, frame, image_label, text_label,
                                                                                text_label2,next_img))
    def bio(self):
        made_by = Label(self.content_frame,text='Made by: ',font=('Segoe Ui',11),background=self.parent.background)
        made_by.grid(row=5,column=0)

        promote = PhotoImage(file='Desktop/Images/middle_frame/Hello/resume.png')
        promote = promote.subsample(x=2,y=2)
        place = Label(self.content_frame,image=promote)
        place.image=promote
        place.grid(row=5,column=7,columnspan=6,rowspan=6,sticky='nw')

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
