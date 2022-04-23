import micropip
import sqlite3
import os

deps = [
    "https://storage.googleapis.com/db-owser/parsedatetime-2.7-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/minimal-snowplow-tracker-0.0.2-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/dbt_core-1.2.0a1.1-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/dbt_sqlite-1.0.0-py3-none-any.whl",
]
for d in deps:
    await micropip.install(d, True)

import dbt.main

def tdb(cmd: str = None):
    if cmd is None:
        return dbt.main.main([])
    else:
        return dbt.main.main(cmd.split(" "))

def cat(filename: str) -> None:
    f = open(filename)
    for line in f:
        print(line)

def ls(root_dir: str) -> None:
    for root, _, files in os.walk(root_dir):
        for filename in files:
            print(f"{root}/{filename}")

class DB(object):
    def __init__(self, filename: str) -> None:
        self._con = sqlite3.connect(filename)

def select(db: DB, query: str) -> None:
    cur = db._con.cursor()
    for row in cur.execute(query):
        print(row)

def tables(db: DB) -> None:
    return select(db, "select * from sqlite_master")

tdb("debug")
tdb("seed")
tdb("run")
tdb("test")

# ls("/home/pyodide/")
db = DB("./dev.db")
print("")
print("======================================")
print("============TABLES====================")
print("======================================")
tables(db)
print("======================================")
print("===select * from customers limit 2====")
print("======================================")
select(db, "select * from customers limit 2")
print("======================================")
print("====select * from orders limit 2======")
print("======================================")
select(db, "select * from orders limit 2")
print("======================================")

