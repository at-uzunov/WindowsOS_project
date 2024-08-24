from tkinter import *

from Desktop.Settings_categories import SettingsMainWindow


class Cont:
    def __init__(self, parent, root, width):
        self.parent = parent
        self.root = root
        self.cnv_width = width
        self.active_lbl = []
        self.category_frames = []

    def run(self):
        self.file_btn()
        self.computer_and_view_btn()
        self.init_category(0)
        self.searchbar()

    def file_btn(self):
        mbtn = Menubutton(self.parent, text='File', width=8, bg='blue', fg='white')
        mbtn.grid(row=0, column=0, padx=(3, 0), pady=(3, 0))

        mbtn.menu = Menu(mbtn, tearoff=0)
        mbtn["menu"] = mbtn.menu

        mbtn.menu.add_cascade(label='New Window')

    def computer_and_view_btn(self):
        lbl = Label(self.parent, text='Computer', width=12)
        lbl.grid(row=0, column=1, padx=(2, 0), pady=(3, 0), stick='nsew')
        lbl.bind('<Button-1>', lambda e, val=0: self.start_categry(e, val))

        lbl1 = Label(self.parent, width=8, text='View')
        lbl1.grid(row=0, column=2, sticky='nsew', padx=(2, 0), pady=(3, 0))
        lbl1.bind('<Button-1>', lambda e, val=1: self.start_categry(e, val))

        self.active_lbl.append(lbl)
        self.active_lbl.append(lbl1)

        self.computer_frm = Frame(self.parent, width=975, height=95, bg='#E3E4E5')
        self.computer_frm.grid_propagate(False)

        self.view_frm = Frame(self.parent, width=975, height=95, bg='#E3E4E5')
        self.view_frm.grid_propagate(False)

        self.category_frames.append(self.computer_frm)
        self.category_frames.append(self.view_frm)

    def init_category(self, number):
        if number == 0:
            self.rn = Computerfldr(self.computer_frm, self.root)
            self.computer_frm.grid(row=1, column=0, columnspan=1000, sticky='w', padx=(3, 0))
            self.computer_frm.grid_propagate(False)
            self.active_lbl[number].configure(relief='sunken', bg='silver')
        elif number == 1:
            self.rn = Viewfldr(self.view_frm, self.root)
            self.view_frm.grid(row=1, column=0, columnspan=1000, sticky='w', padx=(3, 0))
            self.view_frm.grid_propagate(False)
            self.active_lbl[number].configure(relief='sunken', bg='silver')

    def start_categry(self, e, category):
        current = category
        for index, content in enumerate(self.active_lbl):
            self.category_frames[index].grid_forget()
            self.active_lbl[index].configure(relief='flat')
            bground = e.widget.winfo_toplevel().cget('bg')
            self.active_lbl[index].configure(bg=bground)
        self.init_category(current)

    def searchbar(self):
        sbar = Searchbar(self.parent, self.cnv_width)
        sbar.run()


