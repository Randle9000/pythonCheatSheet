import asyncio
import time


async def find_divisibles(inrange, div_by):

    """
    the main difference is that time.sleep(5) is blocking, and asyncio.sleep(5) is non-blocking.
    When time.sleep(5) is called, it will block the entire execution of the script and it will 
    be put on hold, just frozen, doing nothing. But when you call await asyncio.sleep(5), 
    it will ask the event loop to run something else while your await statement finishes its execution.
    """

    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            # come back to find_divisibale of particuluar task when sleep is over
            await asyncio.sleep(0.0001) # it tells thread to run other task
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def main():
    """We need to actually create tasks, making our main now:"""
    d1 = loop.create_task(find_divisibles(508000, 43123))
    d2 = loop.create_task(find_divisibles(1231241, 1234))
    d3 = loop.create_task(find_divisibles(50013, 3))

    # come back to main whten d1, d2 ,d3 will be ready
    await asyncio.wait([d1, d2, d3])
    return d1, d2, d3

if __name__ == '__main__':
    """In order to use Asyncio, we will need an event loop, a way input tasks to be done in this loop,
      and of course the tasks themselves! With asynchronous programming,
      you're going to want your tasks to be coroutines. 
      Under the current syntax with Python 3.5 onward, the word "coroutine" isn't actually used. 
      Instead, to denote your coroutines, 
    you will preface your function with async. Rather than 
    """
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(1)
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())
    except Exception as e:
        # logging...etc
        pass
    finally:
        loop.close()