import pymysql
import pandas as pd
import requests, io
from datetime import datetime
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def open_db():
    try:
        # ost=os.getenv.get("HOST") //本地使用
        conn = pymysql.connect(
            host=os.environ.get("HOST"),
            port=int(os.environ.get("PORT")),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            database=os.environ.get("NAME"),
            ssl={"ca": None},
        )
        cursor = conn.cursor()

        return conn, cursor
    except Exception as e:
        print(e)
    return None, None


print(open_db())
