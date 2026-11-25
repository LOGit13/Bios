import os
import runpy


PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TASKS = range(4, 10)


def main():
    print("Biosignalverarbeitung: Aufgaben 4 bis 9")
    print("Plots schliessen, um mit der naechsten Aufgabe fortzufahren.\n")

    for task_number in TASKS:
        task_directory = os.path.join(
            PROJECT_DIRECTORY, "Aufgabe", f"Aufgabe{task_number}"
        )
        task_script = os.path.join(
            task_directory, f"Aufgabe{task_number}.py"
        )
        if not os.path.isfile(task_script):
            raise FileNotFoundError(f"Aufgabenskript nicht gefunden: {task_script}")

        print(f"\n--- Aufgabe {task_number} ---")
        runpy.run_path(task_script, run_name="__main__")

    print("\nAlle Aufgaben wurden ausgefuehrt.")


if __name__ == "__main__":
    main()
