#Iron Valhal Fitness

import csv
from datetime import date
from pathlib import Path

#Setting up some paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True) #create data if it doesnt exist

WORKOUT_LOG = DATA_DIR / "workout.log"

def get_today():
    """Return today's date as YYYY-MM-DD"""
    return date.today().isoformat()

def greeting():
    print("=" * 40)
    print("  WELCOME TO IRON VALHALLA v0.1")
    print("=" * 40)
    print(f"date: {get_today()}")
    print("log your workout and earn your place in Valhal. \n")

def input_exercise():
    """
    Ask the user to enter exercises one by one.
    Returns a list of dictionaries: [{name, sets, reps, weight}, ...]
    """
    exercises = []
    while True:
        try:
            sets = int(input(" Sets:"))
            reps = int(input(" Reps:"))
            weight = float(input(" Weight:"))
            break
        except ValueError:
            print("Please enter numbers for sets/reps/weight.")

    exercises.append({
        "Name": name,
        "Sets": sets,
        "Reps": reps,
        "Weight": weight
       })

    print("Exercises added.\n")

    return exercises

def calculate_total_volume(exercises):
    """Total volume = sum(sets * reps * weight)"""
    total = 0
    for ex in exercises:
        total += ex["sets"] * ex["reps"] * ex["weight"]
    return total

def save_workout(exercises):
    """Append today's workout to workout.csv"""
    if not exercises:
        print("No exercises added. Nothing to save")
        return
    #if file is new, write header row
    file_exists = WORKOUT_LOG.exists()

    with WORKOUT_LOG.open(mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "date", "exercise", "sets", "reps", "weight", "volume"
                ])

        today = get_today()
        for ex in exercises:
            volume = ex["sets"] * ex["reps"] * ex["weight"]
            writer.writerow([
                today,
                ex["name"],
                ex["sets"],
                ex["reps"],
                ex["weight"],
                volume
            ])

    print(f"\nWorkout saved to {WORKOUT_LOG}")

def main():
    greeting()
    exercises = input_exercise()

    if not exercises:
        print("\nNo workout logged today. The gates of Valhal remained closed... for now...")
        return

    total_volume = calculate_total_volume(exercises)

    print("\n~~~~Workout Summary~~~~")
    for ex in exercises:
        volume = ex["sets"] * ex["reps"] * ex["weight"]
        print(f"- {ex['name']}: {ex['sets']} x {ex['reps']} x {ex['weight']} lbs "
              f" {volume:.1f} lbs volume")

    print(f"Total volume: {total_volume:.1f} lbs lifted upon this day")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    save_workout(exercises)
    print("\nSKAL, Warrior. Another brick in the forge of fate has been laid")

if __name__ == "__main__":

        main()

