# type: ignore

import asyncio


async def worker(id, semaphore) -> None:
    await semaphore.acquire()
    print(f'worker {id} : semaphore aquired')

    await asyncio.sleep(5)
    print(f'worker {id} : semaphore released')
    semaphore.release()



async def main(workers: int = 5, value: int = 2) -> None:
    semaphore = asyncio.Semaphore(value=value)
    await asyncio.wait(list(worker(id, semaphore) for id in range(1, workers + 1)))
    print('worker n : all work complete')


if __name__ == '__main__':
        
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(1000, 10))
    loop.close()
