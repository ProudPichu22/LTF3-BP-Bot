import keyboard
import time

stop = 0

def stopProgram(test):
    global stop
    print(test)
    stop = 1

keyboard.hook_key("p", stopProgram)

while True:
    keyboard.wait("l")
    if stop:
        break

    while True:
        time.sleep(0.3)
        keyboard.press_and_release("Enter")
        if stop:
            stop = 0
            break
