import fileinput
import itertools


def main():
    min_p = 165432
    max_p = 707912

    cnt = 0
    for i in range(min_p, max_p):
        last_last_x = None
        last_x = str(i)[0]
        myb = True
        repeating = [len(list(y)) for (c,y) in itertools.groupby(str(i)) if c in [str(ab) for ab in range(10)]]
        myb = 2 in repeating
        if myb:
            i_ = i
            curdig = i % 10
            i = i//10
            good = True
            while i>0 and good:
                if i % 10 <= curdig:
                    curdig = i% 10
                    i = i//10
                else:
                    good = False

            if good:
                cnt += 1
                print(cnt)



if __name__ == '__main__':
    main()
