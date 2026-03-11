"""Session 9 student template: Experiment pipeline + plotting preparation.

This script imports Session 8 modules and Session 9 evaluation helpers to
run a systematic parameter sweep, compute accuracy, and store the results.
"""

import os
import sys

import pandas as pd

# Ensure the root directory is in sys.path so imports work correctly
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from session9.iris_eval import accuracy_score, train_test_split
from session8.iris_session8_utils import load_iris_csv
from session8.iris_session8_models import NumpyCentroidClassifier


def run_experiment(test_size=0.2, seed=1, metric="l2"):
    """Run one experiment and return the accuracy.
    
    Args:
        test_size (float): Proportion of data for testing.
        seed (int): Random seed for reproducibility.
        metric (str): Distance metric to use ('l1' or 'l2').
        
    Returns:
        float: Accuracy score.
    """
    # Load arrays produced in Session 8 style
    X, y = load_iris_csv("iris.csv", skip_header=1)

    # Split into train/test using our evaluation helper
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, seed=seed)

    # Instantiate the classifier, fit it, and predict
    model = NumpyCentroidClassifier(metric=metric)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Calculate and return accuracy
    acc = accuracy_score(y_test, y_pred)
    return acc


def run_single_setting_sweep(metrics, seeds, test_size=0.2):
    """Loop over metrics and seeds for a single test_size, printing outputs."""
    print(f"--- Sweep: test_size={test_size} ---")
    for metric in metrics:
        for seed in seeds:
            acc = run_experiment(test_size=test_size, seed=seed, metric=metric)
            print(f"metric={metric} | seed={seed} | acc={acc:.3f}")


def run_multiple_trials(metrics, test_sizes, num_trials):
    """Run repeated trials and return a list of dictionary results.
    
    Args:
        metrics (list): List of metric strings to try.
        test_sizes (list): List of test size floats.
        num_trials (int): Number of random seeds (trials) to run for each setting.
        
    Returns:
        list: A list of dicts containing the results.
    """
    results_list = []

    for metric in metrics:
        for test_size in test_sizes:
            print(f"\n[Config] metric={metric} | test_size={test_size}")
            for trial in range(1, num_trials + 1):
                seed = trial  # use trial number as seed
                acc = run_experiment(test_size=test_size, seed=seed, metric=metric)
                
                print(f"  Trial {trial}/{num_trials} | seed={seed} | acc={acc:.3f}")

                run_data = {
                    "metric": metric,
                    "test_size": test_size,
                    "trial": trial,
                    "seed": seed,
                    "accuracy": acc
                }
                results_list.append(run_data)

    return results_list


def main():
    print("=== Student Label ===")
    student_id = "YOUR_ID_HERE"
    full_name = "YOUR_FULL_NAME_HERE"
    print("Student ID:", student_id)
    print("Full Name:", full_name)

    # You can test a single run or a small sweep:
    # run_single_setting_sweep(["l1", "l2"], [1, 2, 3], 0.2)

    # Run the full experiment grid
    all_results = run_multiple_trials(
        metrics=["l1", "l2"],
        test_sizes=[0.2, 0.3, 0.4],
        num_trials=10,
    )

    # Convert results list into a Pandas DataFrame
    results_df = pd.DataFrame(all_results)
    
    print("\n--- Raw Results Preview ---")
    print(results_df.head())

    # Save DataFrame to Excel
    output_filename = "iris_experiment_results.xlsx"
    try:
        results_df.to_excel(output_filename, index=False)
        print(f"\nSaved: {output_filename}")
    except Exception as exc:
        print(f"\n[ERROR] Failed to save Excel file: {exc}. Make sure it is not open in another program.")
        
    # Optional: Save to CSV as well
    csv_filename = "iris_experiment_results.csv"
    results_df.to_csv(csv_filename, index=False)
    print(f"Saved: {csv_filename}")


if __name__ == "__main__":
    main()
