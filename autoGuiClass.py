import datetime
import pyautogui
import time

class AutoGui(object):

    def __init__(self,windows):
        self.windows = windows


    @staticmethod
    def datetimeNow():
        return datetime.datetime.now()

    def character(self,str):
        return "{0}\{1}.png".format(self.windows , str)

    def makeEquasion(self,str):
        for oneChar in str:
            located      = self.character(oneChar)
            locatedRaw   = located[5:6]
            toClick      = pyautogui.locateCenterOnScreen(located)
            coordinates  = pyautogui.position()

            if toClick is None:
                czas = 1.1
                print("{} | Nie znaleziono {} czekam {}s ".format(AutoGui.datetimeNow(), locatedRaw , czas))
                time.sleep(czas)
                toClick = pyautogui.locateCenterOnScreen(located)

            if toClick is not None:
                pyautogui.click(toClick)
                print("{} | Znaleziono     {} - x,y {}".format(AutoGui.datetimeNow() , locatedRaw, coordinates ))
            else:
                print("{} | Nie ma elementu{} ".format(AutoGui.datetimeNow(), locatedRaw))

    def iterate(self, table):
        for element in table:
            self.makeEquasion(element)

    def shortcuts(self):
        for i in range(1,5):
            print('{} | Alt + {}'.format(AutoGui.datetimeNow(), i))
            pyautogui.hotkey('Alt', '{}'.format(i))
            time.sleep(1)