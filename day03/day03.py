import fileinput
import os
import tempfile
import turtle
import canvasvg
from functools import reduce
from itertools import product

def output(bob: turtle.Turtle, name = "t1.svg"):
    nameSav = "kita.png"
    tmpdir = tempfile.mkdtemp()  # create a temporary directory
    tmpfile = os.path.join(tmpdir, name)  # name of file to save SVG to
    ts = bob.getscreen().getcanvas()
    canvasvg.saveall(tmpfile, ts)
    bob.clear()

def main():
    grid = [bytearray(100000) for y in range(100000)]
    wire1, wire2 = [x.split(",") for x in fileinput.input()]
    isects = []

    bob = turtle.Turtle()
    bob.speed(0)
    bob.pensize(50)
    bob.setpos(0, 1)
    bob.setpos(0, 0)
    bob.pensize(10)
    posx = posy = 50000
    for instruction in wire1:
        if instruction[0] == 'R':
            for i in range(int(instruction[1:])):
                posx += 1
                grid[posx][posy] = 1
            bob.setpos(posx - 50000, posy - 50000)
        elif instruction[0] == 'L':
            for i in range(int(instruction[1:])):
                posx -= 1
                grid[posx][posy] = 1
            bob.setpos(posx - 50000, posy - 50000)
        elif instruction[0] == 'U':
            for i in range(int(instruction[1:])):
                posy += 1
                grid[posx][posy] = 1
            bob.setpos(posx - 50000, posy - 50000)
        elif instruction[0] == 'D':
            for i in range(int(instruction[1:])):
                posy -= 1
                grid[posx][posy] = 1
            bob.setpos(posx - 50000, posy - 50000)

    posx = posy = 50000
    for instruction in wire2:
        if instruction[0] == 'R':
            for i in range(int(instruction[1:])):
                posx += 1
                if grid[posx][posy] == 1:
                    isects.append((posx, posy))
            bob.setpos(posx - 50000, posy - 50000)
        elif instruction[0] == 'L':
            for i in range(int(instruction[1:])):
                posx -= 1
                if grid[posx][posy] == 1:
                    isects.append((posx, posy))
            bob.setpos(posx - 50000, posy - 50000)
        elif instruction[0] == 'U':
            for i in range(int(instruction[1:])):
                posy += 1
                if grid[posx][posy] == 1:
                    isects.append((posx, posy))
            bob.setpos(posx - 50000, posy - 50000)
        elif instruction[0] == 'D':
            for i in range(int(instruction[1:])):
                posy -= 1
                if grid[posx][posy] == 1:
                    isects.append((posx, posy))
            bob.setpos(posx - 50000, posy - 50000)
    output(bob)
    dist = 100000000
    for x, y in isects:
        dist_ = abs(x - 50000) + abs(y - 50000)
        if dist_ < dist:
            print("NUB")
        print(f"{x - 50000}, {y - 50000} -> {dist_}")
        dist = dist_
    print("done")


def main2():
    grid = [bytearray(100000) for y in range(100000)]
    wire1, wire2 = [x.split(",") for x in fileinput.input()]
    isects = []

    posx = posy = 50000
    for instruction in wire1:
        if instruction[0] == 'R':
            for i in range(int(instruction[1:])):
                posx += 1
                grid[posx][posy] = 1
        elif instruction[0] == 'L':
            for i in range(int(instruction[1:])):
                posx -= 1
                grid[posx][posy] = 1
        elif instruction[0] == 'U':
            for i in range(int(instruction[1:])):
                posy += 1
                grid[posx][posy] = 1
        elif instruction[0] == 'D':
            for i in range(int(instruction[1:])):
                posy -= 1
                grid[posx][posy] = 1

    posx = posy = 50000
    for instruction in wire2:
        if instruction[0] == 'R':
            for i in range(int(instruction[1:])):
                posx += 1
                if grid[posx][posy] == 1:
                    isects.append((posx, posy))
        elif instruction[0] == 'L':
            for i in range(int(instruction[1:])):
                posx -= 1
                if grid[posx][posy] == 1:
                    isects.append((posx, posy))
        elif instruction[0] == 'U':
            for i in range(int(instruction[1:])):
                posy += 1
                if grid[posx][posy] == 1:
                    isects.append((posx, posy))
        elif instruction[0] == 'D':
            for i in range(int(instruction[1:])):
                posy -= 1
                if grid[posx][posy] == 1:
                    isects.append((posx, posy))
    steps_min = 100000000
    for x, y in isects:
        posx = posy = 50000
        steps = 0
        done = False
        for instruction in wire1:
            if instruction[0] == 'R':
                for i in range(int(instruction[1:])):
                    steps += 1
                    posx += 1
                    if posx == x and posy == y:
                        done = True
                        break
            elif instruction[0] == 'L':
                for i in range(int(instruction[1:])):
                    steps += 1
                    posx -= 1
                    if posx == x and posy == y:
                        done = True
                        break
            elif instruction[0] == 'U':
                for i in range(int(instruction[1:])):
                    steps += 1
                    posy += 1
                    if posx == x and posy == y:
                        done = True
                        break
            elif instruction[0] == 'D':
                for i in range(int(instruction[1:])):
                    steps += 1
                    posy -= 1
                    if posx == x and posy == y:
                        done = True
                        break

            if done:
                break

        posx = posy = 50000
        done = False
        for instruction in wire2:
            if instruction[0] == 'R':
                for i in range(int(instruction[1:])):
                    steps += 1
                    posx += 1
                    if posx == x and posy == y:
                        done = True
                        break
            elif instruction[0] == 'L':
                for i in range(int(instruction[1:])):
                    steps += 1
                    posx -= 1
                    if posx == x and posy == y:
                        done = True
                        break
            elif instruction[0] == 'U':
                for i in range(int(instruction[1:])):
                    steps += 1
                    posy += 1
                    if posx == x and posy == y:
                        done = True
                        break
            elif instruction[0] == 'D':
                for i in range(int(instruction[1:])):
                    steps += 1
                    posy -= 1
                    if posx == x and posy == y:
                        done = True
                        break

            if done:
                break

        print(f"{x - 50000}, {y - 50000} -> {steps}")
        if steps < steps_min:
            steps_min = steps
    print(steps_min)
    print("done")


