CREATE TABLE tblContext(context_id INTEGER PRIMARY KEY, context TEXT, vocab_id INTEGER);
CREATE TABLE tblRoot(canonical_id INTEGER PRIMARY KEY, root TEXT);
CREATE TABLE tblTags(tag_id INTEGER PRIMARY KEY, tag TEXT, vocab_id INTEGER);
CREATE TABLE tblVocab(vocab_id INTEGER PRIMARY KEY, canonical_id INTEGER, vocabulary TEXT, part_of_speech TEXT, type TEXT, gender TEXT, language TEXT);