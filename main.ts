input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("steps")
    basic.showNumber(steps)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    steps += 1
})
let steps = 0
basic.showIcon(IconNames.Heart)
steps = 0
basic.forever(function on_forever() {
    
})
