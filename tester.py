import time
import sketch
from sketch import Sketch
import HellingerDistance

#performance measurement without threads
"""
start = time.time()
performance_of_init(16, 1)
performance_of_init(16, 1)
end = time.time()
print(end - start)
"""

#performance measurements with threads
"""
thread1 = sketch.myThread(1, "Thread-1", 1)
thread2 = sketch.myThread(2, "Thread-2", 2)
start = time.time()
thread1.start()
thread2.start()
end = time.time()
print ("time son: %f ---\n" %(end - start))
"""

"""
#performance of clear the whole sketch
sketch.performance_of_clear(4,100)
sketch.performance_of_clear(4,1000)
sketch.performance_of_clear(4,10000)

sketch.performance_of_clear(8,100)
sketch.performance_of_clear(8,1000)
sketch.performance_of_clear(8,10000)

sketch.performance_of_clear(16,1)
sketch.performance_of_clear(16,10)
sketch.performance_of_clear(16,100)
"""
a=Sketch(4)
b=Sketch(4)
a.count_matrix(0,1)
a.count_matrix(0,1)
a.count_matrix(0,3)
a.count_matrix(0,0)
b.count_matrix(0,2)
b.count_matrix(0,3)
b.count_matrix(0,1)
b.count_matrix(0,0)

print(HellingerDistance.hellinger1(a,b))