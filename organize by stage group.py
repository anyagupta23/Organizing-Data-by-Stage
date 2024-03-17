import os
import pandas as pd
import shutil

# Load the spreadsheet into a pandas DataFrame
spreadsheet_path = ''  # Update with your spreadsheet path
df = pd.read_csv(spreadsheet_path)  # Use read_csv for CSV files

# Path to the main folder containing patient subfolders
main_folder = ''  # Update with your main folder path

def organize_folders(subject, group):
    subject_folder_path = os.path.join(main_folder, subject)

    # Check if the patient folder exists
    if not os.path.exists(subject_folder_path):
        return

    print(f"Processing patient: {subject}")
    print(f"Group: {group}")

    # Create folder for the group
    group_folder_path = os.path.join(subject_folder_path, group)
    os.makedirs(group_folder_path, exist_ok=True)
    print(f"Created folder for group: {group_folder_path}")

    # Move all files for the current subject to the group folder
    for filename in os.listdir(subject_folder_path):
        file_path = os.path.join(subject_folder_path, filename)

        # Skip if it's a directory (subfolder)
        if os.path.isdir(file_path):
            continue

        # Move the file into the group folder
        shutil.move(file_path, os.path.join(group_folder_path, filename))
        print(f"Moved file: {file_path} -> {group_folder_path}")

# Iterate through the DataFrame rows
for index, row in df.iterrows():
    subject = str(row['Subject'])
    group = str(row['Group'])

    # Organize folders for the current subject and group
    organize_folders(subject, group)
