import numpy as np 
from sklearn import preprocessing, neighbors, model_selection
import pandas as pd 

df = pd.read_csv('votering2.csv')
print(list(df))
df.drop(['punkt'], 1, inplace = True)

df = df[["rost", "parti", "fodd", "kon", "intressant_id"]]

print(df.head(3))

input_label = ['kvinna', 'man'] #kvinna -> 0 man -> 1
encoder = preprocessing.LabelEncoder()
encoder.fit(input_label)
df['kon'] = encoder.transform(df['kon'])

input_label = ['C','KD','M','L','MP','V','M','S','SD',"-"] #- -> 0 C -> 1 KD -> 2 L -> 3 M -> 4 MP -> 5 S -> 6 SD -> 7 V -> 8
encoder.fit(input_label)
df['parti'] = encoder.transform(df['parti'])

input_label = ['Nej','Ja','Frånvarande','Avstår'] #Avstår -> 0 Frånvarande -> 1 Ja -> 2 Nej -> 3
encoder.fit(input_label)
df['rost'] = encoder.transform(df['rost'])

for i, item in enumerate(encoder.classes_):
    print(item, "--->", i)

df.replace('?', '-9999', inplace= True)

print(df.head(4))

X = np.array(df.drop(['rost'], 1))
Y = np.array(df['rost'])

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y, test_size=  0.2)
X_train = X_train.reshape(len(X_train), -1)
Y_train = Y_train.reshape(len(Y_train), -1)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)
print("Accuracy is " + str(accuracy) + ", nice!")

#print(X_test[0])

#"Anne Oskarsson","42413114103","SD","Kalmar län","Ja","sakfrågan","60","kvinna","1946","2019-11-28"
#"Jörgen Hellman","781520322912","S","Västra Götalands läns norra","Ja","sakfrågan","100","man","1963","2019-11-28"

#"Maria Stockhaus","932000030511","M","Stockholms län","Ja","sakfrågan","246","kvinna","1963","2018-06-20"
#"Olle Felten","46426524512","-","Södermanlands län","Ja","sakfrågan","286","man","1953","2018-06-20"

example_measure = np.array([[4,1963,0,932000030511], [0,1953,0,46426524512]])

example_measure = example_measure.reshape(len(example_measure), -1)
prediction = clf.predict(example_measure)
print(prediction)

decoded_list = encoder.inverse_transform(prediction)
print("Decoded", list(decoded_list))

