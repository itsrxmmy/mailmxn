'''
Project Name: mailmxn
Project Version Tag: v1.1.0 - Beta
Author: itsrxmmy
Description: Email Automation Tool
'''

coming_soon = "\n\n\nComing Soon."
error = "\nAn error occurred."
pip_upgrade = "python -m pip install --upgrade pip"
pip_requirements = "python -m pip install -r requirements.txt"

def on_start():
    try:
        system(pip_upgrade)
    except:
        print("\nCouldn't upgrade pip.")
    try:
        system(pip_requirements)
    except:
        print("\nCouldn't install required packages.")
    
on_start()

import os, sys
import time
import datetime
import smtplib, ssl
import json
import random
from os import system, name

class clr:
    reset = "\u001b[0m"
    black = "\u001b[30m"
    bblack = "\u001b[30;1m"
    red = "\u001b[31m"
    bred = "\u001b[31;1m"
    green = "\u001b32m"
    bgreen = "\u001b[32;1m"
    yellow = "\u001b[33m"
    byellow = "\u001b[33;1m"
    blue = "\u001b[34m"
    bblue = "\u001b[34;1m"
    magenta = "\u001b[35m"
    bmagenta = "\u001b[35;1m"
    cyan = "\u001b[36m"
    bcyan = "\u001b[36;1m"
    white = "\u001b[37m"
    bwhite = "\u001b[37;1m"

class bgr:
    black = "\u001b[40m"
    red = "\u001b[41m"
    bred = "\u001b[41;1m"
    green = "\u001b[42m"
    bgreen = "\u001b[42;1m"
    yellow = "\u001b[43m"
    byellow = "\u001b[43;1m"
    blue = "\u001b[44m"
    bblue = "\u001b[44;1m"
    magenta = "\u001b[45m"
    bmagenta = "\u001b[45;1m"
    cyan = "\u001b[46m"
    bcyan = "\u001b[46;1m"
    white = "\u001b[47m"
    bwhite = "\u001b[47;1m"
    reset = "\u001b[0m"

banner = """



                            ███  ████
                           ░░░  ░░███
 █████████████    ██████   ████  ░███  █████████████   █████ █████ ████████
░░███░░███░░███  ░░░░░███ ░░███  ░███ ░░███░░███░░███ ░░███ ░░███ ░░███░░███
 ░███ ░███ ░███   ███████  ░███  ░███  ░███ ░███ ░███  ░░░█████░   ░███ ░███
 ░███ ░███ ░███  ███░░███  ░███  ░███  ░███ ░███ ░███   ███░░░███  ░███ ░███
 █████░███ █████░░████████ █████ █████ █████░███ █████ █████ █████ ████ █████
░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░
"""

description = """

Version 1.1.0 (Beta)
Developed by @itsrxmmy (https://www.github.com/itsrxmmy/)
Official Repository: https://www.github.com/itsrxmmy/mailmxn/
License: MIT License

"""

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


choices = """

[01] Email Flooder                                            [02] Email Automation (Coming Soon)
[03] Email Account Generator (Coming Soon)                    [04] License
[05] End Session

"""

def _return():
    input("\n\nPress enter to return to the Menu.    ")
    main()

def force_return():
    main()

def main():
    clear()
    print(banner)
    print(description)
    print(choices)
    trash = 0
    while True:
        choice = str(input("> Choice: "))
        if choice == "01" or choice == "1":
            mail_flooder()
            break
        elif choice == "02" or choice == "2":
            print(coming_soon)
            _return()
            break
        elif choice == "03" or choice == "3":
            print(coming_soon)
            _return()
            break
        elif choice == "04" or choice == "4":
            LICENSE()
            _return()
            break
        elif choice == "05" or choice == "5":
            end_session()
            break
        else:
            trash += 1
            if trash == 7:
                force_return()
                break
            else:
                continue
        break


def mail_flooder():
    print()
    print()
    while True:
        sender_email = str(input("<str> Sender Email: "))
        if "@" not in sender_email and "." not in sender_email:
            print("Must be a valid email address.")
            continue
        elif "@" in sender_email and "." in sender_email:
            break
        else:
            print("Must be a valid email address.")
            continue
        break
    while True:
        sender_password = str(input("<str> Sender Password: "))
        if len(sender_password) == 0:
            print("Password is required to log in.")
            continue
        elif len(sender_email) < 6:
            print("Password is only <{0}> characters long. Are you sure you've entered it properly?".format(str(len(sender_password))))
            continue
        else:
            break
        break
    while True:
        try:
            amount_of_targets = int(input("<int> Amount of Targets: "))
        except:
            print("Must be an Integer.")
            continue
        else:
            break
        break
    target_emails = []
    for i in range(amount_of_targets):
        target_email = str(input("<str> Target Email: "))
        target_emails.append(target_email)
    while True:
        try:
            amount_of_messages = int(input("<int> Amount of Messages: "))
        except:
            print("Must be an Integer.")
            continue
        else:
            break
        break
    message = str(input("<str> Message: "))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
    except:
        print(error)
    else:
        for i in range(amount_of_messages):
            try:
                server.sendmail(sender_email, target_emails, message)
                print("<1> Message has been sent.")
            except:
                print("Failed to send <1> Message.")
                continue
            break
    _return()

def LICENSE():
    with open("./LICENSE", "r") as f:
        license = f.read()
    print()
    print(license)
    print()

def end_session():
    while True:
        confirmation = str(input("> Are you sure you would like to end this session? [Y/n]: "))
        if confirmation == "Y" or confirmation == "y":
            clear()
            print("\nSession Ended.")
            break
        elif confirmation == "N" or confirmation == "n":
            force_return()
            break
        else:
            continue
        break

main()

