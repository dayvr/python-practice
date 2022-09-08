# Memoization is a way to make code run faster by saving previously computed results.  
# Instead of needing to recompute the value of an expression, a memoized computation 
# first looks for the value in a cache of pre-computed values.

# Takes in three inputs: a cache, which is a Dictionary that maps inputs to proc to
# their previously computed values, a function, which can be called by writing proc(proc_input), 
# and proc_input which is the input to proc.
# Returns the value of the proc with input proc_input,
# But it is only evaluate it if it has not been previously called.

import time

def time_execution(function, inputs):
    start = time.process_time()
    result = function(inputs)
    run_time = time.process_time() - start
    return result, run_time

def cached_execution(cache, proc, proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]

def factorial(n):
    print("Running factorial")
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

cache = {} # start cache as an empty dictionary
### first execution (should print out Running factorial and the result)
print(cached_execution(cache, factorial, 50))
print("Second time:")
### second execution (print out the result)
print(cached_execution(cache, factorial, 50))

def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1 )
               + cached_execution(cache,  cached_fibo, n - 2 ))
               
cache = {} # new cache
print(cached_execution(cache, cached_fibo,100))
print(time_execution(cached_fibo, 40))
