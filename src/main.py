from src import utils

func_1 = utils.info_operation(utils.load_info)
func_2 = utils.get_operations_executed(func_1)
func_3 = utils.get_last_five_operations(func_2)
func_4 = utils.get_operations_formatted(func_3)

for string in func_4:
    print(f"{string}\n")
