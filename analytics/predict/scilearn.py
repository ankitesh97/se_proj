
from sklearn import svm
from firebase import firebase
import numpy as np

db = firebase.FirebaseApplication('https://agrilife-7cbc7.firebaseio.com/',None)
result = db.get('/dataset',None)
crops_list = db.get('/crops',None)
crops_list = crops_list.values()
result = result.values()
temp = [result[0]['N'],result[0]['P'],result[0]['K'],result[0]['water']]
X = np.matrix(temp) #dataset
y = np.matrix(result[0]['crop_class']) #observed values
num_labels = len(result)
for i in range(1,len(result)):
	temp = [result[i]['N'],result[i]['P'],result[i]['K'],result[i]['water']]
	X = np.vstack((X,temp))
	temp = result[i]['crop_class']
	y = np.vstack((y,temp))

clf = svm.SVC(gamma=0.001, C=100)
clf.fit(X,y)
prediction =  clf.predict([10,20,14,11])

hand = filter(lambda x: x['id'] == prediction[0],crops_list).pop()

print "predicted crops that can be grown is " + hand['name']
