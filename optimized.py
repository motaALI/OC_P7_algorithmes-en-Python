import sys
import csv
import time

MAX_INVEST = 50000

start_at = time.time()

def main():
    
    """Ask user for a filename to be used in the algo"""
    try:
        filename = "data/" + sys.argv[1] + ".csv"
    except IndexError:
        print("\nFile not found. Please try again.\n")
        time.sleep(1)
        sys.exit()
        
    shares_list = read_data_set_csv(filename)
    
    cost = []
    profit = []

    for item in sacADos(shares_list):
        print(f"{item[0]} | {item[1] / 100} € | +{item[2]} €")
        cost.append(item[1] / 100)
        profit.append(item[2])
        

    print("\nTotal cost : ", sum(cost), "€")
    print("Profit after 2 years : +", sum(profit), "€")
    # print(f"best combo : {sacADos(shares_list)}")
    print("\nExecution time per second: ", time.time() - start_at, "(s)\n")

def read_data_set_csv(filename):
    try:
        # with open("data/dataset2_Python+P7.csv", "r") as data:
        with open(filename, "r") as data:
            shares_csv_reader = csv.reader(data)
            if filename != "data/dataset1_Python+P7.csv":
                next(shares_csv_reader)
            
            next(shares_csv_reader)
            shares_list = []
            for row in shares_csv_reader:
                share = (
                    row[0],
                    int(float(row[1])*100),
                    float(float(row[1]) * float(row[2]) /100)
                )
                shares_list.append(share)
            return shares_list
        
    except FileNotFoundError:
        print(f"\nNo such file '{filename}' or directory. Please try again.\n")
        time.sleep(1)
        sys.exit()
        
def sacADos(shares_list):
    max_inv = int(MAX_INVEST)     # capacity
    shares_total = len(shares_list)
    cost = []       # weights
    profits = []     # values
    
    for share in shares_list:
        cost.append(share[1])
        profits.append(share[2])
        
    # Profit optimal
    sa = [[0 for x in range(max_inv + 1)] for x in range(shares_total + 1)]
    
    for i in range(1, shares_total + 1):
        action = shares_list[i - 1]
        profit = action[2]
        price = action[1]
        
        for w in range(1, max_inv + 1):
            if price <= 0:
                sa[i][w] = sa[i-1][w]
                continue
            if cost[i-1] <= w:
                
                sa[i][w] = max(sa[i-1][w], profit + sa[i-1][w - price])
                
            else:
                sa[i][w] = sa[i-1][w]
                
     # Profit optimal combination
    best_combo = []
    
    while max_inv >= 0 and shares_total > 0:
        if cost[shares_total - 1] <= 0:
            shares_total -= 1
            continue
        if sa[shares_total][max_inv] == \
            sa[shares_total-1][max_inv - cost[shares_total-1]] + profits[shares_total-1]:

            best_combo.append(shares_list[shares_total-1])
            max_inv -= cost[shares_total-1]

        shares_total -= 1

    return best_combo


if __name__ == "__main__":
    main()