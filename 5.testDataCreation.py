import pandas as pd

nds = pd.DataFrame(columns=['0', '1', '2', '3', '4', '5', '6', 'predict'])

flag = 0

for j in range(12):
    path = "test/" + str(j) + ".txt"
    Kf = open(path, 'r')
    kf = Kf.read()
    d = kf.split(",")

    nds.loc[flag] = [d[0], d[1], d[2], d[3], d[4], d[5], d[6], ""]
    flag = flag+1

nds.to_csv('test.csv')