def checkWin():
    if not (ARoll == 0) and not (BRoll == 0):
        control.wait_micros(1000000)
        while True:
            basic.clear_screen()
            if ARoll == BRoll:
                basic.show_string("Remiza")
            elif ARoll > BRoll:
                basic.show_string("A Vyhrava")
            elif ARoll < BRoll:
                basic.show_string("B Vyhrava")
def updateScreen():
    basic.clear_screen()
    if ARoll == 1:
        led.plot(0, 2)
    elif ARoll == 2:
        led.plot(0, 2)
        led.plot(0, 3)
    elif ARoll == 3:
        led.plot(0, 2)
        led.plot(0, 3)
        led.plot(0, 4)
    elif ARoll == 4:
        led.plot(0, 2)
        led.plot(0, 4)
        led.plot(1, 2)
        led.plot(1, 4)
    elif ARoll == 5:
        led.plot(0, 2)
        led.plot(0, 3)
        led.plot(0, 4)
        led.plot(1, 2)
        led.plot(1, 4)
    elif ARoll == 6:
        led.plot(0, 2)
        led.plot(0, 3)
        led.plot(0, 4)
        led.plot(1, 2)
        led.plot(1, 3)
        led.plot(1, 4)
    if BRoll == 1:
        led.plot(3, 2)
    elif BRoll == 2:
        led.plot(3, 2)
        led.plot(3, 3)
    elif BRoll == 3:
        led.plot(3, 2)
        led.plot(3, 3)
        led.plot(3, 4)
    elif BRoll == 4:
        led.plot(3, 2)
        led.plot(3, 4)
        led.plot(4, 2)
        led.plot(4, 4)
    elif BRoll == 5:
        led.plot(3, 2)
        led.plot(3, 3)
        led.plot(3, 4)
        led.plot(4, 2)
        led.plot(4, 4)
    elif BRoll == 6:
        led.plot(3, 2)
        led.plot(3, 3)
        led.plot(3, 4)
        led.plot(4, 2)
        led.plot(4, 3)
        led.plot(4, 4)

def on_button_pressed_a():
    global ARoll
    if ARoll == 0:
        index = 0
        while index <= randint(1, 10):
            ARoll = randint(1, 6)
            updateScreen()
            control.wait_micros(100000)
            index += 1
    checkWin()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global BRoll
    if BRoll == 0:
        index2 = 0
        while index2 <= randint(1, 10):
            BRoll = randint(1, 6)
            updateScreen()
            control.wait_micros(100000)
            index2 += 1
    checkWin()
input.on_button_pressed(Button.B, on_button_pressed_b)

BRoll = 0
ARoll = 0
ARoll = 0
BRoll = 0

def on_forever():
    pass
basic.forever(on_forever)
