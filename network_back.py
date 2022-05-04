# import and libraries
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import zipfile
with zipfile.ZipFile('Dataset-Unicauca-Version2-87Atts.zip') as zip:
    with zip.open('Dataset-Unicauca-Version2-87Atts.csv') as myZip:
        data = pd.read_csv(myZip)


# get non numeric columns
non_num_cols = [col for col in data.columns if data[col].dtype == 'O']
non_num_data = data[non_num_cols]

# get distribution of non numeric columns
num_cols = list(set(data.columns) - set(non_num_cols))
data[num_cols].describe()


# proportions of values in non numeric
def summarize_cat(col_name):
    df = pd.DataFrame(columns=['Summary', 'Proportion'])
    sorted_values = sorted(non_num_data[col_name].value_counts(
    ).iteritems(), key=lambda x: x[1], reverse=True)
    remaining_per = 100
    for (value, count) in sorted_values:
        per = count / len(non_num_data) * 100
        if per >= 1:
            df2 = pd.DataFrame({'Summary': [value],
                                'Proportion': [f'{per:.2f}%'],
                                })
            df = pd.concat([df, df2], ignore_index=True, axis=0)

            print(f'{value} : {per:.2f}%')
        else:
            df2 = pd.DataFrame({'Summary': ['Others'],
                                'Proportion': [f'{remaining_per:.2f}%'],
                                })

            df = pd.concat([df, df2], ignore_index=True, axis=0)
            print(f'Others : {remaining_per:.2f}%')
            break
        remaining_per = remaining_per - per
    return df


for col in non_num_cols:
    print(f"Summary of {col} column : ")
    df = summarize_cat(col)
    df.to_csv(f"./analysis/Summary_of_{col}_column.csv")
    print('\n')


# histogram
cols_for_hist = [col for col in num_cols if data[col].nunique() <= 50]
data[cols_for_hist].hist(layout=(7, 3), figsize=(12, 20))
plt.tight_layout()

# # correlation matrix
corr = data[num_cols].corr()
f = plt.figure(figsize=(25, 25))
plt.matshow(corr, fignum=f.number)
plt.title('Correlation Matrix of Numeric columns in the dataset', fontsize=20)
plt.xticks(range(len(num_cols)), num_cols, fontsize=14, rotation=90)
plt.yticks(range(len(num_cols)), num_cols, fontsize=14)
plt.gca().xaxis.set_ticks_position('bottom')
cb = plt.colorbar(fraction=0.0466, pad=0.02)
cb.ax.tick_params(labelsize=10)
plt.show()


# network graph
N = nx.from_pandas_edgelist(
    data, source='Source.IP', target='Destination.IP', edge_attr=None)
degrees = [N.degree[node] for node in N.nodes()]
pos = nx.random_layout(N)
plt.figure(3, figsize=(20, 12))
nx.draw_networkx_nodes(N, pos, node_size=degrees)
nx.draw_networkx_edges(N, pos, alpha=0.005)
plt.savefig("./analysis/Graph.png", format="PNG")
plt.show()
