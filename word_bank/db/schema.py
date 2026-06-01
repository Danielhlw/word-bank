SCHEMA = """
CREATE TABLE IF NOT EXISTS verbs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    base TEXT NOT NULL,
    infinitive TEXT,
    present_participle TEXT,
    past TEXT,
    past_participle TEXT,
    portuguese TEXT
);

CREATE TABLE IF NOT EXISTS be_forms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    base TEXT NOT NULL,
    infinitive TEXT,
    present_participle TEXT,
    past TEXT,
    past_participle TEXT,
    portuguese TEXT
);

CREATE TABLE IF NOT EXISTS adjectives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english TEXT NOT NULL,
    portuguese TEXT
);

CREATE TABLE IF NOT EXISTS possessive_adjectives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person TEXT NOT NULL,
    form TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS nouns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    singular TEXT NOT NULL,
    plural TEXT,
    portuguese TEXT
);

CREATE TABLE IF NOT EXISTS subject_pronouns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person TEXT NOT NULL,
    form TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS object_pronouns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person TEXT NOT NULL,
    form TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS possessive_pronouns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person TEXT NOT NULL,
    form TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tense_examples (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER,
    simple_present TEXT,
    present_continuous TEXT,
    simple_past TEXT,
    simple_future TEXT,
    present_perfect TEXT
);

CREATE TABLE IF NOT EXISTS yesno_examples (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    situation TEXT NOT NULL,
    yesno_question TEXT,
    response TEXT,
    wh_question TEXT,
    statement TEXT
);
"""

TABLES = [
    "verbs",
    "be_forms",
    "adjectives",
    "possessive_adjectives",
    "nouns",
    "subject_pronouns",
    "object_pronouns",
    "possessive_pronouns",
    "tense_examples",
    "yesno_examples",
]
