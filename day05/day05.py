import fileinput


def main():
    ints = list([int(x) for x in fileinput.input().readline().split(',')])
    pos = 0
    while True:
        op_code = ints[pos] % 100
        modes = [(ints[pos] // pow(10, 2 + x)) % 10 for x in range(3)]
        if op_code == 1:
            inputs = [(y if modes[i] == 1 else ints[y]) for i, y in enumerate([ints[pos + i + 1] for i in range(2)])]
            output_address = ints[pos + 3]
            ints[output_address] = inputs[0] + inputs[1]
            pos += 4
        elif op_code == 2:
            inputs = [(y if modes[i] == 1 else ints[y]) for i, y in enumerate([ints[pos + i + 1] for i in range(2)])]
            output_address = ints[pos + 3]
            ints[output_address] = inputs[0] * inputs[1]
            pos += 4
        elif op_code == 3:
            input_value_output_address = ints[pos + 1]
            ints[input_value_output_address] = int(input("Please provide input: "))
            pos += 2
        elif op_code == 4:
            inputs = [(y if modes[i] == 1 else ints[y]) for i, y in enumerate([ints[pos + i + 1] for i in range(1)])]
            print(inputs[0])
            pos += 2
        elif op_code == 5:
            inputs = [(y if modes[i] == 1 else ints[y]) for i, y in enumerate([ints[pos + i + 1] for i in range(2)])]
            if inputs[0] != 0:
                pos = inputs[1]
            else:
                pos += 3
        elif op_code == 6:
            inputs = [(y if modes[i] == 1 else ints[y]) for i, y in enumerate([ints[pos + i + 1] for i in range(2)])]
            if inputs[0] == 0:
                pos = inputs[1]
            else:
                pos += 3
        elif op_code == 7:
            inputs = [(y if modes[i] == 1 else ints[y]) for i, y in enumerate([ints[pos + i + 1] for i in range(2)])]
            if inputs[0] < inputs[1]:
                ints[ints[pos + 3]] = 1
            else:
                ints[ints[pos + 3]] = 0
            pos += 4
        elif op_code == 8:
            inputs = [(y if modes[i] == 1 else ints[y]) for i, y in enumerate([ints[pos + i + 1] for i in range(2)])]
            if inputs[0] == inputs[1]:
                ints[ints[pos + 3]] = 1
            else:
                ints[ints[pos + 3]] = 0
            pos += 4
        elif op_code == 99:
            print(",".join([str(x) for x in ints]))
            return


if __name__ == '__main__':
    main()
