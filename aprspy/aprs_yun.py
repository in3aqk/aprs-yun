#!/usr/bin/python


import argparse

from AprsToIs import AprsToIs


def parse():
    parser = argparse.ArgumentParser(description='Aprs Arduino YUN to aprs-is logger')
    parser.add_argument("-d", "--data", action='store', help="Data to send")

    args= parser.parse_args()

    if args.data:
        print(args.data)
        aprsToIs = AprsToIs()
        aprsToIs.send(data)



if __name__ == "__main__":
    parse()
    