import sqlite3


class DataBase():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER, isbn_no INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn_no):

        self.cur.execute("INSERT INTO store VALUES (NULL, ?, ?, ?, ?)",
                         (title, author, year, isbn_no))
        self.conn.commit()

    def view(self):

        self.cur.execute("SELECT * FROM store")
        rows = self.cur.fetchall()
        return rows

    def search(self, title, author, year, isbn_no):

        self.cur.execute(
            "SELECT * FROM store WHERE title=? OR author=? OR year=? OR isbn_no=? ", (title, author, year, isbn_no))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):

        self.cur.execute("DELETE FROM store WHERE id=?", (id, ))
        self.conn.commit()

    def update(self, id, title, author, year, isbn_no):

        self.cur.execute(
            "UPDATE store SET title=?, author=?, year=?, isbn_no=? WHERE id=?", (title, author, year, isbn_no, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



# update('Water Glass', 11, 9.5)
# create_table()
# delete(4)
# update(1, "Book2", "Book1_Author", 2001, 1)
# print(view())
# print(search("Book2", "Book2_Author", 2002, 2))
# print(view())
