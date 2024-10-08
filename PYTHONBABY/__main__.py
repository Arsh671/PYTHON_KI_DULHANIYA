import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from PYTHONBABY import LOGGER, app, userbot
from PYTHONBABY.core.call import Hotty
from PYTHONBABY.misc import sudo
from PYTHONBABY.plugins import ALL_MODULES
from PYTHONBABY.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

from PYTHONBABY.plugins.tools.clone import restart_bots




async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PYTHONBABY.plugins" + all_module)
    LOGGER("PYTHONBABY.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("PYTHONBABY").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("PYTHONBABY").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 𝗨𝗧𝗧𝗔𝗠★𝗥𝗔𝗧𝗛𝗢𝗥𝗘\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("PYTHONBABY").info("Stopping Brandrd Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
