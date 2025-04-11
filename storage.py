import os
import pickle

class Storage:
    def __init__(self):
        self.filename = r"C:\Users\292593\Desktop\master\python training\Hackatons\Friday_4th\292593_SanjuJacob_UST\Hackaton_11_April\Hackaton3_v2\storage_data.pkl"

    def save_data(self, data):
        directory = os.path.dirname(self.filename)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(self.filename, "wb") as f:
            pickle.dump(data, f)

    def load_data(self):
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []
        except pickle.UnpicklingError:
            print("Error unpickling file. Data might be corrupted.")
            return []
