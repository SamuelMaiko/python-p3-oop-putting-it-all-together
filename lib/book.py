#!/usr/bin/env python3

class Book:
    def __init__(self,title, page_count):
        self.title=title
        self.page_count=page_count

    def get_page(self):
        return self.page_count
    def set_page(self,page):
        if type(page) !=int:
            print("page_count must be an integer")
        else:
            self.page_count=page
    page_count=property(get_page, set_page,)
    
    def turn_page(self):
        self.page_count+=1
        print("Flipping the page...wow, you read fast!")