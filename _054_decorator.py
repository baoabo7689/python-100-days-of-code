import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
  begin_time = time.time()
  function()
  end_time = time.time()
  print(f"{end_time - begin_time}")

def fast_function():
  for i in range(1000000):
    i * i
        

def slow_function():
  for i in range(10000000):
    i * i