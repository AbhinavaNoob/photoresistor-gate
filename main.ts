let allow = 0
basic.forever(function () {
    allow = pins.digitalReadPin(DigitalPin.P2)
    if (allow < 1) {
        basic.pause(2000)
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else {
        basic.pause(2000)
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
})
