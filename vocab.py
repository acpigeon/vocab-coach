import sqlite3 as sql
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'tmp', 'vocab.db')

con = sql.connect(DATABASE)
with con:
	cur = con.cursor()
	#cur.execute("CREATE TABLE tblVocab(vocab_id INT, canonical_id INT, vocabulary TEXT, part_of_speech TEXT, type TEXT, gender TEXT, language TEXT)")
	cur.execute("INSERT INTO tblVocab VALUES(?,?,?,?,?,?,?)", (1, 1, 'tener', 'verb', 'infinitive', 'nothing', 'spanish'))