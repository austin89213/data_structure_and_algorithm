head = {
    "value": 11,
    "next": {
        'value': 3,
        "next": {
            'value': 23,
            "next": {
                'value': 7,
                "next": None
            },
        }
    }
}

print(head['next']['next']['next'])

# This will only run with a linked list
# print(my_linked_list.head.next.next.value)