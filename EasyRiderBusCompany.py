import re
import json
import itertools
abc = [
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]


def check_type(database):
    data_types = {
        "bus_id": "(128|256|512)",
        "stop_id": "\d{1}",
        "stop_name": "[A-Z]\w+\s?\w+?\s(Road|Avenue|Boulevard|Street)\Z",
        "next_stop": "\d+",
        "stop_type": "(S|O|F)\Z",
        "a_time": "[0-2][0-9]:[0-5][0-9]\Z"
    }
    report_mistakes = {
        "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0
    }
    for i in database:
        for j in i:
            if j == 'stop_type' and not i.get(j):
                continue
            if j in report_mistakes:
                matches = re.match(data_types.get(j), str(i.get(j)))
                if matches:
                    continue
                else:
                    report_mistakes.update({j: report_mistakes.get(j) + 1})
    print_result(report_mistakes)


def bus_stops(database):
    """Check how many bus lines we have and how many stops there are"""
    res = {}
    for i in database:
        for j in i:
            if j == "bus_id" and i.get(j):
                if not res.get(i.get(j)):
                    res.update({i.get(j): 0})
                res.update({i.get(j): res.get(i.get(j)) + 1})
    print_bus_stops(res)


def print_bus_stops(res):
    for i in res:
        print(f"bus_id: {i}, stops: {res.get(i)}")


def print_result(result):
    print(f'Type and required field validation: {sum(result.values())} errors')
    for key in result:
        if result.get(key) == 0:
            continue
        print(f'{key}: {result.get(key)}')



main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]
dict = {}


for i, j in zip(itertools.combinations(itertools.chain(main_courses, desserts, drinks), 3), itertools.combinations(itertools.chain(price_main_courses, price_desserts, price_drinks), 3)):
    if i[0] in main_courses and i[1] in desserts and i[2] in drinks and sum(j) <= 30:
        print(i, sum(j))