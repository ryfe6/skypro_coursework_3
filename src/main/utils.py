import os
import json

load = os.path.join("../js/operations.json")


def info_client(filename):
    with open(filename, 'r', encoding='utf8') as file:
        info = json.load(file)
        return info


def mask_card(num_card: str) -> str:
    """Функция принимает номер карты, маскирует его и
    возвращает замаскированный номер с отступами после 4 символов."""
    num_list = list(num_card)
    masks_card = []
    for num in num_list:
        if len(masks_card) < 6:
            masks_card.append(num)
        elif 6 <= len(masks_card) < 12:
            masks_card.append("*")
        else:
            masks_card.append(num)
    return (
        f'{"".join(masks_card[0:4])} {"".join(masks_card[4:8])} '
        f'{"".join(masks_card[8:12])} {"".join(masks_card[12:])}'
    )


def score_mask(num_score: str) -> str:
    """Функция принимает номер счета и возвращает последние 4 цифры номера счета."""
    score_list = list(num_score)
    return f'**{"".join(score_list[-4:])}'

