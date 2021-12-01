import sys

class FASTACountPlugin:
    def input(self, filename):
        self.fastafile = open(filename, 'r')

    def run(self):
        self.count = 0
        for line in self.fastafile:
           if line.startswith('>'):
              self.count = self.count+1

    
    def output(self, filename):
        print("TOTAL SEQUENCES: "+str(self.count))
