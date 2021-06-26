#!/usr/bin/env python3

import sys
from shmup import game

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    app = game.Game()
    app.run()

if __name__ == '__main__':
    sys.exit(main())