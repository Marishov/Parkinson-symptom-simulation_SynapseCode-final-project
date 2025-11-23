import random

def simulate_symptom(base, growth, noise_level, steps):
    values = []
    current = base
    for _ in range(steps):
        drift = growth
        noise = random.uniform(-noise_level, noise_level)
        current = max(0.0, current + drift + noise)
        values.append(round(current, 3))
    return values

def mean_list(xs):
    if len(xs) == 0:
        return 0.0
    total = 0.0
    for x in xs:
        total += x
    return total / len(xs)

def compute_age_factor(age):
    if age < 50:
        return 0.9
    if age < 65:
        return 1.0
    return 1.15

def compute_sleep_factor(hours):
    if hours >= 7:
        return 0.9
    if hours >= 5:
        return 1.0
    return 1.1

def combine_scores(tremor_mean, rig_mean, slow_mean, symptom_score, age_factor, sleep_factor, weights):
    weighted = tremor_mean * weights[0] + rig_mean * weights[1] + slow_mean * weights[2]
    symptom_scaled = (symptom_score / 10.0) * 100.0
    base = (weighted + symptom_scaled) / 2.0
    adjusted = base * age_factor * sleep_factor
    prob = max(0.0, min(adjusted, 100.0))
    return prob

def format_list(xs):
    return "[" + ", ".join(str(v) for v in xs) + "]"

def main():
    output_lines = []

    output_lines.append("Parkinsons mixed symptom simulation")
    age = float(input("Enter age in years: "))
    sleep_hours = float(input("Enter typical sleep hours per night: "))
    symptom_score = float(input("Self reported symptom score from 0 to 10 where 0 none 10 severe: "))
    steps = 10

    tremor_base = 5.0
    rigidity_base = 3.0
    slowness_base = 4.0

    tremor_growth = 0.3
    rigidity_growth = 0.2
    slowness_growth = 0.25

    noise_level = 0.6

    tremor = simulate_symptom(tremor_base, tremor_growth, noise_level, steps)
    rigidity = simulate_symptom(rigidity_base, rigidity_growth, noise_level, steps)
    slowness = simulate_symptom(slowness_base, slowness_growth, noise_level, steps)

    tremor_mean = mean_list(tremor)
    rig_mean = mean_list(rigidity)
    slow_mean = mean_list(slowness)

    age_factor = compute_age_factor(age)
    sleep_factor = compute_sleep_factor(sleep_hours)

    weights = [0.4, 0.3, 0.3]

    probability = combine_scores(tremor_mean, rig_mean, slow_mean, symptom_score, age_factor, sleep_factor, weights)

    output_lines.append("")
    output_lines.append("Simulated symptom curves over " + str(steps) + " steps")
    output_lines.append("Tremor: " + format_list(tremor))
    output_lines.append("Rigidity: " + format_list(rigidity))
    output_lines.append("Slowness: " + format_list(slowness))
    output_lines.append("")
    output_lines.append("Mean tremor: " + str(round(tremor_mean, 3)))
    output_lines.append("Mean rigidity: " + str(round(rig_mean, 3)))
    output_lines.append("Mean slowness: " + str(round(slow_mean, 3)))
    output_lines.append("Age factor: " + str(round(age_factor, 2)))
    output_lines.append("Sleep factor: " + str(round(sleep_factor, 2)))
    output_lines.append("Final estimated probability of noticeable Parkinsons like progression in this simple model: " + str(round(probability, 2)) + "%")
    output_lines.append("")
    output_lines.append("Note this is a simple educational simulation not a medical diagnosis")

    # print to terminal
    for line in output_lines:
        print(line)

    # save to results_examples.txt
    with open("results_examples.txt", "a") as f:
        
     f.write("=== New Simulation ===\n")
     f.write(f"Inputs:\n")
     f.write(f"Age: {age}\n")
     f.write(f"Sleep hours: {sleep_hours}\n")
     f.write(f"Self-reported symptom score: {symptom_score}\n\n")
     f.write("Simulated symptom curves:\n")
     f.write(f"Tremor: {format_list(tremor)}\n")
     f.write(f"Rigidity: {format_list(rigidity)}\n")
     f.write(f"Slowness: {format_list(slowness)}\n\n")
     f.write("Mean values:\n")
     f.write(f"Tremor: {round(tremor_mean,3)}\n")
     f.write(f"Rigidity: {round(rig_mean,3)}\n")
     f.write(f"Slowness: {round(slow_mean,3)}\n")
     f.write(f"Age factor: {round(age_factor,2)}\n")
     f.write(f"Sleep factor: {round(sleep_factor,2)}\n")
     f.write(f"Estimated probability of progression: {round(probability,2)}%\n")
     f.write("Note: simple educational simulation, not medical advice\n\n")



    print("")
    print("Simulated symptom curves over", steps, "steps")
    print("Tremor:", format_list(tremor))
    print("Rigidity:", format_list(rigidity))
    print("Slowness:", format_list(slowness))
    print("")
    print("Mean tremor:", round(tremor_mean, 3))
    print("Mean rigidity:", round(rig_mean, 3))
    print("Mean slowness:", round(slow_mean, 3))
    print("Age factor:", round(age_factor, 2))
    print("Sleep factor:", round(sleep_factor, 2))
    print(
        "Final estimated probability of noticeable Parkinsons-like progression in this simple model:",
        str(round(probability, 2)) + "%"
    )
    print("")
    print("Note: this is a simple educational simulation, not a medical diagnosis.")

if __name__ == "__main__":
    main()
