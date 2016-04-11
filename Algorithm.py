from flask import Flask
from flask import render_template
import FootballLeague as fl
import operator
#import DataGather as dg

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'
@app.route('/results')
def algorithm(results = []):
    results = []

    nfl = fl.FootballLeague('.','NFL')
    ncaa = fl.FootballLeague('.', 'NCAA')
    list1 = nfl.get_team("New England Patriots").find_match(ncaa)
    list2 = ncaa.get_team("Texas A&M").find_match(nfl)

    results.append( "Top 3 Recommendations for New England Patriots: \n")
    for num in range(0,3):
        results.append( str(num+1)+": "+ str(list1[num][0])+" - "+str(list1[num][1])+'\n')

    results.append( "\nTop 3 Recommendations for Texas A&M: ")
    for num in range(0,3):
        results.append( str(num+1)+": "+ str(list2[num][0])+" - "+str(list2[num][1])+'\n')


    results.append( "\nTop 5 NCAA Rush Defenses: ")
    for num in range(0,5):
        results.append( str(num+1)+": "+ str(ncaa.characteristic_ranking("Rush Defense",False,False,False)[num][0])+'\n')

    results.append( "\nTop 5 NCAA Pass Defenses: ")
    for num in range(0,5):
        results.append( str(num+1)+": "+str(ncaa.characteristic_ranking("Pass Defense",False,False,False)[num][0])+'\n')

    results.append( "\nTop 5 Most Exciting NFL Rush Offenses: ")
    for num in range(0,5):
        results.append( str(num+1)+": "+ str(nfl.characteristic_ranking("Rush Offense",False,False,True)[num][0])+'\n')

    results.append( "\nTop 5 Most Exciting NFL Pass Offense: ")
    for num in range(0,5):
        results.append( str(num+1)+": "+str(nfl.characteristic_ranking("Pass Offense",False,False,True)[num][0])+'\n')

    return render_template('home.html', results = results)




if __name__ == '__main__':
    app.run(debug=True)