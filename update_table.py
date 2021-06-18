import requests
import psycopg2
import dateparser

TVSHOW = "http://api.tvmaze.com/search/shows?q="


def insert_into_table(cur, data):
    try:
        cur.execute("insert into tvshows(id, name, url, premiered,status)" +
                    "values(%s, %s, %s, %s,%s)", data)
    except psycopg2.errors.UniqueViolation:
        print("Сериал уже существует")


if __name__ == '__main__':
    with psycopg2.connect(dbname="postgres", user="postgres", password="example") as conn:
        cur = conn.cursor()
        tv_show = input("Поиск: ")
        req = requests.get(TVSHOW + tv_show)
        response = req.json()
        if len(response) > 0:
            new_show = {'id': response[0]['show']['id'],
                        'name': response[0]['show']['name'],
                        'url': response[0]['show']['url'],
                        'premiered': dateparser.parse(response[0]['show']['premiered']),
                        'status': response[0]['show']['status']}

            insert_into_table(cur, list(new_show.values()))
        cur.close()
