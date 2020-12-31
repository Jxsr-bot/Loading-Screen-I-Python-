import time
import os


def clear():
    print("\n" * 105)


class main:

    def loading_screen(self, name):
        loading_list = [' | ', ' / ', ' _ ', ' > ', ' < ', ' * ', '    ']

        for chr in loading_list:
            print(f"Loading {chr}")
            time.sleep(.6)
            clear()
