# https://poki.pl/g/stick-merge

import time
import random
import keyboard
import pyautogui as pgui

top_right_corner = (330, 220)
y = 280
x = 900

inventory_slots = [(895, 170), (892, 272), (891, 368), (890, 474), (1027, 166), (1018, 266), (1018, 363), (1023, 470),
                   (1142, 165), (1138, 272), (1148, 373), (1141, 471)]


def upgrade_guns():
    # Program tries to buy guns
    for i in range(4):
        pgui.click(1037, 579)
    # Program shuffles items at random trying to merge them
    for i in range(len(inventory_slots)):
        if i != len(inventory_slots):
            pgui.moveTo(inventory_slots[i-1])
            pgui.mouseDown()
            pgui.dragTo(inventory_slots[random.randint(0, 11)], button='left')
        if keyboard.is_pressed('ctrl'):
            break

if __name__ == "__main__":
    # 2 seconds to give time to alt-tab to browser
    time.sleep(2)
    # Main loop, ctrl key is failsafe. Needs to be pressed for a while.
    while keyboard.is_pressed('ctrl') == False:
        # program checks upper and lower lever for black pixels. If found it moves cursor over the found pixel.
        for height in range(0, 40, 20):
            for width in range(0, x, 15):
                if pgui.pixel(top_right_corner[0] + width, top_right_corner[1] + height)[0] == 0:
                    pgui.moveTo((top_right_corner[0] + width, top_right_corner[1] + height))

        # Second level. Bit lazy coding, but it isn't worth a separate function I guess.
        for height in range(190, 230, 20):
            for width in range(0, x, 15):
                if pgui.pixel(top_right_corner[0] + width, top_right_corner[1] + height)[0] == 0:
                    pgui.moveTo((top_right_corner[0] + width, top_right_corner[1] + height))

        # If level if finished, program clicks "ok" button to get back to inventory screen.
        pgui.moveTo(646, 634)
        if pgui.pixelMatchesColor(646, 634, (46, 181, 49)):
            pgui.click(646, 634)

        # Then accept other popup windows and proceeds with buying new items.
        if pgui.pixelMatchesColor(836, 506, (46, 181, 49)):
            pgui.click(836, 506)
            time.sleep(1)
            pgui.click(804, 530)
            # Repeats shuffling 10 times.
            for i in range(11):
                upgrade_guns()
