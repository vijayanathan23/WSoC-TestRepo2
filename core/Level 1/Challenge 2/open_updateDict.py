import pickle
pickle_rw = open("WSOC.pkl","rb") #opening the required pickle file in read mode
VITAP = pickle.load(pickle_rw) #stores the pickle file values into VITAP
print(VITAP)
VITAP["clubs"].append("Beat the Heat")
pickle_rw.close()
pickle_write = open("WSOC.pkl","wb")
print("Updating dictionary")
pickle.dump(VITAP,pickle_write) #updating pickle 
pickle_write.close()
