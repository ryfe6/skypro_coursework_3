import os
import json
from datetime import datetime

load = os.path.join("../js/operations.json")


def info_client(filename):
    with open(filename, 'r', encoding='utf8') as file:
        info = json.load(file)
        return info


def get_operations_executed(data):
    operations_executed = []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            operations_executed.append(operation)
    operations_with_list = []
    for operation in operations_executed:
        if 'from' in operations_executed:
            if 'from' in operation:
                operations_with_list.append(operation)
    return operations_with_list


def get_last_five_operations(operation_with_list):
    sort_operations = sorted(operation_with_list, key=lambda operation: operation['data'], reverse=True)
    last_five_operations = sort_operations[0:5]
