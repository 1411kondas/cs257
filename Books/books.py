import booksdatasource
import argparse



def books_print(titles):
    for book in titles:
        print(book)

def authors_print(name)
    for author in name:
        print(author)
           
def books_between_years_print(books_from_years):
    for book in books_from_years:
        print(book)
        
def main()
  data_source = booksdatasource.BooksDataSource('books1.csv')

  parser = argparse.ArgumentParser(description='Search for books based on different specifications')
  mainFunctionGroup = parser.add_mutually_exclusive_group()

  mainFunctionGroup.add_argument('--ftitle', metavar='SEARCH_TEXT', help="Search for books by title", #use to specify which command-line options the program is willing to accept.
                    type=str)

  mainFunctionGroup.add_argument('--fauth', metavar='SEARCH_TEXT', help="Search for books by author", #use to specify which command-line options the program is willing to accept.
                    type=str)

  mainFunctionGroup.add_argument('--fyears', metavar='YEAR', help="Search for books by publication year", #use to specify which command-line options the program is willing to accept.
                    type=str, nargs=2)

  searchGroup= parser.add_mutually_exclusive_group()

  searchGroup.add_argument('-y', '--year', help='sort results by publication year *ONLY FOR FTITLE', action='store_true')
  searchGroup.add_argument('-a', '--alpha', help='sort results by author *ONLY FOR FTITLE', action='store_true') #just for looks, really unfunctional...

  args = parser.parse_args()

  if args.ftitle: # call books
      if args.year:
          list_books = data_source.books(args.ftitle, 'year')
          books_print(list_books)
      else:
          list_books = data_source.books(args.ftitle)
          books_print(list_books)

  if args.fauth: #call authors
      list_authors = data_source.authors(args.fauth)
      authors_print(list_authors)

  if args.fyears: #call books_between_years
      if args.fyears[0] == 'None':
          start_year = None
      else:
          start_year = args.fyears[0]

      if args.fyears[1] == 'None':
          end_year = None
      else:
          end_year = args.fyears[1]

      if (start_year != None) and (end_year != None):
          if int(args.fyears[1]) >= int(args.fyears[0]):
              start_year = args.fyears[0]
              end_year = args.fyears[1]
          else:
              start_year = args.fyears[1]
              end_year = args.fyears[0]
      book_years_list = data_source.books_between_years(start_year, end_year)
      books_between_years_print(book_years_list)
      

        
        
        
        
main()        
        
