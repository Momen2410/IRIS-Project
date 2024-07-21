import pickle

def LoadModel(file_path: str):

    with open(file_path, 'rb') as file:
        loaded_model = pickle.load(file)

    return loaded_model