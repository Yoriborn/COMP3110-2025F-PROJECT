import os
import subprocess

DATABASE_DIR = "database"
COMPARISON_SCRIPT = "file_comparison/alex-comparison-script.py"
OUTPUT_DIR = "comparison_output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def is_v1_file(filename):
    return filename.endswith("_V1.c") or filename.endswith("_V1.h") or filename.endswith("_V1.s")

def get_v2_filename(v1_filename):
    return v1_filename.replace("_V1", "_V2")

def main():
    all_files = sorted(os.listdir(DATABASE_DIR))
    v1_files = [f for f in all_files if is_v1_file(f)]

    print(f"Found {len(v1_files)} V1 files. Running comparisons...\n")

    for v1 in v1_files:
        v2 = get_v2_filename(v1)

        v1_path = os.path.join(DATABASE_DIR, v1)
        v2_path = os.path.join(DATABASE_DIR, v2)

        if not os.path.exists(v2_path):
            print(f"Missing V2 for {v1}, skipping...")
            continue

        print(f"Comparing: {v1} <-> {v2}")

        out_name = v1.replace("_V1", "") + "_comparison.txt"
        out_path = os.path.join(OUTPUT_DIR, out_name)

        with open(out_path, "w", encoding="utf-8") as out:
            subprocess.run(
                ["python", COMPARISON_SCRIPT, v1_path, v2_path],
                stdout=out,
                stderr=out,
                text=True
            )

        print(f"Saved → {out_path}\n")

    print("All comparisons complete.")

if __name__ == "__main__":
    main()
