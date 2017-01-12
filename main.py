#!/usr/bin/env python3

# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.


from curses import wrapper

from ten.controller import main


def console_main():
    wrapper(main)


if __name__ == '__main__':
    console_main()
