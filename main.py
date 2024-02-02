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
        else:
            incorrect_trades += 1

    print(f"Toplam işlemler: {total_trades}")
    print(f"Doğru tahminler: {correct_trades}")
    print(f"Yanlış tahminler: {incorrect_trades}")
    accuracy = correct_trades / total_trades * 100 if total_trades > 0 else 0
    print(f"Doğruluk oranı: {accuracy:.2f}%")

file_path = "C:\\Users\\user\\OneDrive\\Masaüstü\\Projects\\github repos\\SageBot\\data\\sagebot_result.csv"

analyze_results(file_path)
