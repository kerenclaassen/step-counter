def on_button_pressed_a():
    basic.show_string("steps")
    basic.show_number(steps)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global steps
    steps += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

steps = 0
basic.show_icon(IconNames.HEART)
steps = 0

def on_forever():
    pass
basic.forever(on_forever)