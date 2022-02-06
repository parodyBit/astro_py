
class Tokens:
    string = []
    delimiters = []
    position = int()

    def __init__(self, string,  *args):
        for arg in args:
            self.delimiters.append(arg)
        for c in string:
            self.string.append(c)
        self.position = 0


    def next_token(self):
        self.next_token(self.delimiters)


    def next_token(self, delimiters):
        token = ''
        while self.position < self.string.__sizeof__() and self.isDelimiter(self.string[self.position],delimiters):
            self.position += 1
        while self.position < self.string.__sizeof__() and self.isDelimiter(self.string[self.position],delimiters) == False:
            self.position += 1
            token = token + self.string[self.position-1]
        if token.__sizeof__() == 0:
            return None
        return token

    def isDelimiter(self, char, delimiters):
        for c in delimiters:
            if char == c:
                return True
        return False