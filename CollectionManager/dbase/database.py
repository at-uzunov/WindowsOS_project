import sqlite3


class Database:
    def __init__(self):
        self.conn_db()

    def conn_db(self):
        self.con = sqlite3.connect('collection_manager_database.db')
        self.curs = self.con.cursor()

    def books_db(self):
        self.curs.execute('CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT, genre TEXT, characters TEXT, '
                          'description TEXT, photo BLOB, id INTEGER PRIMARY KEY AUTOINCREMENT)')
        self.con.commit()

    def games_db(self):
        self.curs.execute('CREATE TABLE IF NOT EXISTS games(title TEXT, author TEXT, genre TEXT, characters TEXT, '
                          'description TEXT, photo BLOB, id INTEGER PRIMARY KEY AUTOINCREMENT)')
        self.con.commit()

    def movies_db(self):
        self.curs.execute('CREATE TABLE IF NOT EXISTS movies(title TEXT, author TEXT, genre TEXT, characters TEXT, '
                          'description TEXT, photo BLOB, id INTEGER PRIMARY KEY AUTOINCREMENT)')
        self.con.commit()

    def insert_into_books_db(self, title, author, genre, characters, description, photo):
        self.curs.execute('INSERT OR IGNORE INTO books(title, author, genre, characters, description, photo)'
                          'SELECT ?, ?, ?, ?, ?, ?'
                          'WHERE NOT EXISTS (SELECT 1 FROM books where title = ?)'
                          , (title, author, genre, characters, description, photo, title))
        self.con.commit()

    def insert_into_games_db(self, title, author, genre, characters, description, photo):
        self.curs.execute('INSERT OR IGNORE INTO games(title, author, genre, characters, description, photo)'
                          'SELECT ?, ?, ?, ?, ?, ?'
                          'WHERE NOT EXISTS (SELECT 1 FROM games where title = ?)'
                          , (title, author, genre, characters, description, photo, title))
        self.con.commit()

    def insert_into_movies_db(self, title, author, genre, characters, description, photo):
        self.curs.execute('INSERT OR IGNORE INTO movies(title, author, genre, characters, description, photo)'
                          'SELECT ?, ?, ?, ?, ?, ?'
                          'WHERE NOT EXISTS (SELECT 1 FROM movies where title = ?)'
                          , (title, author, genre, characters, description, photo, title))
        self.con.commit()

    def update_into_books_db(self, title, author, genre, characters, description, photo, id):
        if photo != None:
            self.curs.execute(
                'UPDATE books SET title = ?, author = ?, genre = ?, characters = ?, description = ?, photo = ? '
                'WHERE id = ?',
                (title, author, genre, characters, description, photo, id))
            self.con.commit()
        else:
            self.curs.execute(
                'UPDATE books SET title = ?, author = ?, genre = ?, characters = ?, description = ?'
                'WHERE id = ?',
                (title, author, genre, characters, description, id))
            self.con.commit()

    def update_into_games_db(self, title, author, genre, characters, description, photo, id):
        if photo != None:
            self.curs.execute(
                'UPDATE games SET title = ?, author = ?, genre = ?, characters = ?, description = ?, photo = ? '
                'WHERE id = ?',
                (title, author, genre, characters, description, photo, id))
            self.con.commit()
        else:
            self.curs.execute(
                'UPDATE games SET title = ?, author = ?, genre = ?, characters = ?, description = ?'
                'WHERE id = ?',
                (title, author, genre, characters, description, id))
            self.con.commit()

    def update_into_movies_db(self, title, author, genre, characters, description, photo, id):
        if photo != None:
            self.curs.execute(
                'UPDATE movies SET title = ?, author = ?, genre = ?, characters = ?, description = ?, photo = ? '
                'WHERE id = ?',
                (title, author, genre, characters, description, photo, id))
            self.con.commit()
        else:
            self.curs.execute(
                'UPDATE movies SET title = ?, author = ?, genre = ?, characters = ?, description = ?'
                'WHERE id = ?',
                (title, author, genre, characters, description, id))
            self.con.commit()