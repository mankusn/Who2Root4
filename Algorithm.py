import FootballLeague as fl
import operator
#import DataGather as dg



def main():


    nfl = fl.FootballLeague('.','NFL')
    ncaa = fl.FootballLeague('.', 'NCAA')
    list1 = nfl.get_team("New England Patriots").find_match(ncaa)
    list2 = ncaa.get_team("Texas A&M").find_match(nfl)

    print "Top 3 Recommendations for New England Patriots: "
    for num in range(0,3):
        print sorted(list1.items(), key=operator.itemgetter(1),reverse=True)[num]

    print "\nTop 3 Recommendations for Texas A&M: "
    for num in range(0,3):
        print sorted(list2.items(), key=operator.itemgetter(1),reverse=True)[num]

    print nfl.find_by_characteristic("Rush Defense")




if __name__ == '__main__':
    main()