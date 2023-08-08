                                                                                                                                                                                                                                                                                                                                                                                          pin0Dir = 90
pin1Dir = 90
pin2Dir = 90
pin3Dir = 45
Servo.servo(4, pin0Dir)
Servo.servo(5, pin1Dir)
Servo.servo(2, pin2Dir)
Servo.servo(6, pin3Dir)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    global pin1Dir, pin3Dir, pin2Dir, pin0Dir
    pin1Dir = 160
    pin3Dir = 0
    Servo.servo(5, pin1Dir)
    Servo.servo(6, pin3Dir)
    basic.pause(1000)
    pin2Dir = 0
    Servo.servo(2, pin2Dir)
    basic.pause(1000)
    pin1Dir = 0
    pin3Dir = 180
    Servo.servo(5, pin1Dir)
    Servo.servo(6, pin3Dir)
    basic.pause(1000)
    pin0Dir = 0
    Servo.servo(4, pin0Dir)
    basic.pause(1000)
    pin1Dir = 160
    pin3Dir = 0
    Servo.servo(5, pin1Dir)
    Servo.servo(6, pin3Dir)
    basic.pause(1000)
    pin2Dir = 0
    Servo.servo(2, pin2Dir)
    basic.pause(1000)
    pin2Dir = 90
    Servo.servo(2, pin2Dir)
    basic.pause(1000)
    pin1Dir = 0
    pin3Dir = 180
    Servo.servo(5, pin1Dir)
    Servo.servo(6, pin3Dir)
    basic.pause(1000)
    pin0Dir = 90
    Servo.servo(4, pin0Dir)
    basic.pause(1000)
basic.forever(on_forever2)
