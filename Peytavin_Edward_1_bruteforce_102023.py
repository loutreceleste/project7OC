import json
from itertools import combinations


# Fonction pour extraire les prix à partir d'un fichier JSON
def creating_price_database():
    # Ouvre et lit un fichier JSON 'data.json'
    with open('data.json') as user_file:
        data = json.load(user_file)

    # Crée une liste de prix extraits du fichier
    price_database = []

    for key, value in data.items():
        prices = value['price']
        price_database.append(prices)

    return price_database


# Fonction pour extraire les pourcentages d'investissement à partir du même fichier JSON
def creating_precentage_database():
    with open('data.json') as user_file:
        data = json.load(user_file)

    # Crée une liste de pourcentages extraits du fichier
    percentage_database = []

    for key, value in data.items():
        precentage = value['percentage']
        percentage_database.append(precentage)

    return percentage_database


# Fonction pour créer un dictionnaire associant les prix aux pourcentages
def creating_price_percent_dict(precentage_database, price_database):
    price_percentage_dict = {}

    for price in price_database:
        for percentage in precentage_database:
            price_percentage_dict[price] = percentage
            precentage_database.remove(percentage)
            break

    return price_percentage_dict


# Fonction pour calculer le produit du prix et du pourcentage
def mult_price_income(price_percentage_dict):
    mult_price_percentages_list = [key * val / 100 for key, val in price_percentage_dict.items()]
    return mult_price_percentages_list


# Fonction pour créer un dictionnaire associant les prix aux revenus potentiels en euros
def creating_price_income_percentage_database(income_list, price_database):
    price_percentage_dict = {}

    for price in price_database:
        for income in income_list:
            price_percentage_dict[price] = income
            income_list.remove(income)
            break

    return price_percentage_dict


# Fonction pour générer toutes les combinaisons possibles de prix
def possibilities_prices(price_data):
    list_possibilitie_prices = []

    for i in range(1, len(price_data) + 1):
        list_of_possibilities = combinations(price_data, i)

        for possibilitie in list_of_possibilities:
            if sum(possibilitie) <= amount_to_invest:
                list_possibilitie_prices.append(list(possibilitie))

    return list_possibilitie_prices


# Fonction pour générer les benefices associés à chaque combinaison de prix
def possibilities_percentages(all_possibilities_prices, price_income_dict):
    list_possibilitie_percentages = []

    for possibilities_price in all_possibilities_prices:
        possibilitie_percentage_list = []

        for possibilitie_price in possibilities_price:
            if possibilitie_price in price_income_dict:
                percentage_value = price_income_dict[possibilitie_price]
                possibilitie_percentage_list.append(percentage_value)

        list_possibilitie_percentages.append(possibilitie_percentage_list)

    return list_possibilitie_percentages


# Fonction pour calculer la somme des benefices pour chaque combinaison de prix
def sum_income(all_possibilities_income):
    sum_percentages = []

    for possibilities_income in all_possibilities_income:
        percentages = sum(possibilities_income)
        sum_percentages.append(percentages)

    return sum_percentages


# Fonction pour trouver le nombre de combinaisons possibles
def find_number_of_posibilities(all_sum_possibilities_income):
    number_of_posibilities = len(all_sum_possibilities_income)
    return number_of_posibilities


# Fonction pour identifier le meilleur benefice parmi les combinaisons possibles
def identifi_best_income(all_sum_possibilities_income, number_of_posibilities):
    if number_of_posibilities <= 0:
        print("Aucun investissement disponible avec vos paramètres")
        return None

    best_income = all_sum_possibilities_income[0]

    for i in range(1, len(all_sum_possibilities_income)):
        if all_sum_possibilities_income[i] > best_income:
            best_income = all_sum_possibilities_income[i]

    return best_income


# Fonction pour trouver la position du meilleur benefice
def find_position_best_income(best_income, all_sum_possibilities_income):
    position_best_invest = all_sum_possibilities_income.index(best_income)
    return position_best_invest


# Fonction pour identifier le meilleur investissement (somme des prix) parmi les combinaisons possibles
def identifi_best_invest(all_possibilities_prices, position_best_income):
    best_invest = sum(all_possibilities_prices[position_best_income])
    return best_invest


# Fonction pour déterminer les actions à acheter pour la meilleure combinaison
def determination_actions_to_buy(position_best_income, all_possibilities_prices, price_database):
    best_invest_prices = all_possibilities_prices[position_best_income]
    best_combination_actions = []

    for best_invest_price in best_invest_prices:
        action = price_database.index(best_invest_price)
        best_combination_actions.append(action + 1)  # Ajoute 1 car l'indice commence à 0

    return best_combination_actions


if __name__ == '__main__':
    amount_to_invest = 500

    # Extraction des données de prix et de pourcentage
    precentage_database = creating_precentage_database()
    price_database = creating_price_database()

    # Création du dictionnaire associant les prix aux pourcentages
    price_percent_decimal_dict = creating_price_percent_dict(precentage_database, price_database)

    # Calcul du produit des prix et des pourcentages
    income_list = mult_price_income(price_percent_decimal_dict)

    # Création du dictionnaire associant les prix aux benefices potentiels
    price_income_dict = creating_price_income_percentage_database(income_list, price_database)

    # Génération de toutes les combinaisons possibles de prix
    all_possibilities_prices = possibilities_prices(price_database)

    # Génération des benefices associés à chaque combinaison de prix
    all_possibilities_income = possibilities_percentages(all_possibilities_prices, price_income_dict)

    # Calcul de la somme des benefices pour chaque combinaison
    all_sum_possibilities_income = sum_income(all_possibilities_income)

    # Trouver le nombre de combinaisons possibles
    number_of_posibilities = find_number_of_posibilities(all_sum_possibilities_income)

    # Identifier le meilleur benefice parmi les combinaisons
    best_income = identifi_best_income(all_sum_possibilities_income, number_of_posibilities)
    round_best_income = round(best_income, 3)  # Arrondi à 3 décimales

    # Trouver la position du meilleur benefice parmi les combinaisons
    position_best_income = find_position_best_income(best_income, all_sum_possibilities_income)

    # Identifier la meilleure combinaison d'investissement (somme des prix)
    best_invest = identifi_best_invest(all_possibilities_prices, position_best_income)

    # Déterminer quelles actions acheter pour la meilleure combinaison
    actions_to_buy = determination_actions_to_buy(position_best_income, all_possibilities_prices, price_database)

    # Afficher les résultats
    print(f"J'ai investi {best_invest}€")
    print(f"J'ai récupéré {round_best_income}€")
    print(f"En investissant dans les actions suivantes {actions_to_buy}")
