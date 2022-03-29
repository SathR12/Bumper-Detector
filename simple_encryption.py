import json
import time

menu = input("save or search? ")

def cipher():
    web = input("Enter website name ")
    password = input("Enter your password ")
    
    with open('save.json', 'r') as f:
        info = json.load(f)
    
    if web.lower() in info:
        print("password updating...")
        time.sleep(2)
        
    string = "" 
    ciphered_list = []
    num = []
    alph = list('abcdefghijklmnopqrstuvwxyz')
    
    for i in range(0, len(password.lower())):
        lower = password.lower() 
        if lower[i] not in alph:
            string += lower[i]

            
        else: 
            indexed = alph.index(lower[i])
            if indexed < 22:
                caesar = alph[indexed+4]
                string += caesar
                
                
            elif indexed > 22:
                caesar = indexed+4
                mod = caesar % len(alph)
                ch = alph[mod]
                string += ch
                
    with open('save.json', 'w') as f:
        info[web.lower()] = string
        json.dump(info, f)
        print("saving...")
        time.sleep(3)
        print("saved")
    
             
    
                    
def decipher():
    web = input("Enter website name ")
    with open('save.json', 'r') as f:
            info = json.load(f)
    plaintext = "" 
    alph = list('abcdefghijklmnopqrstuvwxyz')
    
    if web.lower() not in info.keys():
        print("searching...")
        time.sleep(5)
        print("Website not saved")
    else:
        for i in range(0, len(info[web.lower()].lower())):
            if info[web.lower()].lower()[i] not in alph:
                plaintext += info[web].lower()[i]
            if info[web.lower()].lower()[i] in alph:
                indexed = alph.index(info[web.lower()].lower()[i])
                caesar = alph[indexed-4]
                plaintext += caesar
        print("fetching credentials...")
        time.sleep(3)
        print("password:", plaintext)
            


if menu.lower() == "save":
    cipher()
    

if menu.lower() == "search":
    decipher()
