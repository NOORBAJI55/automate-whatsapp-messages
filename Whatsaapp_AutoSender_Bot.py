import pyautogui as pg
import time

print("Program will run after 5 seconds. Please focus WhatsApp Web and open the chat.")
time.sleep(5)
print("Sending messages...")

for i in range(10):
    pg.write("Fuck U Bitch 💖")
    pg.press("enter")
    time.sleep(1)

print("Done!")
