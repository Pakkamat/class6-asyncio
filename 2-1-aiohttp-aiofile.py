# Wed Aug  9 13:33:04 2023 - Starting...
# Wed Aug  9 13:33:05 2023 - Writing 'dub grunge to './asyncout/new_file18.txt'...
# Wed Aug  9 13:33:05 2023 - Writing 'athens euro alternative with prominent tuba to './asyncout/new_file19.txt'...
# Wed Aug  9 13:33:05 2023 - Writing 'anthem didgeridootune to './asyncout/new_file11.txt'...
# Wed Aug  9 13:33:05 2023 - Writing 'russiastep to './asyncout/new_file7.txt'...
# Wed Aug  9 13:33:05 2023 - Writing 'speed R&B to './asyncout/new_file1.txt'...
# Wed Aug  9 13:33:05 2023 - Writing 'jig and taiwanese EDM to './asyncout/new_file10.txt'...
# Wed Aug  9 13:33:05 2023 - Writing 'cryptic anti-whittle to './asyncout/new_file14.txt'...
# Wed Aug  9 13:33:05 2023 - Writing 'reggae dirt to './asyncout/new_file15.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'flute speed era to './asyncout/new_file6.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'grave trumpet-step to './asyncout/new_file2.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'seattle guitar party to './asyncout/new_file9.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'ugandan trombonestyle to './asyncout/new_file5.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'ska lute to './asyncout/new_file0.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'doo wop clarinet to './asyncout/new_file17.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'EBM reel to './asyncout/new_file13.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'slam deathfuture to './asyncout/new_file3.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'southern mandolinvision to './asyncout/new_file8.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'heterocore to './asyncout/new_file4.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'military scottish lounge to './asyncout/new_file16.txt'...
# Wed Aug  9 13:33:06 2023 - Writing 'second wave aussielounge to './asyncout/new_file12.txt'...
# Time to complete asyncio rad/writes: 2.71 seconds

# pip install aiofiles==0.7.0
# pip install aiohttp==3.7.4.post0

import sys
import asyncio
import time

import aiohttp
import aiofiles


async def write_genre(file_name):
    """
    Uses genrenator from binaryjazz.us to write a random genre to the
    name of the given file
    """

    async with aiohttp.ClientSession() as session:
        async with session.get("https://binaryjazz.us/wp-json/genrenator/v1/genre") as response:
            genre = await response.json()

    async with aiofiles.open(file_name, "w") as new_file:
        print(f"{time.ctime()} - Writing '{genre} to '{file_name}'...")
        await new_file.write(genre)
    


async def main():
    tasks = []

    print(f"{time.ctime()} - Starting...")
    start = time.time()

    for i in range(20):
        tasks.append(write_genre(f"./asyncout/new_file{i}.txt"))

    await asyncio.gather(*tasks)

    end = time.time()
    print(f"Time to complete asyncio rad/writes: {round(end - start, 2)} seconds")    

if __name__ == "__main__":
    # On Windows, this finishes successfully, but throws 'RuntimeError: Event loop is closed'
    # The following lines fix this
    # Source: https://github.com/encode/httpx/issues/914#issuecomment-622586610
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
