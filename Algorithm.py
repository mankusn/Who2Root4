from flask import Flask , redirect, url_for
from flask import request
from flask import render_template
import unicodedata
import FootballLeague as fl
import operator
#import DataGather as dg

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('layout.html',titles = None)

@app.route('/results', methods =['POST'])
def algorithm(titles = {}):
    titles = {}
    results1,results2 = [],[]
    nfl = fl.FootballLeague('.','NFL')
    ncaa = fl.FootballLeague('.', 'NCAA')
    team=''
    league =''
    team = str(request.form['Team'])

    print type(request.form['league'])
    league = str(request.form['league'])
    print league
    if team in nfl.leagueTeams:
        searchLeague = nfl
    elif team in ncaa.leagueTeams:
        searchLeague = ncaa
    else:
        return render_template('layout.html')

    if league =='NCAA':
        otherLeague = ncaa
    elif league =='NFL':
        otherLeague = nfl
    list1 = searchLeague.get_team(team).find_match(otherLeague)


    # results.append( "Top 3 Recommendations for New England Patriots: \n")
    for num in range(0,3):
        results1.append( str(num+1)+": "+ str(list1[num][0])+" - "+str(list1[num][1])+'\n')
    titles["Top 3 Recommendations for "+team+" in "+league+": "] = results1


    # results.append( "\nTop 5 NCAA Rush Defenses: ")
    # for num in range(0,5):
    #     results.append( str(num+1)+": "+ str(ncaa.characteristic_ranking("Rush Defense",False,False,False)[num][0])+'\n')
    #
    # results.append( "\nTop 5 NCAA Pass Defenses: ")
    # for num in range(0,5):
    #     results.append( str(num+1)+": "+str(ncaa.characteristic_ranking("Pass Defense",False,False,False)[num][0])+'\n')
    #
    # results.append( "\nTop 5 Most Exciting NFL Rush Offenses: ")
    # for num in range(0,5):
    #     results.append( str(num+1)+": "+ str(nfl.characteristic_ranking("Rush Offense",False,False,True)[num][0])+'\n')
    #
    # results.append( "\nTop 5 Most Exciting NFL Pass Offense: ")
    # for num in range(0,5):
    #     results.append( str(num+1)+": "+str(nfl.characteristic_ranking("Pass Offense",False,False,True)[num][0])+'\n')

    return render_template('layout.html', titles = titles)




if __name__ == '__main__':
    app.run(debug=True)