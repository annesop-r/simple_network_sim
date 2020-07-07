"""
a converter to take files of the kind linked here: 
https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/population/population-estimates/2011-based-special-area-population-estimates/small-area-population-estimates/mid-2016/detailed-data-zone-tables 
and generate something in the format linked here: 
https://github.com/ScottishCovidResponse/simple_network_sim/blob/master/sample_input_files/sample_hb2019_pop_est_2018_row_based.csv Write a converter 

For example: 
Health_Board,Sex,Age,Total
S08000015,Female,"[0,17)",31950
S08000015,Female,"[17,70)",127574
S08000015,Female,70+,32930
S08000015,Male,"[0,17)",33357
S08000015,Male,"[17,70)",118106
S08000015,Male,70+,25753
"""

from pathlib import Path
from urllib.request import urlretrieve
import openpyxl
import pandas as pd
import numpy as np

# import the Health Board and Local Authority data dictionaries we need
import healthBoardData as ds









# First get the data file
#if the following files do not exist get them, they contains the population data
mal_data_file = Path("./downloads/2016-sape-det-tab-mal.xlsx")
fem_data_file = Path("./downloads/2016-sape-det-tab-fem.xlsx")
try:
    mal_data_file.resolve(strict=True)
    fem_data_file.resolve(strict=True)
except FileNotFoundError:
    print("Retrieving data from https://www.nrscotland.gov.uk/files//statistics/population-estimates/sape16/")
    url = 'https://www.nrscotland.gov.uk/files//statistics/population-estimates/sape16/2016-sape-det-tab-mal.xlsx'
    urlretrieve(url, mal_data_file)
    url = 'https://www.nrscotland.gov.uk/files//statistics/population-estimates/sape16/2016-sape-det-tab-fem.xlsx'
    urlretrieve(url, fem_data_file)


# The age ranges defined in simple_network_sim as keys and a list of the ages (column names int he form AGEX
# in the spreadsheet) as values
# NOTE: To change the returned age just edit these lines, 
age_ranges = {
"[0,17)" : ["AGE" + str(x) for x in range(0,17)],
"[17,70)" : ["AGE" + str(x) for x in range(17, 70)],
"70+" :  ["AGE" + str(x) for x in range(70, 120)]
}

# Read the excel spreadsheet and transform the data by
# removing the first n lines and the last 2 (a blank line followed by the copyright symbol)
# adding column names to the dataframe (Area, Council Area, All Ages, AGE0, AGE1, etc)

fem_data = pd.read_excel(fem_data_file, header=3) 
mal_data = pd.read_excel(mal_data_file, header=3) 

new_columns = fem_data.columns.values
new_columns[0] = 'Area'
new_columns[1] = 'Council Area'
new_columns[2] = 'All Ages'
for i in range(0, len(new_columns)):
    new_columns[i] = new_columns[i].rstrip('+') 
fem_data.columns  = new_columns
mal_data.columns  = new_columns

# do a little cleaning up, remove the first and last two rows
fem_data.drop(fem_data.head(2).index, inplace=True)
fem_data.drop(fem_data.tail(2).index, inplace=True)
mal_data.drop(mal_data.head(2).index, inplace=True)
mal_data.drop(mal_data.tail(2).index, inplace=True)


def calcTotalsInAgeGroupsByHealthBoard(dataFrame, sex):
    """
    Given a dataFrame obbject with the data from the excel spreadsheet,
    group the data by council area and age group (as defined in the
    age_ranges dict) and return a dict with (health board Id, Sex, age range)
    as a key and the population in that category as a value.
    """
    data_by_council_area = dataFrame.groupby(by=['Council Area'])
    health_board_data = {}

    for la_name, grouping in data_by_council_area:
        # the name is the council area, we need to get the id of the health board this is in
        # but before we do we have to make sure the name is a valid local authority name
        hb_id = ds.LocalAuthorityToHealthBoardIdMap[la_name]

        for group, ages in age_ranges.items():
            group_sum=0
            for age in ages:
                try:
                    group_sum += grouping[age].agg(np.sum)
                except KeyError:
                    pass # the age wasn't found in the females_by_council_area

                # Now we have the hb_id, the sex, age and the total in that age group,
                # append id to the health_board_data
            key = (hb_id, f"{sex}", group)
            if key in health_board_data:
                health_board_data[key] = health_board_data[key] + group_sum
            else:
                health_board_data[key] = group_sum
    return health_board_data


female_age_data = calcTotalsInAgeGroupsByHealthBoard(fem_data, "Female")
male_age_data = calcTotalsInAgeGroupsByHealthBoard(mal_data, "Male")


# Now we need to print these in the right format
#Health_Board,Sex,Age,Total
#S08000015,Female,"[0,17)",31950
# Note, these will not be in alphabetical order....
with open("hb2019_pop_est.csv", "w") as f:
    f.write("Health_Board,Sex,Age,Total")
    for key, val in female_age_data.items():
        f.write(f"{key[0]},{key[1]},\"{key[2]}\",{int(val)}\n")
    for key, val in male_age_data.items():
        f.write(f"{key[0]},{key[1]},\"{key[2]}\",{int(val)}\n")

# we can just ѕort this on the command line but is no better than
"""
data = []
for key, val in female_age_data.items():
    data.append(f"{key[0]},{key[1]},\"{key[2]}\",{int(val)}\n")
for key, val in male_age_data.items():
    data.append(f"{key[0]},{key[1]},\"{key[2]}\",{int(val)}\n")

data.sort()
"""

