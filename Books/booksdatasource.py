#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2021

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2021.
'''

import csv

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        global listOfAllAuthors
        self.listOfAllAuthors = []
        global ListOfAllBooks
        self.listOfAllBooks = []
        file = open(books_csv_file_name)
        reader = csv.reader(file)
        for row in reader:
            title = row[0]
            pub_year = int(row[1])
            auth_string = row[2]

            authorAttributes = auth_string.split(' ')
            if len(authorAttributes) == 3:
                authorFirstName, authorLastName, authorYearsString = authorAttributes[0], authorAttributes[1], authorAttributes[2]
            if len(authorAttributes) == 4:
                authorFirstName, authorLastName, authorYearsString = authorAttributes[0], authorAttributes[1] + ' ' + authorAttributes[2], authorAttributes[3]

# Need to implement something about the book that has 2 authors :)

            authorYearsString.strip('('')')
            authorYears = authorYearsString.split('-')
            birthYear = authorYears[0]
            if len(authorYears) == 2:
                deathYear = authorYears[1]
            authorObject = Author(authorFirstName, authorLastName, birthYear, deathYear)
            # add authorObject to listOfAllAuthors
            self.listOfAllAuthors.append(authorObject)

            bookObject = Book(title, pub_year, authorObject)
            # add bookObject to listOfAllBooks
            self.listOfAllBooks.append(bookObject)
        file.close


    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        authorList = []
        searchLower = search_text.lower()

        if searchLower == '':
            authorList = BooksDataSource.listOfAllAuthors
        # search text is none, return all Author objects

        else:
            for author in BooksDataSource.listOfAllAuthors:
                if searchLower in author.surname.lower() or author.given_name.lower():
                    authorList.append(author)

        authorList.sort(key=lambda auth: (auth.suname, auth.given_name))
        # sort result List alphabetically
            #if last names are equal, sort by given name

        return authorList



    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        bookList = []
        searchLower = search_text.lower()

        if searchLower == '':
            bookList = BooksDataSource.listOfAllBooks
        # search text is none, return all book objects -- sorted alphabetically

        else:
            for book in BooksDataSource.listOfAllBooks:
                if searchLower in book.title.lower():
                    bookList.append(book)

        if sort_by == 'year':
            bookList.sort(key=lambda book: (book.publication_year, book.title))

        else: #otherwise it is null or title or random string, so do by title
            bookList.sort(key=lambda book: (book.title, book.publication_year))


        return bookList


    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''

        bookList = []
        if start_year == '': #because we instantiated publication_year as int
            startYearInt = 0 #out of range of list
        else:
            startYearInt = int(start_year)

        if end_year == '': #because we instantiated publication_year as int
            endYearInt = 2050 #out of range of list
        else:
            endYearInt = int(end_year)

        for book in BooksDataSource.listOfAllBooks:
            if startYearInt <= book.publication_year <= endYearInt:
                bookList.append(book)

        bookList.sort(key=lambda book: (book.publication_year, book.title))
        return bookList

