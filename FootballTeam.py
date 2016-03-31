import DataGather as dg
import copy

class StatKeeper:
    def __init__(self,n):
        self.name = n
        self.list = {}

    def show(self):
        print self.get

class FootballTeam:



    def __init__(self,name,league,statistics):
        self.name = name
        self.league = league
        self.statistics = statistics
        self.rankings ={}
        self.percentiles = {}
        self.get_rankings()

    def get_rank(self,statList,stat):
        return self.rankings[statList].list[stat]

    def get_stat(self,statList,stat):
        statList = self.league +' '+ statList
        return self.statistics[statList][self.name][stat]

    def get_pct(self,statList,stat):
        return self.percentiles[statList].list[stat]

    def check_stats(self,statistics):
        for statList in statistics.keys():
            for team in statistics[statList]:
                #print team
                if type(statistics[statList][team]) is int:
                    print 'FOUND'

    def get_rankings(self):

        for statList in self.statistics.keys():

            # print statList
            if statList.startswith(self.league):
                name = statList.replace(self.league,'').strip()
                # print "Name:"+name
                statRank = StatKeeper(name)
                statPct = StatKeeper(name)
                for stat in self.statistics[statList][self.name]:
                    # print stat
                    rank = dg.find_rank(self.statistics[statList],self.name,stat,True)
                    pct = dg.percentile(self.statistics[statList],self.name,stat,True)
                    # print rank
                    statRank.list[stat]=rank
                    statPct.list[stat] = pct
                self.rankings[name]=statRank
                self.percentiles[name] = statPct


        #print self.rankings['Pass Offense'].show()
