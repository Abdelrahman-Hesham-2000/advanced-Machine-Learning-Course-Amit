import os
import random

# Define the directory path
directory = r"C:\Users\Kimo Store\Desktop\AMIT\advanced-Machine-Learning-Course-Amit\materials\python_for_ML\tasks\tasks_2\directory"

# Step 1: Create the directory if it does not exist
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directory created: {directory}")
else:
    print(f"Directory already exists: {directory}")

# Step 2: Create 20 files in the directory
for i in range(1,21):
    file_path = os.path.join(directory, f"file_{i}.txt")  
    open(file_path, 'w') 

# Step 3: List all files in the directory
files = os.listdir(directory)
print(f"Files in the directory: {files}")

# Step 4: Randomly select 10 unique files to delete
selected_files = random.sample(files, k=10)  # Use random.sample for unique selections

# Step 5: Delete the selected files
for file_name in selected_files:
    file_path = os.path.join(directory, file_name)  # Construct full file path
    os.remove(file_path)  # Delete the file
    print(f"File deleted: {file_path}")

# Step 6: List remaining files
remaining_files = os.listdir(directory)
print(f"Remaining files in the directory: {remaining_files}")
    