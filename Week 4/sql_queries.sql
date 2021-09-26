-- add stars to table
INSERT INTO Star VALUES 
(7115384,	3789,	27.384),
(8106973,	5810,	0.811),
(9391817,	6200,	0.958);

-- fix table issues
DELETE FROM Planet
WHERE radius < 0;

UPDATE Planet
SET kepler_name = NULL
WHERE status <> 'CONFIRMED';

-- make own table and add entries
CREATE TABLE Planet (
  kepler_id INTEGER NOT NULL,
  koi_name VARCHAR(15) NOT NULL UNIQUE,
  kepler_name VARCHAR(15),
  status VARCHAR(20) NOT NULL,
  radius FLOAT NOT NULL
);

INSERT INTO Planet VALUES
(6862328,	'K00865.01','',	'CANDIDATE',	119.021),
(10187017,	'K00082.05',	'Kepler-102 b',	'CONFIRMED',	5.286),
(10187017,	'K00082.04',	'Kepler-102 c',	'CONFIRMED',	7.071);

-- create table from csv
CREATE TABLE Star (
  kepler_id INTEGER NOT NULL,
  t_eff INTEGER NOT NULL,
  radius FLOAT NOT NULL,
  PRIMARY KEY (kepler_id)
);

CREATE TABLE Planet (
  kepler_id INTEGER REFERENCES Star(kepler_id),
  koi_name VARCHAR(20) NOT NULL,
  kepler_name VARCHAR(20),
  status VARCHAR(20) NOT NULL,
  period FLOAT,
  radius FLOAT,
  t_eq INTEGER,
  PRIMARY KEY (koi_name)
);


COPY Star (kepler_id, t_eff, radius) FROM 'stars.csv' CSV;

COPY Planet (kepler_id, koi_name, kepler_name, status, period, radius, t_eq) FROM 'planets.csv' CSV;

-- create new table after dropping old
DROP TABLE Star;

CREATE TABLE Star (
  kepler_id INTEGER PRIMARY KEY,
  t_eff INTEGER,
  radius FLOAT,
  ra FLOAT,
  decl FLOAT
);


COPY Star (kepler_id, t_eff, radius, ra, decl) FROM 'stars_full.csv' CSV;

