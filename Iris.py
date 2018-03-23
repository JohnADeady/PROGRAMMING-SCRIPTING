# John Deady,2018-01-03
# Iris Dat Set



with open(".vscode/iris.data.csv") as x:
    for line in x:
        print(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3])
