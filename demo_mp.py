import time
from multiprocessing import pool

# to demonstrate the sequential and mp call of execution

def calc_square(n):
    return n*n*n

def sequential_call(numbers):
    start_time = time.time()
    result=[]
    for i in numbers:
        result.append(calc_square(i))
    print('total processing time by sequential cal: ', time.time()-start_time)

def mp_call(numbers):
    start_time = time.time()
    p = pool.Pool(4)
    res = p.map(calc_square,numbers)
    p.close()
    p.join()
    print('total processing time by mp cal: ', time.time()-start_time)

if __name__=='__main__':
    numbers =range(10000000)
    sequential_call(numbers)
    mp_call(numbers)
