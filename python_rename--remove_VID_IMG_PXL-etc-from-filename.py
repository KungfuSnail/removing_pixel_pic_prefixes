import os
import sys


def rename_files(directory):
    os.chdir(directory)
    # List all files in the provided directory
    for filename in os.listdir():
        # Check if the file name starts with the specified prefixes
        if filename.startswith("VID_") or filename.startswith("PXL_") or filename.startswith("IMG_"):
            # Generate the new file name by removing the prefix
            new_filename = filename.split('_', 1)[1]
            # Create full path for old and new file names
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_filename}'")

# Example usage:
# Replace '/path/to/your/directory' with the path to the directory containing your files
rename_files(sys.argv[1])
