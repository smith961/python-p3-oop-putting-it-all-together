#!/usr/bin/env python3

class Book:
    #constructor method of the class
    #self: reference to the instance of the class. Allows access and modify attributes & methods of the object within the class.
    #title & page_count: These are parameters that the constructor expects.
    def __init__(self, title, page_count):
        #self.title = title: This line assigns the value of the title parameter to the title attribute of the object.
        #self.page_count = page_count: this line assigns the value of the page_count parameter to the page_count attribute of the object.
        #: <--this is for my setter
        self.title = title
        self.page_count = page_count

    def get_page_count(self):
        return self._page_count
    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
    
        