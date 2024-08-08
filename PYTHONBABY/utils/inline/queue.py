from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="✰𝐂ʟᴏsᴇ✰",
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="✰𝐂ʟᴏsᴇ✰",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="✰𝐂ʟᴏsᴇ✰",
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="✰𝐎ᴡɴᴇʀ✰", url=f"https://t.me/UTTAM470"
            ),
            InlineKeyboardButton(
                text="✰𝐒ᴜᴘᴘᴏʀᴛ✰", url=f"https://t.me/BABY09_WORLD"
            ),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="✰𝐂ʟᴏsᴇ✰")],
    ]
    return buttons



def queuemarkup(_, vidid, chat_id):

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="✰𝐒ᴛᴏᴘ✰", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="✰𝐒ᴋɪᴘ✰", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="✰𝐑ᴇsᴜᴍ✰", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="✰𝐑ᴇᴘʟᴀ✰", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✰𝐌ᴏʀᴇ✰",
                url="https://t.me/BABY09_WORLD",
            ),
        ],
    ]

    return buttons
