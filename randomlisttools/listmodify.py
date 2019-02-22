def remove_list_dupes(the_list):
    new_list = []
    for x in range(len(the_list)):
        if the_list[x] not in new_list:
            new_list.append(the_list[x])
    return new_list


def remove_list_dupes_inplace(the_list):
    for x in range(len(the_list)):
        try:
            if the_list.count(the_list[x]) >= 2:
                for y in range(1, the_list.count(the_list[x])):
                    the_list.remove(the_list[x])
        except IndexError:
            return the_list
    return the_list
