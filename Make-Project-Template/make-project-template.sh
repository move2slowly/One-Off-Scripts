#!/bin/bash

# Get the project name from the user
read -p "Enter your project name: " project_name

# Create the main project directory
mkdir "$project_name"

# Move into the project directory
cd "$project_name" || exit

# Create subdirectories
mkdir src docs tests

# Create basic template files
touch README.md
touch .gitignore
touch src/main.py

# Add basic content to README.md
echo "# $project_name" > README.md
echo "This is the $project_name project." >> README.md

echo "Project '$project_name' has been created successfully with the following structure:"
echo "$project_name/"
echo "├── README.md"
echo "├── .gitignore"
echo "├── src/"
echo "│   └── main.py"
echo "├── docs/"
echo "└── tests/"

exit 0

