#!/usr/bin/python3
"""
holdrightclick.py - script for holding the right mouse button
"""

import time
import argparse
import pyautogui

__version__ = "1.0"


def main():
    """
    main function
    """
    parser = argparse.ArgumentParser(description="script to hold right click forever")
    parser.add_argument(
        "--wait",
        "-w",
        type=float,
        default=3,
        help="how many seconds to wait before actually holdinging",
    )
    parser.add_argument(
        "--interval",
        "-i",
        type=float,
        default=0.1,
        help="how much time to wait between mouse downing",
    )
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version=f"%(prog)s {__version__}",
        help="display version information and exit",
    )
    args = parser.parse_args()

    time.sleep(args.wait)
    while True:
        pyautogui.mouseDown(button="right")
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
