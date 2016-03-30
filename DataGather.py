import csv
import os
import operator

#returns what percentile team lies in
def percentile(collection,team,stat,desc):
    rank = (find_rank(collection,team,stat,desc))
    return (rank*100/len(collection))
#returns rank of specific team
def find_rank(collection,team,stat,desc):
    orderedList = order_stats_by(collection,stat,desc)
    return [y[0] for y in orderedList].index(team) + 1

#returns an ordered list of specific team-stat tuples
def order_stats_by(collection,stat,desc):
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
#imports data from csv files
def import_data(statistics):
    for file in os.listdir('.'):
        if file.endswith(".csv"):
            name =str(file)[:-4].replace("_"," ")
            statistics[name] = get_csv_data(file)

def main():


    statistics={}
    import_data(statistics)

    #Sample data access: statistics[#statistical set][#teamname][#statistic]
    #print statistics["NFL Pass Defense"]["Denver Broncos"]['YdsL']

    #print order_stats_by(statistics["NFL Pass Defense"], "TD",False)
    ne_rank =  find_rank(statistics["NFL Pass Offense"],"New England Patriots","Yds",True)
    ne_pct = percentile(statistics["NFL Pass Offense"], "New England Patriots","Yds", True)
    print "\nNew England Patriots Pass Yards rank: " + str(ne_rank)
    print "New England Patriots Pass Yards Percentile: " +str(ne_pct)+"\n"
    a = order_stats_by(statistics["NFL Pass Offense"], "Yds",True)
    count = 1
    print "NFL Passing Yards"
    print "====================="
    for team in a:
        print str(count)+'. '+team[0] +': '+ str(team[1])
        count+=1
    #print a[0]

    tamu_rank =  find_rank(statistics["NCAA Pass Offense"],"Texas A&M","TD",True)
    tamu_pct = percentile(statistics["NCAA Pass Offense"], "Texas A&M","TD", True)
    print "\nTAMU Pass TD rank: " + str(tamu_rank)
    print "TAMU Pass TD percentile: " + str(tamu_pct)+"\n"
    b = order_stats_by(statistics["NCAA Pass Offense"], "TD",True)
    count = 1
    print "NCAA Passing TDs"
    print "====================="
    for team in b:
        print str(count)+'. '+team[0] +': '+ str(team[1])
        count+=1

if __name__ == '__main__':
    main()