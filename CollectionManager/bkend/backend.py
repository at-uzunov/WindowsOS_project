from tkinter import *
from tkinter import Widget
from tkinter import filedialog
from PIL import Image, ImageTk
import io
from CollectionManager.dbase.database import Database


class Backend:
    def __init__(self, parent):
        self.parent = parent
        self.db = Database()
        self.db.books_db()
        self.db.games_db()
        self.db.movies_db()
        self.current_category = None
        self.category_holder = []
        self.new_btn = None
        self.listbox = None
        self.title_label = Label()
        self.pic_label = Label()
        self.author_label = Label()
        self.gnr_label = Label()
        self.cst_label = Label()
        self.description = Text()
        self.entry_search = Entry()
        self.entry_search_variable = StringVar()
        self.get_image = ''
        self.labels_data_search = ''

    def get_data_from_db(self):
        title_search = self.labels_data_search
        category = self.return_category()
        query = ''
        if category == 'Books':
            query = f'SELECT * FROM books WHERE title LIKE ?'
        elif category == 'Games':
            query = f'SELECT * FROM games WHERE title LIKE ?'
        elif category == 'Movies':
            query = f'SELECT * FROM movies WHERE title LIKE ?'
        self.db.curs.execute(query, (f'{title_search}',))
        result = self.db.curs.fetchone()
        #print(result)
        return result


    def on_entry_search_click(self, event):
        event.widget.delete(0, 'end')
        self.entry_search.configure(justify='left')

    def on_leave_search_entry(self, event):
        self.entry_search_variable.set('Search...')
        self.entry_search.configure(justify='right')


    def entry_listbox_data(self, event):
        var = ''
        title = self.entry_search.get()
        if self.current_category == 'Books':
            var = self.search('SELECT * FROM books WHERE title LIKE ? COLLATE NOCASE', f'%{title}%')
        elif self.current_category == 'Games':
            var = self.search('SELECT * FROM games WHERE title LIKE ? COLLATE NOCASE', f'%{title}%')
        elif self.current_category == 'Movies':
            var = self.search('SELECT * FROM movies WHERE title LIKE ? COLLATE NOCASE', f'%{title}%')
        self.listbox.configure(listvariable=var)

    def setup_labels(self):
        result = self.get_data_from_db()
        self.title_label.configure(text=result[0])
        self.author_label.configure(text=result[1])
        self.gnr_label.configure(text=result[2])
        self.cst_label.configure(text=result[3])
        self.description.delete(1.0, 'end')
        self.description.insert(END, result[4])

        try:
            self.pic_label.grid_propagate(False)

            label_width, label_height = self.pic_label.winfo_width(), self.pic_label.winfo_height()
            img = Image.open(io.BytesIO(result[-2]))
            img.thumbnail((label_width, label_height))
            tk_image = ImageTk.PhotoImage(img)
            self.pic_label.configure(image=tk_image)
            self.pic_label.image = tk_image
            self.pic_label.configure(width=142, height=152)
        except:
            img = ''
            self.pic_label.configure(text='', image='')
            self.pic_label.image = img
            self.pic_label.configure(width=20, height=10)

    def set_category(self, category):
        self.current_category = category
        print(self.current_category)

    def search(self, sqlitequery, searchitem):
        self.db.curs.execute(sqlitequery, (searchitem,))
        result = self.data_extraction()
        return result


    def listbox_books(self, sqlitequery):
        self.db.curs.execute(sqlitequery)
        result = self.data_extraction()
        return result

    def listbox_games(self, sqlitequery):
        self.db.curs.execute(sqlitequery)

        result = self.data_extraction()
        return result

    def listbox_movies(self, sqlitequery):
        self.db.curs.execute(sqlitequery)

        result = self.data_extraction()
        return result

    def get_listbox_curse_selection(self, event):
        self.listbox.selection_clear(0, 'end')
        clicked_index = self.listbox.nearest(event.y)
        if clicked_index >= 0:
            self.listbox.selection_set(clicked_index)
            # print(self.listbox.get(clicked_index)[4:].strip())
            self.labels_data_search = self.listbox.get(clicked_index)[4:].strip()
            #print(self.listbox.get(clicked_index))
        self.setup_labels()

    def data_extraction(self):
        data_set = []
        count = 0
        records = self.db.curs.fetchall()
        for i in records:
            count += 1
            data_set.append(f'[{count}]   {i[0]}')

        var = Variable(value=data_set)
        return var

    def new_btn_window(self, e):
        self.newbtnwindow = NewBtnWindow(self.parent)
        self.newbtnwindow.run()
        self.labels_setup()

        def cancel_btn_action(event):
            self.newbtnwindow.destroy()

        def check_entry_content(event):
            title = self.newbtnwindow.entry_holder[0].get().strip()
            author = self.newbtnwindow.entry_holder[1].get().strip()
            genre = self.newbtnwindow.entry_holder[2].get().strip()
            characters = self.newbtnwindow.entry_holder[3].get().strip()
            description = self.newbtnwindow.entry_holder[4].get(1.0, "end-1c").strip()
            try:
                img = self.newbtnwindow.convert_image(self.newbtnwindow.get_image)
            except:
                img = ''


            if self.current_category == 'Books':
                self.db.insert_into_books_db(title, author, genre, characters, description, img)
            elif self.current_category == 'Games':
                self.db.insert_into_games_db(title, author, genre, characters, description, img)
            elif self.current_category == 'Movies':
                self.db.insert_into_movies_db(title, author, genre, characters, description, img)
            self.listbox_data()
            #print(self.current_category)

        self.newbtnwindow.ok_btn.bind('<Button-1>', check_entry_content)
        self.newbtnwindow.cancel_btn.bind('<Button-1>', cancel_btn_action)

    def edit_btn_window(self, e):
        result = self.get_data_from_db()
        self.newbtnwindow = NewBtnWindow(self.parent)
        self.newbtnwindow.run()
        self.labels_setup()
        self.newbtnwindow.title('Edit')

        def cancel_btn_action(event):
            self.newbtnwindow.destroy()

        def inset_data_into_holders():
            for i in range(len(self.newbtnwindow.entry_holder)):
                if i < len(self.newbtnwindow.entry_holder)-1:
                    self.newbtnwindow.entry_holder[i].insert(0, result[i])
                else:
                    self.newbtnwindow.entry_holder[i].insert(1.0, result[i])

        inset_data_into_holders()

        def check_entry_content(event):
            title = self.newbtnwindow.entry_holder[0].get()
            author = self.newbtnwindow.entry_holder[1].get()
            genre = self.newbtnwindow.entry_holder[2].get()
            characters = self.newbtnwindow.entry_holder[3].get()
            description = self.newbtnwindow.entry_holder[4].get(1.0, "end-1c")
            try:
                img = self.newbtnwindow.convert_image(self.newbtnwindow.get_image)
            except:
                img = None
            if self.current_category == 'Books':
                self.db.update_into_books_db(title, author, genre, characters, description, img, result[-1])
            elif self.current_category == 'Games':
                self.db.update_into_games_db(title, author, genre, characters, description, img, result[-1])
            elif self.current_category == 'Movies':
                self.db.update_into_movies_db(title, author, genre, characters, description, img, result[-1])
            self.listbox_data()

        self.newbtnwindow.ok_btn.bind('<Button-1>', check_entry_content)
        self.newbtnwindow.cancel_btn.bind('<Button-1>', cancel_btn_action)

    def return_category(self):
        return self.current_category

    def on_enter(self, e):
        e.widget.configure(bg='orange')

    def on_leave(self, e):
        e.widget.configure(bg='cadetblue')
 
    def on_leave_selected(self, e):
        e.widget.configure(bg='orange')

    def binds(self):
        for i in self.category_holder:
            i.bind('<Enter>', self.on_enter)
            i.bind('<Leave>', self.on_leave)
            i.bind('<Button-1>', self.style_category_selection)

    def labels_setup(self):
        get_category = self.return_category()
        if get_category == "Books":
            self.books_labels_setup()
        elif get_category == 'Games':
            self.games_labels_setup()
        elif get_category == 'Movies':
            self.movies_labels_setup()

    def style_category_selection(self, e):
        for i in self.category_holder:
            i.configure(relief='flat', bg='cadetblue', fg='white')
            i.bind('<Leave>', self.on_leave)  
        e.widget.configure(relief='sunken', bg='orange', fg='black')
        e.widget.bind('<Leave>', self.on_leave_selected)
        txt = e.widget.cget('text')
        self.set_category(txt)
        self.configure_label_frames(self.current_category)
        self.listbox_data()

    def configure_label_frames(self, category):
        if category == 'Books':
            parent_widget_name = self.cst_label.winfo_parent()
            parent_name = Widget.nametowidget(self.parent, parent_widget_name)
            parent_name.configure(text='Main Characters: ')

            parent_widget_name = self.author_label.winfo_parent()
            parent_name = Widget.nametowidget(self.parent, parent_widget_name)
            parent_name.configure(text='Author: ')
        elif category == 'Games':
            parent_widget_name = self.author_label.winfo_parent()
            parent_name = Widget.nametowidget(self.parent, parent_widget_name)
            parent_name.configure(text='Company: ')
        elif category == 'Movies':
            parent_widget_name = self.author_label.winfo_parent()
            parent_name = Widget.nametowidget(self.parent, parent_widget_name)
            parent_name.configure(text='Director: ')

    def delete_btn(self, event):
        result = self.get_data_from_db()
        cat = self.return_category()
        if cat == 'Books':
            self.db.curs.execute('DELETE FROM books WHERE id = ?', (result[-1],))
            self.db.con.commit()
        elif cat == 'Games':
            self.db.curs.execute('DELETE FROM games WHERE id = ?', (result[-1],))
            self.db.con.commit()
        elif cat == 'Movies':
            self.db.curs.execute('DELETE FROM movies WHERE id = ?', (result[-1],))
            self.db.con.commit()
        self.listbox_data()

    def listbox_data(self):
        var = ''
        if self.current_category == 'Books':
            var = self.listbox_books('SELECT * from books')
        elif self.current_category == 'Games':
            var = self.listbox_games('SELECT * from games')
        elif self.current_category == 'Movies':
            var = self.listbox_movies('SELECT * from movies')
        self.listbox.selection_clear(0, END)
        self.listbox.configure(listvariable=var)

    def books_labels_setup(self):
        lbls = ['Book title: ', 'Book author: ', 'Book genre: ', 'Main Characters: ', 'Book description: ',
                'Insert image: ']

        for index, content in enumerate(lbls):
            self.newbtnwindow.lbl_holder[index].configure(text=content)

    def games_labels_setup(self):
        lbls = ['Game title: ', 'Company name: ', 'Game Genre: ', 'Main characters: ',
                'Game description: ', 'Insert image: ']
        for index, content in enumerate(lbls):
            self.newbtnwindow.lbl_holder[index].configure(text=content)

    def movies_labels_setup(self):
        lbls = ['Movie title: ', 'Director: ', 'Movie genre: ', 'Main Characters: ', 'Movie description:',
                'Insert image: ']

        for index, content in enumerate(lbls):
            self.newbtnwindow.lbl_holder[index].configure(text=content)

    def init_category(self, category):
        if category == 'Books':
            self.category_holder[0].configure(relief='sunken', bg='orange', fg='black')
            self.category_holder[0].bind('<Leave>', self.on_leave_selected)
            self.current_category = 'Books'
            parent_widget_name = self.cst_label.winfo_parent()
            parent_name = Widget.nametowidget(self.parent, parent_widget_name)
            parent_name.configure(text='Main Characters: ')
        elif category == 'Games':
            self.category_holder[1].configure(relief='sunken', bg='orange', fg='black')
            self.category_holder[1].bind('<Leave>', self.on_leave_selected)
            self.current_category = 'Games'

        elif category == 'Movies':
            self.category_holder[2].configure(relief='sunken', bg='orange', fg='black')
            self.category_holder[2].bind('<Leave>', self.on_leave_selected)
            self.current_category = 'Movies'
        self.listbox_data()


