import os
import win32api
import win32console
import win32gui


def get_rect(console_id):
    if os.name == 'nt':
        rect = win32gui.GetWindowRect(console_id)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        return x, y, w, h


def get_console_id():
    if os.name == 'nt':
        return win32console.GetConsoleWindow()


def get_system_metrics():
    if os.name == 'nt':
        return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
