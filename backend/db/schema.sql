
CREATE TABLE IF NOT EXISTS rules(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL UNIQUE,
    updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

CREATE TABLE IF NOT EXISTS config(
    ENV VARCHAR(12) PRIMARY KEY NOT NULL,
    MOBSF_URL TEXT,
    MOBSF_API_KEY TEXT,
    SHOULD_DECOMPILE INTEGER,
    SHOULD_USE_MOBSF INTEGER
);