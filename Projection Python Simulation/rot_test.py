import math

class Camera:
    def __init__(self, fov, pan, tilt, position):
        self.fov = float(fov)
        self.pan = float(pan)
        self.tilt = float(tilt)
        self.position = position

    def set_pan(self, pan):
        global cp
        global sp
        self.pan = float(pan)
        cp = math.cos(pan)
        sp = math.sin(pan)

    def set_tilt(self, tilt):
        global ct
        global st
        self.tilt = float(tilt)
        ct = math.cos(tilt)
        st = math.sin(tilt)


class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


camera = Camera(90, math.pi/2, 0.0, Point(2, 3, 5))
wp = [2.0, 2.0, 5.0]

cx = camera.position.x
cy = camera.position.y
cz = camera.position.z

wx = wp[0]
wy = wp[1]
wz = wp[2]

sp = math.sin(camera.pan)
cp = math.cos(camera.pan)

st = math.sin(camera.tilt)
ct = math.cos(camera.tilt)

rel_x = wx*cp*ct + wy*sp*ct + wz*st - cx*cp*ct - cy*sp*ct - cz*st
rel_y = cx*sp + wy*cp - cy*cp - wx*sp
rel_z = -wx*cp*st - wy*sp*st + wz*ct + cx*cp*st + cy*sp*st - cz*ct

print("(" + str(rel_x) + "," + str(rel_y) + "," + str(rel_z) + ")")

