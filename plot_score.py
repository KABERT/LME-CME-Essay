from clean_data import get_country_info
import matplotlib.pylab as plt
import pandas as pd
import numpy as np

def get_plot(path="data/data.csv"):
    df = pd.read_csv(path)
    X, y = [], []
    country_name, _, country_type = get_country_info()
    print(country_name)
    for i in range(len(df["Country"])):
        if df.iloc[i][1].strip() in country_name:
            name = df.iloc[i][1].strip()
            X.append([df.iloc[i][2], df.iloc[i][3]])
            y.append(country_type[country_name.index(name)])
    X = np.asarray(X)

    plt.title("LME CME score through Change")
    plt.scatter(X[:, 0], X[:, 1], color=["r" if y_point == -1 else "b" if y_point == 1 else "g" for y_point in y], s=20,
                alpha=0.5)
    plt.show()


def get_best_line(path="data/data.csv"):
    df = pd.read_csv(path)
    X, y = [], []
    country_name, _, country_type = get_country_info()
    for i in range(len(df["Country"])):
        if df.iloc[i][1].strip() in country_name:
            name = df.iloc[i][1].strip()
            X.append([df.iloc[i][2], df.iloc[i][3]])
            y.append(country_type[country_name.index(name)])
    LME, CME = {}, {}
    for i in range(len(X)):
        point = X[i]
        # The conutry is CME:
        if y[i] == 1:
            if point[0] not in CME:
                CME[point[0]] = [point[1]]
            else:
                CME[point[0]].append(point[1])
        # The conutry is CME:
        else:
            if point[0] not in LME:
                LME[point[0]] = [point[1]]
            else:
                LME[point[0]].append(point[1])

    for keys in LME:
        lst = LME[keys]
        LME[keys] = sum(lst) / len(lst)

    for keys in CME:
        lst = CME[keys]
        CME[keys] = sum(lst) / len(lst)
    print(LME)
    print(CME)


if __name__ == "__main__":
    get_best_line()
