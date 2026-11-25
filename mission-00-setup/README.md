# Mission 0: Create your GitHub workspace

## 1. Task / objective
Create a correctly named public GitHub repository and set up a clear folder structure, with one folder per mission, for the Digital Detective assignment.

## 2. Work completed
- Created the project folder and repository named `digital-detective-8413`.
- Created 9 mission folders (`mission-00-setup` to `mission-08-final-report`) and an `evidence` folder.
- Created a root `README.md` and a `README.md` in every mission folder.
- Created an empty `number_converter.py` in `mission-05-numbers-data`.
- Created a public repository on GitHub with the same name and pushed the initial files.

## 3. Commands / tools used
Tools checked: Python 3 version: 3.9.6, Git version: 2.55.0

- `python3 --version`, `git --version`: show the installed versions, so I know the tools are available.
- `cd`: moves into a folder. `pwd`: prints the full path of the current folder.
- `ls`, `ls -la`: list the files and folders. The `-la` flags add hidden files and details, including whether each item is a folder (`d`) or a file (`-`).
- `mkdir`: creates folders.
- `touch`: creates an empty file.
- `rm -r`: deletes a folder and its contents. I used it only after checking that the folder held nothing important.
- `textutil`, `mv`: `textutil` converted a rich-text file to plain text, and `mv` renamed it.
- `git init`: starts a Git repository in the folder.
- `git add`: stages files for the next commit.
- `git commit`: saves a snapshot of the staged files with a message.
- `git branch -M main`: renames the current branch to `main`.
- `git remote add origin`: links the local folder to the GitHub repository.
- `git push`: uploads the commits to GitHub.
- Tools: Terminal, TextEdit, GitHub website.

## 4. My understanding
A repository is a project folder that Git tracks. It stores the files and the history of every saved change, so I can go back to earlier versions and publish the project on GitHub.

The folders are organised by mission so each part of the assignment has its own place. That keeps the work easy to find and lets each mission be committed separately, which makes the history clear for anyone reviewing it.

## 5. Difficulties faced
- `README.md` was created as a folder instead of a file.
- TextEdit showed the error "cannot open files in the folder format".
- `rmdir` refused to delete the folder and said "directory not empty".
- TextEdit saved my README as `README.rtf` instead of `README.md`.

## 6. How I resolved them
- The folder error happened because `mkdir` makes folders, while `touch` makes files. I used `ls -la` to see that `README.md` started with `d`, which means folder.
- `rmdir` only removes empty folders, so it refused. I looked inside with `ls -la README.md`, saw only empty files and an empty folder, and then removed it with `rm -r README.md`. Then I created a real file with `touch README.md`.
- The `.rtf` file happened because TextEdit defaults to rich text. I used `textutil -convert txt` to make plain text, renamed it to `README.md` with `mv`, and removed the `.rtf` file.

## 7. Evidence / files
- `README.md`
- `mission-00-setup/README.md`
- Folders: `mission-01-computer-basics` to `mission-08-final-report`, `evidence`
- `mission-05-numbers-data/number_converter.py`

## 8. Commit details
- Commit message: "Set up Digital Detective mission structure"
- I pushed the commit to GitHub and confirmed that the folders and commit are visible there.