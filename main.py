import os
import threading
from PyMailGw import MailGwApi
import time
from pystyle import Write, Colors, Center, Colorate, Box
from datetime import datetime
import colorama
import clipboard




banner = """
:::::::::: ::::::::: ::::    ::::      :::     ::::::::::: :::        
:+:             :+:  +:+:+: :+:+:+   :+: :+:       :+:     :+:        
+:+            +:+   +:+ +:+:+ +:+  +:+   +:+      +:+     +:+        
+#++:++#      +#+    +#+  +:+  +#+ +#++:++#++:     +#+     +#+        
+#+          +#+     +#+       +#+ +#+     +#+     +#+     +#+        
#+#         #+#      #+#       #+# #+#     #+#     #+#     #+#        
########## ######### ###       ### ###     ### ########### ########## 
"""


def printheaders(email):
    print('\n')
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(str(banner)), 1))
    print('\n')
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(Box.Lines(str(email))), 1))
    print('\n'*2)


def mailbox():
    os.system('cls')
    api = MailGwApi(timeout=30)
    email = api.get_mail()
    clipboard.copy(str(email))
    printheaders(email)
    showedmails = []
    while True:
        time.sleep(5)
        for mail in api.fetch_inbox():
            now = datetime.now()
            codedetected = False
            if mail['id'] in showedmails:
                pass
            else:
                lastmail = {'subject': mail['subject'], 'mail': mail}
                showedmails.append(mail['id'])
                current_time = now.strftime("%H:%M:%S")
                mailsub = mail['subject']
                for s in mailsub.split():
                    code = s
                    if str(s.replace('.', '')).isdigit() and len(str(s)) > 2:
                        clipboard.copy(str(s))
                        codedetected = True
                print(Center.XCenter(Box.SimpleCube(str(f"(at {current_time} | from {mail['from']['name']}) {mailsub} {f'| Copied {code}' if codedetected else ''}"))))


mailbox()