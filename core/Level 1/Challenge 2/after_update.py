import pickle
infile = open('WSOC.pkl','rb')
new_dict = pickle.load(infile)
infile.close()
print("From: updated file")
print(new_dict)
