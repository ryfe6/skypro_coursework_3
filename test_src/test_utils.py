from src import utils


def test_info_operation():
    assert len(utils.info_operation("../js/operations.json")) > 0


def test_get_operation_executed(test_data):
    assert len(utils.get_operations_executed(test_data)) == 3



def test_get_last_five_operation(test_data):
    assert len(utils.get_last_five_operations(test_data)) == 4
    assert utils.get_last_five_operations(test_data)[0]['date'] == '2019-08-26T10:50:58.294041'

def test_get_operations_formatted(test_data):
    assert (utils.get_operations_formatted(test_data) ==
['        26.08.2019 Перевод организации\n'
 '        Maestro 1596 83** **** 5199->Счет **9589\n'
 '        31957.58 руб.',
 '        03.07.2019 Перевод организации\n'
 '        MasterCard 7158 30** **** 6758->Счет **5560\n'
 '        8221.37 USD',
 '        30.06.2018 Перевод организации\n'
 '        Счет **6952->Счет **6702\n'
 '        9824.07 USD',
 '        23.03.2018 Открытие вклада\n'
 '         **6952->Счет **2431\n'
 '        48223.05 руб.'])