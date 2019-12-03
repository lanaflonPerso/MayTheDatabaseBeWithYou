import csv

filename = './csv/planets2.csv'

# Première lecture pour les climats
climates = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    climate_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            climates_line = row[4].split(',')
            for climate_name in climates_line :
                climate_name = climate_name.strip()
                if climate_name not in climates:
                    climates[climate_name] = climate_id
                    print(
                        f"insert into climate (id, name) values ({climate_id}, '{climate_name}');")
                    climate_id += 1

        line_count += 1

# Première lecture pour les terrains
terrains = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    terrain_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            terrains_line = row[6].split(',')
            for terrain_name in terrains_line :
                terrain_name = terrain_name.strip()
                if terrain_name not in terrains:
                    terrains[terrain_name] = terrain_id
                    print(
                        f"insert into terrain (id, name) values ({terrain_id}, '{terrain_name}');")
                    terrain_id += 1

        line_count += 1

# Première lecture pour les planets
planets = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    planet_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            if (row[1].strip() == 'NA') : row[1] = 'null'
            if (row[2].strip() == 'NA') : row[2] = 'null'
            if (row[3].strip() == 'NA') : row[3] = 'null'
            #if (row[5].strip() == 'NA') : row[5] = 'null'
            if (row[7].strip() == 'NA') : row[7] = 'null'
            if (row[8].strip() == 'NA') : row[8] = 'null'

            print(
                f"insert into planet (id, name, rotation_period, orbital_period, diameter, gravity, surface_water, population) " + 
                f"values ({planet_id}, '{row[0]}', {row[1]}, {row[2]}, {row[3]}, '{row[5]}', {row[7]}, {row[8]});")

            # Climats
            climates_line = row[4].split(',')
            for climate_name in climates_line :
                climate_name = climate_name.strip()
                climate_id = climates.get(climate_name)
                print(
                    f"insert into planets_climates (planet_id, climat_id) values ({planet_id}, {climate_id});")
            
            # Terrains
            terrains_line = row[6].split(',')
            for terrain_name in terrains_line :
                terrain_name = terrain_name.strip()
                terrain_id = terrains.get(terrain_name)
                print(
                    f"insert into planets_terrains (planet_id, terrain_id) values ({planet_id}, {terrain_id});")
            
            planet_id += 1

        line_count += 1

# Characters
filename = './csv/characters2.csv'

# Première lecture pour les climats
colors = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    color_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            # Hair color
            colors_line = row[3].split(',')
            for color_name in colors_line :
                color_name = color_name.strip()
                if color_name not in colors:
                    colors[color_name] = color_id
                    print(
                        f"insert into color (id, name) values ({color_id}, '{color_name}');")
                    color_id += 1

            # Skin color
            colors_line = row[4].split(',')
            for color_name in colors_line :
                color_name = color_name.strip()
                if color_name not in colors:
                    colors[color_name] = color_id
                    print(
                        f"insert into color (id, name) values ({color_id}, '{color_name}');")
                    color_id += 1

            # Eye color
            colors_line = row[5].split(',')
            for color_name in colors_line :
                color_name = color_name.strip()
                if color_name not in colors:
                    colors[color_name] = color_id
                    print(
                        f"insert into color (id, name) values ({color_id}, '{color_name}');")
                    color_id += 1

        line_count += 1

color_id_sv = color_id

# Première lecture pour les homeworlds
homeworlds = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    homeworld_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            homeworlds_line = row[8].split(',')
            for homeworld_name in homeworlds_line :
                homeworld_name = homeworld_name.strip()
                if homeworld_name not in homeworlds:
                    homeworlds[homeworld_name] = homeworld_id
                    print(
                        f"insert into homeworld (id, name) values ({homeworld_id}, '{homeworld_name}');")
                    homeworld_id += 1
       
        line_count += 1

homeworld_id_sv = homeworld_id

# Première lecture pour les species
species = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    specie_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            species_line = row[9].split(',')
            for specie_name in species_line :
                specie_name = specie_name.strip()
                if specie_name not in species:
                    species[specie_name] = specie_id
                    print(
                        f"insert into character_species (id, name) values ({specie_id}, '{specie_name}');")
                    specie_id += 1

        line_count += 1

