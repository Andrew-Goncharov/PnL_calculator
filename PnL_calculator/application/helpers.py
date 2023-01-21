import asyncio
from pprint import pprint

import websockets
import json

auth_msg = \
{
  "jsonrpc": "2.0",
  "id": 48649,
  "method": "public/auth",
  "params": {
    "grant_type": "client_credentials",
    "client_id": "h7NZE3Y-",
    "client_secret": "Po3V6KAkRtdOSVfrBRD_EXG10OBoccBH4PvTpD2SkIg"
  }
}

get_all_currencies_msg = \
{
  "jsonrpc": "2.0",
  "id": 7538,
  "method": "public/get_currencies",
  "params": {
  }
}

get_book_summory_by_currency_msg = \
{
  "jsonrpc": "2.0",
  "id": 9344,
  "method": "public/get_book_summary_by_currency",
  "params": {
    "currency": "BTC",
    "kind": "future"
  }
}

# # access_token = response["result"]["access_token"]
# # print(access_token)
# print(json.dumps(response, indent=3))


async def call_api(msg):
    async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
        await websocket.send(msg)
        while websocket.open:
            response = json.loads(await websocket.recv())
            return response

result = asyncio.get_event_loop().run_until_complete(call_api(json.dumps(get_book_summory_by_currency_msg)))
print(result)


def calculate_PnL(start_date, end_date):
    pass


def calculate_PnL_index(start_date, end_date):
    pass


if __name__ == "__main__":
    pass
