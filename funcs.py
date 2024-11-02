import re


def check_phone(contact: str) -> str:
    phone = '+7'

    if re.findall(r'\+7\s?\(?\d{3}\)?\s?\d+-?\d+-?\d+', contact) != 0:
        for i in range(2, len(contact)):
            if len(phone) == 2:
                phone += '('
            if len(phone) == 6:
                phone += ')'
            elif len(phone) in (10, 13):
                phone += '-'
            elif len(phone) == 16:
                break
            if contact[i].isdigit():
                phone += contact[i]

    elif re.findall('^8.+', contact) != 0:
        for i in range(1, len(contact)):
            if len(phone) == 6:
                phone += ')'
            elif len(phone) in (10, 13):
                phone += '-'
            elif len(phone) == 16:
                break
            if contact[i].isdigit():
                phone += contact[i]

    if 'доб' in contact:
        phone += ' доб. '
        for i in range(19, len(contact)):
            if contact[i].isdigit():
                phone += contact[i]

    return phone


def check_name(contact: list) -> tuple:
    lastname, firstname, surname = '', '', ''
    a = contact[0].split()
    b = contact[1].split()
    c = contact[2].split()
    if len(a) == 3:
        lastname = a[0]
        firstname = a[1]
        surname = a[2]
    elif len(a) == 2:
        lastname = a[0]
        firstname = a[1]
    elif len(a) == 1:
        lastname = a[0]

    if len(b) == 2:
        firstname = b[0]
        surname = b[1]
    elif len(b) == 1:
        firstname = b[0]

    if len(c) == 1:
        surname = c[0]

    return lastname, firstname, surname


def merge_contacts(contact_a, contact_b):
    """Сливает данные двух контактов, выбирая непустые поля."""
    contact_a.surname = contact_b.surname or contact_a.surname
    contact_a.organization = contact_b.organization or contact_a.organization
    contact_a.position = contact_b.position or contact_a.position
    contact_a.phone = contact_b.phone or contact_a.phone
    contact_a.email = contact_b.email or contact_a.email