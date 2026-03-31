CREATE TABLE game_progress (
	progress TEXT
);
INSERT INTO 'game_progress' (progress) VALUES ('uninitialised')

CREATE TABLE settlers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    victory_points INTEGER DEFAULT 0 NOT NULL,
    army_strength INTEGER DEFAULT 0 NOT NULL 
);

CREATE TABLE settlements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    settler_id INTEGER NOT NULL,
    resource_1 TEXT,
    roll_1 INTEGER,
    resource_2 TEXT,
    roll_2 INTEGER,
    resource_3 TEXT,
    roll_3 INTEGER,
    is_city INTEGER,
    FOREIGN KEY (settler_id) REFERENCES settlers(id)
);

CREATE TABLE knights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    settler_id INTEGER NOT NULL,
    "level" INTEGER NOT NULL,
    active_status INTEGER NOT NULL,
    FOREIGN KEY (settler_id) REFERENCES settlers(id)
);

CREATE TABLE resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL
);

CREATE TABLE city_resources_comodoties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL
);


-- rows = db.execute('SELECT ...')
-- row = (id, settler_id, resource_1_name, roll_1, resource_2_name, roll_2, resource_3_name, roll_3, resource_4_name, resource_5_name, resource_6_name, is_city)

-- if row.roll_1:
--   take row.resource_1_name
--   if row.is_city:
--     take row.resource_4_name
-- if row.roll_2:
--   take row.resource_2_name
--   if row.is_city:
--     take row.resource_5_name
-- if row.roll_3:
--   take row.resource_3_name
--   if row.is_city:
--     take row.resource_6_name
