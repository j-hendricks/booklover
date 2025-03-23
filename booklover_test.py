import unittest 
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        book_lover_1 = BookLover("Jim","jim8zc@virgina.edu","fantasy")
        book_lover_1 = BookLover("Jim","jim8zc@virgina.edu","fantasy")
        book_lover_1.add_book("Great Gatsby", 4)
        expected = 1
        self.assertEqual(book_lover_1.has_read("Great Gatsby"),expected)
    
    def test_2_add_book(self):
        book_lover_1 = BookLover("Jim","jim8zc@virgina.edu","fantasy")
        book_lover_1.add_book("Great Gatsby", 4)
        book_lover_1.add_book("Great Gatsby", 4)
        expected = 1
        self.assertEqual(book_lover_1.num_books_read(),expected)
        
    def test_3_has_read(self):
        book_lover_1 = BookLover("Jim","jim8zc@virgina.edu","fantasy")
        book_lover_1.add_book("Great Gatsby", 4)
        expected = True
        self.assertEqual(book_lover_1.has_read("Great Gatsby"),expected)
        
    def test_4_has_read(self):
        book_lover_1 = BookLover("Jim","jim8zc@virgina.edu","fantasy")
        book_lover_1.add_book("Great Gatsby", 4)
        expected = False
        self.assertEqual(book_lover_1.has_read("Tale of Two Cities"),expected)  
        
    def test_5_num_books_read(self): 
        book_lover_1 = BookLover("Jim","jim8zc@virgina.edu","fantasy")
        book_lover_1.add_book("Great Gatsby", 4)
        book_lover_1.add_book("Tale of Two Cities", 2)
        expected = 2
        self.assertEqual(book_lover_1.num_books_read(),expected)  
        
    def test_6_fav_books(self):
        book_lover_1 = BookLover("Jim","jim8zc@virgina.edu","fantasy")
        book_lover_1.add_book("Great Gatsby", 4)
        book_lover_1.add_book("Tale of Two Cities", 2)
        book_lover_1.add_book("Catch 22",5)
        expected = 2
        self.assertEqual(book_lover_1.fav_books().shape[0],expected) 

if __name__ == "__main__":
    unittest.main(verbosity=3)