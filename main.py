#!/usr/bin/env python3
from game import Game
import argparse


def main():
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print("\nexiting...")
        exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument("-l", "--loop", action="store_true", help="if set to true, makes the game continuously run in a loop.")
    args = parser.parse_args()

    if args.loop:
        while True:
            main()

    else:
        main()

