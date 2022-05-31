from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier as dtc
import xgboost
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score
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


x = ipdata.drop(columns=['ProtocolName', 'Fwd.Packet.Length.Std', 'Bwd.Packet.Length.Std', 'Fwd.IAT.Std', 'Bwd.IAT.Std', 'Fwd.Header.Length', 'Bwd.Header.Length', 'Packet.Length.Std', 'Packet.Length.Variance', 'Avg.Fwd.Segment.Size',
                'Avg.Bwd.Segment.Size', 'Fwd.Header.Length.1', 'Subflow.Fwd.Packets', 'Subflow.Fwd.Bytes', 'Subflow.Bwd.Packets', 'Subflow.Bwd.Bytes', 'Init_Win_bytes_forward', 'Init_Win_bytes_backward', 'act_data_pkt_fwd', 'min_seg_size_forward'])
y = ipdata['ProtocolName']
print(ipdata.shape)

print(x.columns)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=3)
a = y_train.to_numpy()
np.unique(a, return_counts=True)

# print("START XBG")
# xgb_classify = xgboost.XGBClassifier(verbosity=1)
# xgb_classify.fit(x_train, y_train)
# preds = xgb_classify.predict(x_test)
# print(explained_variance_score(preds, y_test))
# print("END XBG")


# print("START DTC")
# tree_classify = dtc()
# tree_classify.fit(x_train, y_train)
# pred = tree_classify.predict(x_test)
# print(explained_variance_score(pred, y_test))
# print("END DTC")


# print("START SVC")
# svm_classify = SVC()
# svm_classify.fit(x_train, y_train)
# pred = svm_classify.predict(x_test)
# print(explained_variance_score(pred, y_test))
# print("END SVC")

# xgb_classify.save_model('xgb_classify.h5')
