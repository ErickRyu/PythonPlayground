import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS MyDB')

cur.execute('CREATE TABLE MyDB (id TEXT, journal TEXT, eissn TEXT, publication_date TEXT, article_type TEXT, '
            'title_display TEXT, score REAL)')

cur.execute('INSERT INTO MyDB (id, journal, eissn, publication_date, article_type, title_display, score) '
            'VALUES (?, ?, ?, ?, ?, ?, ?)', ('a', 'b', 'a', 'a', 'a', 'a', 1.1))

conn.commit()
