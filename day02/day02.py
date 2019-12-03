import fileinput


def main():
    ints = list([int(x) for x in fileinput.input().readline().split(',')])
    for i in range(0, ints.__len__(), 4):
        if ints[i] == 1:
            ints[ints[i + 3]] = ints[ints[i + 2]] + ints[ints[i + 1]]
        elif ints[i] == 2:
            ints[ints[i + 3]] = ints[ints[i + 2]] * ints[ints[i + 1]]
        elif ints[i] == 99:
            print(",".join([str(x) for x in ints]))
            return


def main2():
    line = fileinput.input().readline()
    for noun in range(100):
        for verb in range(100):
            ints = list([int(x) for x in line.split(',')])
            ints[1] = noun
            ints[2] = verb
            for i in range(0, ints.__len__(), 4):
                if ints[i] == 1:
                    ints[ints[i + 3]] = ints[ints[i + 2]] + ints[ints[i + 1]]
                elif ints[i] == 2:
                    ints[ints[i + 3]] = ints[ints[i + 2]] * ints[ints[i + 1]]
                elif ints[i] == 99:
                    print(",".join([str(x) for x in ints]))
                    break
            if ints[0] == 19690720:
                print(f"{100 * noun + verb}")
                return


if __name__ == '__main__':
    main2()
