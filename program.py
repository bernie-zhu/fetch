import csv
import sys
from datetime import datetime

def main(points_to_spend):
    transactions = []
    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            payer = row[0]
            points = int(row[1])
            timestamp = datetime.fromisoformat(row[2][:-1] + '+00:00')
            transactions.append((payer, points, timestamp))

    transactions.sort(key=lambda x:x[2])

    balances = {}
    for payer, points, timestamp in transactions:
        if payer not in balances:
            balances[payer] = 0
        balances[payer] += points

    for payer, points, timestamp in transactions:
        #print("Points Left: ", points_to_spend)
        if points_to_spend <= 0:
            break

        if points >= points_to_spend:
            #print("Subtracting From: ", payer, " This much: ", points_to_spend)
            balances[payer] -= points_to_spend
            points_to_spend -= points_to_spend
        else:
            #print("Subtracting From: ", payer, " This much: ", points)
            points_to_spend -= points
            balances[payer] -= points

    return balances

if __name__ == '__main__':
    points_to_spend = int(sys.argv[1])
    balances = main(points_to_spend)
    print(balances)
