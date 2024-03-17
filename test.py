import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)



PATTERN_TEL = (r"(\+7|\s8)[\s*|\-]?[\(]?(\d\d\d)[\)]?[\s*|-]?(\d\d\d)[\s*|\-]?(\d\d)[\s*|\-]?(\d\d)\s?[(]?("
               r"\s*\д?\о?\б?\.?\s?\d\d\d\d)?[)]?")
# "(\+7|\s8)\s*(\(\d\d\d\)|\d\d\d)(\s*|\-)(\d\d\d)(\s*|\-)(\d\d)(\s*|-)(\d\d)"
# "(?:(?:\+7|8)\s*(?:\(\d+\)\s*|\d+\s*)\d+[\-|\s*]\d+[\-|\s*]\d+)|(?:\+7\d+)"
TEL_SUB = r"+7(\2)\3-\4-\5 \6"

new_contacts = []
for item in contacts_list:
    contact_fullname = ' '.join(item[:3]).split(' ')
    cont_result = [contact_fullname[0], contact_fullname[1], contact_fullname[2], item[3], item[4],
                   re.sub(PATTERN_TEL, TEL_SUB, item[5]), item[6]]
    new_contacts.append(cont_result)
#pprint(new_contacts)
for contact in new_contacts:
    for double in new_contacts:
        if double[0]==contact[0] and double[1]==contact[1]:
            if contact[2]=='':
                contact[2] = double[2]
            if contact[3] == '':
                contact[3] = double[3]
            if contact[4] == '':
                contact[4] = double[4]
            if contact[5] == '':
                contact[5] = double[5]
            if contact[6] == '':
                contact[6] = double[6]
result = []
for i in new_contacts:
    if i not in result:
        result.append(i)
#pprint(result)




# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(result)
