
side_options = ['nw', 'n', 'ne', 'e', 'se', 's', 'sw', 'w']

print(side_options)

# side_options.index(primary_side) 

def get_around_index_list(iterated_list, center_index, range_size):
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

around_list = get_around_index_list(side_options, 6, 2)
print(around_list)

# if not side_options['sw']:
#     print(side_options['sw'])
# if test.contains("_ne"):

# 'n'

# nw []

# def define_cannon_rotation(primary_side, max_rotation):
#     side[primary_side] = 
