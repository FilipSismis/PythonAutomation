import keyboard as keyboard
import time
import os
import win32clipboard
import argparse

parser = argparse.ArgumentParser(
    prog="URLCopy",
    description="Program to copy URLs from browser to .txt file or paste them other way around",
    epilog="See '<command> --help' to read about a specific sub-command."
)

base_parser = argparse.ArgumentParser(add_help=False)

subparsers = parser.add_subparsers(dest='mode', help='Sub-commands')

Copy_parser = subparsers.add_parser("paste", help="copy URLs from browser to .txt", parents=[base_parser])
Copy_parser.add_argument("-N", "--number", required=True, help="number of tabs", type=int)
Copy_parser.add_argument("-n", "--name", required=False, help="name of the file(optional)")

Paste_parser = subparsers.add_parser("paste", help="paste URLs from .txt to browser", parents=[base_parser])

args = parser.parse_args()

if args.mode == 'copy':
    print('Copy mode from browser to notepad')
    nameOfFile = args.name
    numberOfTabs = args.number
    links =[]
    
    print('Sleeping for 2 seconds')
    time.sleep(2)
    
    for i in range(numberOfTabs):
        keyboard.press_and_release('ctrl+l')
        time.sleep(0.1)
        keyboard.press_and_release('ctrl+c')
        time.sleep(0.1)
        keyboard.press_and_release('ctrl+tab')
        time.sleep(0.1)
        win32clipboard.OpenClipboard()
        links.append(win32clipboard.GetClipboardData())
        win32clipboard.CloseClipboard()

    if not nameOfFile:
        nameOfFile = "New Text Document.txt"
    if not nameOfFile.endswith(".txt"):
        nameOfFile = nameOfFile + ".txt"
        
    file = open(nameOfFile , "a")
    for link in links:
        file.write(link + "\n")
    file.close

elif args.mode == 'paste':
    print('Paste mode from notepad to browser')
    print('Sleeping for 2 seconds')
    time.sleep(2)

    filePath = ""
    fileList = os.listdir('.//')
    
    for file in fileList:
        if(file.endswith(".txt")):
            filePath = file
            continue    
            
    file = open(filePath , "r")
    links = file.read().splitlines()
    file.close
    
    for link in links:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(link)
        win32clipboard.CloseClipboard()
        keyboard.press_and_release('ctrl+t')
        time.sleep(0.1)
        keyboard.press_and_release('ctrl+v')
        time.sleep(0.1)
        keyboard.press_and_release('enter')
        time.sleep(0.1)
