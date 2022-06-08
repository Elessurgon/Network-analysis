from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier as dtc
import xgboost
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, explained_variance_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import zipfile
with zipfile.ZipFile('Dataset-Unicauca-Version2-87Atts.zip') as zip:
    with zip.open('Dataset-Unicauca-Version2-87Atts.csv') as myZip:
        data = pd.read_csv(myZip)

data.dropna(inplace=True)

ipdata = data.copy()

print("No. of unique values in Timestamp column :",
      ipdata['Timestamp'].nunique())
print("No. of unique values in FlowID column :", ipdata['Flow.ID'].nunique())

ipdata.drop(['Timestamp', 'Flow.ID'], axis=1, inplace=True)
single_unique_cols = [
    col for col in ipdata.columns if ipdata[col].nunique() == 1]
print(single_unique_cols)

ipdata.drop(single_unique_cols, axis=1, inplace=True)

ip_add_cols = ['Source.IP', 'Source.Port',
               'Destination.IP', 'Destination.Port']
# ipdata[ip_add_cols]

ipdata.drop(ip_add_cols, axis=1, inplace=True)

encoder = LabelEncoder().fit(ipdata['ProtocolName'])
ipdata['ProtocolName'] = encoder.fit_transform(ipdata['ProtocolName'])
# ipdata['ProtocolName']
print(ipdata.columns)
ipdata = ipdata.iloc[:100000, :]


df = pd.read_csv('test_out.csv')

df_top = [i for i in df.columns]
data_top = [i for i in ipdata.columns]
s1 = set(df_top)
s2 = set(data_top)

cols = list(s2.intersection(s1))

x = ipdata[ipdata.columns & cols]
y = ipdata['ProtocolName']

print(ipdata.shape)

print("Features considered:")
for i in x.columns:
    print(i)
print("\nFeatures to Predict:\nProtocolName\n")


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=3)
a = y_train.to_numpy()
np.unique(a, return_counts=True)

print("START XBG")
xgb_classify = xgboost.XGBClassifier(verbosity=1)
xgb_classify.fit(x_train, y_train)
preds = xgb_classify.predict(x_test)
print(explained_variance_score(preds, y_test))
print(accuracy_score(preds, y_test))
print("END XBG")


print("START DTC")
tree_classify = dtc()
tree_classify.fit(x_train, y_train)
pred = tree_classify.predict(x_test)
print(explained_variance_score(pred, y_test))
print(accuracy_score(preds, y_test))
print("END DTC")


print("START SVC")
svm_classify = SVC()
svm_classify.fit(x_train, y_train)
pred = svm_classify.predict(x_test)
print(explained_variance_score(pred, y_test))
print(accuracy_score(preds, y_test))
print("END SVC")

xgb_classify.save_model('xgb_classify.h5')
tree_classify.save_model('tree_classify.h5')
svm_classify.save_model('xgb_classify.h5')
