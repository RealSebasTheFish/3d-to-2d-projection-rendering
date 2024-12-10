import math
from projection import Camera, Point, map_point
import projection


def screen_conv(cam, rel_x, rel_y, rel_z):
    x = rel_y/(rel_x*math.tan(cam.fov/2.0))
    y = rel_z/(rel_x*math.tan(cam.fov/2.0))

    x_map = 600.0 - (x* + 600.0/2.0)
    y_map = 600.0 - (y + 600.0/2.0)
    return [x_map, y_map]


fov = math.pi/4
pan = 0.1199999999
tilt = 0
position = Point(0.930273, -1.79417, 1.6333333)

projection.max_x = 600.0
projection.max_y = 600.0

projection.cp = math.cos(pan)
projection.sp = math.sin(pan)
projection.ct = math.cos(tilt)
projection.st = math.sin(tilt)

camera = Camera(fov, pan, tilt, position)

file = open("testdata.txt", "r")

for i in file:
    parse = i.split(", ")
    res = screen_conv(camera, float(parse[0][1:]), float(parse[1]), float(parse[2][:-2]))
    print("(" + str(res[0]) + ", " + str(res[1]) + ")")
