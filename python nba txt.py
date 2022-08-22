f = open("demo.txt", "wt")
f.write("")

import json
file = open ('NBAGAME.json', "r" ,encoding="utf-8")
data = json.loads(file.read()) # data 是整個資料

# 比分
awayteam_name = data["payload"]["awayTeam"]["profile"]["name"]
awayteam_score = data["payload"]["boxscore"]["awayScore"]
hometeam_name = data["payload"]["homeTeam"]["profile"]["name"]
hometeam_score = data["payload"]["boxscore"]["homeScore"]
lead_changes = data["payload"]["boxscore"]["leadChanges"]

f.write(hometeam_name+"score"+str(hometeam_score)+"\n")
f.write(awayteam_name+"score"+str(awayteam_score)+"\n")
f.write("                    上場時間 得分 阻攻 抄截 籃板 助攻 失誤 罰球率 投籃命中率 三分球命中率\n")

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
   msg="{}      {}       {}       {}      {}      {}      {}      {}      {}    {}    {}\n"
   f.write(msg.format(player_name,player_mins,player_points,player_blocks,player_steals,player_rebs,player_assists,
                      player_turnovers,player_ftpct,player_fgpct,player_tppct,))
   #f.write(player_name+"上場時間"+str(player_mins)+"得分"+str(player_points)+"阻攻"+str(player_blocks)+
   #      "抄截"+str(player_steals)+"籃板"+str(player_rebs)+"助攻"+str(player_assists)+
   #      "失誤"+str(player_turnovers)+"罰球率"+str(player_ftpct)+"投籃命中率"+str(player_fgpct)+
   #      "三分球命中率"+str(player_tppct)+"\n")

away_players = data["payload"]["awayTeam"]["gamePlayers"]
away_players = data["payload"]["awayTeam"]["gamePlayers"]
f.write("                    上場時間   得分   阻攻   抄截   籃板   助攻   失誤   罰球率   投籃命中率   三分球命中率\n")


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

   msg="{}      {}       {}      {}      {}      {}      {}         {}         {}         {}         {}\n"
   f.write(msg.format(player_name,player_mins,player_points,player_blocks,player_steals,player_rebs,
                      player_assists,player_turnovers,player_ftpct,player_fgpct,player_tppct))

 #  f.write(player_name+"上場時間"+str(player_mins)+"得分"+str(player_points)+"阻攻"+str(player_blocks)+
 #        "抄截"+str(player_steals)+"籃板"+str(player_rebs)+"助攻"+str(player_assists)+
 #        "失誤"+str(player_turnovers)+"罰球率"+str(player_ftpct)+"投籃命中率"+str(player_fgpct)+
 #        "三分球命中率"+str(player_tppct)+"\n")
file.close()

f.close()
print("finish")
