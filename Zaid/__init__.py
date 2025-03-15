import asyncio
from pyrogram import Client
from config import (
    API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN,
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, 
    STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, 
    STRING_SESSION9, STRING_SESSION10
)
from datetime import datetime
import time
from aiohttp import ClientSession

# Bot Start Time
StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS

# Ensure OWNER_ID is in SUDO_USERS
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# Properly initialize aiohttp session with event loop
loop = asyncio.get_event_loop()
aiosession = ClientSession(loop=loop)

# Set Default API_ID & API_HASH if missing
if not API_ID:
    print("WARNING: API ID NOT FOUND, USING DEFAULT ⚡")
    API_ID = "24941168"

if not API_HASH:
    print("WARNING: API HASH NOT FOUND, USING DEFAULT ⚡")   
    API_HASH = "2ad0e09b0b43bb53436562030aa6a952"

# Check for BOT_TOKEN
if not BOT_TOKEN:
    print("ERROR: BOT TOKEN NOT FOUND! Please add ⚡")   
    exit(1)

# Main Bot Client
app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Zaid/modules/bot"),
    in_memory=True,
)

# User Clients List
clients = []

# Function to create session clients dynamically
def create_client(name, session_string):
    if session_string:
        print(f"{name}: Found.. Starting.. 📳")
        return Client(
            name=name,
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_string,
            plugins=dict(root="Zaid/modules"),
        )
    return None

# Adding Session Clients
session_list = [
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4,
    STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8,
    STRING_SESSION9, STRING_SESSION10
]

for idx, session in enumerate(session_list, start=1):
    client = create_client(f"client{idx}", session)
    if client:
        clients.append(client)

# Start all clients
async def start_clients():
    print("Starting all clients... 🚀")
    await app.start()
    for client in clients:
        await client.start()
    print("All clients started successfully! ✅")

# Run Clients
if __name__ == "__main__":
    loop.run_until_complete(start_clients())
