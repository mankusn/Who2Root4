import csv
import os
import operator
#import FootballLeague as fl




#returns what percentile team lies in
def percentile(collection,team,stat,desc):
    rank = (find_rank(collection,team,stat,desc))
    return 100-(rank*100/len(collection))
#returns rank of specific team
def find_rank(collection,team,stat,desc):
    orderedList = order_stats_by(collection,stat,desc)
    return [y[0] for y in orderedList].index(team) + 1

#returns an ordered list of specific team-stat tuples
def order_stats_by(collection,stat,desc):
    results = {}
    for team in collection.keys():
        entry = collection[team][stat]
        if entry == '':
            entry = '0'
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
#imports data from csv files
def import_data(statistics,directory):
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            name =str(file)[:-4].replace("_"," ")
            statistics[name] = get_csv_data(file)

