import asyncio
from fastmcp import Client

client = Client('http://127.0.0.1:8000/mcp')


async def main(number1, number2):
    async with client:
        result = await client.call_tool('add_number', {'number1': number1, 'number2': number2})
        print(result)


asyncio.run(main(1, 2))
