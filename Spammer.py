import pyautogui, time

time.sleep(10)
f = open("beemovie.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    time.sleep(1)
    pyautogui.press("enter")