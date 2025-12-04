import sys

def compare_files(file1_path, file2_path):
    """
    Compare two text files line by line and print differences.
    """
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    max_lines = max(len(lines1), len(lines2))
    differences = 0

    print(f"\nComparing '{file1_path}' and '{file2_path}'...\n")

    for i in range(max_lines):
        line1 = lines1[i].strip() if i < len(lines1) else "<no line>"
        line2 = lines2[i].strip() if i < len(lines2) else "<no line>"

        if line1 != line2:
            differences += 1
            print(f"Line {i+1}:")
            print(f"  File 1 → {line1}")
            print(f"  File 2 → {line2}")
            print("-" * 50)

    if differences == 0:
        print("✅ The two files are identical.")
    else:
        print(f"\n⚠️ Found {differences} difference(s).")


# Example usage
if __name__ == "__main__":
    if len(sys.argv) !=3:
        print("Usage: python alex-comparison-script.py <file1> <file2>")
        sys.exit(1)
    file1 = sys.argv[1]
    file2 = sys.argv[2]


    compare_files(file1, file2)