class Computerfldr:
    def __init__(self, parent, rootparent):
        self.parent = parent
        self.root = rootparent
        self.bg_color = '#F5F6F7'
        self.location()
        self.ntwork()
        self.stem()

    def location(self):
        frm = Frame(self.parent, height=75, width=150, bg=self.bg_color)
        frm.grid_propagate(False)
        frm.grid(row=1, column=0, padx=(1, 0), pady=(1, 0), sticky='ns')
        ldr = {'ThisPC/top_frame/icons/properties.png': 'Properties',
               'ThisPC/top_frame/icons/open.png': 'Open',
               'ThisPC/top_frame/icons/rename.png': 'Rename'}
        for index, text in enumerate(ldr):
            img = PhotoImage(file=text)
            lbl = Label(frm, text=ldr[text], image=img, compound='top', font=('Segoe Ui', 9), bg=self.bg_color)
            lbl.image = img
            lbl.grid(row=0, column=index, sticky='nw')

            lbl.bind('<Enter>', self.on_enter)
            lbl.bind('<Leave>', self.on_leave)

        lbl = Label(frm, text='Location', font=('Segoe Ui', 9), bg=self.bg_color)
        lbl.grid(row=1, column=0, columnspan=3, pady=(14, 0))

    def ntwork(self):
        frm = Frame(self.parent, height=92, width=245, bg=self.bg_color)
        frm.grid_propagate(False)
        frm.grid(row=1, column=1, padx=(1, 0), pady=(1, 0), sticky='nw')
        ldr = {'ThisPC/top_frame/icons/media.png': 'Access media',
               'ThisPC/top_frame/icons/network.png': 'Map network drive',
               'ThisPC/top_frame/icons/location.png': 'Add a network location'}
        for index, text in enumerate(ldr):
            img = PhotoImage(file=text)
            lbl = Label(frm, text=ldr[text], image=img, compound='top', wraplength=90, font=('Segoe Ui', 9), width=70,
                        bg=self.bg_color)
            lbl.image = img
            if index == 0:
                lbl.config(wraplength=50)
            lbl.grid(row=0, column=index, padx=(4, 0))

            lbl.bind('<Enter>', self.on_enter)
            lbl.bind('<Leave>', self.on_leave)

        lbl = Label(frm, text='Network', font=('Segoe Ui', 9), bg=self.bg_color)
        lbl.grid(row=1, column=0, columnspan=3)

    def stem(self):
        frm = Frame(self.parent, bg=self.bg_color)
        frm.grid(row=1, column=2, padx=(1, 0), pady=(1, 0), sticky='n')

        cont = {'ThisPC/top_frame/icons/settings.png': 'Open Settings',
                'ThisPC/top_frame/icons/uninstall.png': 'Uninstall or change a program',
                'ThisPC/top_frame/icons/sysprop.png': 'System properties',
                'ThisPC/top_frame/icons/manage.png': 'Manage'}

        for index, text in enumerate(cont):
            img = PhotoImage(file=text)
            if index != 0:
                img = img.subsample(x=3, y=3)
                lbl = Label(frm, text=cont[text], image=img, compound='left', font=('Segoe Ui', 9), bg=self.bg_color)
                lbl.grid(row=index, column=1, sticky='nw')
                lbl.image = img
                lbl.bind('<Enter>', self.on_enter)
                lbl.bind('<Leave>', self.on_leave)
            else:
                lbl = Label(frm, text=cont[text], image=img, compound='top', font=('Segoe Ui', 9),
                            wraplength=60, bg=self.bg_color)
                lbl.grid(row=0, column=0, rowspan=5, sticky='enw', padx=5)
                lbl.image = img
                lbl.bind('<Enter>', self.on_enter)
                lbl.bind('<Leave>', self.on_leave)
                lbl.bind('<Button-1>', self.opn_stings)
        lbl = Label(frm, text='System', font=('Segoe Ui', 9), bg=self.bg_color)
        lbl.grid(row=4, column=0, columnspan=2, pady=(5, 0))

    def opn_stings(self, e):
        stings = SettingsMainWindow.SettingsWindows(self.root.root)
        stings.run()

    def on_enter(self, event):
        event.widget.configure(background='lightblue1')

    def on_leave(self, event):
        event.widget.configure(background=self.bg_color)


