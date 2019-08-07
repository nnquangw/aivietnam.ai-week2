import argparse

import forwhile_loops
import pie_estimate


def main(extype, exnum):
    if extype == 'forwhile_loops':
        if exnum == 1:
            print(forwhile_loops.ex1())
        elif exnum == 2:
            print(forwhile_loops.ex2())
        elif exnum == 3:
            print(forwhile_loops.ex3())
    elif extype == 'pie_estimate':
        if exnum == 1:
            print(pie_estimate.pi())
        elif exnum == 2:
            print(pie_estimate.e())
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Week 2 exercises solution')
    parser.add_argument('--extype', default='forwhile_loops', help='choose exercise type')
    parser.add_argument('--exnum', type=int, default=0, help='exercise number')

    args = parser.parse_args()
    main(args.extype, args.exnum)
