import os
output = os.popen('wmic process get description, processid').read()
def check():
    if ("Telegram.exe" in output):
        return True
    elif ("Zoom.exe" in output):
        return True
    elif ("outlook.exe" in output):
        return True
    elif ("notepad.exe" in output):
        return True
    if ("idea64.exe" in output): #Intellij IDEA
        return True
    if ("studio64.exe" in output): #Android Studio
        return True
    if ("GithubDesktop.exe" in output): #Github Desktop
        return True
    if ("pycharm64.exe" in output): #PyCharm
        return True
