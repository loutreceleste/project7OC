import csv

# Fonction pour créer une liste de prix et de revenus à partir d'un fichier CSV
def creating_prices_incomes_database(database):
    prices_incomes = []

    with open(database, newline='') as csvfile:
        alldata = csv.reader(csvfile)
        for data in alldata:
            morceaux = ', '.join(data).split(',')
            if len(morceaux) >= 3:
                nombre = round(float(morceaux[1].strip()) * 100), (round(float(morceaux[1].strip())) * round(float(morceaux[2].strip())))
                if nombre[0] > 0:
                    prices_incomes.append(nombre)

    return prices_incomes

# Fonction pour extraire la liste des prix à partir de la liste de prix et de revenus
def creating_price_database(prices_incomes_database):
    prices = []

    for price_income_database in prices_incomes_database:
        prices.append(price_income_database[0])
    return prices

# Fonction pour extraire la liste des revenus à partir de la liste de prix et de revenus
def creating_income_database(prices_incomes_database):
    incomes = []

    for price_income_database in prices_incomes_database:
        incomes.append(price_income_database[1])
    return incomes

# Fonction pour déterminer la meilleure combinaison d'actions à acheter
def best_investment(invest, prices, percentages, number_of_action):
    dp = [[0 for _ in range(invest + 1)] for _ in range(number_of_action + 1)]
    selected_items = []

    for i in range(1, number_of_action + 1):
        for w in range(invest + 1):
            if prices[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - prices[i - 1]] + percentages[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    w = invest
    for i in range(number_of_action, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append([prices[i - 1] / 100, percentages[i - 1] / 100])
            w -= prices[i - 1]

    return selected_items

# Fonction pour calculer la somme des prix des actions sélectionnées
def sum_prices_actions(selected_items):
    sum_prices_actions = (sum(items[0] for items in selected_items))
    return sum_prices_actions

# Fonction pour calculer la somme des revenus potentiels des actions sélectionnées
def sum_incomes(selected_items):
    sum_incomes = (sum(items[1] for items in selected_items))
    return sum_incomes

# Fonction pour trouver les noms des actions à acheter
def find_action(database, selected_items):
    all_list = []
    action_to_buy = []

    with open(database, newline='') as csvfile:
        alldata = csv.reader(csvfile)
        for data in alldata:
            data[-2:] = [float(data[-2]), float(data[-1])]
            all_list.append(data)

    for item in selected_items:
        for lst in all_list:
            if item[0] == lst[1]:
                action_to_buy.append(lst[0])

    return action_to_buy

if __name__ == '__main__':
    invest = 50000
    database = 'dataset1_Python+P7.csv'

    # Extraction des prix et des revenus
    prices_incomes_database = creating_prices_incomes_database(database)
    prices = creating_price_database(prices_incomes_database)
    incomes = creating_income_database(prices_incomes_database)

    number_of_action = len(prices)

    # Détermination de la meilleure combinaison d'actions
    selected_items = best_investment(invest, prices, incomes, number_of_action)

    # Calcul de la somme des prix des actions sélectionnées
    sum_prices_actions = sum_prices_actions(selected_items)
    round_sum_prices_actions = round(sum_prices_actions, 3) # Arrondi à 3 décimales

    # Calcul de la somme des revenus potentiels des actions sélectionnées
    sum_incomes = sum_incomes(selected_items)
    round_sum_incomes = round(sum_incomes, 3) # Arrondi à 3 décimales

    # Recherche des noms des actions à acheter
    actions_to_buy = find_action(database, selected_items)

    # Affichage des résultats
    print(f"J'ai investi {round_sum_prices_actions}€")
    print(f"J'ai récupéré {round_sum_incomes}€")
    print(f"En investissant dans les actions suivantes {actions_to_buy}")
