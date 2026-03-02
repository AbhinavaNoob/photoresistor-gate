allow = 0

def on_forever():
    global allow
    allow = pins.digital_read_pin(DigitalPin.P2)
    if allow < 1:
        basic.pause(2000)
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        basic.pause(2000)
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
