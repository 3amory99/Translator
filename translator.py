import sys
from plyer import *
from googletrans import Translator
import time
import os
import pyperclip


# method of translation process
def translation(text):
    # initiate instance
    trans_item = Translator()
    var = trans_item.translate(text, dest='ar')
    notification.notify(
        title=var.origin,
        message=var.text,
        app_name='Translator',
        ticker='',
        app_icon='logo.ico',
        timeout=10
    )


sys.path.append(os.path.abspath("SO_site-packages"))
current_text = ""
while True:
    # temporary value of clipboard chash memory
    tmp_text = pyperclip.paste()
    try:
        if tmp_text != current_text:
            current_text = tmp_text
            translation(current_text)
    except:
        # pass or you could use 'continue' for iterated looping
        pass
    time.sleep(0.1)
