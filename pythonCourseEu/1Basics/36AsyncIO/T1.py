import asyncio, random

def rnd_sleep(n):
    return asyncio.sleep(random.random() * 2 * n)

async def consumer(queue):
    while True:
        number = await queue.get()
        print(f'consumer{number}')


async def producer(queue):
    while True:
        token = random.random()
        print(f'producer{token}')
        if token < .02:
            break
        await queue.put(token)
        await rnd_sleep(.2)


async def main():
    queue = asyncio.Queue()

    # fire up the both producers and consumers
    producers = [loop.create_task(producer(queue))
                 for _ in range(1)]
    consumers = [loop.create_task(consumer(queue))
                 for _ in range(10)]

    # with both producers and consumers running, wait for
    # the producers to finish
    await asyncio.gather(*producers)
    print('---- done producing')

    # wait for the remaining tasks to be processed
    await queue.join()

    # cancel the consumers, which are now idle
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()