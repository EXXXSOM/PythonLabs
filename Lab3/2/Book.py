from Taggable import Taggable

class Book(Taggable):
    count = 0

    def __init__(self, author, name):
        if name == '' or author == '':
            raise ValueError('Error author!')
        else:
            Book.count += 1
            self.__name = name
            self.__author = author
            self.__code = Book.count

    def tag(self):
        lst = []
        words = self.__name.split()
        for word in words:
            if word.istitle():
                lst.append(word)
        return lst

    def __str__(self):
        return "[%d] %s '%s'" % ( self.__code, self.__author, self.__name)
