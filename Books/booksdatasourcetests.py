'''
   booksdatasourcetest.py
   Kitty Tyree and Sriya Kondas, 27 September 2021
'''

import booksdatasource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    def test_titleOne_noflag(self):
        books = self.data_source.books('One')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0] == Book('And Then There Were None'))
   
    def test_emptytitle(self):
        books = self.data_source.books('')
        self.assertTrue(len(books) == 41)

    def test_titleGirl_yearflag(self):
        books = self.data_source.books('girl', 'year')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0] == Book('Schoolgirls'))
 
    def test_titleEE_titleflag(self):
        books = self.data_source.books('ee', 'title')
        self.assertTrue(len(books) == 4 )
        self.assertTrue(books[0] == Book('Main Street'))
        self.assertTrue(books[3] == Book('A Wild Sheep Chase'))
  
    def test_titleAnd_randomflag(self):
        books = self.data_source.books('and', 'apple')
        self.assertFalse(len(books) == 17)
        self.assertTrue(books[2] == Book('Girls and Sex'))

    def test_unknownauthor(self):
        authors = self.data_source.authors('John')
        self.assertTrue(len(authors) == 0)
  
    def test_emptyauthor(self):
        authors = self.data_source.authors('')
        self.assertTrue(len(authors) == 22)
        self.assertTrue(authors[0] == Author('Austen', 'Jane'))
  
    def test_authorPE(self):
        authors = self.data_source.authors('PE')
        self.assertTrue(len(authors) == 2)
        self.assertTrue(authors[0] == Author('Orenstein', 'Peggy'))

    def test_author2lastnames(self):
        authors = self.data_source.authors('G')
        self.assertTrue(len(authors) == 6)
        self.assertTrue(authors[2] == Author('García Márquez', 'Gabriel'))
        self.assertTrue(authors[3] == Author('Grenville Wodehouse', 'Pelham'))
  
    def test_nostartyear(self):
        books = self.data_source.books('', '1938')
        self.assertTrue(len(books) == 16)
        self.assertTrue(books[0] == Book('The Life and Opinions of Tristram Shandy, Gentleman'))
  
    def test_noendyear(self):
        books = self.data_source.books('2000', '')
        self.assertTrue(len(books) == 9)
        self.assertTrue(books[2] == Book('All Clear'))
    
    def test_singlyear(self):
        books = self.data_source.books('1994', '1994')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0] == Book('Mirror Dance'))
    
    def test_rangeofyears(self):
        books = self.data_source.books('1985', '1990')
        self.assertTrue(len(books) == 5)
        self.assertTrue(books[3] == Book('Beloved'))
    
    def test_emptyyears(self):
        books = self.data_source.books('1998', '2002')
        self.assertTrue(len(books) == 0)
    
    def test_noyears(self):
        books = self.data_source.books('', '')
        self.assertTrue(len(books) == 41)
        self.assertTrue(books[0] == Book('The Life and Opinions of Tristram Shandy, Gentleman'))


if __name__ == '__main__':
    unittest.main()
