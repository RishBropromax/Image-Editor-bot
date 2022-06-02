from bs4 import *
import requests
import os
import re
import random
import requests
from pyrogram import filters
from szbot import sz
from szbot.helpers.caption import  repmark
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def download_images(images): 
    count = 0
    print(f"Total {len(images)} Image Found!") 
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"] 
            except: 
                try: 
                    image_link = image["data-src"] 
                except:
                    try:
                        image_link = image["data-fallback-src"] 
                    except:
                        try:
                            image_link = image["src"] 
                        except: 

                            pass
            try: 
                r = requests.get(image_link).content 
                try:

                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open("logo.jpg", "wb+") as f: 
                        f.write(r)
                    count += 1
            except: 
                pass


def mainne(name, typeo):
    url = f"https://www.brandcrowd.com/maker/logos?text={name}&searchtext={typeo}&searchService="
    r = requests.get(url) 
    soup = BeautifulSoup(r.text, 'html.parser') 
    images = soup.findAll('img') 
    random.shuffle(images)
    if images is not None:
       print("level 1 pass")
    download_images(images)

def nospace(s):

    s = re.sub(r"\s+", '%20', s)

    return s


@sz.on_message(filters.command(["rlogo", f"rlogo@szimagebot"]) & ~filters.edited & ~filters.bot)
async def logogen(client, message):
    pablo = await client.send_message(message.chat.id,"`Creating The Logo.....`")
    Godzilla = nospace(message.text.strip().split(None, 1)[1].lower())
    if not Godzilla:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return
    lmao = Godzilla.split(":", 1)
    try:
        typeo = lmao[1]
    except BaseException:
        typeo = "name"
        await pablo.edit(
             "Creating Logo")
    name = lmao[0]
    mainne(name, typeo)
    url = requests.get(f"https://www.brandcrowd.com/maker/logos?text={name}&searchtext={typeo}&searchService=").history[1].url
    imgcaption = f"""
Random Logo Genarated Successfully✅
࿂ **Generated By** : [Emo Logo Bot](https://t.me/Emo_Logo_Bot)
࿂ **Requestor** :. {message.from_user.mention}
࿂ **Powered By **  : [szteambots](https://t.me/ImRishmika)
࿂ **Download link** : `{url}`
"""
    created = "logo.jpg"
    await client.send_photo(message.chat.id, photo = created, caption = imgcaption, reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Download Link••", url=f"{url}"
                    )
                ],
            ]
          ))
    try:
        os.remove(pate)
    except:
        pass
    await pablo.delete()
