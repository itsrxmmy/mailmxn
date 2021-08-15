import os, sys
import json
import smtplib, time, datetime
from os import system, name

"""
Developed by @itsrxmmy
"""
class cli:

    version="1.0.0"
    build="Stable"

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

    def setup():
        try:
            system(pip_upgrade)
        except:
            print("\nCouldn't upgrade pip.")
        try:
            system(pip_requirements)
        except:
            print("\nCouldn't install required packages.")
        try:
            system(upgrade_requirements)
        except:
            print("\nCouldn't install required packages.")

    def clear():
        if name == 'nt':
            system('cls')
        else:
            system('clear')

    def CLI():
        cli.clear()
        while True:
            cmd = input(cli.clr.bblue + "~ " + cli.clr.bcyan + "$ ")
            if cmd

cli.setup()
cli.CLI()
