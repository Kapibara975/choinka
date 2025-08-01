range3: neopixel.Strip = None
range22: neopixel.Strip = None
r2: neopixel.Strip = None
r1: neopixel.Strip = None
range2: neopixel.Strip = None
strip: neopixel.Strip = None
tylko = 0
prędkość = 0
def _5():
    range3.show_color(neopixel.rgb(250, 0, 200))
    range22.show_color(neopixel.rgb(225, 0, 185))
    r2.show_color(neopixel.rgb(113, 0, 63))
    r1.show_color(neopixel.rgb(56, 0, 36))
    range2.show_color(neopixel.rgb(28, 0, 6))
def _2():
    range3.show_color(neopixel.rgb(250, 200, 0))
    range22.show_color(neopixel.rgb(225, 185, 0))
    r2.show_color(neopixel.rgb(113, 63, 0))
    r1.show_color(neopixel.rgb(56, 36, 0))
    range2.show_color(neopixel.rgb(28, 6, 0))

def on_button_pressed_a():
    global strip, tylko, range2, r1, r2, range22, range3, prędkość
    strip = neopixel.create(DigitalPin.P0, 60, NeoPixelMode.RGB)
    tylko = 0
    range2 = strip.range(0, 1)
    r1 = strip.range(1, 1)
    r2 = strip.range(2, 1)
    range22 = strip.range(3, 1)
    range3 = strip.range(4, 1)
    music.set_volume(255)
    music.play(music.string_playable("C F - F G F E D ", 160),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("D G - G A G F E ", 160),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C - C A - A B A ", 160),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G F D C - C D G ", 160),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("E C F A C5 F - - ", 160),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_leds("""
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . # . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # . # . #
        . # # # .
        # # # # #
        . # # # .
        # . # . #
        """)
    while tylko == 0:
        _2()
        for index in range(15):
            prędkość = pins.map(pins.analog_read_pin(AnalogReadWritePin.P1),
                0,
                1023,
                10,
                100)
            strip.shift(1)
            strip.show()
            basic.pause(prędkość)
        _3()
        for index2 in range(15):
            prędkość = pins.map(pins.analog_read_pin(AnalogReadWritePin.P1),
                0,
                1023,
                10,
                100)
            strip.shift(1)
            strip.show()
            basic.pause(prędkość)
        _4()
        for index3 in range(15):
            prędkość = pins.map(pins.analog_read_pin(AnalogReadWritePin.P1),
                0,
                1023,
                10,
                100)
            strip.shift(1)
            strip.show()
            basic.pause(prędkość)
        _5()
        for index4 in range(15):
            prędkość = pins.map(pins.analog_read_pin(AnalogReadWritePin.P1),
                0,
                1023,
                10,
                100)
            strip.shift(1)
            strip.show()
            basic.pause(prędkość)
input.on_button_pressed(Button.A, on_button_pressed_a)

def _4():
    range3.show_color(neopixel.rgb(0, 200, 250))
    range22.show_color(neopixel.rgb(0, 185, 225))
    r2.show_color(neopixel.rgb(0, 63, 113))
    r1.show_color(neopixel.rgb(0, 36, 56))
    range2.show_color(neopixel.rgb(0, 6, 28))

def on_button_pressed_b():
    global tylko
    basic.show_leds("""
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . # . .
        """)
    tylko += 1
    strip.clear()
    music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)

def _3():
    range3.show_color(neopixel.rgb(200, 250, 0))
    range22.show_color(neopixel.rgb(185, 225, 0))
    r2.show_color(neopixel.rgb(63, 113, 0))
    r1.show_color(neopixel.rgb(36, 56, 0))
    range2.show_color(neopixel.rgb(6, 28, 0))