import keyboard as key
import time
import mouse
import pytesseract
import cv2
import numpy as np
import pyautogui
import re
import os
import colorama
from colorama import Fore
import sys
from termcolor import colored, cprint

colorama.init()


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def directory_check():
    fetch_dir = os.getcwd()
    if fetch_dir == r"C:\Users\leo\OneDrive\Documents\GitHub\psychic_btd6":
        print(Fore.GREEN + "correct directory found:", fetch_dir)
    else:
        print(Fore.RED + "incorrect directory found:", fetch_dir)
        os.chdir("C:\\Users\\leo\\OneDrive\\Documents\\GitHub\\psychic_btd6")
        print(Fore.YELLOW + "changing directory...")
        directory_check()

def start_game():
    mouse.move(1831, 1001, duration=0.2)
    mouse.click(button="left")
    time.sleep(0.1)
    mouse.click(button="left")

def alchermist_place():
    alch_poss = [1249, 783]
    mouse.move(alch_poss[0], alch_poss[1])
    key.press("f")
    key.release("f")
    time.sleep(0.1)
    mouse.click(button="left")

def alchermist_upgrade():
    alch_poss = [1249, 783]
    n = 1
    m = 1
    mouse.move(alch_poss[0], alch_poss[1], duration=0.1)
    time.sleep(0.2)
    mouse.click(button="left")
    time.sleep(0.2)
    while n <= 4:
        key.press("comma")
        key.release("comma")
        n += 1
        time.sleep(0.2)
    while m <= 1:
        key.press("slash")
        key.release("slash")
        m += 1
        time.sleep(0.2)

