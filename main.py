import threading
import time
import discord
import requests

userToken = "USER_TOKEN"
userID = 0  # ID
botID = 688202466315206661
header = {
    "authorization": userToken
}
token = "BOT_TOKEN"
client = discord.Client()

arenaThread = False
gachaThread = False
print("Waiting for command.")


def send_message(message):
    payload = {
        "content": message
    }
    r = requests.post("CHANNEL_REQUEST_LINK", data=payload, headers=header)


def gacha():
    while True:

        if not gachaThread:
            break

        time.sleep(20)
        send_message(".gacha")


def arena():
    while True:

        if not arenaThread:
            break

        time.sleep(10)
        send_message(".arena")


@client.event
async def on_message(message):
    if message.author.id == userID or message.author.id == botID:

        time.sleep(3)
        global gachaThread
        global arenaThread

        if message.content == "a.gacha":
            if not gachaThread:
                gachaThread = True
                print("Gacha started.")
                await message.channel.send("Gacha started.")
                t1 = threading.Thread(target=gacha)
                t1.start()
                return
            else:
                gachaThread = False
                print("Gacha stopped.")
                await message.channel.send("Gacha stopped.")
                return

        if message.content == "a.arena":
            if not arenaThread:
                arenaThread = True
                print("Arena started.")
                await message.channel.send("Arena started.")
                t2 = threading.Thread(target=arena)
                t2.start()

                return
            else:
                arenaThread = False
                print("Arena stopped.")
                await message.channel.send("Arena stopped.")

        try:
            if message.author.id == botID:
                embed = message.embeds[0].to_dict()

                if embed["footer"]["text"].find("Avoid") > -1:

                    if embed["fields"][1]["value"].find("ᴀʟᴘʜᴀ") != -1:
                        print(embed["title"] + "| α")
                        # send_message(".burn")

                    elif embed["fields"][1]["value"].find("ʙᴇᴛᴀ") != -1:
                        print(embed["title"] + "| β")
                        # send_message(".burn")

                    elif embed["fields"][1]["value"].find("ɢᴀᴍᴍᴀ") != -1:
                        print(embed["title"] + "| γ")
                        # send_message(".burn")

                    elif embed["fields"][1]["value"].find("ᴅᴇʟᴛᴀ") != -1:
                        print(embed["title"] + "| δ")
                        # send_message(".burn")

                    elif embed["fields"][1]["value"].find("ᴇᴘsɪʟᴏɴ") != -1:
                        print(embed["title"] + "| ε")
                        # send_message(".burn")

                    elif embed["fields"][1]["value"].find("ᴢᴇᴛᴀ") != -1:
                        print(embed["title"] + "| ζ")
                        # send_message(".burn")

                    elif embed["fields"][1]["value"].find("ᴜʟᴛʀᴀ") != -1:
                        print(embed["title"] + "| ζ𝓡")
                        # send_message(".burn")

                    elif embed["fields"][1]["value"].find("sᴄᴀʀʟᴇᴛ") != -1:
                        print(embed["title"] + "| †")
                        # send_message(".burn")

                elif embed["footer"]["text"].find("Burn") != -1:
                    send_message("b")

                else:
                    pass
            else:
                pass
        except:
            pass


client.run(token)
