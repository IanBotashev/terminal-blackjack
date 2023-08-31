#!/usr/bin/env python3
from game import Game
import argparse
GAME_VERSION = 0.2


def main():
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print("\nexiting...")
        exit()


if __name__ == '__main__':
    print(f"Blackjack v{GAME_VERSION}")
    parser = argparse.ArgumentParser(description="Plays a game of blackjack in the terminal.")
    parser.add_argument("-l", "--loop", action="store_true", help="if set to true, makes the game continuously run in a loop.")
    args = parser.parse_args()

    if args.loop:
        while True:
            main()

    else:
        main()

