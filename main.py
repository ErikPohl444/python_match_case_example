import json

# This space intentionally left blank

if __name__ == '__main__':

    # match case against a dict
    return_dict = {
        'parent_id': 1,
        'parent_name': 'parent1'
    }
    print("dict", return_dict)
    match return_dict:
        case {"parent_id": parent_id, "parent_name": parent_name} if (parent_name == "parent1"):
            print("**", parent_id)

    # match case against a dict converted into a string and then into json
    return_json1 = json.dumps(return_dict)
    print(type(return_json1))
    print("dumps", return_json1)
    return_json1 = json.loads(return_json1)
    print("loads", return_json1)
    match return_json1:
        case {'parent_name': parent_name} if (parent_name == "parent1"):
            print("**", parent_name)
        case _:
            print("something wrong with json match")

    # match case against a string converted into json
    return_json = json.loads('{"parent_id": 1, "parent_name": "parent1"}')
    print("loads", return_json)
    print("json", return_json)
    match return_json:
        case {'parent_name': parent_name} if (parent_name == "parent1"):
            print("**", parent_name)
        case _:
            print("something wrong with json match")

    # traditional seeking of parent_id
    if "parent_id" in return_json:
        print("yay?")

    # match a color string against a string
    color_list = ["red", "yellow", "green", "blue"]
    for color in color_list:
        match color:
            case "red":
                print("stop")
            case "yellow" | "green":
                print("go")
            case r"\bl":
                print("blue")

    match color_list:
        case ["red", *a]:
            print(a)
        # does not match second item because it does not continue after matching first
        case [*b, "green"] | (*b, "green"):
            print(*b)

    color_list = color_list[1:]
    match color_list:
        # no longer gets caught on this case
        case ["red", *a]:
            print(a)
        case [*b, "green"]:
            print(*b)

    class Car():
        
        def __init__(self, paint_color):
            self.vehicle = "car"
            self.color = paint_color
    
    class Honda(Car):

        def __init__(self, paint_color):
            self.make = "Honda"
            super().__init__(paint_color)

    # class matching
    auto1 = Honda("red")
    auto2 = Car("blue")
    auto3 = Honda("silver")

    match auto1:
        case Honda():
            print("a honda")
        case Car():
            print("a car")
    match auto1:
        # note: a Honda registers as a car
        case Car():
            print("a car")
        case Honda():
            print("a honda")
    match auto3:
        # note: a car does not register as a Honda
        case Honda(color="silver"):
            print("a silver honda")
        case Car():
            print("a car")
