import re


def check_length(card):
    return len(card.replace('-', '')) == 16


def check_separator(card):
    if card.count('-') == 0:
        return True

    if card.count('-') != 3:
        return False

    for item in card.split('-'):
        if len(item) != 4:
            return False

    return True


def check_repeated_digit(card):
    count = 0
    card_number = card.replace('-', '')
    for i in range(1, len(card_number)):
        if card_number[i-1] == card_number[i]:
            count += 1
        else:
            count = 1
        if count > 3:
            return False

    return True


def check_card(card):
    """Check card validation
    :param card: card number
    :return: Valid | Invalid
    """
    validator = '^[456]+(-?[0-9]+)+$'
    if not re.match(validator, card):
        return 'Invalid'

    if not check_length(card):
        return 'Invalid'

    if not check_separator(card):
        return 'Invalid'

    if not check_repeated_digit(card):
        return 'Invalid'

    return 'Valid'


if __name__ == '__main__':
    n = int(input())
    for _ in range(0, n):
        print(check_card(input().strip()))

