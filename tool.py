import os
import argparse
import datetime


Current_Date = datetime.datetime.today().strftime ('%d.%m.%Y')
date = str(Current_Date)

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Whitelist filename")
parser.add_argument("-m", "--mode", help="b = blacklist | w = whitelist ")
args = parser.parse_args()

whitelist = []

if args.mode == "b":
    mode = '-b'
elif args.mode == "w":
    mode = '-w'
else:
    print('You need to select a mode!')
    exit()

command = 'pihole {} --comment "{}" '.format(mode, date)

with open(args.file, 'r') as file:
    for _ in file:
        whitelist.append(_)

file.close()


while True:
    if not whitelist:
        break
    else:
        gglist = whitelist[:10]
        for _ in gglist:
            whitelist.remove(_)
            command+=_.replace('\n', ' ').replace('\r', ' ')

        os.system(command)
        command = 'pihole {} --comment "{}" '.format(mode, date)
