from config import tp_percentage, sl_percentage, file_path
from config import position_volume

static_balance = position_volume
dynamic_balance = position_volume

def calculate_balance(closed_with_TP):
    global static_balance
    global dynamic_balance
    global tp_percentage
    global sl_percentage

    if closed_with_TP:
        dynamic_balance = dynamic_balance * (1 + tp_percentage)
        static_balance += position_volume * tp_percentage
    else:
        dynamic_balance = dynamic_balance * (1 - sl_percentage)
        static_balance -= position_volume * sl_percentage

def analyze_results(file_path):

    total_trades = 0
    correct_trades = 0
    incorrect_trades = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:
        date, result, prediction = line.strip().split(',')

        total_trades += 1
        if result == prediction:
            correct_trades += 1
            calculate_balance(True)
            
        else:
            incorrect_trades += 1
            calculate_balance(False)

    print(f"Toplam işlemler: {total_trades}")
    print(f"Doğru tahminler: {correct_trades}")
    print(f"Yanlış tahminler: {incorrect_trades}")
    accuracy = correct_trades / total_trades * 100 if total_trades > 0 else 0
    print(f"Doğruluk oranı: {accuracy:.2f}%")
    print(f"Dinamik bakiye: {round(dynamic_balance, 2)}")
    print(f"Statik bakiye: {round(static_balance, 2)}")
    
analyze_results(file_path)
