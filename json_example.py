import json

json_data = '{"name": "Ivan", "age": 20, "is_student": true}'

parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))

data = {
    "name": "Ivan",
    "age": 20,
    "is_student": True
}
json_str = json.dumps(data, indent=4)

print(json_str)

with open("json_example.json", encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(data, type(data))

with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
