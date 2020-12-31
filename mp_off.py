import random
import math
import time

number_of_iterations = int(input("Number of iterations : "))

def monte_carlo():
    inside_circle = 0
    for i in range(0, number_of_iterations):
      x = random.random()
      y = random.random()

      if math.sqrt(x*x + y*y) < 1.0:
          inside_circle += 1
    return inside_circle

start_time = time.time()

pi = (float(monte_carlo()) / number_of_iterations) * 4

ending_time = time.time()

print("Estimation of PI :", pi)
print("Calculations took", ending_time-start_time)