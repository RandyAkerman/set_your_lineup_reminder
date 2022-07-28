"""Main module."""

import requests
import argparse


def get_schedule (date):
    
    url = f'https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={date}'
    
    r = requests.get(url)
    
    schedule = r.json()

    return schedule

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--date',
        required=True,
        type=str,
        help='Date to return schedule for'
    )

    args = parser.parse_args()

    get_schedule(args.date)
