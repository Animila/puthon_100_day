from prettytable import PrettyTable

table = PrettyTable()

# столбцы (название поля, список строк)

table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])

#выравнимание текста слева
table.align = 'l'

print(table)