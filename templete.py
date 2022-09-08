### This is to create the the folders required
import os

# Directories needed
dirs = [
    os.path.join("1 Week Preparation Kit", "Mock Test"),
    os.path.join("1 Month Preparation Kit","Mock Test"),
    "Python",
    "Alogrithms",
    "Data Structures",
    "Mathematics",
    "SQL",
    "30 Days of Code",
    "10 Days of Statistics"
]

# Create the directories and write a .gitkeep file inside each directory (we cannot commit an empty directory in git)
for dir in dirs:
    os.makedirs(dir , exist_ok=True)
    with open(os.path.join(dir , ".gitkeep"),"w") as f: # writing "w" for specifing that we want to write the file also
        pass
