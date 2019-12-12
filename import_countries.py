def import_countries_and_capitals():
    countries = []
    capitals = []
    i = 0
    for line in open('/home/matthew/codecool/hangman/countries_and_capitals.txt'):
        separator = ' | '
        line = line.split(separator)
        for i in range(len(line)):
            if i % 2 == 0:
                countries.append(line[i])
            else:
                capital = ''
                x = line[i]
                for k in range(len(x)):
                    if x[k] != '\n':
                        capital = capital + x[k]
                    else:
                        break
                capitals.append(capital)
    return countries, capitals