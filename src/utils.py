import os
import json
from datetime import datetime

load_info = os.path.join("../js/operations.json")


def info_operation(filename: json) -> list:
    """
    Функция обрабатывает json файл.
    :param filename: json file.
    :return: Преобразованный в список json файл.
    """
    with open(filename, "r", encoding="utf8") as file:
        info = json.load(file)
        return info


def get_operations_executed(data: list) -> list:
    """
    Функция принимает список и фильтрует его по следующим категориям.
    Статус операции == "EXECUTED".
    В списке имеется "from"
    :param data: Список с данными об операциях.
    :return: Фильтрованный по правилу список данных
    """
    operations_executed = []
    for operation in data:
        if "state" in operation and operation["state"] == "EXECUTED":
            operations_executed.append(operation)
    operations_with_list = []
    for operation in operations_executed:
        if "from" in operation:
            operations_with_list.append(operation)
    return operations_with_list


def get_last_five_operations(operation_with_list: list) -> list:
    """
    Функция сортирует данные по дате, забирает из списка последние пять операций.
    :param operation_with_list: Список с данными об оперциях.
    :return: Список последних пяти операций.
    """
    sort_operations = sorted(
        operation_with_list, key=lambda operation: operation["date"], reverse=True
    )
    last_five_operations = sort_operations[0:5]
    return last_five_operations


def get_operations_formatted(last_five_operations: list) -> list:
    """
    Функция преобразует дату в удобный для чтения формат,
    маскирует номер счета и карты.
    :param last_five_operations: Список с данными об операциях.
    :return: Измененные по правилам данные.
    """
    operations_formatted_list = []
    for operation in last_five_operations:
        date = datetime.strptime(operation["date"],
                                 "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = operation["description"]
        payer_info, payment_method = "", ""
        if "from" in operation:
            payer = operation["from"].split()
            payment_method = payer.pop(-1)
            if payer[0].lower() == "счет":
                payment_method_from = f"**{payment_method[-4:]}"
            else:
                payment_method_from = (f"{payment_method[:4]} "
                                       f"{payment_method[4:6]}** **** {payment_method[12:]}")
            payer_info = " ".join(payer)
        recipients = f"{operation['to'].split()[0]} **{operation['to'][-4:]}"
        operation_amount = (f"{operation['operationAmount']['amount']} "
                            f"{operation['operationAmount']['currency']['name']}")
        operations_formatted_list.append(
            f"""        {date} {description}
        {payer_info} {payment_method_from}->{recipients}
        {operation_amount}"""
        )
    return operations_formatted_list
