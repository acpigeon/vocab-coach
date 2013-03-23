import sqlite3 as sql
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'tmp', 'vocab.db')

# sample entry
wordAttributes = {'vocab': 'tener', 'canonical': 'tener', 'partOfSpeech': 'verb', 'type': 'infinitive', 'gender': 'NULL', 'language': 'spanish',
    'contexts': ['er verbs', 'exam 1', 'exam 2'],
    'tags': ['memory aid', 'whatever else']
}

def createNewVocab (wordAttributes):

    con = sql.connect(DATABASE)
    with con:
        cur = con.cursor()

        #cur.execute("DROP TABLE IF EXISTS tblVocab")
        #cur.execute("DROP TABLE IF EXISTS tblRoot")
        #cur.execute("DROP TABLE IF EXISTS tblContext")
        #cur.execute("DROP TABLE IF EXISTS tblTags")

        #cur.execute("CREATE TABLE tblVocab(vocab_id INTEGER, canonical_id INTEGER, vocabulary TEXT, part_of_speech TEXT, type TEXT, gender TEXT, language TEXT)")
        #cur.execute("CREATE TABLE tblRoot(canonical_id INTEGER, root TEXT)")
        #cur.execute("CREATE TABLE tblContext(context_id INTEGER, context TEXT, vocab_id INTEGER)")
        #cur.execute("CREATE TABLE tblTags(tag_id INTEGER, tag TEXT, vocab_id INTEGER)")

        #tblVocabIndex = 0
        #tblRootIndex = 0
        #tblContextIndex = 0
        #tblTagsIndex = 0

        #print type(cur.execute("SELECT COUNT(`vocab_id`) FROM tblVocab")) # <type 'sqlite3.Cursor'>
        #print cur.execute("SELECT COUNT(`vocab_id`) FROM tblVocab") # <sqlite3.Cursor object at 0x100486420>

        tblVocabIndex = cur.execute("SELECT COUNT(`vocab_id`) FROM tblVocab").fetchone()[0] - 1
        tblRootIndex = cur.execute("SELECT COUNT(`canonical_id`) FROM tblRoot").fetchone()[0] - 1
        tblContextIndex = cur.execute("SELECT COUNT(`context_id`) FROM tblContext").fetchone()[0] - 1
        tblTagsIndex = cur.execute("SELECT COUNT(`tag_id`) FROM tblTags").fetchone()[0] - 1

        cur.execute("INSERT INTO tblVocab VALUES(?,?,?,?,?,?,?)", (tblVocabIndex, tblRootIndex, wordAttributes['vocab'], wordAttributes['partOfSpeech'], wordAttributes['type'], wordAttributes['gender'], wordAttributes['language']))
        cur.execute("INSERT INTO tblRoot VALUES(?,?)", (tblRootIndex, wordAttributes['canonical']))
        for context in wordAttributes['contexts']:
            cur.execute("INSERT INTO tblContext VALUES(?,?,?)", (tblContextIndex, context, tblVocabIndex))
        for tag in wordAttributes['tags']:
            cur.execute("INSERT INTO tblTags VALUES(?,?,?)", (tblTagsIndex, tag, tblVocabIndex))



createNewVocab(wordAttributes)