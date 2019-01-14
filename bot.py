import time
import json
import requests, bs4
from time import strftime, localtime, sleep
from vaqtlar import *
import pyrogram
import urllib
from pyrogram import *

app = Client("my_account")


@app.on_message(Filters.text & Filters.private)
def echo(client, message):
    if message.text=="S":  
       app.edit_message_text(message.chat.id,message.message_id,"Salom")
    if message.text=="X" or message.text=="x" or message.text=="х" or message.text=="Х":
        app.edit_message_text(message.chat.id,message.message_id,"Xaa")
    if message.text=="n" or message.text=="N":
        app.edit_message_text(message.chat.id, message.message_id, "Nimagapla")
    if message.text=="!id" or message.text=="!me" or message.text=="!ID" or message.text=="!Me":
        cid = message.chat.id
        app.send_message(message.chat.id,"**ID:** "+ str(cid) +" ")
    if message.text=="!Pong" or message.text=="!ping" or message.text=="!Ping":
        first_time = time.time()
        sent = client.send_message(message.chat.id,'**Ping!**',reply_to_message_id=message.message_id)
        second_time = time.time()
        client.edit_message_text(message.chat.id, sent.message_id,'**Ping!** `{}`s'.format(str(second_time - first_time)[:5]))
    if message.text.startswith("!keep"):
        s = message.text
        s.replace("!keep ", "")
        text = message.text.split()[1]
        tezt = message.text.split()[2]
        tect = message.text.split()[3]
        app.send_photo(message.chat.id, "http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A{}%0D%0A{}%0D%0A{}&bc=000000&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=500&ps=sq".format(text,tezt,tect))

    if message.text.startswith("!translate"):
        msg = message.text
        trs = msg     
        trs.replace("!translate ", "")
        
        lang = "en-ru"
        s=requests.get('https://translate.yandex.net/api/v1.5/tr/translate?key=trnsl.1.1.20181205T141653Z.24ade72ceb790bf5.ab8150faa41ec9aa2d7c5dceed2c8b8af6860659&text={}&lang=en-ru'.format(trs,lang).replace("!translate ", ""))
        b=bs4.BeautifulSoup(s.text, "html.parser")
        
        p3=b.select('text')
        tr=p3[0].getText()
        message.reply("**Перевод:** `"+tr+"`", quote=True)
        
    #if message.text.startswith("!py"):
    #    mse = message.text
    #    app.send(pyrogram.api.functions.messages.SetTyping())        
    if message.text.startswith("!userid"):
        mes = message.text
        get = app.get_users(int("{}".format(mes.replace("!userid ", ""))))
        app.send_message(message.chat.id, "**ID:** `{}`\n**Username:** `{}`\n**First name:** `{}`\n**Last name:** `{}`".format(get['id'], get['username'], get['first_name'], get['last_name']))
        
    if message.text.startswith("!username"):
        mes = message.text
        get = app.get_users("{}".format(mes.replace("!username ", "")))
        app.send_message(message.chat.id, "**ID:** `{}`\n**Username:** `{}`\n**First name:** `{}`\n**Last name:** `{}`".format(get['id'], get['username'], get['first_name'], get['last_name']))   
    if message.text=="!vaqtlar"or message.text=="nomoz":
        now = strftime("%H:%M", localtime())
        app.send_message(message.chat.id, "__Namoz vaqtlari⏰__\n\n**Tong:** `{}`\n**Quyosh:** `{}`\n**Peshin:** `{}`\n**Asr:** `{}`\n**Shom:** `{}`\n**Xufton:** `{}`\n\n**Hozir: **`{}`".format(Tong, Quyosh, Peshin, Asr, Shom, Xufton, now))
    if message.text=="!now":
        while True:
            now = strftime("%H:%M", localtime())
            
            app.edit_message_text(message.chat.id, message.message_id, now)
    
    if message.text=="!title_on":
         my_file = open("title.txt", "w")
         my_file.write("!title_on")
         my_file.close()
    if message.text:
         my_file = open("title.txt")
         my_string = my_file.read()
         my_file.close()
         if my_string=="!title_on":
             mess = message.text
             app.edit_message_text(message.chat.id, message.message_id, mess.title())
    if message.text=="!title_off":
       my_file = open("title.txt", "w")
       my_file.write("!title_off")
       my_file = open("title.txt")
       my_file.close()

@app.on_message(Filters.chat("python_uz_offtopic"))
def new_alifbo(client, message):
#    if message.text:
#        d = {"sh":"ş","ch":"ç","o'":"ŏ","g'":"ğ", "G'":"Ğ", "Ch":"Ç", "Sh":"Ş", "O'":"Ŏ"}
#        s = message.text
#        tmp = s
#        for key, value in d.items():
#            tmp = tmp.replace(key, value)
#        app.edit_message_text(message.chat.id,message.message_id, tmp)
        if message.text.startswith("!py "):
            msg = message.text
            url = requests.get("https://rextester.com/rundotnet/api?LanguageChoice=5&Program={}".format(msg.replace('!py ', '')))
            json_data = url.json()
            result = json_data['Result']
            app.edit_message_text(message.chat.id,message.message_id, "**Code**: `{}`\n\n**Result**: ```{}```\n".format(msg.replace('!py ', ''),result), parse_mode='markdown')


app.run()
