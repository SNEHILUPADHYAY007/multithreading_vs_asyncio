import asyncio
import aiohttp

sem = asyncio.Semaphore(1)
async def get_data():
    async with aiohttp.ClientSession() as session:
        resp = await fetch_all_data(session)
    print(resp)

async def fetch_all_data(session):
    tasks = []
    urls = [f"https://swapi.dev/api/people/?page={i}" for i in range(1, 9)]
    for url in urls:
        tasks.append(fetch(url, session))
    res = await asyncio.gather(*tasks)
    return res

# Fetching single page response
# Retry Logic could be implemented same as that of OT
async def fetch(url, session):
    async with sem:
        try:
            async with session.get(url, timeout = 60) as req:
                return await req.json()
        except Exception as e:
            print(f"Exception occured for:{url}")

# Make sure to call it in environments without running event loops
# Use asyncio.run() to handle the event loop properly
if __name__ == "__main__":
    try:
        # Try to get the current event loop
        loop = asyncio.get_event_loop()
        # Check if the loop is already closed
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        # Run the event loop
        loop.run_until_complete(get_data())
        # loop.close()
        print("Data Fetched successfully...Hence Exiting")
    except RuntimeError as e:
        # Handle specific runtime errors
        print(f"Runtime Error: {e}")
