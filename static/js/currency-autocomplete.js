$(function(){
  var currencies = [
    { value: 'Washington St.', data: 'NCAA' },
    { value: 'Texas Tech', data: 'NCAA' },
    { value: 'Bowling Green', data: 'NCAA' },
    { value: 'Cincinnati', data: 'NCAA' },
    { value: 'California', data: 'NCAA' },
    { value: 'W. Kentucky', data: 'NCAA' },
    { value: 'Oklahoma St.', data: 'NCAA' },
    { value: 'Georgia St.', data: 'NCAA' },
    { value: 'TCU', data: 'NCAA' },
    { value: 'Mississippi', data: 'NCAA' },
    { value: 'Tulsa', data: 'NCAA' },
    { value: 'Southern Miss', data: 'NCAA' },
    { value: 'Memphis', data: 'NCAA' },
    { value: 'Cent. Michigan', data: 'NCAA' },
    { value: 'Louisiana Tech', data: 'NCAA' },
    { value: 'Mississippi St.', data: 'NCAA' },
    { value: 'Middle Tenn.', data: 'NCAA' },
    { value: 'Oklahoma', data: 'NCAA' },
    { value: 'Boise St.', data: 'NCAA' },
    { value: 'Baylor', data: 'NCAA' },
    { value: 'BYU', data: 'NCAA' },
    { value: 'Arizona St.', data: 'NCAA' },
    { value: 'Clemson', data: 'NCAA' },
    { value: 'UCLA', data: 'NCAA' },
    { value: 'Indiana', data: 'NCAA' },
    { value: 'W. Michigan', data: 'NCAA' },
    { value: 'Miami', data: 'NCAA' },
    { value: 'Idaho', data: 'NCAA' },
    { value: 'East Carolina', data: 'NCAA' },
    { value: 'Nebraska', data: 'NCAA' },
    { value: 'USC', data: 'NCAA' },
    { value: 'Arizona', data: 'NCAA' },
    { value: 'Arkansas', data: 'NCAA' },
    { value: 'N. Carolina', data: 'NCAA' },
    { value: 'Oregon', data: 'NCAA' },
    { value: 'UMass', data: 'NCAA' },
    { value: 'Notre Dame', data: 'NCAA' },
    { value: 'Duke', data: 'NCAA' },
    { value: 'N. Mex. St.', data: 'NCAA' },
    { value: 'Texas A&M', data: 'NCAA' },
    { value: 'Toledo', data: 'NCAA' },
    { value: 'Buffalo', data: 'NCAA' },
    { value: 'Houston', data: 'NCAA' },
    { value: 'Louisville', data: 'NCAA' },
    { value: 'Florida St.', data: 'NCAA' },
    { value: 'Illinois', data: 'NCAA' },
    { value: 'Troy', data: 'NCAA' },
    { value: 'Colorado', data: 'NCAA' },
    { value: 'Ohio', data: 'NCAA' },
    { value: 'Virginia', data: 'NCAA' },
    { value: 'Florida Intl.', data: 'NCAA' },
    { value: 'Purdue', data: 'NCAA' },
    { value: 'Michigan St.', data: 'NCAA' },
    { value: 'Washington', data: 'NCAA' },
    { value: 'Michigan', data: 'NCAA' },
    { value: 'San Jose St.', data: 'NCAA' },
    { value: 'Marshall', data: 'NCAA' },
    { value: 'Wisconsin', data: 'NCAA' },
    { value: 'Wake Forest', data: 'NCAA' },
    { value: 'West Virginia', data: 'NCAA' },
    { value: 'Texas St.', data: 'NCAA' },
    { value: 'Iowa St.', data: 'NCAA' },
    { value: 'Rice', data: 'NCAA' },
    { value: 'East. Michigan', data: 'NCAA' },
    { value: 'Northern Illinois', data: 'NCAA' },
    { value: 'Colorado St.', data: 'NCAA' },
    { value: 'Old Dominion', data: 'NCAA' },
    { value: 'Kansas', data: 'NCAA' },
    { value: 'SMU', data: 'NCAA' },
    { value: 'Ball St.', data: 'NCAA' },
    { value: 'Virginia Tech', data: 'NCAA' },
    { value: 'Temple', data: 'NCAA' },
    { value: 'Alabama', data: 'NCAA' },
    { value: 'Minnesota', data: 'NCAA' },
    { value: 'Florida Atlantic', data: 'NCAA' },
    { value: 'Arkansas St.', data: 'NCAA' },
    { value: 'UNLV', data: 'NCAA' },
    { value: 'Florida', data: 'NCAA' },
    { value: 'Stanford', data: 'NCAA' },
    { value: 'N.C. State', data: 'NCAA' },
    { value: 'Kentucky', data: 'NCAA' },
    { value: 'Penn St.', data: 'NCAA' },
    { value: 'Miami (OH)', data: 'NCAA' },
    { value: 'La Lafayet.', data: 'NCAA' },
    { value: 'LA Monroe', data: 'NCAA' },
    { value: 'South Carolina', data: 'NCAA' },
    { value: 'Rutgers', data: 'NCAA' },
    { value: 'Utah St.', data: 'NCAA' },
    { value: 'Appalachian St.', data: 'NCAA' },
    { value: 'Iowa', data: 'NCAA' },
    { value: 'Tulane', data: 'NCAA' },
    { value: 'South Alabama', data: 'NCAA' },
    { value: 'Tennessee', data: 'NCAA' },
    { value: 'UTEP', data: 'NCAA' },
    { value: 'Pittsburgh', data: 'NCAA' },
    { value: 'Connecticut', data: 'NCAA' },
    { value: 'Akron', data: 'NCAA' },
    { value: 'UTSA', data: 'NCAA' },
    { value: 'Hawaii', data: 'NCAA' },
    { value: 'Utah', data: 'NCAA' },
    { value: 'Wyoming', data: 'NCAA' },
    { value: 'UCF', data: 'NCAA' },
    { value: 'Georgia', data: 'NCAA' },
    { value: 'Ohio St.', data: 'NCAA' },
    { value: 'South Florida', data: 'NCAA' },
    { value: 'Fresno St.', data: 'NCAA' },
    { value: 'Kansas St.', data: 'NCAA' },
    { value: 'Auburn', data: 'NCAA' },
    { value: 'Maryland', data: 'NCAA' },
    { value: 'Charlotte', data: 'NCAA' },
    { value: 'LSU', data: 'NCAA' },
    { value: 'Nevada', data: 'NCAA' },
    { value: 'Vanderbilt', data: 'NCAA' },
    { value: 'Missouri', data: 'NCAA' },
    { value: 'North Texas', data: 'NCAA' },
    { value: 'Oregon St.', data: 'NCAA' },
    { value: 'Syracuse', data: 'NCAA' },
    { value: 'Texas', data: 'NCAA' },
    { value: 'S. Diego St.', data: 'NCAA' },
    { value: 'Northwestern', data: 'NCAA' },
    { value: 'Kent St.', data: 'NCAA' },
    { value: 'New Mexico', data: 'NCAA' },
    { value: 'Air Force', data: 'NCAA' },
    { value: 'Georgia Tech', data: 'NCAA' },
    { value: 'Boston Coll.', data: 'NCAA' },
    { value: 'Army', data: 'NCAA' },
    { value: 'Navy', data: 'NCAA' },
    { value: 'Georgia Southern', data: 'NCAA' },
    { value: 'New Orleans Saints', data: 'NFL' },
    { value: 'Arizona Cardinals', data: 'NFL' },
    { value: 'Pittsburgh Steelers', data: 'NFL' },
    { value: 'San Diego Chargers', data: 'NFL' },
    { value: 'New England Patriots', data: 'NFL' },
    { value: 'Atlanta Falcons', data: 'NFL' },
    { value: 'New York Giants', data: 'NFL' },
    { value: 'Baltimore Ravens', data: 'NFL' },
    { value: 'Detroit Lions', data: 'NFL' },
    { value: 'Jacksonville Jaguars', data: 'NFL' },
    { value: 'Washington Redskins', data: 'NFL' },
    { value: 'Philadelphia Eagles', data: 'NFL' },
    { value: 'New York Jets', data: 'NFL' },
    { value: 'Denver Broncos', data: 'NFL' },
    { value: 'Cincinnati Bengals', data: 'NFL' },
    { value: 'Oakland Raiders', data: 'NFL' },
    { value: 'Tampa Bay Buccaneers', data: 'NFL' },
    { value: 'Houston Texans', data: 'NFL' },
    { value: 'Miami Dolphins', data: 'NFL' },
    { value: 'Seattle Seahawks', data: 'NFL' },
    { value: 'Cleveland Browns', data: 'NFL' },
    { value: 'Indianapolis Colts', data: 'NFL' },
    { value: 'Chicago Bears', data: 'NFL' },
    { value: 'Carolina Panthers', data: 'NFL' },
    { value: 'Green Bay Packers', data: 'NFL' },
    { value: 'Tennessee Titans', data: 'NFL' },
    { value: 'Dallas Cowboys', data: 'NFL' },
    { value: 'Buffalo Bills', data: 'NFL' },
    { value: 'San Francisco 49ers', data: 'NFL' },
    { value: 'Kansas City Chiefs', data: 'NFL' },
    { value: 'Minnesota Vikings', data: 'NFL' },
    { value: 'St. Louis Rams', data: 'NFL' },

  ];
  
  // setup autocomplete function pulling from currencies[] array
  $('#autocomplete').autocomplete({
    lookup: currencies,
    onSelect: function (suggestion) {
      var thehtml = '<strong>Currency Name:</strong> ' + suggestion.value + ' <br> <strong>Symbol:</strong> ' + suggestion.data;
      $('#outputcontent').html(thehtml);
    }
  });
  

});

$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "NCAA_Pass_Defense.csv",
        dataType: "text",
        success: function(data) {processData(data);}
     });
});

function processData(allText) {
    var allTextLines = allText.split(/\r\n|\n/);
    var headers = allTextLines[0].split(',');
    var lines = [];

    for (var i=1; i<allTextLines.length; i++) {
        var data = allTextLines[i].split(',');
        if (data.length == headers.length) {

            var tarr = [];
            for (var j=0; j<headers.length; j++) {
                tarr.push(headers[j]+":"+data[j]);
            }
            lines.push(tarr);
        }
    }
    // alert(lines);
}