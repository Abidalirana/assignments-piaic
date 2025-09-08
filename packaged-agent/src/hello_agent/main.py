import asyncio

# normal function
def abid():
    print("abid ali 256874")

# async main function
async def main():
    # run sync function inside async
    abid()

# entry point
if __name__ == "__main__":
    asyncio.run(main())
