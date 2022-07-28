from PIL import ImageGrab
import time
import pyautogui


def press_key(key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    return


def has_collided(data):
    for x in range(670, 710):
        for y in range(330, 498):
            if data[x, y] < 171:
                press_key("down")

                print("Ducked")

                return

    for x in range(700, 800):
        for y in range(507, 547):
            if data[x, y] < 100:
                press_key("up")

                print("Jumped.")

                return

    return


if __name__ == "__main__":
    time.sleep(4)

    while True:
        screen = ImageGrab.grab().convert("L")
        data = screen.load()

        has_collided(data)

        # Tests for collision positioning
        # for x in range(660, 700):
        #     for y in range(330, 480):
        #         data[x, y] = 171
        #
        # for x in range(702, 790):
        #     for y in range(507, 547):
        #         data[x, y] = 100
        #
        # screen.show()
        # break