class Viewfldr:
    def __init__(self, parent, root):
        self.parent = parent
        self.root = root
        self.bgcolor = '#F5F6F7'
        self.cont_frames()

    def cont_frames(self):
        def panels_frame():
            frm = Frame(self.parent, bg=self.bgcolor)
            frm.grid(row=0, column=0, padx=(1, 0), pady=(1, 0))
            imges = {'ThisPC/top_frame/icons/side_panel_01.png': 'Navigation pane',
                     'ThisPC/top_frame/icons/side_panel_02.png': 'Preview pane',
                     'ThisPC/top_frame/icons/side_panel_03.png': 'Details pane'}
            for index, content in enumerate(imges):
                if index == 0:
                    img = PhotoImage(file=content)
                    lbl = Label(frm, image=img, text=imges[content], compound='top', wraplength=60, bg=self.bgcolor)
                    lbl.grid(row=0, column=0, rowspan=4)
                    lbl.image = img
                    lbl.bind('<Enter>', on_enter)
                    lbl.bind('<Leave>', on_leave)
                else:
                    img = PhotoImage(file=content)
                    lbl = Label(frm, image=img, text=imges[content], compound='left',
                                anchor='w', width=100, bg=self.bgcolor)
                    lbl.grid(row=index - 1, column=1, padx=(5, 0))
                    lbl.image = img
                    lbl.bind('<Enter>', on_enter)
                    lbl.bind('<Leave>', on_leave)
            details = Label(frm, text='Panels', bg=self.bgcolor)
            details.grid(row=5, column=0, columnspan=2, sticky='n')

        def layout_frame():
            frame = Frame(self.parent,bg='white')
            frame.grid(row=0, column=1, padx=(1, 0), pady=(1, 0), sticky='nw', rowspan=4)

            canvas = Canvas(frame, height=65, width=280,bg='white')
            canvas.grid(row=0, column=1, sticky='nw', rowspan=4)

            frm = Frame(canvas,bg='white')
            canvas.create_window((0, 0), window=frm, anchor='nw')

            imges = {'ThisPC/top_frame/icons/extra.png': 'Extra large icons',
                     'ThisPC/top_frame/icons/medium.png': 'Medium icons',
                     'ThisPC/top_frame/icons/list.png': 'List',
                     'ThisPC/top_frame/icons/titles.png': 'Titles',
                     'ThisPC/top_frame/icons/large.png': 'Larget Icons',
                     'ThisPC/top_frame/icons/smallicons.png': 'Small icons',
                     'ThisPC/top_frame/icons/details.png': 'Details',
                     'ThisPC/top_frame/icons/content.png': 'Content'
                     }
            for index, content in enumerate(imges):
                img = PhotoImage(file=content)
                lbl = Label(frm, image=img, text='   ' + imges[content],
                            compound='left', anchor='w', width=130,bg='white')
                if index < 4:
                    lbl.grid(row=index, column=0, sticky='nw')
                    lbl.bind('<Enter>', on_enter)
                    lbl.bind('<Leave>', on_leave2)
                else:
                    lbl.grid(row=index - 4, column=1)
                    lbl.bind('<Enter>', on_enter)
                    lbl.bind('<Leave>', on_leave2)
                lbl.image = img

            scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
            scrollbar.grid(row=0, column=1, sticky='nse')
            canvas.config(yscrollcommand=scrollbar.set)

            description = Label(frame, text='Layout',bg=self.bgcolor)
            description.grid(row=5, column=0, sticky='new', columnspan=2)

            frm.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        def current_frame():
            frm = Frame(self.parent, width=230, height=90,bg=self.bgcolor)
            frm.grid_propagate(False)
            count = 0
            frm.grid(row=0, column=2, rowspan=6, padx=(1, 0), pady=(1, 0), sticky='nw')

            imges = {'ThisPC/top_frame/icons/sortby.png': 'Sort by',
                     'ThisPC/top_frame/icons/groupby.png': 'Group by',
                     'ThisPC/top_frame/icons/addcolumns.png': 'Add columns',
                     'ThisPC/top_frame/icons/sizeall.png': 'Size all columns to fit'}
            for index, content in enumerate(imges):
                img = PhotoImage(file=content)
                if index == 0:
                    lbl = Label(frm, image=img, text=imges[content],
                                compound='top', wraplength=25, width=40,bg=self.bgcolor)
                    lbl.grid(row=0, column=0, rowspan=5, padx=(10, 0), pady=(2, 0), sticky='nw')
                    lbl.image = img
                    lbl.bind('<Enter>', on_enter)
                    lbl.bind('<Leave>', on_leave)
                else:
                    lbl = Label(frm, image=img, text='  ' + imges[content],
                                compound='left', anchor='nw', width=150,bg=self.bgcolor)
                    lbl.grid(row=count, column=1, sticky='nw', padx=(8, 0))
                    lbl.image = img
                    count += 1
                    lbl.bind('<Enter>', on_enter)
                    lbl.bind('<Leave>', on_leave)

            title = Label(frm, text='Current view',bg=self.bgcolor)
            title.grid(row=5, column=0, columnspan=2)

        def show_hide():
            frm = Frame(self.parent, width=215, height=90,bg=self.bgcolor)
            frm.grid_propagate(False)
            frm.grid(row=0, column=3, pady=(1, 0), padx=(1, 0))

            chboxes = ['item check boxes', 'File name extensions', 'Hidden items']
            for index, content in enumerate(chboxes):
                chb = Checkbutton(frm, text=content, width=15, anchor='w',bg=self.bgcolor)
                chb.grid(row=index, column=0, sticky='nw')
            img = PhotoImage(file='ThisPC/top_frame/icons/hideexport.png')
            lbl = Label(frm, image=img, text='Hide selected items',
                        compound='top', wraplength=90, anchor='e',bg=self.bgcolor)
            lbl.grid(row=0, column=1, rowspan=3, sticky='e', padx=(3, 0))
            lbl.image = img
            lbl.bind('<Enter>', on_enter)
            lbl.bind('<Leave>', on_leave)

            title = Label(frm, text='Show/Hide',bg=self.bgcolor)
            title.grid(row=2, column=0, columnspan=2, pady=(20, 0))

        def opt():
            frm = Frame(self.parent, height=90, width=60,bg=self.bgcolor)
            frm.grid_propagate(False)
            frm.grid(row=0, column=4, padx=(1, 0), pady=(1, 0))

            img = PhotoImage(file='ThisPC/top_frame/icons/options.png')
            lbl = Label(frm, image=img, text='Options', compound='top',bg=self.bgcolor)
            lbl.grid(row=0, column=0, pady=(10, 0), padx=(5, 0))
            lbl.image = img

            lbl.bind('<Enter>', on_enter)
            lbl.bind('<Leave>', on_leave)


        def on_enter(event):
            event.widget.configure(background='lightblue1')

        def on_leave(event):
            event.widget.configure(background=self.bgcolor)

        def on_leave2(event):
            event.widget.configure(background='white')

        current_frame()
        panels_frame()
        layout_frame()
        show_hide()
        opt()


