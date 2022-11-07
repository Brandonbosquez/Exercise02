#EXERCISE 11 - INHERITANCE
#PROBLEM 1
print("PROBLEM 1 *-*")
class Publication():
    def __init__(self,name):
        self.name = name
class Book(Publication):
    def __init__(self,name,author):
        Publication.__init__(self,name)
        self.author =author


    def print_information(self):
        print(f"\nBOOK INFORMATION")
        print(f'NAME: {self.name} 'f'\nAUTHOR: {self.author}')

class Magazine(Publication):
    def __init__(self,name,chief_editor,page_count):
        Publication.__init__(self,name)
        self.chief_editor = chief_editor
        self.page_count = page_count

    def print_information(self):
        print(f"\nMAGAZINE INFORMATION")
        print(f'NAME: {self.name} 'f'\nCHIEF EDITOR: {self.chief_editor}'f'\nPAGE COUNT: {self.page_count}')

book1 = Book("Donald Duck","Aki Hyyppä")
magazine1 = Magazine("Compartment No.6","Rosa Liksom",192)

book1.print_information()
magazine1.print_information()