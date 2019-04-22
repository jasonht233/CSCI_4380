/* project schema */

/*
problem general:

1. longitude and latitude would not be interger
2. not a good way for reference to the outdorr_recreation

*/
DROP SCHEMA IF EXISTS Vocation_recommand;
CREATE SCHEMA Vocation_recommand;

DROP TABLE IF EXISTS outdoor_recreation;
CREATE TABLE outdoor_recreation(
  id serial primary key,
  county VARCHAR(127),
  name VARCHAR(127) NOT NULL,
  feature VARCHAR(512), /*Featured recreational activity at the site*/
  description VARCHAR(512),
  /*Description of the site, including any advisories or specifications re.
  accessible features.*/
  primitive BOOLEAN,
  /*Is the site located in a primitive
  natural setting, away from busy roads and human settlement?*/
  tent_site BOOLEAN,
  /*Does the facility include one or more accessible tent camping sites?*/
  pinic_table BOOLEAN,
  /*Does the site include one or more accessible picnic tables?*/
  privy BOOLEAN,
  /* does the site include one or more accessible pit privys?*/
  trails BOOLEAN,
  /*Does the site include one or more accessible trails (generally 1/4 mile or longer)?*/
  equestrian BOOLEAN,
  /*Does the site include one or more accessible equestrian mounting platforms?*/
  scenic_overlook BOOLEAN,
  hunting_blind BOOLEAN,
  fishing_pier BOOLEAN,
  beach BOOLEAN,
  toilet BOOLEAN,
  shower BOOLEAN,
  directions VARCHAR(512),
  longitude NUMERIC,
  latitude NUMERIC
);

DROP TABLE IF EXISTS Fishing_and_River;
CREATE TABLE Fishing_and_River(
  id serial primary key,
  waterbody_name VARCHAR(127) NOT NULL,
  county VARCHAR(127),
  longitude NUMERIC,
  latitude NUMERIC,
  Type_PA VARCHAR(127),
  Acess_owner VARCHAR(127),
  fish VARCHAR(256)
);

DROP TABLE IF EXISTS historic_Places;
CREATE TABLE historic_places(
  id serial primary key,
  name VARCHAR(127) NOT NULL,
  county VARCHAR(127),
  longitude NUMERIC,
  latitude NUMERIC
);

DROP TABLE IF EXISTS liquor;
CREATE TABLE liquor(
  id serial primary key,
  name VARCHAR(127) NOT NULL,
  county VARCHAR(127),
  state VARCHAR(127),
  address VARCHAR(512),
  longitude NUMERIC,
  latitude NUMERIC
);


DROP TABLE IF EXISTS fish;
CREATE TABLE fish(
  id serial primary key, 
  waterbody_name VARCHAR(127) NOT NULL,
  county VARCHAR(127),
  season VARCHAR(32),
  species VARCHAR(32),
  num INTEGER 
);

GRANT ALL PRIVILEGES ON liquor , historic_Places, outdoor_recreation TO resort;
