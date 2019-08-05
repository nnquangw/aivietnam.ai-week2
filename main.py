import argparse

import forwhile_loops


def main(extype, exnum):
    if extype == 'forwhile_loops':
        if exnum == 1:
            print(forwhile_loops.ex1())

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Week 2 exercises solution')
    parser.add_argument('exercise type', default='forwhile_loops', help='choose exercise type')
    parser.add_argument('exercise number', type=int, default=0, help='exercise number')

    args = parser.parse_args()
    main()