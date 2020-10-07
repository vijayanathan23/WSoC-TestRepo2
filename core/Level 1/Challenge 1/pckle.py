import pickle
infile = open('data.pkl','rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