class NewBtnWindow(Toplevel):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.lbl_holder = []
        self.entry_holder = []
        self.ok_btn = None
        self.cancel_btn = None
        self.get_image = ''
        self.wm_transient(self.parent)

    def setup(self):
        self.geometry(
            f'400x350+{int(self.parent.winfo_screenwidth() * 0.3)}+{int(self.parent.winfo_screenheight() * 0.3)}')
        self.configure(bg='white')
        self.title('New')

    def filedialogs(self):
        self.get_image = filedialog.askopenfilename(title=' SELECT IMAGE', filetypes=(("png", "*.png"), ("jpg", "*.jpg")))

    # (2/2)
    def convert_image(self, filename):
        with open(filename, 'rb') as file:
            photo_image = file.read()
        return photo_image

    def ui(self):
        lbls = ['None ', 'None ', 'None ', 'None ', 'None',
                'None ']
        lbls_len = len(lbls) - 1
        for index, content in enumerate(lbls):
            lbl = Label(self, text=content, width=15, anchor='e', bg='white')
            lbl.grid(row=index, column=0, padx=(10, 0), pady=(10, 0), sticky='e')
            self.lbl_holder.append(lbl)

            if index < lbls_len - 1:
                entr = Entry(self, width=40, borderwidth=1, highlightbackground='lightskyblue4', highlightthickness=2)
                entr.grid(row=index, column=1, padx=(10, 0), pady=(10, 0))
                self.entry_holder.append(entr)
            elif index == lbls_len:
                description_entry = Text(self, width=30, height=6, borderwidth=1, highlightbackground='lightskyblue4', highlightthickness=2)
                description_entry.grid(row=4, column=1, padx=(10, 0), pady=(10, 0), columnspan=30)
                self.entry_holder.append(description_entry)
            else:
                btn = Button(self, text='Select image', command=self.filedialogs, width=20, bg='lightskyblue4', fg='white')
                btn.grid(row=lbls_len, column=1, padx=(10, 0), sticky='nw', pady=(10,0))

        self.entry_holder[0].focus_force()

        self.ok_btn = Button(self, text='Ok', width=10, bg='lightskyblue4', fg='white')
        self.ok_btn.grid(row=lbls_len + 1, column=0, pady=(30, 0), padx=(80, 0), columnspan=2, sticky='nw')

        self.cancel_btn = Button(self, text='Close', width=10, bg='lightskyblue4', fg='white')
        self.cancel_btn.grid(row=lbls_len + 1, column=1, pady=(30, 0), padx=(0, 50), sticky='e')

    def run(self):
        self.setup()
        self.ui()
