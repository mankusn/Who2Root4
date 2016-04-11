import FootballLeague as fl
import operator
#import DataGather as dg



def main():


    nfl = fl.FootballLeague('.','NFL')
    ncaa = fl.FootballLeague('.', 'NCAA')

    list = {}
    list = nfl.get_team("New England Patriots").find_match(ncaa)
    print "Top 3 Recommendations for New England Patriots: "
    for num in range(0,3):
        print sorted(list.items(), key=operator.itemgetter(1),reverse=True)[num]






if __name__ == '__main__':
    main()