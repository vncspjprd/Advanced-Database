def convert_currency(dollar):
    peso = dollar * 57.17
    yen = dollar * 146.67
    return peso, yen

numbers = input("Enter currency in ($): ")
dollar_values = [float(val.strip()) for val in numbers.split(",")]

print("Dollar($) \t Phil Peso(P) \t Jpn Yen (Y)")
for convert in dollar_values:
    peso, yen = convert_currency(convert)
    print(f"{convert}\t\t{peso:.2f}\t\t{yen:.2f}")