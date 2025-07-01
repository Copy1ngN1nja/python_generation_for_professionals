import pickle, sys

def func(*args):
    return ' '.join(args)

lines = [line.strip() for line in sys.stdin if line.strip()]
pkl_file = lines[0]
with open(pkl_file, mode='rb') as func_file:
    f = pickle.load(func_file)

args = lines[1:]
result = f(*args)
print(result)