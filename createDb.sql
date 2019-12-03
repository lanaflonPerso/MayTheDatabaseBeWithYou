--**************************************************************************************
-- Characters
--**************************************************************************************
DROP TABLE IF EXISTS character_types_colors;
DROP TABLE IF EXISTS specie_types_colors;
DROP TABLE IF EXISTS color;
DROP TYPE IF EXISTS character_types;
DROP TABLE IF EXISTS character;
DROP TABLE IF EXISTS character_species;
DROP TYPE IF EXISTS genders;
DROP TABLE IF EXISTS specie;
DROP TABLE IF EXISTS homeworld;

CREATE TABLE color (
    id serial not null constraint color_pk primary key,
    name varchar(100)
);

CREATE TYPE genders as ENUM ('NA', 'male', 'female','hermaphrodite');

CREATE TABLE character_species (
    id serial not null constraint character_species_pk primary key,
    name varchar(100)
);

CREATE TABLE homeworld (
    id serial not null constraint homeworld_pk primary key,
    name varchar(100)
);

CREATE TABLE character (
    id serial not null constraint character_pk primary key,
    name varchar(100),
    height int,
    mass int,
    birth_year int,
    gender genders,
    homeworld_id integer constraint homeworld_fk references homeworld,
    character_specie_id integer constraint character_specie_fk references character_species
);

CREATE TYPE character_types AS ENUM ('hair', 'skin', 'eye');

CREATE TABLE character_types_colors (
    character_id integer constraint character_fk references character,
    type character_types,
    color_id integer constraint color_fk references color
);

--**************************************************************************************
-- Planets
--**************************************************************************************
DROP TABLE IF EXISTS planets_terrains;
DROP TABLE IF EXISTS planets_climates;
DROP TABLE IF EXISTS climate;
DROP TABLE IF EXISTS terrain;
DROP TABLE IF EXISTS planet;

CREATE TABLE climate (
    id serial not null constraint climate_pk primary key,
    name varchar(50)
);

CREATE TABLE terrain (
    id serial not null constraint terrain_pk primary key,
    name varchar(50)
);

CREATE TABLE planet (
    id serial not null constraint planet_pk primary key,
    name varchar(100),
    rotation_period int,
    orbital_period int,
    diameter int,
    gravity varchar,
    surface_water int,
    population bigint
);

CREATE TABLE planets_terrains (
    planet_id integer not null constraint planet_fk references planet,
    terrain_id integer not null constraint terrain_fk references terrain
);

CREATE TABLE planets_climates (
    planet_id integer not null constraint planet_fk references planet,
    climat_id integer constraint climat_fk references climate
);

--**************************************************************************************
-- Species
--**************************************************************************************
DROP TABLE IF EXISTS language;
DROP TYPE IF EXISTS speciesClassification;
DROP TYPE IF EXISTS speciesDesignation;

CREATE TYPE speciesClassification as ENUM ('gastropod', 'mammal' , 'reptile', 'amphibian', 'insectoid', 'artificial', 'sentient', 'NA');

CREATE TYPE speciesDesignation as ENUM ('sentient', 'reptilian', 'NA');

CREATE TABLE language (
      id serial not null constraint language_pk primary key,
      name varchar(100)
);

CREATE TABLE specie (
    id serial not null constraint specie_pk primary key,
    average_height int,
    average_lifespan int,
    classification speciesClassification,
    designation speciesDesignation,
    language_id integer constraint language_fk references language,
    homeworld_id integer constraint homeworld_fk references homeworld
);

CREATE TABLE specie_types_colors (
     specie_id integer constraint specie_fk references specie,
     type character_types,
     color_id integer constraint color_fk references color
);

--**************************************************************************************
-- Vehicles
--**************************************************************************************
drop table if exists starship;
drop table if exists vehicule;
drop table if exists vehiculeClass;
drop table if exists vehiculeModel;
drop table if exists vehiculeManufacturer;

create table vehiculeManufacturer
(
    id serial not null constraint vehicule_manufacturer_pk primary key,
    name varchar(100)
);

create table vehiculeModel
(
    id serial  not null constraint vehicule_model_pk primary key,
    name varchar(100),
    vehicule_anufacturer_id integer not null constraint vehicule_manufacturer_fk references vehiculeManufacturer
);

create table vehiculeClass
(
    id serial  not null constraint vehicule_class_pk primary key,
    name varchar(512)
);

create table vehicule (
    id serial not null constraint vehicule_pk primary key,
    name varchar(512),
    cost_in_credits int,
    length decimal(7,2),
    max_atmosphering_speed int,
    crew int,
    passengers int,
    cargo_capacity int,
    consumables varchar,
    vehicule_model_id integer not null constraint vehicule_model_fk references vehiculeModel,
    vehicule_class_id integer not null constraint vehicule_class_fk references vehiculeClass
);

CREATE TABLE starship (
    hyperdrive_rating decimal(7,2),
    mglt int
) INHERITS (vehicule);



insert into climate (id, name) values (1, 'temperate');
insert into climate (id, name) values (2, 'tropical');
insert into climate (id, name) values (3, 'frozen');
insert into climate (id, name) values (4, 'murky');
insert into climate (id, name) values (5, 'arid');
insert into climate (id, name) values (6, 'windy');
insert into climate (id, name) values (7, 'hot');
insert into climate (id, name) values (8, 'artificial temperate');
insert into climate (id, name) values (9, 'frigid');
insert into climate (id, name) values (10, 'humid');
insert into climate (id, name) values (11, 'moist');
insert into climate (id, name) values (12, 'polluted');
insert into climate (id, name) values (13, 'NA');
insert into climate (id, name) values (14, 'superheated');
insert into climate (id, name) values (15, 'subartic');
insert into climate (id, name) values (16, 'artic');
insert into climate (id, name) values (17, 'rocky');