import json

# Fonction pour extraire les prix à partir d'un fichier JSON
def creating_price_database ():
    with open('data.json') as user_file:
        data = json.load(user_file)

    price_database = []

    for key, value in data.items():
        prices = value['price']
        price_database.append(prices)

    return price_database

# Fonction pour calculer les revenus potentiels en fonction des prix et des pourcentages
def creating_income_database():
    with open('data.json') as user_file:
        data = json.load(user_file)

    income_database = []

    for key, value in data.items():
        income = value['price'] * (value['percentage'] / 100)
        income_database.append(income)

    return income_database

# Fonction pour déterminer la meilleure combinaison d'actions à acheter
def best_investment(invest, prices, percentages, number_of_action):
    # Initialisation d'un tableau pour la programmation dynamique
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
            selected_items.append((prices[i - 1], percentages[i - 1]))
            w -= prices[i - 1]

    return selected_items

# Fonction pour calculer la somme des prix des actions sélectionnées
def sum_prices_actions(selected_items):
    sum_prices_actions = sum(items[0] for items in selected_items)
    return sum_prices_actions

# Fonction pour calculer la somme des revenus potentiels des actions sélectionnées
def sum_incomes(selected_items):
    sum_incomes = sum(items[1] for items in selected_items)
    return sum_incomes

# Fonction pour déterminer les actions à acheter dans la meilleure combinaison
def determination_actions_to_buy(selected_items, prices):
    best_combination_actions = []

    for items in selected_items:
        action = prices.index(items[0])
        best_combination_actions.append(action + 1)

    return best_combination_actions

if __name__ == '__main__':
    invest = 500

    # Extraction des prix et des revenus potentiels
    prices = creating_price_database()
    incomes = creating_income_database()
    number_of_action = len(prices)

    # Détermination de la meilleure combinaison d'actions
    selected_items = best_investment(invest, prices, incomes, number_of_action)

    # Calcul de la somme des prix des actions sélectionnées
    sum_prices_actions = sum_prices_actions(selected_items)

    # Calcul de la somme des revenus potentiels des actions sélectionnées
    sum_incomes = sum_incomes(selected_items)

    # Détermination des actions à acheter dans la meilleure combinaison
    actions_to_buy = determination_actions_to_buy(selected_items, prices)

    # Affichage des résultats
    print(f"J'ai investi {sum_prices_actions}€")
    print(f"J'ai récupéré {sum_incomes}€")
    print(f"En investissant dans les actions suivantes {actions_to_buy}")
