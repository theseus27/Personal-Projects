from db import connect
import pandas as pd
DATAFILE = "../data/team_data.csv"

# TeamData: TeamName, City, Abbrev
def send_team(df, db, idx):
    query = "INSERT INTO teams VALUES ("+ str(idx+1) + ", \'" + str(df.loc[idx][0]) + "\', \'" + str(df.loc[idx][1]) + "\', \'" + str(df.loc[idx][2]) + "\');"

    cursor = db.cursor()
    try:
        cursor.execute(query)
        db.commit()
        print("Added " + df.loc[idx][0] + " to Teams")
    except:
        print("Failed to add " + df.loc[idx][0] + " to Teams")
    finally:
        cursor.close()


def fill_in_teams():
    db = connect()

    df = pd.read_csv(DATAFILE)

    if len(df) != 30:
        print(len(df))
        return

    for i in range(len(df)):
        send_team(df, db, i)

fill_in_teams()