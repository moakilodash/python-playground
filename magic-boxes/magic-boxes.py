NUMBER_OF_MAGIC_BOXES = 42
ACTION_FILE = "actions-simple.txt"


def find_obj(boxes, obj):
    for index, box in enumerate(boxes):
        if obj in box:
            return index
    return None


def add_action(boxes, obj):
    x = find_obj(boxes, obj)
    if x is None:
        return False
    else:
        boxes[x].append(obj)
        return True


def remove_action(boxes, obj):
    x = find_obj(boxes, obj)
    if x is None or not boxes[x]:
        return False
    else:
        boxes[x].pop()
        return True


def main():
    magic_box = [list() for _ in range(NUMBER_OF_MAGIC_BOXES)]
    with open(ACTION_FILE) as actions_file:
        for action in actions_file:
            actor, _, _, obj = action.split()
            if actor == 'Bob':
                if not add_action(magic_box, obj):
                    print(f"Alice cannot store a {obj}!")
                    break
            elif actor == 'Carl':
                if not remove_action(magic_box, obj):
                    print(f"Alice cannot take a {obj}!")
                    break
            else:
                assert actor in ['Bob', 'Carl'], f"Unknown actor: {actor}"


if __name__ == "__main__":
    main()
