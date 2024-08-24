from tkinter import *

class PersonalizationSettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background='#F3F3F3'

        self.run()

    def run(self):
        sys_category = PersonalizationCategory(self)
        self.test_frame()

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background=self.background)
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)


class PersonalizationCategory(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.content_frame = None

        self.run()

    def run(self):
        self.category_title()
        self.second_frame()
        self.desktop_picture()
        self.theme_pictures()
        self.categories()

    def category_title(self):
        label = Label(self.parent, text='Personalization', font=('Segoe Ui',19,'bold'),anchor='w'
                      , background =self.parent.background)

        label.grid(row=1, column=2, columnspan=5, sticky='new')

    def second_frame(self):
        self.content_frame = Frame(self.parent,background  =self.parent.background)
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')
        for i in range(25):
            self.content_frame.grid_rowconfigure(i, minsize=40)
            self.content_frame.grid_columnconfigure(i, minsize=40)

    def desktop_picture(self):
        self.content_frame.update()
        desk_img = PhotoImage(file='Desktop//Images/background.png')
        desk_img = desk_img.subsample(x=5, y=5)
        desktop_pic_frame = Frame(self.content_frame, highlightbackground='black', highlightthickness=7)
        desktop_pic_frame.grid(row=0, column=0,columnspan=6,rowspan=5,sticky='w')

        pic = Label(desktop_pic_frame, image=desk_img)
        pic.grid(row=0, column=0,columnspan=6,sticky='nsew',rowspan=5)
        pic.image = desk_img

    def theme_pictures(self):
        path = 'Desktop/Images/middle_frame/Personalization'
        content = [f'{path}/01.png',
                   f'{path}/02.png',
                   f'{path}/03.png',
                   f'{path}/04.png',
                   f'{path}/05.png',
                   f'{path}/06.png']
        label = Label(self.content_frame,text='Select a theme to apply',anchor='w',background =self.parent.background,
                     font=('Segoe Ui',10))
        label.grid(row=5,column=0,sticky='nsew',columnspan=5)
        for index,content in enumerate(content):
            desk_img = PhotoImage(file=content)
            if index < 3:
                desk_img = desk_img.subsample(x=5, y=5)
                desktop_pic_frame = Frame(self.content_frame)
                desktop_pic_frame.grid(row=6, column=index,rowspan=2,sticky='w',columnspan=2)
                pic = Label(desktop_pic_frame, image=desk_img)
                pic.grid(row=0, column=0,columnspan=2)
                pic.image = desk_img
            else:
                desk_img = desk_img.subsample(x=5, y=5)
                desktop_pic_frame = Frame(self.content_frame)
                desktop_pic_frame.grid(row=8, column=index-3,rowspan=2,sticky='w')
                pic = Label(desktop_pic_frame, image=desk_img)
                pic.grid(row=0, column=0,columnspan=2)
                pic.image = desk_img
    def categories(self):
        self.category_content = []
        path = 'Desktop/Images/middle_frame/Personalization'
        content = {f'{path}/background.png': 'Background',
                   f'{path}/colors.png': 'Colors',
                   }
        text_containt = ['Background image, color, slideshow', 'Accent color, transparency effects, color theme']
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame, bg='white')
            frame.grid(row=index + 10, columnspan=8, sticky='nsew', pady=(5,0))
            for i in range(2):
                frame.grid_rowconfigure(i, minsize=40)
            for i in range(17):
                frame.grid_columnconfigure(i, minsize=40)
            self.category_content.append(frame)

            image_label = Label(frame, image=img,bg='white')
            image_label.grid(row=0, column=0,rowspan=2)
            image_label.image = img
            self.category_content.append(image_label)

            text_label = Label(frame, text=content[text], anchor='w', font=('Segoe Ui',11),bg='white')
            text_label.grid(row=0, column=1, sticky='swe', padx=10, columnspan=10)
            self.category_content.append(text_label)

            text_label2 = Label(frame, text=text_containt[index], anchor='w', font=('Segoe Ui',9),bg='white')
            text_label2.grid(row=1, column=1, sticky='nwe', padx=10, columnspan=10)
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

    def on_enter(self, event, *args):
        for i in args:
            i.configure(bg='#E3E3E3')

    def on_leave(self, event, *args):
        for i in args:
            i.configure(bg='white')
