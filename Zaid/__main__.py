import asyncio
import importlib
from pyrogram import Client, idle
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
from Zaid import clients, app  # Removed ids

# Ensure ids exists
try:
    from Zaid import ids
except ImportError:
    ids = []  # Fallback to an empty list if not found

async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module(f"Zaid.modules.{all_module}")  # Fixed module import
        print(f"Successfully Imported {all_module} 💥")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)  # Ensure ids exists
        except Exception as e:
            print(f"{e}")
    await idle()

if __name__ == "__main__":
    asyncio.run(start_bot())  # Clean execution
