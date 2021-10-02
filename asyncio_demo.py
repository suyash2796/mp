import asyncio
import time

async def my_couroutine():
    print("step1")
    await asyncio.sleep(1)
    print("step2")

async def main():
    await asyncio.gather(my_couroutine(), my_couroutine(), my_couroutine())


def synchronous_call():
    for i in range(3):
        print("step1")
        time.sleep(1)
        print("step2")

if __name__=='__main__':
    print("asynchronous call started")
    t1 =time.time()
    loop =  asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    print("asynchronous call completed")
    print("time taken by asyncio call: ", time.time()-t1)

    print("synchronous call started")
    t2=time.time()
    synchronous_call()
    print("synchronous call completed")
    print("time taken by synchronous call: ", time.time()-t2)