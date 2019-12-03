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
            print(
                f"insert into planet (id, name, rotation_period, orbital_period, diameter, gravity, surface_water, population) " + 
                f"values ({planet_id}, '{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[5]}', '{row[7]}', '{row[8]}');")

            # Climats
            


            planet_id += 1

        line_count += 1

