#!/usr/bin/env python3

import RealMe.globals  # Add this line to import globals module
from RealMe import core

if __name__ == '__main__':
    RealMe.globals.headless = True  # Now this will work
    core.run()