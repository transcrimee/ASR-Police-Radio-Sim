import ctypes
import time

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("ki", KEYBDINPUT)]
    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_ulong), ("_input", _INPUT)]

# Constants
INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_SCANCODE = 0x0008

def press_key(scan_code):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wScan=scan_code, dwFlags=KEYEVENTF_SCANCODE, wVk=0, time=0, dwExtraInfo=None))
    ctypes.windll.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def release_key(scan_code):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wScan=scan_code, dwFlags=KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, wVk=0, time=0, dwExtraInfo=None))
    ctypes.windll.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

# Example: Press and release W key (Scan code for W is 0x11)
time.sleep(2)  # Give you 2 seconds to focus the game
press_key(0x11)
time.sleep(0.1)
release_key(0x11)
