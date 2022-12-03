from itertools import combinations
import csv

"""maximum spend per client 500 €"""
MAX_INVEST = 500

def main():
    shares_list = read_data_set_csv()

    print(f"\nProcessing {len(shares_list)} shares for {MAX_INVEST}€ :")

    best_combo = set_combos(shares_list)
    # print(f"best_combo : {best_combo}")
    # print(f"best_combo len : {len(best_combo)}")
    print(f"\nMost profitable investment ({len(best_combo)} shares) :\n")

    for item in best_combo:
        print(f"{item[0]} | {item[1]} € | +{item[2]} %")

    print("\nTotal cost : ", calculate_cost(best_combo), "€")
    print("Profit after 2 years : +", calc_profit(best_combo), "€")

def read_data_set_csv():
    """Import shares data from dataset_test.csv"""
    with open("data/dataset_test.csv", "r") as data:
        shares_csv_reader = csv.reader(data)
        next(shares_csv_reader)
        shares_list = []
        for row in shares_csv_reader:
            shares_list.append(
                (row[0], float(row[1]), float(row[2]))
            )
            

        return shares_list
    

def set_combos(shares_list):
    """Set all possible combinations of shares"""
    profit = 0
    best_combo = []

    for i in range(len(shares_list)):
        combos = combinations(shares_list, i+1)

        for combo in combos:
            total_cost = calculate_cost(combo)

            if total_cost <= MAX_INVEST:
                total_profit = calc_profit(combo)

                if total_profit > profit:
                    profit = total_profit
                    best_combo = combo

    return best_combo


def calculate_cost(combo):
    """Sum of current share combo prices"""
    prices = []
    for el in combo:
        prices.append(el[1])

    return sum(prices)


def calc_profit(combo):
    """Sum of current share combo profit"""
    profits = []
    for el in combo:
        profits.append(el[1] * el[2] / 100)

    return sum(profits)

    
if __name__ == "__main__":
    main()
