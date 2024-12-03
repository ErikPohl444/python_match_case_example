import json

if __name__ == '__main__':
    return_dict = {
        'parent_id': 1,
        'parent_name': 'parent1'
    }
    print("dict", return_dict)
    match return_dict:
        case {"parent_id": parent_id, "parent_name": parent_name} if (1==1):
            print("**", parent_id)
    return_json1 = json.dumps(return_dict)
    print(type(return_json1))
    print("dumps", return_json1)
    return_json1 = json.loads(return_json1)
    match return_json1:
        case {'parent_name': parent_name} if (1==1):
            print("**", parent_id)
        case _:
            print("something wrong with json match")

    return_json = json.loads('{"parent_id": 1, "parent_name": "parent1"}')
    print("loads", return_json)
    print("json", return_json)
    match return_json:
        case {'parent_name': parent_name} if (1==1):
            print("**", parent_id)
        case _:
            print("something wrong with json match")

    if "parent_id" in return_json:
        print("yay?")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/