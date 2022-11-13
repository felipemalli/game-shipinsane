def get_around_index_list_by_range(iterated_list, center_index, range_size):
    around_list = list()
    
    for i in range(1, range_size + 1):
        around_index = center_index + i
        if around_index >= len(iterated_list):
            around_index -= len(iterated_list)
        around_list.append(iterated_list[around_index])
        
        around_index = center_index - i
        if around_index < 0:
            around_index += len(iterated_list)
        around_list.append(iterated_list[around_index])

    return around_list


def get_around_string_list(string_list, string):
    around_list = []
    
    direction_i = string_list.index(string)
    
    if (direction_i) == len(string_list) - 1: around_list.append(string_list[0])
    else: around_list.append(string_list[direction_i + 1])
    if (direction_i) < 0: around_list.append(string_list[len(direction_i) - 1])
    else: around_list.append(string_list[direction_i - 1])

    return around_list
