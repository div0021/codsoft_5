import re


def is_valid_name(name: str) -> bool:
    pattern = re.compile(r'[a-zA-Z\s]+$')

    match = pattern.match(name)

    return bool(match)


def is_valid_email(email: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    match = pattern.match(email)

    return bool(match)


def is_valid_phone_number(phone_number: str) -> bool:
    pattern = re.compile(r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$')

    match = pattern.match(phone_number)

    return bool(match)
