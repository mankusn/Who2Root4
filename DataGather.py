import csv
import os
import operator

#returns an ordered list of specific team-stat tuples
def ordered_statistics(collection,stat,desc):
    # if stat not in collection:
    #     print "Stat does not exist"
    #     return []
    results = {}
    for team in collection.keys():
        entry = collection[team][stat]
        results[team] = float(entry)
    return sorted(results.items(), key=operator.itemgetter(1),reverse=desc)

#gets a dictionary of statistics, team name is the key
def import_csv_data(filename):
    reader = csv.DictReader(open(filename,'rU'))
    dictionary = {}
    for row in reader:
        key = row.pop('Tm')
        if key in dictionary:
            continue
        dictionary[key] = row
    return dictionary
def main():


    statistics={}
    for file in os.listdir('.'):
        if file.endswith(".csv"):
            name =str(file)[:-4].replace("_"," ")
            statistics[name] = import_csv_data(file)

    #Sample data access: statistics[#statistical set][#teamname][#statistic]
    print type(statistics["NFL Pass Defense"]["Denver Broncos"]['YdsL'])
    
    a = ordered_statistics(statistics["NFL Pass Defense"], "TD",False)
    print a[1][0]

if __name__ == '__main__':
    main()