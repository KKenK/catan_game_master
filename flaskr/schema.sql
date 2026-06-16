CREATE TABLE game_progress (
	progress TEXT,
    settler_turn INTEGER DEFAULT 0 NOT NULL,
    is_settler_two INTEGER DEFAULT 0 NOT NULL
);
INSERT INTO 'game_progress' (progress) VALUES ('uninitialised');

CREATE TABLE settlers (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    victory_points INTEGER DEFAULT 0 NOT NULL,
    longest_road INTEGER DEFAULT 1 NOT NULL,
    is_longest_road INTEGER DEFAULT 0 NOT NULL,
    defender_of_catan INTEGER DEFAULT 0 NOT NULL,
    army_strength INTEGER DEFAULT 0 NOT NULL 
);

CREATE TABLE settlements (
    id INTEGER PRIMARY KEY,
    settler_id INTEGER NOT NULL,
    resource_1 INTEGER,
    roll_1 INTEGER,
    resource_2 INTEGER,
    roll_2 INTEGER,
    resource_3 INTEGER,
    roll_3 INTEGER,
    is_city INTEGER,
    FOREIGN KEY (settler_id) REFERENCES settlers(id)
);

CREATE TABLE knights (
    id INTEGER PRIMARY KEY,
    settler_id INTEGER NOT NULL,
    "level" INTEGER NOT NULL,
    is_active INTEGER DEFAULT 0 NOT NULL,
    FOREIGN KEY (settler_id) REFERENCES settlers(id)
);

CREATE TABLE resources (
    id INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL
);

CREATE TABLE city_resources_commodities (
    id INTEGER PRIMARY KEY,
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
