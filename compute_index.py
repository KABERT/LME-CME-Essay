import pandas as pd

def get_index(input_path="data/all in one excel.xlsx", output_path ="data/test.xlsx"):
    df = pd.read_excel(input_path)
    titles = df.columns.ravel().tolist()[1:]
    r_df = init_df(titles, df)
    all_data = {}
    for i in range(2, len(titles)):
        subject = titles[i]
        for c in range(19):
            for j in range(19):
                country_type = df["Country Type"].tolist()[j*19+c]
                # Check if subject is in all_data:
                if subject not in all_data:
                    all_data[subject] = [[], []]
                if country_type == 1:
                    all_data[subject][0].append(df[subject].tolist()[j*19+c])
                if country_type == -1:
                    all_data[subject][1].append(df[subject].tolist()[j*19+c])
    print(all_data)
    # r_df.to_excel(output_path, index=True)


def init_df(titles, df):
    r_df = pd.DataFrame(columns=titles)
    yr_list = df["Year"].tolist()[:19]
    for i in range(38):
        df1 = pd.DataFrame([["NaN"] * (len(df.columns) - 1)], columns=titles)
        r_df = df1.append(r_df, ignore_index=True, sort=False)
    for i in range(38):
        if i < 19:
            r_df.iloc[i][1] = yr_list[i]
            r_df.iloc[i][2] = "LME"
        else:
            r_df.iloc[i][1] = yr_list[i-19]
            r_df.iloc[i][2] = "CME"
    return r_df


if __name__ == "__main__":
    get_index()
