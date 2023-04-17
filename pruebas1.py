from csv import reader

def get_data_from_user(name_file):
    with open(name_file, 'r') as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        print(list_of_rows)
get_data_from_user("coach_1_pokemons.csv")