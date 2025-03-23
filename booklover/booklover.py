import pandas as pd

class BookLover():
    def __init__(self, name, email, fav_genre, num_books = 0, 
                 book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        
        if not book_name in list(self.book_list['book_name']):
            
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
            self.num_books += 1
        
        else:
            pass

    def has_read(self, book_name):
        return book_name in list(self.book_list['book_name'])
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]

if __name__ == "__main__":
    book_lover_1 = BookLover("Jim","jim8zc@virgina.edu","fantasy")
    book_lover_1.add_book("Great Gatsby", 4)
    print("Has Read Great Gatsby:", book_lover_1.has_read("Great Gatsby"))
    print("Has Read The Invisible Man:", book_lover_1.has_read("The Invisible Man"))
    print("Books Read:", book_lover_1.num_books_read())
    print("Favorite Books:\n", book_lover_1.fav_books())

    

    