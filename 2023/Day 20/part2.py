import math

file = open("input.txt", "r")
lines = file.read().split(sep="\n")

module_map = {}

pulse_counters = {False: 0, True: 0}

exit_counter = 0

press_list = []

def send_pulse(source: str, module: str, input_pulse: bool):
    global exit_counter
    queue = []

    # Based on data, we need to find out when source modules all output high pulses to vr so that vr will output a
    # low pulse to rx
    if module == "vr" and input_pulse:
        print(f"{source} emits high pulse after {button_presses} presses.")
        press_list.append(button_presses)
        exit_counter += 1

        # Calculate the LCM for these button presses, that when the source modules would all end up sending high
        # pulses to vr
        if exit_counter > 3:
            print(math.lcm(*press_list))
            exit()

    if module not in module_map.keys():
        return queue
    module_info = module_map[module]

    pulse = input_pulse
    if module_info["module_type"] == "%":
        if input_pulse == False:
            module_info["state"] = "off" if module_info["state"] == "on" else "on"
            pulse = True if module_info["state"] == "on" else False

            for destination in module_info["destinations"]:
                pulse_counters[pulse] += 1
                queue.append((module, destination, pulse))
        return queue
    elif module_info["module_type"] == "&":
        module_info["state"][source] = input_pulse

        pulse = True
        if all(module_info["state"].values()):
            pulse = False

    for destination in module_info["destinations"]:
        pulse_counters[pulse] += 1
        queue.append((module, destination, pulse))

    return queue


# register all modules
for line in lines:
    source, destinations = line.split("->")

    source = source.strip()
    module_type = "broadcaster"
    if source != "broadcaster":
        module_type = source[0]
        source = source[1:]

    destination_list = []
    for destination in destinations.split(","):
        destination = destination.strip()
        destination_list.append(destination)

    info = {"destinations": destination_list, "module_type": module_type}

    if module_type == "%":
        info["state"] = "off"
    elif module_type == "&":
        info["state"] = {}

    module_map[source] = info

# Evaluate again to register inputs for conjuction modules
for line in lines:
    source, destinations = line.split("->")

    source = source.strip()
    module_type = "broadcaster"
    if source != "broadcaster":
        module_type = source[0]
        source = source[1:]

    for destination in destinations.split(","):
        destination = destination.strip()
        if destination in module_map.keys() and module_map[destination]["module_type"] == "&":
            module_map[destination]["state"][source] = False

print(module_map)

button_presses = 0

while True:
    button_presses += 1
    queue = [("button", "broadcaster", False)]
    pulse_counters[False] += 1
    while len(queue) > 0:
        # print(queue)
        source, module, pulse = queue.pop(0)
        queue.extend(send_pulse(source, module, pulse))