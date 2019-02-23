def remove_list_dupes(the_list):
    new_list = []
    for x in range(len(the_list)):
        if the_list[x] not in new_list:
            new_list.append(the_list[x])
    return new_list


def remove_list_dupes_inplace(the_list):
    x = 0
    while x < len(the_list):
        if the_list.count(the_list[x]) >= 2:
            for y in range(1, the_list.count(the_list[x])):
                the_list.remove(the_list[x])
            continue
        x += 1
    return the_list
