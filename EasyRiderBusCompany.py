import re
import json
import itertools


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


def count_starts_and_stops(database):
    start_stops = []
    transfer_stops = []
    finish_stops = []
    temp = {}
    for i in database:
        temp_id = i.get('bus_id')
        if temp_id not in temp:
            if i.get('stop_type') == 'S':
                temp.update({temp_id: [i.get('stop_type')]})
            else:
                print(f'There is no start or end stop for the line: {temp_id}.')
                break
        else:
            temp[temp_id].append(i.get('stop_type'))

        if i.get('bus_id') == temp_id and i.get('stop_type') == 'S':
            if i.get('stop_name') in start_stops:
                transfer_stops.append(i.get('stop_name'))
                continue
            start_stops.append(i.get('stop_name'))
        elif i.get('bus_id') == temp_id and i.get('stop_type') == 'F':
            if i.get('stop_name') in finish_stops:
                transfer_stops.append(i.get('stop_name'))
                continue
            finish_stops.append(i.get('stop_name'))
        else:
            transfer_stops.append(i.get('stop_name'))
    for i in temp:
        if temp.get(i).count('S') == 1 and temp.get(i).count('F') == 1:
            continue
        else:
            print(f'There is no start or end stop for the line: {i}.')
            break
    tem = [i for i in itertools.chain(start_stops, transfer_stops, finish_stops)]
    print(tem)
    res = []
    for i in tem:
        if tem.count(i) >= 2 and i not in res:
            res.append(i)
    print(f'Start stops: {len(start_stops)}', start_stops)
    print(f'Transfer stops: {len(res)}', res)
    print(f'Finish stops: {len(finish_stops)}', finish_stops)


def valid_time(database):
    temp = {}
    result = {}
    for i in database:
        temp_id = i.get('bus_id')
        if temp_id in result:
            continue
        time = i.get('a_time')
        if temp_id not in temp:
            temp.update({temp_id: [time]})
        else:
            temp[temp_id].append(time)
            if temp[temp_id] != sorted(temp[temp_id]):
                result.update({temp_id: [i.get('stop_name')]})
    print('Arrival time test: ')
    if result:
        for i in result:
            print(f'bus_id line {i}: wrong time on station {"".join(result.get(i))}')
    else:
        print('OK')


tmp = input()
json_format = json.loads(tmp)
valid_time(json_format)



