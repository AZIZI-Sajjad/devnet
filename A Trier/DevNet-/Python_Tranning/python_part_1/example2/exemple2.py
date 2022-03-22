#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 1
Author: Hank Preston <hapresto@cisco.com>

example2.py
Illustrate the following concepts:
- Reading from and writing to files
- The "with" statement
- Writing to command line
- Requesting interactive user input
"""

__author__ = "AZZI Sajjad"
__author_email__ = "sajjaad.azizi@yahoo.com"
__copyright__ = "Copyright (c) 2020 SDACO, Inc."
__license__ = "CCNA"

from datetime import datetime

log_file = "log_exemple2.log"

def read_log(log):
    """
    Open the logfile and print contents to the terminal
    """
    # ----------> ETAPE 3
    # open(log, "r") =>
    # r : Read
    # a : Append => Ajouter a la fin du fichier
    # wr : Write => Replacer le contenu par le nouveau
    #--------------------------------------------------
    # with open(log, "r") as f:
    # open : ouvrir un fichier "log"
    # r : en lecture
    # with ... as f :mettre le fichier "log" dans la vraible "f"
    with open(log, "r") as f:
        print(f.read())

def write_log(log, name):
    """
    Add new logfile entry with datestamp
    """
    # ----------> ETAPE 2
    # Get current date and time
    # log_time = str(datetime.now())
    # datetime.now() => Le temps actuel
    # str => convertir en STRING
    #--------------------------------------------------
    # with open(log, "a") as f:
    # open : ouvrir un fichier "log"
    # a : Ajouter a la fin du fichier
    # with ... as f :mettre le fichier "log" dans la vraible "f"
    log_time = str(datetime.now())
    with open(log, "a") as f:
        # f.writelines => Ajouter la ligne dans le fichier
        f.writelines("Entry logged at: {} by {}\n".format(log_time, name))

# Entry point for program
if __name__ == '__main__':
    # ----------> ETAPE 1
    # Get users name
    name = input("What is your name? ")

    # Add entry to log file
    print("Adding new log entry")
    # Deux variables definies :
    # log_file : au debut du code
    # name : entree en CLI
    write_log(log_file, name)
    print("")

    # Access Starting Log File
    print("Log File Contents")
    print("-----------------")
    read_log(log_file)
