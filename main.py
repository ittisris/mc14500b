def on_microbit_id_button_b_pin_evt_rise():
    led.plot(0, 0)
    basic.pause(100)
    led.unplot(0, 0)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_B,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_button_b_pin_evt_rise)

def on_microbit_id_io_p0_pin_evt_rise():
    basic.show_number(pc)
control.on_event(EventBusSource.MICROBIT_ID_IO_P0,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_io_p0_pin_evt_rise)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(500)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(500)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_microbit_id_io_p0_pin_evt_fall():
    global pc
    pc = pc + 1
    if pc > 9:
        pc = 0
control.on_event(EventBusSource.MICROBIT_ID_IO_P0,
    EventBusValue.MICROBIT_PIN_EVT_FALL,
    on_microbit_id_io_p0_pin_evt_fall)

pc = 0
led.set_brightness(100)
pins.set_pull(DigitalPin.P1, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P0, PinPullMode.PULL_NONE)
pc = 0

def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        led.plot(4, 0)
    else:
        led.unplot(4, 0)
    basic.pause(100)
basic.forever(on_forever)
