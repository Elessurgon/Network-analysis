import csv
import zipfile
import pandas as pd


def transform():
    filename = 'test_data.csv'
    x = []
    with open(filename, 'r') as f:
        r = csv.reader(f)
        lines = list(r)
        line = lines[0]
        for i in line:
            x.append(i.lstrip().rstrip().replace(' ', '.'))

    with open(filename, newline='') as inFile, open('test_out.csv', 'w', newline='') as outfile:
        r = csv.reader(inFile)
        w = csv.writer(outfile)

        next(r, None)
        w.writerow(x)

        for row in r:
            w.writerow(row)


with zipfile.ZipFile('Dataset-Unicauca-Version2-87Atts.zip') as zip:
    with zip.open('Dataset-Unicauca-Version2-87Atts.csv') as myZip:
        data = pd.read_csv(myZip)

data.dropna(inplace=True)
ipdata = data.copy()
ipdata.drop(['Timestamp', 'Flow.ID'], axis=1, inplace=True)
single_unique_cols = [
    col for col in ipdata.columns if ipdata[col].nunique() == 1]


ipdata.drop(single_unique_cols, axis=1, inplace=True)
ip_add_cols = ['Source.IP', 'Source.Port',
               'Destination.IP', 'Destination.Port']
ipdata.drop(ip_add_cols, axis=1, inplace=True)
ipdata.drop(columns=['ProtocolName', 'Fwd.Packet.Length.Std', 'Bwd.Packet.Length.Std', 'Fwd.IAT.Std', 'Bwd.IAT.Std', 'Fwd.Header.Length', 'Bwd.Header.Length', 'Packet.Length.Std', 'Packet.Length.Variance', 'Avg.Fwd.Segment.Size',
                     'Avg.Bwd.Segment.Size', 'Fwd.Header.Length.1', 'Subflow.Fwd.Packets', 'Subflow.Fwd.Bytes', 'Subflow.Bwd.Packets', 'Subflow.Bwd.Bytes', 'Init_Win_bytes_forward', 'Init_Win_bytes_backward', 'act_data_pkt_fwd', 'min_seg_size_forward'], inplace=True)


df = pd.read_csv('test_out.csv')

df_top = [i for i in df.columns]
data_top = [i for i in ipdata.columns]
s1 = set(df_top)
s2 = set(data_top)

print(list(s2.intersection(s1)))
