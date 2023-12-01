import inspect

import requests

from utils import secrets
from utils.fetch_input import _extract_path_day_part


def submit_answer(answer):
    calling_frame = inspect.stack()[1]
    day_path, year, day, part = _extract_path_day_part(calling_frame)
    url = f'https://adventofcode.com/{year}/day/{day}/answer'
    cookies = {
        "session": secrets.SESSION,
    }
    payload = {
        'level': part,
        'answer': answer,
    }
    response = requests.post(url, data=payload, cookies=cookies)
    text = response.text
    if "That's the right answer!" in text:
        print("## [DEBUG] answer correct")
    else:
        print("## [ERROR] answer wrong")
        answer_from = text.find('<article>')
        answer_to = text.find('</article>')
        print(text[answer_from + 9:answer_to])
    return text
