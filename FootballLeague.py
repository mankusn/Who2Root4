import operator
import numpy as np
import DataGather as dg


#A collection of teams and their stats in a league
class FootballLeague:

    def __init__(self, directory,league):
        self.directory = directory
        self.league = league
        self.statistics = {}
        dg.import_data(self.statistics,directory)
        self.gather_teams()

    def is_in_league(self, team):
        return team in self.leagueTeams

    def gather_teams(self):
        self.leagueTeams = {}
        for name in self.statistics[self.league +" Pass Offense"].keys():
            team = FootballTeam(name, self.league,self.statistics)
            self.leagueTeams[name] = team

    def get_team(self,team):
        return self.leagueTeams[team]

#class to store stats from a Stat List i.e Pass Offense
class StatKeeper:
    def __init__(self,n,t):
        self.name = n
        self.type = t
        self.list = {}

    def values(self):
        return self.list
    def show(self):
        print self.name+" "+self.type
        print "==============="
        for stat in self.list.keys():
            print stat+": "+ str(self.list[stat])


class FootballTeam:

    wanted = ['Yds','Yds!','Cmp%','Cmp%!','Att/G','Att/G!','TD','TD!','Int','Int!',
              'Att','Att!','Y/G','Y/G!','Rush/G','A/G!','Y/A!']
    def __init__(self,name,league,statistics):
        self.name = name
        self.league = league
        self.statistics = statistics
        self.rankings ={}
        self.percentiles = {}
        self.get_rankings()
        self.get_stat_list()


    def print_rankings(self,statList):
        self.rankings[statList].show()

    def print_percentiles(self,statList):
        self.percentiles[statList].show()

    def print_stats(self,statList):
        print "All "+statList+" Statistics"
        print "============================"
        listName = self.league+" "+statList
        for stat in self.statistics[listName][self.name].keys():
            print stat+": "+self.statistics[listName][self.name][stat]

    #Return Rank of specific stat
    def get_rank(self,statList,stat):
        return self.rankings[statList].list[stat]
    #Return Stat value of specific stat
    def get_stat(self,statList,stat):
        statList = self.league +' '+ statList
        return self.statistics[statList][self.name][stat]

    #Return Percentile of specific stat
    def get_pct(self,statList,stat):
        return self.percentiles[statList].list[stat]

    #finds football team rank and percentiles
    def get_rankings(self):
        #For every League stat category
        for statList in self.statistics.keys():
            if statList.startswith(self.league):
                name = statList.replace(self.league,'').strip()
                statRank = StatKeeper(name,"Ranks")
                statPct = StatKeeper(name,"Percentile")
                #For every statistc for team
                for stat in self.statistics[statList][self.name]:
                    if stat not in self.wanted:
                        continue
                    flag = True
                    if(stat.endswith('!')):
                        flag = False
                    rank = dg.find_rank(self.statistics[statList],self.name,stat,flag)
                    pct = dg.percentile(self.statistics[statList],self.name,stat,flag)
                    statRank.list[stat]=rank
                    statPct.list[stat] = pct
                self.rankings[name]=statRank
                self.percentiles[name] = statPct

    def get_stat_list(self):
        self.statList = []
        for statList in sorted(self.percentiles.keys()):
            for stat in sorted(self.percentiles[statList].list.keys()):
                self.statList.append(self.percentiles[statList].list[stat])

    def cosine(self,otherStatList):
        dotProduct = np.dot(otherStatList,self.statList)
        magnitude = np.linalg.norm(otherStatList) * np.linalg.norm(self.statList)
        return dotProduct/magnitude

    def find_match(self, otherLeague):
        teamCos = {}
        for teamName in otherLeague.leagueTeams.keys():
            cos = self.cosine(otherLeague.leagueTeams[teamName].statList)
            teamCos[teamName] = cos
        return teamCos