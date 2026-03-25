from prettytable import PrettyTable 
table = PrettyTable() 

table.field_names = ["Pokemon","Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Pikachu","Electric"])
table.add_row(["Pikachu","Electric"])
table.add_row(["Charmender","Fire"])

print(table)

table.add_column("Power",[234,23211,232,213])

print(table)

table.align = "l"

print(table)