import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

def preprocess_data(xv, yv, grpvar, data):
    """
    docstring for later
    """
    n = data[grpvar].value_counts().tolist()[0]
    seq = range(1, n+1)
    ID = np.repeat(seq, len(data)/len(seq))
    data.insert(0, "ID", ID)

    xwide = data.pivot(index = "ID", columns = grpvar, values = xv)
    ywide = data.pivot(index = "ID", columns = grpvar, values = yv)

    num_times = len(xwide.columns)
    num_ent = len(xwide.index)

    allxt = xwide.iloc[:, :-1].values.flatten("F").tolist() # Fortran Style
    allyt = ywide.iloc[:, :-1].values.flatten("F").tolist()

    mx = np.nanmean(allxt)
    my = np.nanmean(allyt)

    tichxt = xwide.diff(axis = 1,
                        periods = 1).drop(xwide.columns[0],
                                          axis=1).values.flatten("F").tolist()
    tichyt = ywide.diff(axis = 1,
                        periods = 1).drop(ywide.columns[0],
                                          axis=1).values.flatten("F").tolist()
    idmiss =  list(set(np.argwhere(np.isnan([allxt, allyt,
                                             tichxt, tichyt])).flatten()))
 
    allx = [v for i, v in enumerate(allxt) if i not in idmiss]
    ally = [v for i, v in enumerate(allyt) if i not in idmiss]
    tichx = [v for i, v in enumerate(tichxt) if i not in idmiss]
    tichy = [v for i, v in enumerate(tichyt) if i not in idmiss]
    xs = allx / mx
    ys = ally / my
    chxs = tichx / mx
    chys = tichy / my

    output = {"xwide": xwide, "ywide": ywide, "num_times": num_times,
              "num_ent": num_ent, "allx": allx, "ally": ally,
              "tichx": tichx, "tichy": tichy, "mx": mx, "my": my,
              "xs": xs, "ys": ys, "chxs": chxs, "chys": chys}
    return output
