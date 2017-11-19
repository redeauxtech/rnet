#!/usr/bin/env python2.7


# Included modules
import sys

# rNET Modules
import rnet


def main():
    sys.argv = [sys.argv[0]]+["--open_browser", "default_browser"]+sys.argv[1:]
    rnet.main()

if __name__ == '__main__':
    main()
