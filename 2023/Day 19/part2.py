file = open("input.txt", "r")
lines = file.read().split(sep="\n")

counter = 0

workflows = dict()

while lines[counter] != "":
    line = lines[counter]
    name, rules = line.split("{")
    rules = rules[:-1].split(",")
    workflows[name] = dict()
    for rule in rules:
        try:
            criteria, result = rule.split(":")
        except ValueError:
            result = rule
            criteria = "default"
        workflows[name][criteria] = result
    counter += 1
print(workflows)


def branch_out(workflow, valid_criterias, ratings):
    for criteria, result in workflow.items():

        new_ratings = ratings.copy()
        if criteria != 'default':
            category, comparison, number = criteria[0], criteria[1], int(criteria[2:])

            if comparison == '<':
                return new_ratings[category]
            elif comparison == '>':
                return part[category] > number
            elif comparison == '=':
                return part[category] == number


        if result == 'A':
            print(valid_criterias + [criteria])
        elif result == 'R':
            pass
            # print(valid_criterias)
        else:
            branch_out(workflows[result], valid_criterias + [criteria], new_ratings)


branch_out(workflows["in"], [], {'x': [(0, 4000)], 'm': (0, 4000), 'a': 4000, 's': 4000})
