import sqlite3
from sqlite3 import Error
import math

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_user(conn, userid):
    try:
        c = conn.cursor()
        sql_setup_users = "INSERT OR IGNORE INTO users(id, nickname, box) VALUES($id, $nickname, $box)"
        placeholders = {"id" : id, "nickname" : nickname, "box" : box}
        c.execute(sql_setup_waifugacha, placeholders)
        conn.commit()
    except Error as e:
        print(e)


#################################################################
#Main DB Setup
#################################################################
def setup_waifugacha(conn, id, name, rarity):
    try:
        c = conn.cursor()
        sql_setup_waifugacha = """INSERT OR IGNORE INTO waifugacha(id, name, rarity) VALUES($id, $name, $rarity)"""
        placeholders = {"id": id, "name": name, "rarity": rarity}
        c.execute(sql_setup_waifugacha, placeholders)
        conn.commit()
    except Error as e:
        print(e)

def load_waifudata(path):
    data = {}
    with open(path, mode='r') as file:
        for line in file:
            line_data = line.split(",")
            data[int(line_data[0])] = (line_data[1], int(line_data[2]))
    return data

sql_create_waifugacha_table = """CREATE TABLE IF NOT EXISTS waifugacha(id integer PRIMARY KEY, name text NOT NULL UNIQUE, rarity integer NOT NULL)"""
sql_create_users_table = """CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, name text NOT NULL UNIQUE, box integer NOT NULL)"""
def initialize(conn):
    # create_table(conn, sql_create_pikapoints_table)
    create_table(conn, sql_create_waifugacha_table)
    create_table(conn, sql_create_users_table)
    print("tables loaded")

    waifu = load_waifudata('waifubase.csv')
    for key in waifu:
        setup_waifugacha(conn, key, waifu[key][0], waifu[key][1])

    # teams = ['Team Electrocution', 'Team Lensflare', 'Team Hyperjoy']
    # initialize_teams(conn, teams)
    #
    # ranks = [('Recruit', 0), ('Crook', 250), ('Grunt', 500), ('Thug', 750), ('Associate', 1000), ('Hitman', 1250),
    #          ('Officer', 1500), ('Sergeant', 1750), ('Captain', 2000), ('Lieutenant', 2250), ('Admin', 2500),
    #          ('Commander', 2750), ('Boss', 3500)]
    # initialize_ranks(conn, ranks)
#################################################################
#################################################################
