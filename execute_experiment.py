# execute_experiment.py
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python execute_experiment.py <username> <jobid>")
        sys.exit(1)

    username = sys.argv[1]
    jobid = sys.argv[2]

    print(f"Username: {username}")
    print(f"Job ID: {jobid}")
    print("success")
