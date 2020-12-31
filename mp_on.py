import random
import math
import time
import concurrent.futures

def monte_carlo(iterations):
    inside = 0
    for i in range(0, iterations):
      x = random.random()
      y = random.random()

      if math.sqrt(x*x + y*y) < 1.0:
          inside += 1
    return inside

def main():
    number_of_processes = int(input("Number of processes : "))
    number_of_iterations = int(input("Number of iterations per process: "))
    result = 0

    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        processes = [executor.submit(monte_carlo, number_of_iterations) for _ in range(number_of_processes)]
        for f in concurrent.futures.as_completed(processes):
            result += f.result()

    pi = (float(result) / (number_of_processes*number_of_iterations)) * 4

    ending_time = time.time()

    print(f"Estimation of PI : {pi}")
    print(f"Calculations took {ending_time - start_time}s")

if __name__ == '__main__':
    main()