def intersect(pair):
    s1_x = pair[0][0][0] - pair[0][1][0]
    s1_y = pair[0][0][1] - pair[0][1][1]
    s2_x = pair[1][0][0] - pair[1][1][0]
    s2_y = pair[1][0][1] - pair[1][1][1]
    com = ((-1 * s2_x) * s1_y + s1_x * s2_y)
    if com != 0:
        s = ((-1 * s1_y) * (pair[0][0][0] - pair[1][0][0]) + s1_x * (pair[0][0][1] - pair[1][0][1])) / com
        t = (s2_x * (pair[0][0][1] - pair[1][0][1]) - s2_y * (pair[0][0][0] - pair[1][0][0])) / com
        if 0 <= s <= 1:
            if 0 <= t <= 1:
                i_x = pair[0][0][0] + int(t * s1_x)
                i_y = pair[0][0][1] + int(t * s1_y)
                if (min([pair[0][0][0], pair[0][1][0]]) <= i_x <= max([pair[0][0][0], pair[0][1][0]]) or min(
                        [pair[1][0][0], pair[1][1][0]]) <= i_x <= max([pair[1][0][0], pair[1][1][0]])) and (min(
                    [pair[0][0][1], pair[0][1][1]]) <= i_y <= max([pair[0][0][1], pair[0][1][1]]) or min(
                    [pair[1][0][1], pair[1][1][1]]) <= i_y <= max([pair[1][0][1], pair[1][1][1]])):
                    print(f"{i_x} {i_y}")
                return True
    return False


def main1_2():
    bob = turtle.Turtle()
    bob.speed(0)
    bob.pensize(50)
    bob.setpos(0, 1)
    bob.setpos(0, 0)
    bob.pensize(10)
    # pair = (((-2, 0), (2, 0)), ((0, 2), (0, -2)))
    # s1_x = pair[0][0][0] - pair[0][1][0]
    # s1_y = pair[0][0][1] - pair[0][1][1]
    # s2_x = pair[1][0][0] - pair[1][1][0]
    # s2_y = pair[1][0][1] - pair[1][1][1]
    # com = ((-1 * s2_x) * s1_y + s1_x * s2_y)
    # s = ((-1 * s1_y) * (pair[0][0][0] - pair[1][0][0]) + s1_x * (pair[0][0][1] - pair[1][0][1])) / com
    # t = (s2_x * (pair[0][0][1] - pair[1][0][1]) - s2_y * (pair[0][0][0] - pair[1][0][0])) / com
    # print(s)
    # print(t)

    lines = list(fileinput.input())
    # lines_1 = [
    #     [
    #         x[:i+1] for i, y in enumerate(x)
    #     ]
    #     for x
    #     in [[
    #         (instruction[0], int(instruction[1:]))
    #         for instruction
    #         in lines[0].split(",")
    #     ]]
    # ][0]
    lines_1_2 = list(filter(
        lambda pair:
        intersect(pair),
        # True
        # if (
        #        s1_x := pair[0][0][0] - pair[0][1][0], s1_y := pair[0][0][1] - pair[0][1][1],
        #        s2_x := pair[1][0][0] - pair[1][1][0], s2_y := pair[1][0][1] - pair[1][1][1],
        #        com := ((-1 * s2_x) * s1_y + s1_x * s2_y),
        #        s := ((-1 * s1_y) * (pair[0][0][0] - pair[1][0][0]) + s1_x * (pair[0][0][1] - pair[1][0][1])) / com
        #        if com != 0
        #        else 0,
        #        t := (s2_x * (pair[0][0][1] - pair[1][0][1]) - s2_y * (pair[0][0][0] - pair[1][0][0])) / com
        #        if com != 0
        #        else 0,
        #        i_x := pair[0][0][0] + (t * s1_x),
        #        i_y := pair[0][0][1] + (t * s1_y),
        #        com != 0 and 0 <= s <= 1 and 0 <= t <= 1 and (i_x in [pair[0][0][0],pair[0][1][0],pair[1][0][0],pair[1][1][0]] or i_y in [pair[0][0][1],pair[0][1][1],pair[1][0][1],pair[1][1][1]])
        #    )[-1]
        # else False,
        [
            list(product(a, b))
            for a, b
            in [tuple([
            [
                [
                    list(zip(z, z[1:]))
                    for z
                    in
                    [[x for x in list(
                        reduce(
                            lambda a, b:
                            ((a[0] + b[1], a[1]) if b[0] == 'R'
                             else ((a[0] - b[1], a[1]) if b[0] == 'L'
                                   else ((a[0], a[1] + b[1]) if b[0] == 'U'
                                         else ((a[0], a[1] - b[1]) if b[0] == 'D' else "I fucked up")))) + (b[2],),
                            [(0, 0)] + x[:i + 1]
                        )
                        for i, y
                        in enumerate(x)
                    ) if bob.setposition(x[0], x[1]) is None]]
                ][0]
                for x
                in
                [[
                    (instruction[0], int(instruction[1:]), instruction)
                    for instruction
                    in line.split(",")
                ]]
            ][0]
            for line
            in lines
        ])]
        ][0]
    ))
    output(bob, name="t2.svg")
    print("Done")


if __name__ == '__main__':
    main()
    # main2()
    main1_2()
