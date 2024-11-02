import csv
from funcs import check_phone, check_name, merge_contacts
from contact import Contact


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

contacts = list()
for i in range(1, len(contacts_list)):
    name = check_name(contacts_list[i])
    lastname = name[0]
    firstname = name[1]
    surname = name[2]
    organization = contacts_list[i][3]
    position = contacts_list[i][4]
    if contacts_list[i][5] != '':
        phone = check_phone(contacts_list[i][5])
    else:
        phone = ''
    email = contacts_list[i][6]

    contact = Contact(
        lastname, firstname,
        surname, organization,
        position, phone, email
    )
    contacts.append(contact)

for i in range(len(contacts) - 1):
    for j in range(i + 1, len(contacts)):
        if contacts[i].status == 1:
            if contacts[i] == contacts[j]:
                merge_contacts(contacts[i], contacts[j])
                contacts[j].status = 0

list_for_write = list()
list_for_write.append(contacts_list[0])
for i in contacts:
    if i.status == 1:
        list_for_write.append([
            i.lastname, i.firstname,
            i.surname, i.organization,
            i.position, i.phone, i.email
        ])


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(list_for_write)