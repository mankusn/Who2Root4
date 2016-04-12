from flask import Flask , redirect, url_for,flash
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

    league = str(request.form['league'])

    if league == None:
        flash('Please Select League')
        return render_template('layout.html')
    if team in nfl.leagueTeams:
        searchLeague = nfl
    elif team in ncaa.leagueTeams:
        searchLeague = ncaa
    else:
        flash('Oops! We don\'t know that team. Please enter another.')
        return render_template('layout.html')

    if league =='NCAA':
        otherLeague = ncaa
    elif league =='NFL':
        otherLeague = nfl
    list1 = searchLeague.get_team(team).find_match(otherLeague)


    # results.append( "Top 3 Recommendations for New England Patriots: \n")
    for num in range(0,3):
        line = str(num+1)+'. '+str(list1[num][0])+' - '+str(list1[num][1])
        results1.append( line)

    title = "Top 3 Recommendations for "+team+" in "+league+": "

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

    return render_template('layout.html', results = results1, title = title)




if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    app.run(debug=True)