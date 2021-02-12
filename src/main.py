import json, sys, time
from colorama import Fore
import keyboard
import config

DEBUG = False

class Main():
    def __init__(self, debug=False) -> None:
        self.debug = debug

    def __print(self, txt: str) -> str:
        if self.debug:
            print(txt)
    
    def __loadSnippets(self):
        try:
            for snippet in config.snippets:
                if len(snippet) < 2 or len(snippet) > 2:
                    self.__print("Snippet invalid, passing;")
                    pass
                else:
                    self.__print("Snippet is valid, adding abbreviation;")
                    exec(f"keyboard.add_abbreviation(\"{snippet[0]}\", \"{snippet[1]}\")")
            self.__print("\nLoaded snippets;\n")
        except Exception as e:
            print(f"\n\nERROR OCCORED WHILE LOADIND SNIPPETS: {e}\n\n")
            time.sleep(10)
            quit()

    def __mainLoop(self):
        while True:
            time.sleep(1)
            self.__print("\nRunning loop;\n")
            if keyboard.is_pressed("ESC"):
                self.__print("\nESC is pressed, exiting loop;\n")
                break

    def run(self):
        self.__loadSnippets()
        self.__mainLoop()

if __name__ == "__main__":
    try:
        main = Main(debug=DEBUG)
        main.run()
        quit()
    except KeyboardInterrupt:
        print("Exiting...")