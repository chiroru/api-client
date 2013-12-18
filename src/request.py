# -*- coding: utf-8 -*-

class Request():
    
    def __init__(self, uri, elapsed):
        self.uri = uri
        self.sum = int(elapsed)
        self.count = int(1)

    def countUp(self, elapsed):
        self.sum = self.sum + int(elapsed)
        self.count = self.count + 1
        
    def getSum(self):
        return self.sum 
    
    def getAverage(self):
        return self.sum/self.count