import csv
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

x,y=[],[]
print('please wait...')
with open('./output.csv','r') as file:
    readFile = csv.reader(file,delimiter='#')
    for row in readFile:
        
        x.append(row[0:4])
        y.append(row[4])

encoder = OneHotEncoder(sparse_output=False)
x_encoded = encoder.fit_transform(x)

labelEncoder = LabelEncoder()
y_encoded = labelEncoder.fit_transform(y)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_encoded,y_encoded)

while True:
    try:
        a1 = input('name:')
        a2 = input('mileage:')
        a3 = input('year:')
        a4 = input('location:')
        newData = [[a1,a2,a3,a4]]
        newDataEncoded = encoder.transform(newData)

        encodedAnswer = clf.predict(newDataEncoded)

        answer = labelEncoder.inverse_transform(encodedAnswer)

        for i in answer:
            print("predicted price:",i,'تومان')
            print("********")
    except ValueError:
        print('Invalid Data.')
        print("********")
        