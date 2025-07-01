import pickle

name_of_pkl_file, control_sum = input(), int(input())

with open(name_of_pkl_file, mode='rb') as pkl_file:
    data = pickle.load(pkl_file)
    if isinstance(data, list):
        int_data = [x for x in data if isinstance(x, int)]
        if not int_data:
            cur_control_sum = 0
        else:
            cur_control_sum = min(int_data) * max(int_data)
    else:
        int_keys = [x for x in data.keys() if isinstance(x, int)]
        if not int_keys:
            cur_control_sum = 0
        else:
            cur_control_sum = sum(int_keys)
    if cur_control_sum == control_sum:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')