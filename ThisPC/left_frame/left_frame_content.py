from tkinter import *

#from ThisPC.top_frame.top_frame_content import Searchbar
#from ThisPC.top_frame.create_top_canvas import TopCanvas

class LeftContent:
    def __init__(self, parent, width):
        self.parent = parent
        self.width_scale = int(width * 0.1)
        self.access_holder = []
        self.thispc_holder = []
        self.photo_images = []
        self.category_content = []
        self.selected_frame = None
        self.click_count = 0

    def run(self):
        self.quick_access()
        self.thispc()

    def quick_access(self):
        self.quick_access_label_holder = []
        frames = {
            "ThisPC/left_frame/left_frame_icons/quick_access/access.png": "Quick Access",
            "ThisPC/left_frame/left_frame_icons/quick_access/desktop.png": "Desktop",
            "ThisPC/left_frame/left_frame_icons/quick_access/downloads.png": "Downloads",
            "ThisPC/left_frame/left_frame_icons/quick_access/documents.png": "Documents",
            "ThisPC/left_frame/left_frame_icons/quick_access/pictures.png": "Pictures",
            "ThisPC/left_frame/left_frame_icons/quick_access/newvolume.png": "New Volume (D:)"
        }
        for index, content in enumerate(frames):
            img = PhotoImage(file=content)
            img = img.subsample(x=3, y=3)
            frame_init = Frame(self.parent, bg='white')
            frame_init.grid(row=index, column=0, sticky='news')
            self.access_holder.append(frame_init)

            label_cont = Label(frame_init, image=img, text=frames[content], width=150, compound='left',
                               anchor='w', bg='white', font=('Segoe Ui', 9))
            label_cont.grid(row=0, column=1, sticky='nwes')
            label_cont.image = img
            self.quick_access_label_holder.append(label_cont)

            if index == 0:
                quick_img = PhotoImage(file='ThisPC/left_frame/left_frame_icons/quick_access/down.png')
                quick_img = quick_img.subsample(x=3, y=3)

                quick_down = Label(frame_init, image=quick_img, bg='white')
                quick_down.grid(row=0, column=0)
                quick_down.image = quick_img

                quick_down.bind('<Button-1>', self.remove_quick_access)

            if index != 0:
                label_cont.grid(row=0, column=1, sticky='nwes', padx=(20, 0))
                label_cont.configure(padx=5)
            else:
                label_cont.grid(row=0, column=1, sticky='nwes')

            label_cont.bind('<Button-1>', lambda e, category='Quick_Access', indx=index, label=label_cont
            : self.selected_category(e, category, indx, label))
            label_cont.bind('<Enter>', lambda e, label=label_cont: self.on_enter(e, label))
            label_cont.bind('<Leave>', lambda e, label=label_cont: self.on_leave(e, label))

    def thispc(self):
        self.thispc_label_holder = []
        frames = {
            'ThisPC/left_frame/left_frame_icons/thispc/pc.png': 'This PC',
            "ThisPC/left_frame/left_frame_icons/thispc/3d.png": "3D Objects",
            "ThisPC/left_frame/left_frame_icons/quick_access/desktop.png": "Desktop",
            "ThisPC/left_frame/left_frame_icons/quick_access/documents.png": "Documents",
            "ThisPC/left_frame/left_frame_icons/quick_access/downloads.png": "Downloads",
            "ThisPC/left_frame/left_frame_icons/thispc/music.png": "Music",
            "ThisPC/left_frame/left_frame_icons/quick_access/pictures.png": "Pictures",
            "ThisPC/left_frame/left_frame_icons/thispc/videos.png": "Videos",
            "ThisPC/left_frame/left_frame_icons/thispc/c.png": "Local (C:)",
            "ThisPC/left_frame/left_frame_icons/quick_access/newvolume.png": "New Volume (D:)"
        }
        for index, content in enumerate(frames):
            frame_init = Frame(self.parent, bg='white')
            frame_init.grid(row=index + 6, column=0, sticky='nsew')

            label_image = PhotoImage(file=content)
            label_image = label_image.subsample(x=3, y=3)
            self.photo_images.append(label_image)

            label_cont = Label(frame_init, image=label_image, text=frames[content], width=150,
                               anchor='w', bg='white', font=('Segoe Ui', 9), compound='left')
            label_cont.image = label_image

            self.thispc_label_holder.append(label_cont)

            self.thispc_holder.append(frame_init)

            if index != 0:
                label_cont.grid(row=0, column=1, sticky='nwes', padx=(20, 0))
                label_cont.configure(padx=5)

            else:
                label_cont.grid(row=0, column=1, sticky='nwes')
            if index == 0:
                next_img = PhotoImage(file='ThisPC/left_frame/left_frame_icons/quick_access/down.png')
                next_img = next_img.subsample(x=3, y=3)

                quick_down = Label(frame_init, image=next_img, bg='white')
                quick_down.image = next_img
                quick_down.grid(row=0, column=0)

                quick_down.bind('<Button-1>', self.remove_thispc)

            label_cont.bind('<Button-1>', lambda e, category='ThisPC', indx=index, label=label_cont
            : self.selected_category(e, category, indx, label))
            label_cont.bind('<Enter>', lambda e, label=label_cont: self.on_enter(e, label))
            label_cont.bind('<Leave>', lambda e, label=label_cont: self.on_leave(e, label))

    def selected_category(self, e, category, number, label):
        img = e.widget.cget('image')
        txt = e.widget.cget('text')
        print(f'{img} | {txt}')

        for index, content in enumerate(self.thispc_label_holder):
            content.configure(bg='white')
            content.bind('<Leave>', lambda e, label=content: self.on_leave(e, label))
            self.thispc_holder[index].configure(bg='white')
            self.thispc_holder[index].bind('<Leave>',
                                           lambda e, frame=self.thispc_holder[index]: self.on_leave(e, frame))

        for index, content in enumerate(self.quick_access_label_holder):
            content.configure(bg='white')
            content.bind('<Leave>', lambda e, label=content: self.on_leave(e, label))
            self.access_holder[index].configure(bg='white')
            self.access_holder[index].bind('<Leave>',
                                           lambda e, frame=self.access_holder[index]: self.on_leave(e, frame))
        if category == 'Quick_Access':
            e.widget.bind('<Leave>',
                          lambda e, category='Quick_Access', num=number: self.mark_selected(e, category, num))
            label.configure(bg='#E3E3E3')
            self.access_holder[number].configure(bg='#E3E3E3')
            self.access_holder[number].bind('<Leave>', lambda e, category='Quick_Access',
                                                              num=number: self.mark_selected(e, category, num))

        if category == 'ThisPC':
            e.widget.bind('<Leave>', lambda e, category='ThisPC', num=number: self.mark_selected(e, category, num))
            label.configure(bg='#E3E3E3')
            self.thispc_holder[number].configure(bg='#E3E3E3')
            self.thispc_holder[number].bind('<Leave>', lambda e, category='ThisPC',
                                                              num=number: self.mark_selected(e, category, num))

    def mark_selected(self, e, category, number):
        if category == 'Quick_Access':
            self.access_holder[number].configure(background='#E3E3E3')
            self.quick_access_label_holder[number].configure(background='#E3E3E3')
        if category == 'ThisPC':
            self.thispc_holder[number].configure(background='#E3E3E3')
            self.thispc_label_holder[number].configure(background='#E3E3E3')

    def remove_quick_access(self, e):
        if self.click_count == 0:
            self.click_count = 1
            for i, content in enumerate(self.access_holder[1:]):
                content.grid_forget()
        else:
            self.click_count = 0
            for i, content in enumerate(self.access_holder[1:]):
                content.grid(row=i + 1, column=0)

    def remove_thispc(self, e):
        if self.click_count == 0:
            self.click_count = 1
            for i, content in enumerate(self.thispc_holder[1:]):
                content.grid_forget()
        else:
            self.click_count = 0
            for i, content in enumerate(self.thispc_holder[1:]):
                content.grid(row=(len(self.access_holder) + 1) + i, column=0)

    def on_enter(self, event, *args):
        for i in args:
            i.configure(background='#E3E3E3')

    def on_leave(self, event, *args):
        for i in args:
            i.configure(background='white')

    ## Work in progress
    #def update_search_img(self, img, txt):
        #tcanvas = TopCanvas(self.parent, 0, 0)
        #parent = tcanvas.create_cavnas()
        #srch = Searchbar(tcanvas.parent, 0)
        #srch.main_frame()
        #srch.frame1()
        #rch.update_searchbar_img(img, txt)
