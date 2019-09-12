import vars
import math

target = [
    {'lat': 0, 'lon': 0},
    {'lat': 100, 'lon': 0},
    {'lat': 100, 'lon': 100},
    {'lat': 0, 'lon': 100}
]

wayPoints = []

def angle_to_metres(lon, lat):
    t = []
    t.append(lon * (111321) * math.cos(lat / math.pi * 180))
    t.append(lat * 111134)  # metres
    return t


def dist(x1, y1, z1, x2, y2, z2):
    a = (x1 - x2) * (x1 - x2)
    b = (y1 - y2) * (y1 - y2)
    c = (z1 - z2) * (z1 - z2)
    return math.sqrt(a + b + c)


def min_battery_to_shot_area(h, A, B):
    a1 = 2 * math.tan(A / 2 / math.pi * 180) * h
    b1 = 2 * math.tan(B / 2 / math.pi * 180) * h
    print("###", h, a1, b1)
    n_a = abs(target[0]['x'] - target[2]['x']) / a1 + min(abs(target[0]['x'] - target[2]['x']) % a1, 1)
    n_b = abs(target[0]['y'] - target[2]['y']) / b1 + min(abs(target[0]['y'] - target[2]['y']) % b1, 1)
    wayPoints.clear()
    for i in range(0, int(n_a)):
        for j in range(0, int(n_b)):
            point_x = i * a1 + target[0]['x'] + a1 / 2
            point_y = j * b1 + target[0]['y'] + b1 / 2
            wayPoints.append([point_x, point_y])
    num_of_shots = n_a * n_b
    var1 = n_a * (abs(target[0]['y'] - target[2]['y']) - b1) + abs(target[0]['x'] - target[2]['x']) - a1
    var2 = abs(target[0]['y'] - target[2]['y']) - b1 + n_b * (abs(target[0]['x'] - target[2]['x']) - a1)
    return min(var1, var2) * vars.battery_usage_per_meter + num_of_shots * vars.battery_usage_shot





def start():
    for i in range(0, 4):
        t = angle_to_metres(target[i]['lon'], target[i]['lat'])
        target[i].update({'x': t[0]})
        target[i].update({'y': t[1]})
    t = angle_to_metres(vars.drone[i]['lon'], vars.drone[i]['lat'])
    vars.drone.update({'x': t[0]})
    vars.drone.update({'y': t[1]})



def get_height():
    l = 1
    r = 1000
    var = 0
    while (r - l > 1):
        m = (l + r) / 2
        var1 = min_battery_to_shot_area(m, vars.A, vars.B)
        var2 = min_battery_to_shot_area(m, vars.B, vars.A)
        if (vars.battery_remaining -  var1 >= vars.battery_remaining / 100 * 5 or vars.battery_remaining -  var2 >= vars.battery_remaining / 100 * 5):
            r = m
        else:
            l = m
    var1 = min_battery_to_shot_area(l, vars.A, vars.B)
    var2 = min_battery_to_shot_area(l, vars.B, vars.A)
    if (vars.battery_remaining - var1 >= vars.battery_remaining / 100 * 5 or vars.battery_remaining - var2 >= vars.battery_remaining / 100 * 5):
        return l
    else:
        return r

target[0].update({'x': 0, 'y': 0})
target[1].update({'x': 0, 'y': 100})
target[2].update({'x': 100, 'y': 100})
target[3].update({'x': 100, 'y': 0})
vars.drone.update({'x': 0, 'y': 0})


print(vars.drone)
# dist1 = dist(vars.drone['x'], vars.drone['y'], vars.drone['alt'], target[0]['x'], target[0]['y'], 0)
# dist2 = dist(vars.drone['x'], vars.drone['y'], vars.drone['alt'], target[1]['x'], target[1]['y'], 0)
# dist3 = dist(vars.drone['x'], vars.drone['y'], vars.drone['alt'], target[2]['x'], target[2]['y'], 0)
# dist4 = dist(vars.drone['x'], vars.drone['y'], vars.drone['alt'], target[3]['x'], target[3]['y'], 0)
# minn = min(dist1, dist2, dist3, dist4)

final_h = get_height()
min_battery_to_shot_area(final_h, vars.A, vars.B)
print(final_h)
for i in range(0, len(wayPoints)):
    print(wayPoints[i][0], wayPoints[i][1])
