import pygame
import math
import json
from projection import Point, Camera, map_point
import projection

# Define canvas size
projection.max_x = 600.0
projection.max_y = 600.0

# Create my pygame canvas
pygame.init()
canvas = pygame.display.set_mode((projection.max_x, projection.max_y))
pygame.display.set_caption("3D Projection")

# Define camera properties and create camera object
position = Point(0.0, 0.0, 0.0)
fov = math.pi/4.0  # in radians
pan = 0.0  # in radians
tilt = 0.0  # in radians
max_tilt = math.pi/4.0  # in radians

projection.cp = math.cos(pan)
projection.sp = math.sin(pan)
projection.ct = math.cos(tilt)
projection.st = math.sin(tilt)

camera = Camera(fov, pan, tilt, position)

# Load points data from points.json file
with open('points.json', 'r') as file:
    data = json.load(file)

# Set basic parameters for game functionality
fps = 60.0
movement_sens = 2.0 / fps
rotate_sens = 0.3 / fps
background = (255, 255, 255)
clock = pygame.time.Clock()
pressedExit = False
pygame.mouse.set_visible(0)
pygame.event.set_grab(True)


# MAIN GAME LOOP
while not pressedExit:
    # For measuring performance and calibrating sensitivities
    dt = clock.tick()
    """print(clock.get_fps())"""

    # Fill background
    canvas.fill(background)

    # Render axes
    origin = map_point(Point(0, 0, 0), camera)
    axis_length = 3
    if origin != [-1, -1]:
        x_axis = map_point(Point(axis_length, 0, 0), camera)
        y_axis = map_point(Point(0, axis_length, 0), camera)
        z_axis = map_point(Point(0, 0, axis_length), camera)
        if x_axis != [-1, -1]:
            pygame.draw.line(canvas, (255, 0, 0), origin, x_axis)
        if y_axis != [-1, -1]:
            pygame.draw.line(canvas, (0, 255, 0), origin, y_axis)
        if z_axis != [-1, -1]:
            pygame.draw.line(canvas, (0, 0, 255), origin, z_axis)

    # Render points from file
    for i in range(len(data)):
        curr_point_1 = map_point(Point(data[i][0][0], data[i][0][1], data[i][0][2]), camera)
        curr_point_2 = map_point(Point(data[i][1][0], data[i][1][1], data[i][1][2]), camera)
        if curr_point_1 != [-1, -1] and curr_point_2 != [-1, -1]:
            pygame.draw.line(canvas, (0, 0, 0), curr_point_1, curr_point_2)
        else:
            print("FAIL")

    # Detect and apply movement
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
            pressedExit = True

        # Forwards (w)
        if keys[pygame.K_w]:
            camera.update_position(camera.direction.forward, movement_sens)

        # Left (a)
        if keys[pygame.K_a]:
            camera.update_position(camera.direction.right.reverse(), movement_sens)

        # Backwards (s)
        if keys[pygame.K_s]:
            camera.update_position(camera.direction.forward.reverse(), movement_sens)

        # Right (d)
        if keys[pygame.K_d]:
            camera.update_position(camera.direction.right, movement_sens)

        # Up (q)
        if keys[pygame.K_q]:
            camera.update_position(camera.direction.up, movement_sens)

        # Down (e)
        if keys[pygame.K_e]:
            camera.update_position(camera.direction.up.reverse(), movement_sens)

        if keys[pygame.K_p]:
            pressedExit = True

    # Handle camera rotation
    mouse_movement = pygame.mouse.get_rel()

    # Pan
    camera.set_pan(camera.pan + rotate_sens*-mouse_movement[0])

    # Tilt
    target_tilt = camera.tilt + rotate_sens*-mouse_movement[1]
    if abs(target_tilt) < max_tilt:
        camera.set_tilt(target_tilt)


    # Update new canvas to display
    pygame.display.update()

    # Lock game at fps
    clock.tick(fps)

    # Debug message
    print(camera.get_specs())




