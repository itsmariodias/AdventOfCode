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
# print(workflows)

counter += 1
parts = []
while lines[counter] != "":
    line = lines[counter]
    parts.append({x.split("=")[0]: int(x.split("=")[1]) for x in line[1:-1].split(",")})
    counter += 1
# print(parts)


def analyze(criteria, part):
    if criteria == 'default':
        return True

    category, comparison, number = criteria[0], criteria[1], int(criteria[2:])

    if comparison == '<':
        return part[category] < number
    elif comparison == '>':
        return part[category] > number
    elif comparison == '=':
        return part[category] == number

    return False


def get_result(rules, part):
    for criteria, result in rules.items():
        if analyze(criteria, part):
            return result


statuses = ['A', 'R']

total = 0

for part in parts:
    current_workflow = workflows["in"]
    while True:
        result = get_result(current_workflow, part)
        if result not in statuses:
            current_workflow = workflows[result]
        elif result == 'A':
            total += sum(part.values())
            break
        else:
            break

print(total)
