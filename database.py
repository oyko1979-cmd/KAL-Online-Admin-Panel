import pyodbc
import configparser
from player import Player
from item import Item


# ----- Cinfigparser setup/loading config from config.ini ----- #
config = configparser.ConfigParser()
config.read("config.ini")

# ----- Connection String ----- #
uid = config['Database']['UID']
pwd = config['Database']['PWD']

# ----- SQL AUTH Connection ----- #
sql_connection_string = (
    f"DRIVER={config['Database']['Driver']};"
    f"SERVER={config['Database']['Server']};"
    f"DATABASE={config['Database']['Database']};"
    f"UID={uid};"
    f"PWD={pwd};"
    f"TrustServerCertificate={config['Database']['TrustServerCertificate']};"
)

# ----- Windows AUTH Connection ----- #
windows_connection_string = (
    f"DRIVER={config['Database']['Driver']};"
    f"SERVER={config['Database']['Server']};"
    f"DATABASE={config['Database']['Database']};"
    f"TrustServerCertificate={config['Database']['TrustServerCertificate']};"
    f"Trusted_Connection={config['Database']['TrustedConnection']};"
)

# ----- Check either Windows or SQL Connection ----- #
def get_connection():
    if not uid and not pwd:
        return windows_connection()
    else:
        return sql_connection()

def sql_connection():
    return pyodbc.connect(sql_connection_string)

def windows_connection():
    return pyodbc.connect(windows_connection_string)


# ----- Functions SQL Query ----- #
def get_player_pid(charname):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT PID
    FROM kal_db.dbo.Player
    WHERE Name = ?
    """, charname)

    result = cursor.fetchone()
    if not result:
        return

    return result[0]



def search_player(charname):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT UID, PID, Admin, Name, Class, Specialty, Level, Contribute, Exp, GID, GRole,
    Strength, Health, Intelligence, Wisdom, Dexterity, CurHP, CurMP, PUPoint, SUPoint, Killed, Map, X, Y, Z
    FROM kal_db.dbo.Player
    WHERE Name = ?
    """, charname)

    result = cursor.fetchone()
    if result is None:
        return None

    return Player(*result)

def search_item(pid):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT IID, [Index], Prefix, Info, Num
    FROM kal_db.dbo.Item
    WHERE PID = ?
    """, pid)

    result = cursor.fetchall()
    if not result:
        raise Exception("Keine Items gefunden")
    
    items = []

    for value in result:
        item = Item(
            pid, 
            value[0],
            value[1],
            value[2],
            value[3],
            value[4]
        )
        items.append(item)

    return items



# ----- Player Fields ----- #

PLAYER_FIELDS = {
    "UID": "UID",
    "PID": "PID",
    "Admin": "Admin",
    "Name": "Name",
    "Class": "Class",
    "Specialty": "Specialty",
    "Level": "Level",
    "Contribute": "Contribute",
    "Exp": "Exp",
    "GID": "GID",
    "GRole": "GRole",
    "Strength": "Strength",
    "Health": "Health",
    "Intelligence": "Intelligence",
    "Wisdom": "Wisdom",
    "Dexterity": "Dexterity",
    "CurHP": "CurHP",
    "CurMP": "CurMP",
    "PUPoint": "PUPoint",
    "SUPoint": "SUPoint",
    "Killed": "Killed",
    "Map": "Map",
    "X": "X",
    "Y": "Y",
    "Z": "Z"
}


def update_player_field(field, value, pid):

    column = PLAYER_FIELDS[field]

    connection = get_connection()
    cursor = connection.cursor()

    query = f"""
    UPDATE kal_db.dbo.Player
    SET {column} = ?
    WHERE PID = ?
    """

    cursor.execute(query, value, pid)
    connection.commit()


def update_item_field(iid, field, value):
    ITEM_FIELDS = {
        "Prefix": "Prefix",
        "Info": "Info",
        "Num": "Num"
    }
    column = ITEM_FIELDS[field]

    connection = get_connection()
    cursor = connection.cursor()

    query = f"""
    UPDATE kal_db.dbo.Item
    SET {column} = ?
    WHERE IID = ?
    """

    cursor.execute(query, value, iid)
    connection.commit()


def send_item_to_player(pid, iid):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE kal_db.dbo.Item
    SET PID = ?
    WHERE IID = ?
    """, pid, iid
    )

    connection.commit()


def delete_item(iid, pid):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM kal_db.dbo.Item
    WHERE IID = ?
    AND PID = ?
    """, iid, pid)

    connection.commit()
    return True

