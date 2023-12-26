import os
import sys
import random
import statistics
import datetime
import logging
from timeit import Timer

print(os.getcwd())  # get the current directory where this module is
# sys.stderr.write("error message")  # print to error stream
# sys.stdout.write("normal message")  # print to standard output


stuff = ['apple', 'banana', 'orange', 'watermelon', 'tangerine', 'pawpaw']

print(random.choice(stuff))  # choose single a random item from list
print(random.sample(range(1000), 10))  # return a subset which is a sample of arg1 items from the arg0 sequence
print(random.random())  # return a random float from 0 (inclusive) to 1 (exclusive)
print(random.randrange(1000)) # choose a single number from the range. it's like the range function but this time it picks a random number

weights = list(random.random() for _ in range(len(stuff)))
print(weights)

# choose a desired number of items from a sequence using weights
print(random.choices(stuff, weights=weights, k=3)) #Return a k-sized list of population elements chosen with replacement.
                                                   # If the relative weights or cumulative weights are not specified,
                                                   # the selections are made with equal probability.

print("mean: ", statistics.mean(weights))
print("mode: ", statistics.mode(weights))
print("median: ", statistics.median(weights))
print("stdev: ", statistics.stdev(weights))
print("pstdev: ", statistics.pstdev(weights))
print("variance: ", statistics.variance(weights))

print(datetime.date(2023, 11, 17))


# python logging functions. make sure to import logging module
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


print(datetime.date.today())
print(datetime.datetime.today())


import time
obj = time.gmtime(0)
epoch = time.asctime(obj)
print("The epoch is:",epoch)
curr_time = round(time.time() * 1000)
print("Milliseconds since epoch:",curr_time)

print(time.time() * 1000)
print(time.time_ns())

print('-----')
from datetime import datetime

curr_time = datetime.now()
hour = curr_time.hour
minute = curr_time.minute
second = curr_time.second

print(curr_time, hour, minute, second)