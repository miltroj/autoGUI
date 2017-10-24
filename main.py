from autoGuiClass import *


classAutoGui = AutoGui("win7")


if __name__ == "__main__":

    stringTab = ['c','123456789_x-+=,0' , 'c' ]

    exampleData = input( "> insert equation ")
    time.sleep(2)

    classAutoGui.iterate(exampleData)

    time.sleep(1)
    print("\nMake actions from action list {}\n".format(stringTab))

    classAutoGui.iterate(stringTab)

    time.sleep(1)
    classAutoGui.shortcuts()