import csv

filename = './csv/vehicules2.csv'

# Première lecture pour les manufacturers
manufacturers = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    manufacturer_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            manufacturers_line = row[2].split(',')
            for manufacturer_name in manufacturers_line :
                manufacturer_name = manufacturer_name.strip()
                if manufacturer_name not in manufacturers:
                    manufacturers[manufacturer_name] = manufacturer_id
                    print(
                        f"insert into vehiculeManufacturer (id, name) values ({manufacturer_id}, '{manufacturer_name}');")
                    manufacturer_id += 1

        line_count += 1

# Première lecture pour les models
models = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    model_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            models_line = row[1].split(',')
            for model_name in models_line :
                model_name = model_name.strip()
                if model_name not in models:
                    models[model_name] = model_id
                    manu_id = manufacturers.get(row[2].strip())
                    print(
                        f"insert into vehiculeModel (id, name, vehicule_anufacturer_id) values ({model_id}, '{model_name}', {manu_id});")
                    model_id += 1

        line_count += 1

# Première lecture pour les vclasss
vclasss = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    vclass_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            vclasss_line = row[10].split(',')
            for vclass_name in vclasss_line :
                vclass_name = vclass_name.strip()
                if vclass_name not in vclasss:
                    vclasss[vclass_name] = vclass_id
                    print(
                        f"insert into vehiculeClass (id, name) values ({vclass_id}, '{vclass_name}');")
                    vclass_id += 1

        line_count += 1


# Première lecture pour les vehicules
vehicules = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    planet_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            if (row[3].strip() == 'NA') : row[3] = 'null'
            if (row[4].strip() == 'NA') : row[4] = 'null'
            if (row[5].strip() == '') : row[5] = 'null'
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
