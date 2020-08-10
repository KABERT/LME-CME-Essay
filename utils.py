def join_all_data(path="data/temp/resulttable-"):
    temp = []
    for i in range(1, 153):
        file_name = path + str(i) + ".csv"
        with open(file_name, 'r') as f:
            lines = f.readlines()[1:]
            temp += lines
    with open(path+"0.csv", 'w') as f:
        for item in temp:
            f.write("%s" % item)


if __name__ =='__main__':
    join_all_data()
