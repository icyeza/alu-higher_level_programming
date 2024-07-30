#!/usr/bin/python3
# display Content-Lengthfter editing, stage the changes
git add 0-body_size.sh

# Commit the changes
git commit -m "Updated 0-body_size.sh"

# Push the changes to the remote repository
git push origin <branch-name>  # Replace <branch-name> with your branch name

curl -sI "$1" | grep 'Content-Length' | cut -d " " -f2
