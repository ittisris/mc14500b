control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_B, EventBusValue.MICROBIT_PIN_EVT_RISE, function () {
    led.plot(0, 0)
    basic.pause(100)
    led.unplot(0, 0)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(pc)
    pc = pc + 1
    if (pc > 9) {
        pc = 0
    }
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P1, 0)
    basic.pause(500)
})
let pc = 0
pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
pc = 0
basic.forever(function () {
    basic.pause(500)
})
