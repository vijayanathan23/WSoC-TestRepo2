import pickle
import matplotlib.pyplot as plot
pickle_read = open("Data.pkl","rb") #opening pkl file in read mode
sub = pickle.load(pickle_read) #unpickle
print(sub)

#getting keys and values 
subs = sub.keys()
marks = sub.values()


#subs-> type(dict) to subs ->type(list)
subList = []
for x in subs:
	subList.append(x)

#similarly to marks
markList = []
for x in marks:
	markList.append(x)

#making percentage value (ocnverting "out of 50" to "out of 100")

for i in range(len(markList)):
	markList[i] = markList[i]/50.0
	markList[i] = markList[i] * 100
	



plot.pie(markList,labels=subList) #plotting pie chart and displying
plot.show() 


#creating xpos for bar graph
xpos = []
i = 0
for x in subList:
	xpos.append(i)
	i = i+1

plot.xticks(xpos,subList)#subject list in x-axsis 
plot.bar(xpos,markList)#plotting bargraph
plot.show() #displaying bargraph