def plane_place():
    plane1_poss = [1255, 871]
    plane2_poss = [1408, 870]
    plane3_poss = [1412, 957]
    mouse.move(plane1_poss[0], plane1_poss[1])
    key.press("v")
    key.release("v")
    time.sleep(0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    mouse.move(plane2_poss[0], plane2_poss[1])
    key.press("v")
    key.release("v")
    time.sleep(0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    mouse.move(plane3_poss[0], plane3_poss[1])
    key.press("v")
    key.release("v")
    time.sleep(0.1)
    mouse.click(button="left")

def plane_203():
    n = 1
    m = 1
    while m <= 2:
        key.press("comma")
        key.release("comma")
        m += 1
        time.sleep(0.1)
    while n <= 3:
        key.press("slash")
        key.release("slash")
        n += 1
        time.sleep(0.1)

def plane_upgrade():
    plane1_poss = [1255, 871]
    plane2_poss = [1408, 870]
    plane3_poss = [1412, 957]
    mouse.move(plane1_poss[0], plane1_poss[1], duration=0.1)
    time.sleep(0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    plane_203()
    time.sleep(0.1)
    mouse.move(plane2_poss[0], plane2_poss[1], duration=0.1)
    time.sleep(0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    plane_203()
    time.sleep(0.1)
    mouse.move(plane3_poss[0], plane3_poss[1], duration=0.1)
    time.sleep(0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    plane_203()

def monkeyV_place():
    monkeyV1_poss = [1341, 775]
    monkeyV2_poss = [1463, 776]
    mouse.move(monkeyV1_poss[0], monkeyV1_poss[1])
    key.press("k")
    key.release("k")
    time.sleep(0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    mouse.move(monkeyV2_poss[0], monkeyV2_poss[1])
    key.press("k")
    key.release("k")
    time.sleep(0.1)
    mouse.click(button="left")

def monkeyV_sell():
    monkeyV1_poss = [1341, 775]
    mouse.move(monkeyV1_poss[0], monkeyV1_poss[1], duration=0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    key.press("backspace")
    key.release("backspace")
    time.sleep(0.3)
    key.press("k")
    key.release("k")
    time.sleep(0.1)
    mouse.click(button="left")

def monkeyV_sell2():
    monkeyV2_poss = [1463, 776]
    mouse.move(monkeyV2_poss[0], monkeyV2_poss[1], duration=0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    key.press("backspace")
    key.release("backspace")
    time.sleep(0.3)

def monkeyV_upgrade1():
    monkeyV1_poss = [1341, 775]
    monkeyV2_poss = [1463, 776]
    mouse.move(monkeyV1_poss[0], monkeyV1_poss[1], duration=0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    key.press("slash")
    key.release("slash")
    time.sleep(0.1)
    key.press("slash")
    key.release("slash")
    time.sleep(0.3)
    mouse.move(monkeyV2_poss[0], monkeyV2_poss[1], duration=0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    key.press("slash")
    key.release("slash")
    time.sleep(0.1)
    key.press("slash")
    key.release("slash")
    time.sleep(0.3)

def monkeyV_upgrade2():
    n = 1
    m = 1
    monkeyV1_poss = [1341, 775] 
    #mouse.move(300, 400, duration=0.1) # klickar p?? marken?
    #mouse.click(button="left")
    mouse.move(monkeyV1_poss[0], monkeyV1_poss[1], duration=0.1)
    mouse.click(button="left")
    time.sleep(0.1)
    while m <= 2:
        key.press("period")
        key.release("period")
        time.sleep(0.1)
        m += 1
    while n <= 2:
        key.press("comma")
        key.release("comma")
        time.sleep(0.1)
        n += 1
    
def start():
    print(Fore.YELLOW + "bot starts in 10 seconds")
    time.sleep(10)
    print(Fore.YELLOW + "starting bot..\n")
    time.sleep(0.1)
    #deflation_s1()
    pop_farmer()

def hero_place(): # Sauda / obyn
    hero_poss = [548, 111] #[439, 440]
    mouse.move(hero_poss[0], hero_poss[1])
    key.press("u")
    key.release("u")
    time.sleep(0.1)
    mouse.click(button="left")

def extra_tower_xp():
    extra_tower1_poss = [1429, 538]
    targeting_poss = [84, 364]
    mouse.move(extra_tower1_poss[0], extra_tower1_poss[1])
    key.press("w") # N = mortar monekey B = helikopter w = boomerang 
    key.release("w") # N = mortar monekey B = helikopter w = boomerang
    time.sleep(0.2)
    mouse.click(button="left")
    time.sleep(0.2)
    mouse.move(extra_tower1_poss[0], extra_tower1_poss[1])
    mouse.click(button="left")
    time.sleep(0.2)
    mouse.move(targeting_poss[0], targeting_poss[1])
    mouse.click(button="left")

def screenCapture():
    key.wait("alt+f3")
    img = pyautogui.screenshot(region=(1435, 29, 175, 60))
    
    numpyImage = np.array(img)
    greyImage = cv2.cvtColor(numpyImage, cv2.COLOR_BGR2GRAY)

    final_image = cv2.threshold(greyImage, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
   
    text = pytesseract.image_to_string(final_image,  config='--psm 7').replace("\n", "")
    fixed_text = text.replace("a", "")

    if re.search(r"(\d+/\d+)", fixed_text):
        return fixed_text
        
    else:
        print(Fore.RED + "active round NOT found!")
        return None
    
def victory_detect():
    #key.wait("alt+f3")
    wicktory_detected = pyautogui.locateOnScreen("Victory.png", confidence=0.9)
    if wicktory_detected == None:
        return False
    else:
        return True

def defeat_detect():
    #key.wait("alt+f3")
    defeat_detected = pyautogui.locateOnScreen("Defeat.png", confidence=0.9)
    if defeat_detected == None:
        return False
    else:
        return True

def game_over_detect():
    #key.wait("alt+f3")
    game_over_detect = pyautogui.locateOnScreen("Game_over.png", confidence=0.9)  
    if game_over_detect == None:
        return False
    else:
        return True

def level_up_detect():
    #key.wait("alt+f3")
    level_up_detect = pyautogui.locateOnScreen("level_up.png", confidence=0.9)
    if level_up_detect == None:
        return False
    else:
        return True

def monkey_knowlage_detect():
    #key.wait("alt+f3")
    monkey_knowlage_detect = pyautogui.locateOnScreen("monkey_knowlage.png", confidence=0.9)
    if monkey_knowlage_detect == None:
        return False
    else:
        return True

def insta_monkey_detect():
    #key.wait("alt+f3")
    insta_monkey_detect = pyautogui.locateOnScreen("insta_monkey.png", confidence=0.9)
    if insta_monkey_detect == None:
        return False
    else:
        return True

def pause_detect():
    #key.wait("alt+f3")
    pause_detect = pyautogui.locateOnScreen("pause.png", confidence=0.9)
    if pause_detect == None:
        return False
    else:
        return True

def restart_game():
    Victory = victory_detect() # True or False
    defeat = defeat_detect() # True or False
    game_over = game_over_detect() # True or False
    level_up = level_up_detect() # True or False
    monkey_knowlage = monkey_knowlage_detect() # True or False
    insta_monkey = insta_monkey_detect() # True or False
    if Victory == True:
        mouse.move(958, 895, duration=0.1)
        time.sleep(0.4)
        mouse.click(button="left")
        time.sleep(0.4)
        mouse.move(1190, 816, duration=0.1)
        time.sleep(2)
        mouse.click(button="left")
        mouse.move(1596, 29, duration = 0.5) # 947, 740
        mouse.click(button="left")
        time.sleep(1)
        mouse.move(1596, 29, duration=0.1) #pause menu button position
        time.sleep(0.4)
        mouse.click(button="left")
        mouse.move(1068, 836, duration=0.1) # restart button position
        time.sleep(0.4)
        mouse.click(button="left")
        mouse.move(1163, 717, duration=0.1) #confirmation button position
        time.sleep(0.3)
        mouse.click(button="left")

    elif defeat == True:
        mouse.move(945, 811, duration=0.1)
        time.sleep(0.2)
        mouse.click(button="left")
        time.sleep(0.2)
        mouse.move(1101, 712, duration=0.1)
        time.sleep(0.2)
        mouse.click(button="left")

    elif game_over == True:
        mouse.move(950, 901, duration=0.1)
        time.sleep(0.2)
        mouse.click(button="left")
        time.sleep(0.2)
        mouse.move(950, 770, duration=0.1)
        time.sleep(0.2)
        mouse.click(button="left")
        time.sleep(0.2)
        mouse.move(1108, 714, duration=0.1)
        time.sleep(0.2)
        mouse.click(button="left")
        time.sleep(0.2)
    
    elif level_up == True:
        current_lv() # om lv blir 155 s?? kan boten st??ngas av.
        
        mouse.move(835, 538, duration=0.1) #center of the screen
        time.sleep(0.2)
        mouse.click(button="left")
        time.sleep(0.3)
        mouse.click(button="left")
        time.sleep(0.2)
        restart_game()

    elif monkey_knowlage == True:
        mouse.move(835, 538, duration=0.1) #center of screen
        mouse.click(button="left")
        time.sleep(0.2)
        print(Fore.GREEN + "Monkey knowlage detected!")
        restart_game()

    elif insta_monkey == True:
        mouse.move(835, 538, duration=0.1) #center of screen
        mouse.click(button="left")
        time.sleep(0.2)
        print(Fore.GREEN + "Insta monkey detected!")
        restart_game()

    elif pause_detect == True:
        mouse.move(1068, 836, duration=0.1)
        time.sleep(0.2)
        mouse.click(button="left")
        time.sleep(0.2)
        pop_farmer()

    else:
        time.sleep(0.2)
        restart_game()

def deflation_s1(): # #ouch map
    print(Fore.CYAN + "bot started!")
    key.press_and_release("alt")
    time.sleep(0.2)
    monkeyV_place()
    time.sleep(0.2)
    monkeyV_upgrade1()
    time.sleep(0.2)
    plane_place()
    time.sleep(0.2)
    plane_upgrade()
    time.sleep(0.2)
    alchermist_place()
    time.sleep(0.2)
    alchermist_upgrade()
    time.sleep(0.2)
    monkeyV_sell()
    time.sleep(0.2)
    monkeyV_sell2()
    time.sleep(0.2)
    hero_place()
    time.sleep(0.2)
    monkeyV_upgrade2()
    time.sleep(0.2)
    extra_tower_xp()
    time.sleep(0.2)
    start_game()
    time.sleep(15)
    print(Fore.YELLOW + "restart process started...")
    restart_game()
    time.sleep(0.2)
    deflation_s1()

def pop_farmer(): #dark kastle map
    n = 0
    print(Fore.CYAN + "bot started!")  
    key.press_and_release("alt")
    mouse.move(958, 895, duration=0.1) #center of the screen
    key.press_and_release("z")
    time.sleep(0.2)
    key.press_and_release("space")
    time.sleep(0.2)
    key.press_and_release("space")
    time.sleep(0.2)
    restart_game()
    time.sleep(0.2)
    pop_farmer()

def main():
    directory_check()
    print(Fore.CYAN + "Starting process...\n")
    start()
    

#get_mouse_position()

#restart_game()

#screenCapture()

# color coding in console:
# red = error/bad, 
# green = success/good, 
# yellow = progress/processing/in-process/ongoing change.
# blue = information/informative/notification/notification.
#this earns you 59,735 account xp every 5-6 mins. (60min = 597,350 xp ish)
#var lv 124 men resetartade
# account ID: VPLUUFECY
main()