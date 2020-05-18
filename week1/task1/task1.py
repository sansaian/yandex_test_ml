import pandas
import operator


def main():
    data = pandas.read_csv('../titanic.csv', index_col='PassengerId')

    # how match male and fenale on bord ?
    count_sex = data['Sex'].value_counts()
    print(count_sex['male'], end=" ")
    print(count_sex['female'])

    # how many people survived? percentage response
    survived = data.groupby('Survived').size() / len(data)
    print(round(survived[1] * 100, 2))

    # What is the proportion of first-class passengers among all passengers?
    proc_first_class = data.groupby('Pclass').size() / len(data)
    print(round(proc_first_class[1] * 100, 2))

    # How old were the passengers? Calculate the average and median age of passengers.
    average_age = data["Age"].mean()
    median_age = data["Age"].median()
    print(round(average_age, 2), end=" ")
    print(median_age)

    # Count the Pearson correlation between the SibSp and Parch traits.
    sisp = data['SibSp']
    parch = data['Parch']
    corr = sisp.corr(parch, method='pearson')
    print(round(corr, 2))
    # What is the most popular female name in core
    i = 0
    # res = data['Name']
    list_name = []
    for name_row in data['Name']:
        is_woman = ("Miss." in name_row) or ("Mrs." in name_row)
        if is_woman:
            index_brace = name_row.find("(")
            if index_brace != -1:
                name_row = name_row[index_brace + 1:]
                index_space = name_row.find(" ")
                name_row = name_row[:index_space]
                list_name.append(name_row)
            else:
                index_point = name_row.find(".")
                name_row = name_row[index_point + 2:]
                index_space = name_row.find(" ")
                name_row = name_row[:index_space]
                list_name.append(name_row)
            i += 1

    dict_name = {}
    for name in list_name:
        value = dict_name.get(name)
        if value is None:
            dict_name[name] = 1
        else:
            dict_name[name] = value + 1

    field, value = max(dict_name.items(), key=operator.itemgetter(1))
    print(field)


if __name__ == "__main__":
    main()
