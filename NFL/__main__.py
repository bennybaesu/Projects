import mysql.connector
import pandas as pd
import Team

teams = []

# CONNECT TO MYSQL DATABASE
nfl = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MySQL_1234',
    database='NFL')

# NFL DATABASE CURSOR
c = nfl.cursor()

# Get Team Database
teamDF = pd.DataFrame([])
c.execute("SELECT * FROM TEAM")
result = c.fetchall()
for x in result:
    df = pd.DataFrame([x])
    teamDF = teamDF.append(df)

# Rename column labels
teamDF = teamDF.rename(columns={0: "CITY", 1: "NAME",
                                        2: "CONFERENCE", 3: "DIVISION",
                                    4: "STADIUM", 5: "STADIUM LOCATION", 6: "W",
                                    7: "L", 8: "T", 9: "DIV W", 10: "DIV L",
                                    11: "DIV T", 12: "PS", 13: "PA"})