# Première lecture pour les characters
characters = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    character_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            if (row[1].strip() == 'NA') : row[1] = 'null'
            if (row[2].strip() == 'NA') : row[2] = 'null'
            homeworld_id = homeworlds.get(row[8].strip())
            specie_id = species.get(row[9].strip())

            print(
                f"insert into character (id, name, height, mass, birth_year, gender, homeworld_id, character_specie_id) " + 
                f"values ({character_id}, '{row[0]}', {row[1]}, {row[2]}, '{row[6]}', '{row[7]}', {homeworld_id}, {specie_id});")

            # Hair color
            colors_line = row[3].split(',')
            for color_name in colors_line :
                color_id = colors.get(color_name.strip())
                print(
                    f"insert into character_types_colors (character_id, type, color_id) values ({character_id}, 'hair', {color_id});")

            # Skin color
            colors_line = row[4].split(',')
            for color_name in colors_line :
                color_id = colors.get(color_name.strip())
                print(
                    f"insert into character_types_colors (character_id, type, color_id) values ({character_id}, 'skin', {color_id});")

            # Eye color
            colors_line = row[5].split(',')
            for color_name in colors_line :
                color_id = colors.get(color_name.strip())
                print(
                    f"insert into character_types_colors (character_id, type, color_id) values ({character_id}, 'eye', {color_id});")

            character_id += 1

        line_count += 1


#-----------------------------------------------
# Première lecture pour les tspecies - language
#-----------------------------------------------
# Species
filename = './csv/species2.csv'

languages = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    language_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            languages_line = row[8].split(',')
            for language_name in languages_line :
                language_name = language_name.strip()
                if language_name not in languages:
                    languages[language_name] = language_id
                    print(
                        f"insert into language (id, name) values ({language_id}, '{language_name}');")
                    language_id += 1

        line_count += 1

# Ajout des colors species
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    color_id = color_id_sv
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            # Hair color
            colors_line = row[4].split(',')
            for color_name in colors_line :
                color_name = color_name.strip()
                if color_name not in colors:
                    colors[color_name] = color_id
                    print(
                        f"insert into color (id, name) values ({color_id}, '{color_name}');")
                    color_id += 1

            # Skin color
            colors_line = row[5].split(',')
            for color_name in colors_line :
                color_name = color_name.strip()
                if color_name not in colors:
                    colors[color_name] = color_id
                    print(
                        f"insert into color (id, name) values ({color_id}, '{color_name}');")
                    color_id += 1

            # Eye color
            colors_line = row[6].split(',')
            for color_name in colors_line :
                color_name = color_name.strip()
                if color_name not in colors:
                    colors[color_name] = color_id
                    print(
                        f"insert into color (id, name) values ({color_id}, '{color_name}');")
                    color_id += 1

        line_count += 1

# Ajout des homeworlds
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    homeworld_id = homeworld_id_sv
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            homeworlds_line = row[9].split(',')
            for homeworld_name in homeworlds_line :
                homeworld_name = homeworld_name.strip()
                if homeworld_name not in homeworlds:
                    homeworlds[homeworld_name] = homeworld_id
                    print(
                        f"insert into homeworld (id, name) values ({homeworld_id}, '{homeworld_name}');")
                    homeworld_id += 1
       
        line_count += 1


# Première lecture pour les tspecies
tspecies = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    tspecie_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            if (row[3].strip() == 'NA') : row[3] = 'null'
            if (row[7].strip() == 'NA') : row[7] = 'null'

            language_id = languages.get(row[8].strip())
            homeworld_id = homeworlds.get(row[9].strip())

            print(
                f"insert into specie (id, name, average_height, average_lifespan, classification, designation, language_id, homeworld_id) " + 
                f"values ({tspecie_id}, '{row[0]}', {row[3]}, {row[7]}, '{row[1]}', '{row[2]}', {language_id}, {homeworld_id});")

            # Hair color
            colors_line = row[5].split(',')
            for color_name in colors_line :
                color_id = colors.get(color_name.strip())
                print(
                    f"insert into specie_types_colors (specie_id, type, color_id) values ({tspecie_id}, 'hair', {color_id});")

            # Skin color
            colors_line = row[4].split(',')
            for color_name in colors_line :
                color_id = colors.get(color_name.strip())
                print(
                    f"insert into specie_types_colors (specie_id, type, color_id) values ({tspecie_id}, 'hair', {color_id});")

            # Eye color
            colors_line = row[6].split(',')
            for color_name in colors_line :
                color_id = colors.get(color_name.strip())
                print(
                    f"insert into specie_types_colors (specie_id, type, color_id) values ({tspecie_id}, 'hair', {color_id});")
            
            tspecie_id += 1

        line_count += 1

