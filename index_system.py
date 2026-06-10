import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

# BOOK CLASS

class Book:

    def __init__(self, index_id, title, author):
        self.__index_id = index_id
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def index_id(self):
        return self.__index_id

    def get_record(self):
        return (
            f"{self.__index_id}: "
            f"{self.__title}, "
            f"{self.__author}"
        )

# INDEX MANAGER

class LibraryIndexer:

    def __init__(self):
        self.books = []

    def clear(self):
        self.books.clear()

    def load_file(self, filename):

        self.clear()

        with open(filename, "r", encoding="utf-8") as file:

            for count, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                if " - " in line:

                    title, author = line.split(
                        " - ",
                        maxsplit=1
                    )

                else:
                    title = line
                    author = "Unknown"

                index = f"prog{count:02}"

                self.books.append(
                    Book(
                        index,
                        title.strip(),
                        author.strip()
                    )
                )

    def search(self, keyword):

        keyword = keyword.lower()

        return [

            book

            for book in self.books

            if keyword in book.title.lower()
            or keyword in book.author.lower()

        ]

    def save_output(self, filename):

        with open(filename, "w", encoding="utf-8") as file:

            for book in self.books:

                file.write(
                    book.get_record() + "\n"
                )

    def get_count(self):
        return len(self.books)

# GUI

class LibraryGUI:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "College Library Index System"
        )

        self.root.geometry("1000x700")

        self.indexer = LibraryIndexer()

        self.input_file = None

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="College Library Index System",
            font=("Arial", 18, "bold")
        )

        title.pack(pady=10)

        top_frame = tk.Frame(self.root)
        top_frame.pack(fill="x")

        tk.Button(
            top_frame,
            text="Load File",
            command=self.load_file
        ).pack(side="left", padx=5)

        tk.Button(
            top_frame,
            text="Generate Index",
            command=self.generate_index
        ).pack(side="left", padx=5)

        tk.Button(
            top_frame,
            text="Export File",
            command=self.export_file
        ).pack(side="left", padx=5)

        tk.Label(
            top_frame,
            text="Search:"
        ).pack(side="left", padx=10)

        self.search_entry = tk.Entry(
            top_frame,
            width=25
        )

        self.search_entry.pack(side="left")

        tk.Button(
            top_frame,
            text="Go",
            command=self.search_books
        ).pack(side="left", padx=5)

        middle_frame = tk.Frame(self.root)
        middle_frame.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.output_box = tk.Text(
            middle_frame,
            width=90,
            height=30
        )

        self.output_box.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            middle_frame,
            command=self.output_box.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.output_box.config(
            yscrollcommand=scrollbar.set
        )

        self.status_label = tk.Label(
            self.root,
            text="No file loaded.",
            anchor="w"
        )

        self.status_label.pack(
            fill="x",
            pady=5
        )

    def load_file(self):

        self.input_file = filedialog.askopenfilename(
            filetypes=[
                ("Text Files", "*.txt")
            ]
        )

        if self.input_file:

            self.status_label.config(
                text=f"Loaded: {Path(self.input_file).name}"
            )

    def generate_index(self):

        if not self.input_file:

            messagebox.showerror(
                "Error",
                "Please load a file."
            )

            return

        try:

            self.indexer.load_file(
                self.input_file
            )

            self.display_books(
                self.indexer.books
            )

            self.status_label.config(
                text=f"{self.indexer.get_count()} books indexed."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def display_books(self, books):

        self.output_box.delete(
            "1.0",
            tk.END
        )

        for book in books:

            self.output_box.insert(
                tk.END,
                book.get_record() + "\n"
            )

    def search_books(self):

        keyword = (
            self.search_entry
            .get()
            .strip()
        )

        if keyword == "":

            self.display_books(
                self.indexer.books
            )

            return

        results = self.indexer.search(
            keyword
        )

        self.display_books(results)

    def export_file(self):

        if not self.indexer.books:

            messagebox.showerror(
                "Error",
                "No records available."
            )

            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt")
            ]
        )

        if filename:

            self.indexer.save_output(
                filename
            )

            messagebox.showinfo(
                "Success",
                "Indexed file saved."
            )

# MAIN

root = tk.Tk()

app = LibraryGUI(root)

root.mainloop()