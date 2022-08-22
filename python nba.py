import json
file = open ('NBAGAME.json', "r" ,encoding="utf-8")
data = json.loads(file.read()) # data 是整個資料
print(data)

# 比分
awayteam_name = data["payload"]["awayTeam"]["profile"]["name"]
awayteam_score = data["payload"]["boxscore"]["awayScore"]
hometeam_name = data["payload"]["homeTeam"]["profile"]["name"]
hometeam_score = data["payload"]["boxscore"]["homeScore"]
lead_changes = data["payload"]["boxscore"]["leadChanges"]

print(hometeam_name,"score",hometeam_score)
print(awayteam_name,"score",awayteam_score)

# 球員數據
home_players = data["payload"]["homeTeam"]["gamePlayers"]
away_players = data["payload"]["homeTeam"]["gamePlayers"]

for player in home_players:
   player_name=player["profile"]["displayNameEn"]

   player_mins=player["statTotal"]["mins"]

   player_points=player["statTotal"]["points"]

   player_blocks=player["statTotal"]["blocks"]
   
   player_steals=player["statTotal"]["steals"]

   player_rebs=player["statTotal"]["rebs"]

   player_assists=player["statTotal"]["assists"]

   player_turnovers=player["statTotal"]["turnovers"]

   player_ftpct=player["statTotal"]["ftpct"]

   player_fgpct=player["statTotal"]["fgpct"]

   player_tppct=player["statTotal"]["tppct"]
   print(player_name,"上場時間",player_mins,"得分",player_points,"阻攻",player_blocks,
         "抄截",player_steals,"籃板",player_rebs,"助攻",player_assists,
         "失誤",player_turnovers,"罰球率",player_ftpct,"投籃命中率",player_fgpct,
         "三分球命中率",player_tppct)

away_players = data["payload"]["awayTeam"]["gamePlayers"]
away_players = data["payload"]["awayTeam"]["gamePlayers"]

for player in away_players:
   player_name=player["profile"]["displayNameEn"]
   
   player_mins=player["statTotal"]["mins"]
   
   player_points=player["statTotal"]["points"]

   player_blocks=player["statTotal"]["blocks"]

   player_steals=player["statTotal"]["steals"]

   player_rebs=player["statTotal"]["rebs"]

   player_assists=player["statTotal"]["assists"]

   player_turnovers=player["statTotal"]["turnovers"]

   player_ftpct=player["statTotal"]["ftpct"]

   player_fgpct=player["statTotal"]["fgpct"]

   player_tppct=player["statTotal"]["tppct"]
   print(player_name,"上場時間",player_mins,"得分",player_points,"阻攻",player_blocks,
         "抄截",player_steals,"籃板",player_rebs,"助攻",player_assists,
         "失誤",player_turnovers,"罰球率",player_ftpct,"投籃命中率",player_fgpct,
         "三分球命中率",player_tppct)
file.close()
