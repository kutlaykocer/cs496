#!/usr/bin/python
import math
import time
import threading

class Sketch:
    matrix = [[]]
    rowSize = 0
    columnSize = 0
    
    def __init__(self, size):
        self.rowSize = size
        self.columnSize = 2 ** size #more faster than pow and return int value
        self.matrix = [[0 for i in range(self.columnSize)] for j in range(self.rowSize)]

    def print_matrix(self):
        for i in range(self.rowSize):
            for j in range(self.columnSize):
                print(self.matrix[i][j], end="")
            print("")

    def get_matrix(self):
        return self.matrix

    def count_matrix(self, i, j):
        self.matrix[i][j] += 1

    def clear_matrix(self):
        for i in range(self.rowSize):
            for j in range(self.columnSize):
                self.matrix[i][j]=0

    def clear_matrix2(self):
        self.matrix = [[0 for i in range(self.columnSize)] for j in range(self.rowSize)]
    def get_rowsize(self):
        return self.rowSize

    def get_columnsize(self):
        return self.columnSize
    def get(self,i,j):
        return self.matrix[i][j]
    def get_totalhit(self,i):
        result=0
        for j in range(self.columnSize):
            result=result+self.matrix[i][j]
        if result==0:
            return 1
        else:
            return result
def performance_of_clear(sketch_size, loop):
    import time
    s=Sketch(sketch_size)
    print("sketch size: %d"%sketch_size)
    print("loop: %d"%loop)
    
    start = time.time()
    for i in range(loop):
        s.clear_matrix()
    end = time.time()
    print("clear_matrix time: %f" %(end - start))

    start = time.time()
    for i in range(loop):
        s.clear_matrix2()
    end = time.time()
    print("clear_matrix2 time: %f" %(end - start))

def performance_of_init(sketch_size, loop):
    import time
    start = time.time()
    for i in range(loop):
        s=Sketch(sketch_size)
    end = time.time()
    print ("time: %f ---\n" %(end - start))

class myThread(threading.Thread):
    
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        performance_of_init(16, 1)


