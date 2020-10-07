import pickle
VITAP = {"clubs":["OSC","Bioscope"],"schools":["SENSE","SCOPE"]}
pickle_write = open("WSOC.pkl","wr")
pickle.dump(VITAP,pickle_write) #saves into WSOC.pkl  
