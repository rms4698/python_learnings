"""
A program to store the book information
    Title, Author, Year, ISBN

User can:
1. View all records
2. Search an entry
3. Add an entry
4. Delete an entry
5. Update an entry
6. Close

"""

from tkinter import *
from BackEnd import DataBase

""" Helper functions """


class Window():

    def __init__(self):

        self.database = DataBase('BookStore.db')
        self.window = Tk()
        self.window.wm_title("Book Store")

        title_label = Label(self.window, text="Title")
        title_label.grid(row=0, column=0)

        self.title = StringVar()
        self.title_entry = Entry(self.window, textvariable=self.title)
        self.title_entry.grid(row=0, column=1)

        author_label = Label(self.window, text="Author")
        author_label.grid(row=0, column=2)

        self.author = StringVar()
        self.author_entry = Entry(self.window, textvariable=self.author)
        self.author_entry.grid(row=0, column=3)

        year_label = Label(self.window, text="Year")
        year_label.grid(row=1, column=0)

        self.year = StringVar()
        self.year_entry = Entry(self.window, textvariable=self.year)
        self.year_entry.grid(row=1, column=1)

        isbn_label = Label(self.window, text="ISBN")
        isbn_label.grid(row=1, column=2)

        self.isbn_no = StringVar()
        self.isbn_entry = Entry(self.window, textvariable=self.isbn_no)
        self.isbn_entry.grid(row=1, column=3)

        row = 2

        self.list_box = Listbox(self.window, height=6, width=35)
        self.list_box.grid(row=row, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(self.window)
        sb1.grid(row=row, column=2, rowspan=6)

        self.list_box.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list_box.yview)

        self.list_box.bind('<<ListboxSelect>>', self.get_selected_row)

        column = 3
        view_all = Button(self.window, text="View all",
                          width=12, command=self.view_command)
        view_all.grid(row=3, column=3)

        search_button = Button(self.window, text="Search Entry",
                               width=12, command=self.search_command)
        search_button.grid(row=4, column=3)

        """ Adding an entry """
        add = Button(self.window, text="Add entry",
                     width=12, command=self.add_command)
        add.grid(row=5, column=3)

        update = Button(self.window, text="Update Selected",
                        width=12, command=self.update_selected)
        update.grid(row=6, column=3)

        delete = Button(self.window, text="Delete Selected",
                        width=12, command=self.delete_selected)
        delete.grid(row=7, column=3)

        close = Button(self.window, text="Close", width=12,
                       command=self.window.destroy)
        close.grid(row=8, column=3)


    def get_year(self):
        try:
            return int(self.year.get())
        except ValueError:
            return 0

    def get_isbn_no(self):
        try:
            return int(self.isbn_no.get())
        except ValueError:
            return 0

    def get_selected_row(self, event):
        try:
            global selected_row
            index = self.list_box.curselection()[0]
            selected_row = self.list_box.get(index)
            self.title_entry.delete(0, END)
            self.title_entry.insert(END, selected_row[1])
            self.author_entry.delete(0, END)
            self.author_entry.insert(END, selected_row[2])
            self.year_entry.delete(0, END)
            self.year_entry.insert(END, str(selected_row[3]))
            self.isbn_entry.delete(0, END)
            self.isbn_entry.insert(END, str(selected_row[4]))

            return selected_row
        except IndexError:
            pass

    def view_command(self):
        self.list_box.delete(0, END)
        entries = self.database.view()
        for entry in entries:
            self.list_box.insert(END, entry)

    def add_command(self):
        self.list_box.delete(0, END)
        self.database.insert(self.title.get(), self.author.get(),
                             int(self.year.get()), int(self.isbn_no.get()))
        self.list_box.insert(END, (self.title.get(), self.author.get(),
                                   int(self.year.get()), int(self.isbn_no.get())))

    def search_command(self):
        entries = self.database.search(self.title.get(), self.author.get(),
                                       self.get_year(), self.get_isbn_no())
        self.list_box.delete(0, END)
        for entry in entries:
            self.list_box.insert(END, entry)

    def delete_selected(self):
        self.database.delete(selected_row[0])

    def update_selected(self):
        self.database.update(selected_row[0], self.title.get(),
                             self.author.get(), self.get_year(), self.get_isbn_no())

window = Window()
window.window.mainloop()