class Searchbar:
    def __init__(self, parent, width):
        self.parent = parent
        self.bgcolor = '#F5F6F7'
        self.cnv_width = width

    def run(self):
        self.main_frame()
        self.arrows()
        self.frame1()

    def main_frame(self):
        self.main_frm = Frame(self.parent, width=self.cnv_width, height=32, bg=self.bgcolor)
        self.main_frm.grid_propagate(False)
        self.main_frm.grid(row=3, column=0, columnspan=350, sticky='nsew', padx=(3, 0), pady=(2, 0))
        return self.main_frm

    def arrows(self):
        frm = Frame(self.main_frm, bg=self.bgcolor)
        frm.grid(row=2, column=0, pady=(5, 0), sticky='w', rowspan=3, columnspan=2)

        imges = ['ThisPC/top_frame/icons/left.png',
                 'ThisPC/top_frame/icons/right.png',
                 'ThisPC/top_frame/icons/down.png',
                 'ThisPC/top_frame/icons/up.png']

        for index, content in enumerate(imges):
            img = PhotoImage(file=content)
            lbl = Label(frm, image=img, bg=self.bgcolor)
            if index < 2:
                lbl.grid(row=0, column=index, padx=10)
                lbl.image = img
            else:
                lbl.grid(row=0, column=index, padx=2)
                lbl.image = img

    def frame1(self):
        self.searchbar_frm = Frame(self.main_frm, height=30, width=int(self.cnv_width * 0.6), bg='white',
                                   highlightbackground='black', highlightthickness=1)
        self.searchbar_frm.grid_propagate(False)
        self.searchbar_frm.grid(row=2, column=4, sticky='nsew', columnspan=4, rowspan=3, padx=(10, 0), pady=(2, 0))

        self.searchbar_img = PhotoImage(file='ThisPC/left_frame/left_frame_icons/thispc/pc.png')
        self.searchbar_img = self.searchbar_img.subsample(x=3, y=3)
        self.searchbar_text = '  This PC'
        self.searchbar_lbl = Label(self.searchbar_frm, image=self.searchbar_img, text=self.searchbar_text,
                                   compound='left', bg='white')
        self.searchbar_lbl.grid(row=0, column=0, padx=(2, 0), pady=(3, 0))
        self.searchbar_lbl.image = self.searchbar_img

    # Work in progress
    def update_searchbar_img(self, img, txt):
        self.searchbar_img = img
        self.searchbar_text = txt
        self.searchbar_lbl.destroy()
        self.searchbar_lbl = Label(self.searchbar_frm, image=self.searchbar_img, text=self.searchbar_text)
        self.searchbar_lbl.grid(row=0, column=0)
        self.searchbar_lbl.image = self.searchbar_img
