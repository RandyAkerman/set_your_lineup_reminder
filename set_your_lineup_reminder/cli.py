"""Console script for set_your_lineup_reminder."""
import argparse
import sys


def main():
    """Console script for set_your_lineup_reminder."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "set_your_lineup_reminder.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
