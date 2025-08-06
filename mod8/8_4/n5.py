def dict_travel(d):
    def make_flattened_dict(d, cur_key=''):
        res = dict()
        for key, value in d.items():
            if isinstance(value, dict):
                new_key = f'{cur_key}.{key}' if cur_key else key
                nested_res = make_flattened_dict(value, new_key)
                res.update(nested_res)
            else:
                if cur_key:
                    res[cur_key + '.' + key] = value
                else:
                    res[key] = value
        return res

    flattened = make_flattened_dict(d)
    for key, value in sorted(flattened.items()):
        print(f'{key}: {value}')


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)

data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)

data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)