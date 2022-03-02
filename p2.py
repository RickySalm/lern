a = {1:1, 2:2, 3:3}
b = {1:31, 4:2, 3:'None'}


def sum_dict(f_dict, s_dict):           #my version
    for i in s_dict:
        if i in f_dict:
            list_ = []
            list_ += s_dict[i], f_dict[i]
            f_dict[i] = list_
        else:
            f_dict.update()
    return f_dict


def dictionary(*dictionaries):
    res = dictionaries[0].copy()
    for d in dictionaries[1:]:
        for k, v in d.items():
            if k not in res:
                res[k] = v
            else:
                if isinstance(res[k], list):
                    res[k].append(v)
                else:
                    res[k] = [res[k], v]
    return res

"""
def merge(*dicts):
    
    res_dict = dict1.copy()
    
    for key in set(dict1) | set(dict2):
        if key not in dict2:
            res_dict = [dict1[key], dict2[key]]
    return res_dict
"""

"""
c = {
    1:[1, 31],
    2:2, 
    3:[3, 'None'], 
    4:2
}
"""

print(sum_dict(a, b))
print(dictionary(a, b))

#стэк
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop(0))
print(stack)
