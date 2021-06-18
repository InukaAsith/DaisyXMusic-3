from pyrogram import Client

from DaisyXMusic import config SESSION_NAME
from DaisyXMusic import config API_ID
from DaisyXMusic import config API_HASH

client = Client(SESSION_NAME, API_ID, API_HASH)

run = client.run
