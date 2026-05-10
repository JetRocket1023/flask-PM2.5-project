import pymysql
import pandas as pd
import requests, io
from datetime import datetime
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_latest_data():
    conn, cursor = open_db()
    result = {"success": True, "message": None, "columns": None, "rows": None}
    if not conn:
        result["success"] = False
        result["massage"] = "資料庫開啟失敗"
        return result

    sql = """
    select * from data where datacreationdate=
    (select max(datacreationdate) from data);
    """

    # sql = "select max(datacreationdate) from data;"
    try:
        cursor.execute(sql)
        # 取得資料欄位名稱
        # print(cursor.description)
        columns = [col[0] for col in cursor.description]

        rows = cursor.fetchall()
        result["success"] = True
        result["columns"] = columns
        result["rows"] = rows
        return result
    except Exception as e:
        result["success"] = False
        result["massage"] = f"資料庫查詢失敗(e)"
        return result
    finally:
        conn.close()


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


print(get_latest_data())
