import fileinput


def main():
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
    dist = 100000000
    for x, y in isects:
        dist_ = abs(x - 50000) + abs(y - 50000)
        if dist_ < dist:
            print(f"{x}, {y} -> {dist_}")
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

        print(f"{x}, {y} -> {steps}")
        if steps < steps_min:
            steps_min = steps
    print(steps_min)
    print("done")


if __name__ == '__main__':
    #main()
    main2()
