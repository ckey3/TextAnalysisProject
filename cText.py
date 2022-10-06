
class text:
    '''analyze text using stats'''
    def __init__(self, filename):
        self.fname = filename
        with open(self.fname) as f:
            self.lines = f.readlines()

        
#findes how many lines in file
    def fileLength(self):
        n = len(self.lines)
        
        return(n)
