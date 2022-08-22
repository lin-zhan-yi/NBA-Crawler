writeList=[]
csvList=[]

import requests
import json

def getData(game_id):
   link='https://tw.global.nba.com/stats2/game/snapshot.json?countryCode=TW&gameId='+game_id+'&locale=zh_TW&tz=%2B8'
   r = requests.get(link)
   data={}
   if r.status_code == requests.codes.ok:
      data=json.loads(r.text)
   else:
      file = open ('NBAGAME.json', "r" ,encoding="utf-8")
      data = json.loads(file.read()) # data 是整個資料
      file.close()
   return data

def parseData(input_data):
   data = input_data
   # 比分
   awayteam={
      "name":data["payload"]["awayTeam"]["profile"]["name"],
      "score":data["payload"]["boxscore"]["awayScore"]
      }
   hometeam={
      "name":data["payload"]["homeTeam"]["profile"]["name"],
      "score":data["payload"]["boxscore"]["homeScore"]
      }

   lead_changes = data["payload"]["boxscore"]["leadChanges"]

   writeList.append(hometeam["name"]+str(hometeam["score"])+"\n")
   tmp=[hometeam["name"],hometeam["score"]]
   #csvList.append(tmp)
   writeList.append(awayteam["name"]+str(awayteam["score"])+"\n")
   tmp=[awayteam["name"],awayteam["score"]]
   #csvList.append(tmp)
   writeList.append("                    上場時間 得分 阻攻 抄截 籃板 助攻 失誤 罰球率 投籃命中率 三分球命中率\n")
   tmp=["球員姓名","上場時間","得分","阻攻","抄截","籃板","助攻","失誤","罰球率","投籃命中率","三分球命中率"]
   csvList.append(tmp)
   # 球員數據
   home_players = data["payload"]["homeTeam"]["gamePlayers"]
   away_players = data["payload"]["awayTeam"]["gamePlayers"]

   for player in home_players:
      player_data = {
            "name":player["profile"]["displayNameEn"],
            "mins":player["statTotal"]["mins"],
            "points":player["statTotal"]["points"],
            "blocks":player["statTotal"]["blocks"],
            "steals":player["statTotal"]["steals"],
            "rebs":player["statTotal"]["rebs"],
            "assists":player["statTotal"]["assists"],
            "turnovers":player["statTotal"]["turnovers"],
            "ftpct":player["statTotal"]["ftpct"],
            "fgpct":player["statTotal"]["fgpct"],
            "tppct":player["statTotal"]["tppct"],
         }   
      msg="{}      {}       {}       {}      {}      {}      {}      {}      {}    {}    {}\n"
      writeList.append(msg.format(player_data['name'],player_data['mins'],player_data['points'],player_data['blocks'],player_data['steals'],
                         player_data['rebs'],player_data['assists'],player_data['turnovers'],player_data['ftpct'],player_data['fgpct'],player_data['tppct'],))
      tmp=[player_data['name'],player_data['mins'],player_data['points'],player_data['blocks'],player_data['steals'],
                         player_data['rebs'],player_data['assists'],player_data['turnovers'],player_data['ftpct'],player_data['fgpct'],player_data['tppct']]
      csvList.append(tmp)
   writeList.append("                    上場時間 得分 阻攻 抄截 籃板 助攻 失誤 罰球率 投籃命中率 三分球命中率\n")
   tmp=["","上場時間","得分","阻攻","抄截","籃板","助攻","失誤","罰球率","投籃命中率","三分球命中率"]
   #csvList.append(tmp)
   for player in away_players:
      player_data = {
            "name":player["profile"]["displayNameEn"],
            "mins":player["statTotal"]["mins"],
            "points":player["statTotal"]["points"],
            "blocks":player["statTotal"]["blocks"],
            "steals":player["statTotal"]["steals"],
            "rebs":player["statTotal"]["rebs"],
            "assists":player["statTotal"]["assists"],
            "turnovers":player["statTotal"]["turnovers"],
            "ftpct":player["statTotal"]["ftpct"],
            "fgpct":player["statTotal"]["fgpct"],
            "tppct":player["statTotal"]["tppct"],
         }   
      msg="{}      {}       {}       {}      {}      {}      {}      {}      {}    {}    {}\n"
      writeList.append(msg.format(player_data['name'],player_data['mins'],player_data['points'],player_data['blocks'],player_data['steals'],
                         player_data['rebs'],player_data['assists'],player_data['turnovers'],player_data['ftpct'],player_data['fgpct'],player_data['tppct'],))

      tmp=[player_data['name'],player_data['mins'],player_data['points'],player_data['blocks'],player_data['steals'],
                         player_data['rebs'],player_data['assists'],player_data['turnovers'],player_data['ftpct'],player_data['fgpct'],player_data['tppct']]
      csvList.append(tmp)
def txtWriter():
   f = open("demo.txt", "wt")
   f.write("")
   f.writelines(writeList)
   f.close()
   print("finish")

import csv

def csvWriter(name):
    with open(name+'.csv', 'w', newline='', encoding='UTF-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        for row in csvList:
         writer.writerow(row)
game_id="0032100001"
nba_data=getData(game_id)
parseData(nba_data)
txtWriter()
csvWriter(game_id)
