'''
   booksdatasourcetest.py
   Kitty Tyree and Sriya Konda, 27 September 2021
'''

import booksdatasource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
#        print('in unique author\n')
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0].surname == 'Pratchett')

    def test_titleOne_noFlag(self):
#        print('in title One \n')
        books = self.data_source.books('One')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0].title == 'And Then There Were None')

    def test_emptyTitle(self):
#        print('in empty title\n')
        books = self.data_source.books(None)
        self.assertTrue(len(books) == 41)

    def test_titleGirl_yearFlag(self):
#        print('in title girl year\n')
        books = self.data_source.books('girl', 'year')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0].title == 'Schoolgirls')

    def test_titleEE_titleFlag(self):
#        print('in title EE by title\n')
        books = self.data_source.books('ee', 'title')
        self.assertTrue(len(books) == 4 )
        self.assertTrue(books[0].title == 'A Wild Sheep Chase')
        self.assertTrue(books[3].title == 'Right Ho, Jeeves')

    def test_titleAnd_randomFlag(self):
#        print('in title And randomg flag\n')
        books = self.data_source.books('and', 'apple')
        self.assertFalse(len(books) == 17)
        self.assertTrue(books[2].title == 'Girls and Sex')

    def test_unknownAuthor(self):
#        print('in unknown author\n')
        authors = self.data_source.authors('John')
        self.assertTrue(len(authors) == 0)

    def test_emptyAuthor(self):
#        print('in empty author\n')
        authors = self.data_source.authors(None)
        self.assertTrue(len(authors) == 22)
        self.assertTrue(authors[0].surname == 'Austen')

    def test_authorPE(self):
#        print('in unique PE\n')
        authors = self.data_source.authors('PE')
        self.assertTrue(len(authors) == 2)
        self.assertTrue(authors[1].given_name == 'Peggy')

    def test_author2LastNames(self):
#        print('in 2 last names \n')
        authors = self.data_source.authors('G')
        self.assertTrue(len(authors) == 6)
        self.assertTrue(authors[2].surname == 'García Márquez')
        self.assertTrue(authors[3].surname == 'Grenville Wodehouse')

    def test_noStartYear(self):
#        print('in no start year\n')
        books = self.data_source.books_between_years(None, '1938')
        self.assertTrue(len(books) == 16)
        self.assertTrue(books[0].title == 'The Life and Opinions of Tristram Shandy, Gentleman')

    def test_noEndYear(self):
#        print('in no end year\n')
        books = self.data_source.books_between_years('2000', None)
        self.assertTrue(len(books) == 9)
        self.assertTrue(books[2].title == 'All Clear')

    def test_singlYear(self):
#        print('in one year\n')
        books = self.data_source.books_between_years('1994', '1994')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0].title == 'Mirror Dance')

    def test_rangeofYears(self):
#        print('in random year\n')
        books = self.data_source.books_between_years('1985', '1990')
        self.assertTrue(len(books) == 5)
        self.assertTrue(books[3].title == 'Beloved')

    def test_emptyYears(self):
#        print('in empty year\n')
        books = self.data_source.books_between_years('1998', '2002')
        self.assertTrue(len(books) == 0)

    def test_noYears(self):
#        print('in no years\n')
        books = self.data_source.books_between_years(None,None)
        self.assertTrue(len(books) == 41)
        self.assertTrue(books[0].title == 'The Life and Opinions of Tristram Shandy, Gentleman')


if __name__ == '__main__':
    unittest.main()
