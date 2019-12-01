import fileinput
import math

debug: bool = False


def main():
    part1()
    part2()


def part1():
    line: str
    total_fuel_required: int = 0

    for line in fileinput.input():
        if len(line.strip()) > 0:
            try:
                mass: int = int(line)
                fuel_requirement: int = rocket_equation(mass)
                total_fuel_required += fuel_requirement
                if debug:
                    print(f"part1: rocket_equation({mass}) = {fuel_requirement}")
            except ValueError:
                print(f"Input line should be a string of an integer value, but it is \"{line}\"")

    print(f"Total fuel required: {total_fuel_required}")


def part2():
    line: str
    total_fuel_required: int = 0

    for line in fileinput.input():
        if len(line.strip()) > 0:
            try:
                mass: int = int(line)
                fuel_requirement: int = 0

                while mass > 0:
                    fuel_requirement: int = rocket_equation(mass)
                    mass = fuel_requirement
                    total_fuel_required += fuel_requirement

                if debug:
                    print(f"part2: rocket_equation({mass}) = {fuel_requirement}")
            except ValueError:
                print(f"Input line should be a string of an integer value, but it is \"{line}\"")

    print(f"Total fuel required accounting for fuel weight: {total_fuel_required}")


def rocket_equation(mass: int) -> int:
    fuel_requirement: float = float(mass)  # Transform input into a float for division
    fuel_requirement /= 3  # Divide by 3
    fuel_requirement = math.floor(fuel_requirement)  # Round down
    fuel_requirement -= 2  # Subtract 2
    if fuel_requirement > 0:  # Make sure not to return negative fuel
        return int(fuel_requirement)  # Turn back into int for output
    else:
        return 0


if __name__ == '__main__':
    main()
