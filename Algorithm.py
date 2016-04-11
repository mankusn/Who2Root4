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
        print str(num+1)+": "+ str(list1[num][0])+" - "+str(list1[num][1])

    print "\nTop 3 Recommendations for Texas A&M: "
    for num in range(0,3):
        print str(num+1)+": "+ str(list2[num][0])+" - "+str(list2[num][1])


    print "\nTop 5 Rush Defenses: "
    for num in range(0,5):
        print str(num+1)+": "+ str(ncaa.characteristic_ranking("Rush Defense",False,False,False)[num][0])

    print "\nTop 5 Pass Defenses: "
    for num in range(0,5):
        print str(num+1)+": "+str(ncaa.characteristic_ranking("Pass Defense",False,False,False)[num][0])

    print "\nTop 5 Rush Offense: "
    for num in range(0,5):
        print str(num+1)+": "+ str(ncaa.characteristic_ranking("Rush Offense",False,False,False)[num][0])

    print "\nTop 5 Pass Offense: "
    for num in range(0,5):
        print str(num+1)+": "+str(ncaa.characteristic_ranking("Pass Offense",False,False,True)[num][0])






if __name__ == '__main__':
    main()