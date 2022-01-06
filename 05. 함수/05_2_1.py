counter = 0

def flatten(data):
    flatten_arr = []
    for i in data:
        global counter
        counter += 1
        if type(i) is list:
            flatten_arr += flatten(i)
        else:
            flatten_arr.append(i)
    return flatten_arr

example = [[1,2,3], [4, [5, 6]], 7, [8, 9]]
print(flatten(example))
print(counter)