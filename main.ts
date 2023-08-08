let pin0Dir = 90
let pin1Dir = 90
let pin2Dir = 90
let pin3Dir = 45
Servo.Servo(4, pin0Dir)
Servo.Servo(5, pin1Dir)
Servo.Servo(2, pin2Dir)
Servo.Servo(6, pin3Dir)
basic.forever(function () {
    pin1Dir = 160
    pin3Dir = 0
    Servo.Servo(5, pin1Dir)
    Servo.Servo(6, pin3Dir)
    basic.pause(1000)
    pin2Dir = 0
    Servo.Servo(2, pin2Dir)
    basic.pause(1000)
    pin1Dir = 0
    pin3Dir = 180
    Servo.Servo(5, pin1Dir)
    Servo.Servo(6, pin3Dir)
    basic.pause(1000)
    pin0Dir = 0
    Servo.Servo(4, pin0Dir)
    basic.pause(1000)
    pin1Dir = 160
    pin3Dir = 0
    Servo.Servo(5, pin1Dir)
    Servo.Servo(6, pin3Dir)
    basic.pause(1000)
    pin2Dir = 0
    Servo.Servo(2, pin2Dir)
    basic.pause(1000)
    pin2Dir = 90
    Servo.Servo(2, pin2Dir)
    basic.pause(1000)
    pin1Dir = 0
    pin3Dir = 180
    Servo.Servo(5, pin1Dir)
    Servo.Servo(6, pin3Dir)
    basic.pause(1000)
    pin0Dir = 90
    Servo.Servo(4, pin0Dir)
    basic.pause(1000)
})
basic.forever(function () {
	
})
