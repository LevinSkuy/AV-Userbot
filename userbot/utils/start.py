from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/a32e8d858ca79f8396121.jpg",
                caption="✨ **AV Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.1.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @trashme2 ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/trashme2"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
