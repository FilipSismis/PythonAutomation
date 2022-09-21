import keyboard as keyboard
import time
import win32clipboard

print('(1)...From browser to notepad' + '\n' +
    '(2)...From notepad to browser' + '\n' + 
    '(3)...Exit' + '\n' + 
    '-----------------------------')
choice = input("Enter your choice:")
if choice == '1':
    print('(1)...From browser to notepad')
    numberOfTabs = int(input("Enter number of tabs:"))
    links =[]
    
    print('Sleeping for 2 seconds')
    time.sleep(2)
    
    for i in range(numberOfTabs):
        keyboard.press_and_release('ctrl+tab')
        time.sleep(0.1)
        keyboard.press_and_release('ctrl+l')
        time.sleep(0.1)
        keyboard.press_and_release('ctrl+c')
        time.sleep(0.1)
        win32clipboard.OpenClipboard()
        links.append(win32clipboard.GetClipboardData())
        win32clipboard.CloseClipboard()
    
    file = open("New Text Document.txt" , "a")
    for link in links:
        file.write(link + "\n")
    file.close

elif choice == '2':
    print('(2)...From notepad to browser')
    print('Sleeping for 2 seconds')
    time.sleep(2)
    
    file = open("New Text Document.txt" , "r")
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
            
else:
    print('Wrong input!')

