import json

person = {
    'basic_info': {'name': '王声援',
                   'age': 24,
                   'sex': 'male',
                   'merry': False},
    'work_info': {'salary': 99999,
                  'position': 'engineer',
                  'department': None}
}

person_json_indent = json.dumps(person,indent=4)
print(f'person_json_indent 类型为：{type(person_json_indent)}')
person_dict = json.loads(person_json_indent)
print(f'person_dict 类型为：{type(person_dict)}')

print(person_dict)