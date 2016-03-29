import csv
import os
import operator

#returns rank of specific team
def find_rank(collection,team,stat,desc):
    orderedList = ordered_statistics(collection,stat,desc)
    return [y[0] for y in orderedList].index(team) + 1

#returns an ordered list of specific team-stat tuples
def ordered_statistics(collection,stat,desc):
    results = {}
    for team in collection.keys():
        entry = collection[team][stat]
        results[team] = float(entry)
    return sorted(results.items(), key=operator.itemgetter(1),reverse=desc)

#gets a dictionary of statistics, team name is the key
def get_csv_data(filename):
    reader = csv.DictReader(open(filename,'rU'))
    dictionary = {}
    for row in reader:
        key = row.pop('Tm')
        if key in dictionary:
            continue
        dictionary[key] = row
    return dictionary
def import_data(statistics):
    for file in os.listdir('.'):
        if file.endswith(".csv"):
            name =str(file)[:-4].replace("_"," ")
            statistics[name] = get_csv_data(file)

def main():


    statistics={}
    import_data(statistics)

    #Sample data access: statistics[#statistical set][#teamname][#statistic]
    print statistics["NFL Pass Defense"]["Denver Broncos"]['YdsL']

    print ordered_statistics(statistics["NFL Pass Defense"], "TD",False)
    a= ordered_statistics(statistics["NFL Pass Offense"], "Yds",True)
    print a
    print find_rank(statistics["NFL Pass Offense"],"New England Patriots","Yds",True)

if __name__ == '__main__':
    main()