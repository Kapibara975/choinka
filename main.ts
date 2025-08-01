let range3: neopixel.Strip = null
let range22: neopixel.Strip = null
let r2: neopixel.Strip = null
let r1: neopixel.Strip = null
let range2: neopixel.Strip = null
let strip: neopixel.Strip = null
let tylko = 0
let prędkość = 0
function _5 () {
    range3.showColor(neopixel.rgb(250, 0, 200))
    range22.showColor(neopixel.rgb(225, 0, 185))
    r2.showColor(neopixel.rgb(113, 0, 63))
    r1.showColor(neopixel.rgb(56, 0, 36))
    range2.showColor(neopixel.rgb(28, 0, 6))
}
function _2 () {
    range3.showColor(neopixel.rgb(250, 200, 0))
    range22.showColor(neopixel.rgb(225, 185, 0))
    r2.showColor(neopixel.rgb(113, 63, 0))
    r1.showColor(neopixel.rgb(56, 36, 0))
    range2.showColor(neopixel.rgb(28, 6, 0))
}
input.onButtonPressed(Button.A, function () {
    strip = neopixel.create(DigitalPin.P0, 60, NeoPixelMode.RGB)
    tylko = 0
    range2 = strip.range(0, 1)
    r1 = strip.range(1, 1)
    r2 = strip.range(2, 1)
    range22 = strip.range(3, 1)
    range3 = strip.range(4, 1)
    music.setVolume(255)
    music.play(music.stringPlayable("C F - F G F E D ", 160), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("D G - G A G F E ", 160), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C - C A - A B A ", 160), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("G F D C - C D G ", 160), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("E C F A C5 F - - ", 160), music.PlaybackMode.InBackground)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . # . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        # . # . #
        . # # # .
        # # # # #
        . # # # .
        # . # . #
        `)
    while (tylko == 0) {
        _2()
        for (let index = 0; index < 15; index++) {
            prędkość = pins.map(
            pins.analogReadPin(AnalogReadWritePin.P1),
            0,
            1023,
            10,
            100
            )
            strip.shift(1)
            strip.show()
            basic.pause(prędkość)
        }
        _3()
        for (let index = 0; index < 15; index++) {
            prędkość = pins.map(
            pins.analogReadPin(AnalogReadWritePin.P1),
            0,
            1023,
            10,
            100
            )
            strip.shift(1)
            strip.show()
            basic.pause(prędkość)
        }
        _4()
        for (let index = 0; index < 15; index++) {
            prędkość = pins.map(
            pins.analogReadPin(AnalogReadWritePin.P1),
            0,
            1023,
            10,
            100
            )
            strip.shift(1)
            strip.show()
            basic.pause(prędkość)
        }
        _5()
        for (let index = 0; index < 15; index++) {
            prędkość = pins.map(
            pins.analogReadPin(AnalogReadWritePin.P1),
            0,
            1023,
            10,
            100
            )
            strip.shift(1)
            strip.show()
            basic.pause(prędkość)
        }
    }
})
function _4 () {
    range3.showColor(neopixel.rgb(0, 200, 250))
    range22.showColor(neopixel.rgb(0, 185, 225))
    r2.showColor(neopixel.rgb(0, 63, 113))
    r1.showColor(neopixel.rgb(0, 36, 56))
    range2.showColor(neopixel.rgb(0, 6, 28))
}
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . # . .
        `)
    tylko += 1
    strip.clear()
    music.stopAllSounds()
})
function _3 () {
    range3.showColor(neopixel.rgb(200, 250, 0))
    range22.showColor(neopixel.rgb(185, 225, 0))
    r2.showColor(neopixel.rgb(63, 113, 0))
    r1.showColor(neopixel.rgb(36, 56, 0))
    range2.showColor(neopixel.rgb(6, 28, 0))
}
