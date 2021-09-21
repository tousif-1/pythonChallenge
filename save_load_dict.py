# Saving dictionary objects to file
# using pickle module: https://docs.python.org/3/library/pickle.html
# Python pickle module is used for serializing and de-serializing a Python object structure,
# it  is a way to convert a python object (list, dict, etc.) into a character stream

import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

test_dict = {1: 'a', 2:'b', 3:'c'}

save_dict(test_dict, 'test_dict.pickle')
recovered = load_dict('test_dict.pickle')
print(recovered)
