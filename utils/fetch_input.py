import os.path
import re
import sys

import requests

from utils import secrets


def _extract_path_day_part():
    module = sys.argv[0]
    module_name = os.path.basename(module)
    module_path = os.path.dirname(module)
    matches = re.match(r'd(\d{1,2})p([12])\.py', module_name)
    day, part = int(matches.group(1)), int(matches.group(2))
    matches = re.search(r'(\d{4})', module_path)
    year = int(matches.group(1))
    return module_path, year, day, part


def fetch_input():
    day_path, year, day, part = _extract_path_day_part()
    input_file = os.path.join(day_path, 'input.txt')
    if os.path.exists(input_file):
        print(f'## [INFO] reading cached input from {input_file}')
        with open(input_file, 'r') as f:
            text = f.read()
    else:
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        cookies = {
            "session": secrets.SESSION,
        }
        print(f'## [WARN] fetching input from {url}')
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()
        text = response.text
        print(f'## [INFO] caching input into {input_file}')
        with open(input_file, 'w') as f:
            f.write(text)
    return text
