import tkinter as tk

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.reviews = []

class BookReviewApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Letterbookd")
        self.master.configure(bg="#808080")  # Background color

        self.books = []

        # Title
        title_frame = tk.Frame(master, bg="#ff8000")
        title_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        title_label = tk.Label(title_frame, text="Letterbookd", font=("Arial", 16, "bold"), bg="#ff8000", fg="#40bcf4")
        title_label.pack(pady=10)

        # Labels
        tk.Label(master, text="Title:", bg="#808080", fg="white").grid(row=1, column=0, sticky="w")
        tk.Label(master, text="Author:", bg="#808080", fg="white").grid(row=2, column=0, sticky="w")
        tk.Label(master, text="Year:", bg="#808080", fg="white").grid(row=3, column=0, sticky="w")
        tk.Label(master, text="Review:", bg="#808080", fg="white").grid(row=4, column=0, sticky="w")

        # Entry fields
        self.title_entry = tk.Entry(master)
        self.title_entry.grid(row=1, column=1)

        self.author_entry = tk.Entry(master)
        self.author_entry.grid(row=2, column=1)

        self.year_entry = tk.Entry(master)
        self.year_entry.grid(row=3, column=1)

        self.review_text = tk.Text(master, width=40, height=5)
        self.review_text.grid(row=4, column=1, pady=10)

        # Buttons
        self.add_button = tk.Button(master, text="Add Book", command=self.add_book, bg="#00e054", fg="white")
        self.add_button.grid(row=5, column=1, sticky="e")

        self.show_button = tk.Button(master, text="Show Reviews", command=self.show_reviews, bg="#00e054", fg="white")
        self.show_button.grid(row=5, column=0, sticky="w")

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        review = self.review_text.get("1.0", tk.END)

        new_book = Book(title, author, year)
        new_book.reviews.append(review)

        self.books.append(new_book)

        # Clear entry fields
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.review_text.delete("1.0", tk.END)

    def show_reviews(self):
        review_window = tk.Toplevel(self.master)
        review_window.title("Book Reviews")
        review_window.configure(bg="#808080")  # Background color

        for book in self.books:
            tk.Label(review_window, text=f"Title: {book.title}", bg="#808080", fg="white").pack()
            tk.Label(review_window, text=f"Author: {book.author}", bg="#808080", fg="white").pack()
            tk.Label(review_window, text=f"Year: {book.year}", bg="#808080", fg="white").pack()
            tk.Label(review_window, text="Reviews:", bg="#808080", fg="white").pack()
            for review in book.reviews:
                tk.Label(review_window, text=review, bg="#808080", fg="white").pack()
            tk.Label(review_window, text="", bg="#808080").pack()  # empty line for spacing

def main():
    root = tk.Tk()
    app = BookReviewApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
