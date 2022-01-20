my_list = [11,3,23,7]
my_list.append(17)
# my_list = [11,3,23,7,17]
# since no original index changed, it's o(1)
my_list.pop()
# my_list = [11,3,23,7]
# except for the last item, no index changed, it's o(1)
my_list.pop(0)
# my_list = [3,23,7]
# all index changed, it's o(n)
my_list.insert(0, 11)
# my_list = [11,3,23,7]
# all index changed, it's o(n)
# even we insert or remove item in the middle, still o(n) cuz Big talks about the worst case.