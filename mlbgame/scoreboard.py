import urllib2 as url
import xml.etree.ElementTree as etree

def scoreboard(year, month, day):
    monthstr = str(month)
    daystr = str(day)
    if month < 10:
        monthstr = "0"+str(month)
    if day < 10:
        daystr = "0"+str(day)
    data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_"+str(year)+"/month_"+monthstr+"/day_"+daystr+"/scoreboard.xml")
    data = etree.parse(data)
    root = data.getroot()
    games = []
    for game in root:
        game_data = game.find('game')
        game_id = game_data.attrib['id']
        game_league = game_data.attrib['league']
        game_status = game_data.attrib['status']
        game_start_time = game_data.attrib['start_time']
        teams = game.findall('team')
        home_team_data = teams[0].find('gameteam')
        home_team = {'name': teams[0].attrib['name'], 'runs': home_team_data.attrib['R'], 'hits':home_team_data.attrib['H'], 'errors':home_team_data.attrib['E']}
        away_team_data = teams[1].find('gameteam')
        away_team = {'name': teams[1].attrib['name'], 'runs': away_team_data.attrib['R'], 'hits':away_team_data.attrib['H'], 'errors':away_team_data.attrib['E']}
        