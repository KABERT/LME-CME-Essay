import pandas as pd
import math
from clean_data import get_country_info


def out_put_in_one_excel(input_path="data/washed.xlsx", output_path="data/all in one excel.xlsx"):
    df = pd.ExcelFile(input_path)
    sheets = df.sheet_names
    output = pd.DataFrame(columns=["Country", "Year", "Country Type"] + sheets)
    # read the sheet one by one
    for sheet_name in sheets:
        sheet = pd.read_excel(df, sheet_name)
        output = extract_data_from_excel_to_df(sheet, sheet_name, output)
    output.to_excel(output_path, index=True)


def extract_data_from_excel_to_df(excel_df, sheet_name, df):
    title = excel_df.columns.ravel().tolist()
    country_list, yr_list = excel_df[title[0]].tolist(), title[1:]
    # Check if the df is empty
    if len(df["Country"].tolist()) == 0:
        df = init_output(df, yr_list, country_list)

    # If the df is not empty, add the information into the sheet.
    subject_index = df.columns.ravel().tolist().index(sheet_name)
    print(sheet_name)
    for i in range(len(country_list)):
        for j in range(len(yr_list)):
            pos = i * len(yr_list) + j
            # Filter through the dataframe, if it is not a number, then keep "NaN"
            val = excel_df.iloc[i][j+1]
            if not type(val) == str and not math.isnan(val):
                    df.iloc[pos][subject_index] = val
    return df


def init_output(df, yr_list, country_list):
    # Init a Dataframe with all NaN.
    for i in range(len(yr_list) * (len(country_list))):
        df1 = pd.DataFrame([["NaN"] * len(df.columns)], columns=df.columns)
        df = df1.append(df, ignore_index=True)

    _, _, country_type = get_country_info()

    # Write Country and Years into the column
    for i in range(len(country_list)):
        for j in range(len(yr_list)):
            pos = i * len(yr_list) + j
            df.iloc[pos][0] = country_list[i]
            df.iloc[pos][1] = int(yr_list[j])
            df.iloc[pos][2] = country_type[i]
    return df


if __name__ == "__main__":
    out_put_in_one_excel()
