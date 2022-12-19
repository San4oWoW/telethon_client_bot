from telethon import TelegramClient, client
from telethon.tl.types import SendMessageUploadDocumentAction
from telethon.utils import pack_bot_file_id
import datetime
api_id = 
api_hash = ""
name = ""

client = TelegramClient(name, api_id, api_hash)

async def main():
    # Now you can use all client methods listed below, like for example...
    start = datetime.datetime.now()
    r = await client.send_file('me', r'W:\10_ИТ отдел\Техподдержка\1Cv8.dt')
    stop = datetime.datetime.now()

    finish = stop - start
    print(finish)
    # file_id = pack_bot_file_id(r.media)
    # print(file_id)
    # print("Успешно")
    # await client.send_file("me", "BQADAgAD5CEAAsovwEpXzVPKQcAVLwI")

with client:
    client.loop.run_until_complete(main())
