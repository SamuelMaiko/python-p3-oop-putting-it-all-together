#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand=brand
        self.size=size

    def get_size(self):
        return self.size
    def set_size(self,size):
        if type(size) !=int:
            print("size must be an integer")
        else:
            self.size=size
    page_count=property(get_size, set_size,)

    def repair(self):
        print("The shoe has been repaired")
        self.condition='New'