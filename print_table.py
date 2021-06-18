import psycopg2
import pandas as pd
import numpy as np

TVSHOW = "http://api.tvmaze.com/search/shows?q="


def print_table(cur):
    cur.execute("select name, premiered from tvshows order by premiered")
    tab = cur.fetchall()
    try:
        tab = np.array(tab)
        df = pd.DataFrame(data=tab, columns=["name", "premiered"])
        print(df)
    except ValueError:
        print("Таблица пуста")


if __name__ == '__main__':
    with psycopg2.connect(dbname="postgres", user="postgres", password="example") as conn:
        cur = conn.cursor()
        print_table(cur)
        cur.close()