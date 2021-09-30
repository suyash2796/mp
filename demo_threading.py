import threading
import time

def calc_square(n):
    for i in range(1,n+1):
        time.sleep(0.2)
        print('square -> ', i*i)

def calc_cube(n):
    for i in range(1,n+1):
        time.sleep(0.2)
        print('cube -> ', i*i*i)


if __name__=='__main__':
    time1 = time.time()
    t1 = threading.Thread(target=calc_square,args=(5,))
    t2 = threading.Thread(target=calc_cube,args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('total time taken by multi-threaded program - > ', time.time()-time1)

    time2 = time.time()
    calc_square(5)
    calc_cube(5)
    print('total time taken by Normal(single thread) program - > ', time.time()-time2)
