import pickle

def filter_dump(pkl_file_name, objects, typename):
    with open(pkl_file_name, mode='wb') as pkl_file:
        objects = list(filter(lambda x: isinstance(x, typename), objects))
        pickle.dump(objects, pkl_file) 