import csv
import os


def import_csv_data(filename):


    reader = csv.DictReader(open(filename,'rU'))

    dictionary = {}
    for row in reader:
        key = row.pop('Tm')
        if key in dictionary:
            # implement your duplicate row handling here
            pass
        dictionary[key] = row
    return dictionary
def main():

    statistics={}
    nfl = import_csv_data("NFL_Pass_Offense.csv")
    print nfl
    print nfl["New Orleans Saints"]["Att"]
    for file in os.listdir('.'):
        if file.endswith(".csv"):
            name =str(file)[:-4].replace("_"," ")
            statistics[name] = import_csv_data(file)


    print statistics["NFL Pass Offense"]


if __name__ == '__main__':
    main()