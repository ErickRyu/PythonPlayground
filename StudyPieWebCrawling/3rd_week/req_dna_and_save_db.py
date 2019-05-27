import urllib.request
import ssl
import json
import sqlite3

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

DNA_URL = 'http://api.plos.org/search?q=title:DNA'
data = urllib.request.urlopen(DNA_URL, context=ctx).read()
json_file = data.decode('utf-8')

json_data = json.loads(json_file)

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS docs')

cur.execute('CREATE TABLE docs (id TEXT, journal TEXT, eissn TEXT, publication_date TEXT, article_type TEXT, '
            'title_display TEXT, score REAL)')

for item in json_data['response']['docs']:
    cur.execute('INSERT INTO docs (id, journal, eissn, publication_date, article_type, title_display, score) '
            'VALUES (?, ?, ?, ?, ?, ?, ?)', (item['id'], item['journal'], item['eissn'], item['publication_date'],
                                             item['article_type'], item['title_display'], item['score']))
    conn.commit()
