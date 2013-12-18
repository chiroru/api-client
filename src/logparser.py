# -*- coding: utf-8 -*-

from request import Request

__filename__ = "test.log"

def execute():
    logfile = open(__filename__, "r")
    
    result = {}
    
    for row in logfile:
        input = row.split(" ")[2].split(",")
        if result.get(input[1]) != None:
            r = result.get(input[1])
            r.countUp(input[0])
        else:
            r = Request(input[1], input[0])
            result[r.uri] = r
    
        for uri,request in result.iteritems():
            print uri, request.getSum(), request.getAverage()
            
    logfile.close()

if __name__ == "__main__":
    execute()