from tkinter import *

from CollectionManager.bkend.backend import Backend


class CManager_Ui(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.backend = Backend(parent)

    def setup(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.geometry(f'{720}x{520}+{int(screen_width * 0.23)}+{int(screen_height * 0.18)}')
        self.configure(background='white')
        self.title('Collection Manager')

        self.wm_transient(self.parent)

    def btns(self):
        self.backend.new_btn = Button(self, text='New', width=8, bg='lightskyblue4', fg='white')
        self.backend.new_btn.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))
        self.backend.new_btn.bind('<Button-1>', self.backend.new_btn_window)

        self.edit_btn = Button(self, text='Edit', width=8, bg='lightskyblue4', fg='white')
        self.edit_btn.bind('<Button-1>', self.backend.edit_btn_window)
        self.edit_btn.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))

        self.delete_btn = Button(self, text='Delete', width=8, bg='lightskyblue4', fg='white')
        self.delete_btn.bind('<Button-1>', self.backend.delete_btn)
        self.delete_btn.grid(row=0, column=2, padx=(10, 0), pady=(10, 0))

    def right_content(self):
        def title():
            title_label = LabelFrame(self, text='Title')
            title_label.grid(row=5, column=5, padx=(50, 0),
                             pady=(10, 0), rowspan=3, sticky='nw', columnspan=60)
            self.backend.title_label = Label(title_label, text='', width=42, wraplength=420, font=('Arial Bold Italic', 12))
            self.backend.title_label.grid(row=0, column=0, columnspan=30)

        def picture():
            self.backend.pic_label = Label(self, width=20, height=10)
            self.backend.pic_label.grid(row=8, column=5, rowspan=10, columnspan=20, padx=(50, 0), pady=(10, 0))

        def author():
            author_label = LabelFrame(self, text='Author')
            author_label.grid(row=8, column=26, padx=(20, 0), pady=(10, 0), columnspan=40, sticky='nw')

            self.backend.author_label = Label(author_label, text="", width=35, wraplength=200)
            self.backend.author_label.pack()

        def genre():
            genre_label = LabelFrame(self, text='Genre')
            genre_label.grid(row=9, column=26, padx=(20, 0), pady=(5, 0), columnspan=40, sticky='nw')

            self.backend.gnr_label = Label(genre_label, text="", width=35, wraplength=200)
            self.backend.gnr_label.pack()

        def cast():
            cast_label = LabelFrame(self, text='Cast')
            cast_label.grid(row=18, column=5, sticky='nw', padx=(50, 0), pady=(10, 0), columnspan=70)

            self.backend.cst_label = Label(cast_label, width=60, height=5, wraplength=420)
            self.backend.cst_label.pack()

        def description():
            description_label = LabelFrame(self, text='Description')
            description_label.grid(row=19, column=5, sticky='nw', padx=(50, 0), pady=(10, 0), columnspan=60)

            self.backend.description = Text(description_label, width=53, height=5)
            self.backend.description.pack()

        title()
        picture()
        author()
        genre()
        cast()
        description()

    def content(self):
        self.backend.entry_search = Entry(self, width=35, borderwidth=1,
                                          highlightbackground='lightskyblue4',
                                          highlightthickness=2,
                                          textvariable=self.backend.entry_search_variable, justify='right')
        self.backend.entry_search.bind('<KeyRelease>', self.backend.entry_listbox_data)
        self.backend.entry_search.bind('<Button-1>', self.backend.on_entry_search_click)
        self.backend.entry_search.bind('<FocusOut>', self.backend.on_leave_search_entry)
        self.backend.entry_search_variable.set('Search...')
        self.backend.entry_search.grid(row=5, column=0, columnspan=4, padx=(10, 0), pady=(10, 0))

        var = Variable()

        self.backend.listbox = Listbox(self, width=35, height=26, listvariable=var, borderwidth=1,
                                       highlightbackground='lightskyblue4', highlightthickness=2)
        self.backend.listbox.bind('<Button-1>', self.backend.get_listbox_curse_selection)
        self.backend.listbox.grid(row=6, column=0, columnspan=4, rowspan=30, padx=(10, 0), pady=(10, 0))

    def categories(self):
        lbl_width = 8
        lbl_pady = (2, 0)
        hlder = Frame(self, width=250, height=28, borderwidth=1,
                      highlightbackground='lightskyblue4', highlightthickness=2)
        hlder.grid_propagate(False)
        hlder.grid(row=0, column=40, rowspan=3, columnspan=30, pady=(10, 0))

        def books_fnct():
            books_lbl = Label(hlder, text='Books', bg='cadetblue', width=lbl_width, fg='white')
            books_lbl.grid(row=0, column=0, padx=(24, 0), pady=lbl_pady)
            self.backend.category_holder.append(books_lbl)

        def games_fnct():
            games_lbl = Label(hlder, text='Games', bg='cadetblue', width=lbl_width, fg='white')
            games_lbl.grid(row=0, column=1, padx=(10, 0), pady=lbl_pady)
            self.backend.category_holder.append(games_lbl)

        def movies_fnct():
            movies_lbl = Label(hlder, text='Movies', bg='cadetblue', width=lbl_width, fg='white')
            movies_lbl.grid(row=0, column=2, padx=(10, 0), pady=lbl_pady)
            self.backend.category_holder.append(movies_lbl)

        books_fnct()
        games_fnct()
        movies_fnct()
        self.backend.binds()

    def run(self):
        self.setup()
        self.btns()
        self.right_content()
        self.categories()
        self.content()
        self.backend.init_category('Books')
