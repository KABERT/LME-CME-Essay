import pandas as pd
from clean_data import get_country_info


def check_countries_application(path):
    _, _, all_target_country = get_country_info()
    df = pd.read_csv(path, sep=None)
    titles = df.columns.ravel().tolist()
    country_dict = {}
    target_ctry_code = get_target_country()
    for i in range(len(df[titles[1]])):
        # Check if the patent yr is in range:
        if int(df[titles[5]][i]) >= 2000:
            # Check if the patent is granted
            if df[titles[20]][i] == "Y":
                # Check if the patent country is wanted:
                if df[titles[1]][i] in target_ctry_code:
                    if df[titles[1]][i] not in country_dict:
                        country_dict[df[titles[1]][i]] = 1
                    else:
                        country_dict[df[titles[1]][i]] += 1
    print(country_dict)
    count = 0
    for keys in country_dict:
        count += country_dict[keys]


def get_target_country(path="/Users/jinhanmei/Desktop/PATSTAT_Sample_2018Autumn_Global_CSV/tls801_country.csv"):
    country, _, country_type = get_country_info()
    country = country[:country_type.index(0)]
    df = pd.read_csv(path, sep=None)
    titles = df.columns.ravel().tolist()
    ctry_code, ctry_name = df[titles[0]].tolist(), df[titles[2]].tolist()
    r_lst = []
    for i in range(len(ctry_name)):
        if ctry_name[i] in country:
            r_lst.append(ctry_code[i])
    # Add 'US' in the r_lst.
    r_lst.append('US')
    print(r_lst)
    return r_lst


def check_duplicated_class(path="/Users/jinhanmei/Desktop/PATSTAT_Sample_2018Autumn_Global_CSV/tls209_appln_ipc.csv"):
    '''
    class查重，看看是否有一个patent对应多个class的情况。
    '''
    df = pd.read_csv(path,sep=None)
    titles = df.columns.ravel().tolist()
    appln_id_lst = []
    count = 0
    appln_id = df[titles[0]]
    for i in range(len(df[titles[0]])):
        if appln_id[i] not in appln_id_lst:
            appln_id_lst.append(appln_id[i])
        else:
            count += 1
        print(i)
    print(len(appln_id), count)


def check_under_threshold_patent(path="data/patent count by country yr and class.csv", threshold=100):
    df = pd.read_csv(path, sep=";")
    titles = df.columns.ravel().tolist()
    count, total = df[titles[-1]], 0
    dict = {}
    for i in range(len(count)):
        if int(count[i]) < threshold:
            total += 1
            info = df.iloc[i]
            if info[0] not in dict:
                dict[info[0]] = 1
            else:
                dict[info[0]] += 1
    print(len(dict))
    print(dict)
    print(total)


if __name__ == "__main__":
    # check_countries_application("/Users/jinhanmei/Desktop/PATSTAT_Sample_2018Autumn_Global_CSV/tls201_appln.csv")
    # check_duplicated_class()
    check_under_threshold_patent()
