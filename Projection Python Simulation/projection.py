import math

sp = None
cp = None
st = None
ct = None

max_x = None
max_y = None

class VectorDefinition:
    def __init__(self, forward, right, up):
        self.forward = forward
        self.right = right
        self.up = up

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def reverse(self):
        return Point(-self.x, -self.y, -self.z)

class Camera:
    def __init__(self, fov, pan, tilt, position):
        self.fov = float(fov)
        self.pan = float(pan)
        self.tilt = float(tilt)
        self.position = position

        self.direction = VectorDefinition(Vector(1, 0, 0), Vector(0, -1, 0), Vector(0, 0, 1))

    def set_pan(self, pan):
        global cp
        global sp
        self.pan = float(pan)
        cp = math.cos(pan)
        sp = math.sin(pan)
        self.update_direction()

    def set_tilt(self, tilt):
        global ct
        global st
        self.tilt = float(tilt)
        ct = math.cos(tilt)
        st = math.sin(tilt)
        self.update_direction()

    def update_position(self, vector, scalar):
        self.position.x += vector.x * scalar
        self.position.y += vector.y * scalar
        self.position.z += vector.z * scalar

    def update_direction(self):
        global cp
        global sp
        global ct
        global st

        self.direction.forward = Vector(ct*cp, ct*sp, st)
        self.direction.right = Vector(sp, math.cos(self.pan + math.pi), 0)
        self.direction.up = Vector(-cp*st, -sp*st, ct)

    def get_specs(self):
        return "x: " + str(self.position.x) + ", y: " + str(self.position.y) + ", z: " + str(self.position.z) + ", pan: " + str(self.pan) + ", tilt: " + str(self.tilt)


class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


def map_point(world, cam):
    global cp
    global sp
    global ct
    global st

    global max_x
    global max_y

    # Redefine variables to make equations more readable
    cx = cam.position.x
    cy = cam.position.y
    cz = cam.position.z

    wx = world.x
    wy = world.y
    wz = world.z

    # Convert points to frame of reference of camera using a translation matrix for camera offset, a rotation matrix
    # for the pan angle, and another rotation matrix for the tilt angle
    rel_x = wx*cp*ct + wy*sp*ct + wz*st - cx*cp*ct - cy*sp*ct - cz*st
    rel_y = cx*sp + wy*cp - cy*cp - wx*sp
    rel_z = -wx*cp*st - wy*sp*st + wz*ct + cx*cp*st + cy*sp*st - cz*ct

    if rel_x <= 0:
        # Invalid depth or out of range
        return [-1, -1]

    # Convert to screen coordinates using similar triangles
    x = rel_y/(rel_x*math.tan(cam.fov/2.0))
    y = rel_z/(rel_x*math.tan(cam.fov/2.0))

    # Convert to pygame coordinates by changing origin to center of screen
    x_map = max_x - (x + max_x/2.0)
    y_map = max_y - (y + max_y/2.0)

    if x_map > max_x or x_map < 0 or y_map > max_y or y_map < 0:
        return [-1, -1]
    return [x_map, y_map]
