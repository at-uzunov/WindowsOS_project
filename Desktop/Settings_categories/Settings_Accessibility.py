from tkinter import *

class AccessibilitySettings(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background='#F3F3F3'

        self.run()

    def run(self):
        sys_category = AccessibilityCategory(self)
        self.test_frame()

    def test_frame(self):
        self.configure(height=self.parent.winfo_height(), width=int(self.parent.winfo_width() * 0.75),
                       background=self.background)
        self.grid_propagate(False)
        self.grid(row=0, column=5)
        for i in range(25):
            self.rowconfigure(i, minsize=64)
            self.columnconfigure(i, minsize=64)


class AccessibilityCategory(Frame):
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
        label = Label(self.parent, text='Accessibility', font=('Segoe Ui',19,'bold'),anchor='w',
                      background=self.parent.background)
        label.grid(row=1, column=2, columnspan=2, sticky='nsew')

    def second_frame(self):
        self.content_frame = Frame(self.parent, background=self.parent.background)
        self.content_frame.grid(row=2, column=2, columnspan=25, rowspan=25, sticky='nsew')
        for i in range(14):
            self.content_frame.rowconfigure(i, minsize=64)
            self.content_frame.columnconfigure(i, minsize=64)


    def desktop_picture(self):
        text_frame = Frame(self.content_frame, background=self.parent.background)
        text_frame.grid_propagate(False)
        text_frame.grid(row=0, column=0,sticky='news')

        user_label = Label(text_frame, text='Vision', font=('Segoe Ui',10,'bold'), anchor='w', width=6,
                           background=self.parent.background)
        user_label.grid(row=0, column=0, columnspan=10,sticky='w')


    def categories(self):
        self.category_content = []
        content = {'Desktop/Images/middle_frame/Accessibility/text.png': 'Text size',
                   'Desktop/Images/middle_frame/Accessibility/effects.png': 'Visual effects',
                   'Desktop/Images/middle_frame/Accessibility/pointer.png': 'Mouse pointer and touch',
                   'Desktop/Images/middle_frame/Accessibility/cursor.png': 'Text cursor',
                   'Desktop/Images/middle_frame/Accessibility/magnifier.png': 'Magnifier',
                   'Desktop/Images/middle_frame/Accessibility/palette.png': 'Color filters',
                   'Desktop/Images/middle_frame/Accessibility/contrast.png': 'Contrast themes',
                   'Desktop/Images/middle_frame/Accessibility/narator.png': 'Narrator',
                   }
        text_containt = ['Text size that appears throughout Windows and your apps',
                         'Scroll bars, transparency, animations, notification timeout',
                         'Mouse pointer color, size',
                         'Appearance and thickness, text cursor indicator',
                         'Magnifier reading, zoom increment',
                         'Colorblindness filtering, grayscale, inverted',
                         'Color themes for low vision, light sensitivity',
                         'Voice, verbosity, keyboard, braille']
        for index, text in enumerate(content):
            img = PhotoImage(file=text)
            img = img.subsample(x=2, y=2)
            frame = Frame(self.content_frame, bg='white')
            if index == 0:
                frame.grid(row=index, columnspan=11, sticky='nsew', pady=(25,5))
            else:
                frame.grid(row=index, columnspan=11, sticky='nsew', pady=(0,5))
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


    def on_enter(self, event, *args):
        for i in args:
            i.configure(bg='#E3E3E3')

    def on_leave(self, event, *args):
        for i in args:
            i.configure(bg='white')
