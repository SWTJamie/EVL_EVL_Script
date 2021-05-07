import time
import pyautogui
import colorama
from colorama import Fore, Style, Back


popo=0


colorama.init(autoreset=True)
message = input(Fore.LIGHTYELLOW_EX + "welcome to the EVL script please say hello" +Fore.RED + "    A ____  A    w")
time.sleep(0.5)
message = input(Fore.LIGHTYELLOW_EX + "This is not an evil script" + Fore.RED +       "                   ( o\ _ /o )   I ")
time.sleep(0.5)
message = input(Fore.LIGHTYELLOW_EX + "are you ready? Y/N" + Fore.RED +   "                            [   .   ]___/I")
time.sleep(0.5)
message = input(Fore.LIGHTYELLOW_EX + "now please type strat " + Fore.RED +   "                         ]     [     I   ")



time.sleep(5)


pyautogui.hotkey("winleft", "m")
time.sleep(1)
pyautogui.hotkey("winleft", "shift", "m")

time.sleep(1)


pyautogui.hotkey("winleft", "shift", "1")
pyautogui.hotkey("winleft", "shift", "2")
pyautogui.hotkey("winleft", "shift", "3")
pyautogui.hotkey("winleft", "shift", "4")
pyautogui.hotkey("winleft", "shift", "5")
pyautogui.hotkey("winleft", "shift", "6")
pyautogui.hotkey("winleft", "shift", "7")
pyautogui.hotkey("winleft", "shift", "8")
pyautogui.hotkey("winleft", "shift", "9")

time.sleep(1)


while popo <= 30:
    time.sleep(0.3)
    pyautogui.hotkey("alt", "f4")
    time.sleep(0.3)
    pyautogui.press("enter")
    popo += 1
