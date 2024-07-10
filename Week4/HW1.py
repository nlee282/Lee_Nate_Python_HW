class Pet:
    def init(self, name): # def __init__(self, name):
        self.name = name
    
    def introduce(): # need to pass in self: def introduce(self):
        print("Hello, I am ", self.name)