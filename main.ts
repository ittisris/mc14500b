input.onPinPressed(TouchPin.P0, function () {
    led.plot(0, 0)
})
input.onPinReleased(TouchPin.P0, function () {
    led.unplot(0, 0)
})
input.onButtonPressed(Button.B, function () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P1, 0)
    basic.pause(500)
})
pins.setPull(DigitalPin.P0, PinPullMode.PullUp)
basic.forever(function () {
	
})
