import pickle

def serialize_dump(obj):
    with open('serialized_data.txt', 'wb+') as file_object:
        pickle.dump(obj, file_object)
    return

def deserialize_dump():
    with open('serialized_data.txt', 'rb+') as file_object:
        data = pickle.load(file_object)
    return data   