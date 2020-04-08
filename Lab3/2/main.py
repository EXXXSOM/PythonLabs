from Library import Library
from Book import Book
from Taggable import Taggable

library = Library(1, '51 Some str., NY')
library += Book('Leo Tolstoi', 'War and Peace')
library += Book('Charles Dickens', 'David Copperfield')

#out books
for book in library:
    print(book)
    print(book.tag())
