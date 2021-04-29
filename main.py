import json

import requests

"""Ссылка на расписание"""
BASE_URL = "https://miet.ru/schedule"

def error_returning():
    return "Error, code isn't 200"

def get_groups():
    """Метод получения списка групп"""
    group_page = requests.post(BASE_URL + "/groups", {})
    if group_page.status_code == 200:
        return json.loads(group_page.text)
    else:
        error_returning()


def get_schedule(group_name: str):
    schedule_page = requests.post(BASE_URL + "/data", {"group": group_name})
    if schedule_page.status_code == 200:
        return json.loads(schedule_page.text)
    else:
        error_returning()


if __name__ == '__main__':
    schedule = {}

    group_list = get_groups()

    for group in group_list[:3]:
        schedule[group] = get_schedule(group)


    with open("schedule.json", "w+", encoding='utf8') as f:
        f.write(json.dumps(schedule, ensure_ascii=False))


