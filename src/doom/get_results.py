import pickle
# load : get the data from file
file_path = "/home/ianal/work/Gaming/Doom-Map-Generation/Arnold/dumped/test/zsehrir6ht/params.pkl"
data = pickle.load(open(file_path, "rb"))
print(data )