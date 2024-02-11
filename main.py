#!/opt/homebrew/bin/python3
from component_checker import Checker

from cProfile import Profile
from pstats import Stats


def main():
    print("Hello")
    checker = Checker()

    with Profile() as profile:
        checker.spin()
        (
            Stats(profile)
            .strip_dirs()
            .sort_stats('cumulative')
            .print_stats()
        )


if __name__ == '__main__':
    main()
