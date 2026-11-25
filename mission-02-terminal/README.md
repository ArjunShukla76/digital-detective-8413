# Mission 2: Become comfortable with the Terminal

## 1. Task / objective
Use the command line to inspect folders, create and manage practice files, understand flags and pipes, and explain what a package manager does.

## 2. Work completed

### Task 2.1: Basic Terminal operations

| Operation / command | What it does | What I observed |
|---|---|---|
| `pwd` | Prints the full path of the folder I'm in | It showed the path ending in `terminal-practice` (username part [redacted]) |
| `ls` | Lists the files and folders in the current location | Empty at first, then it showed my files once I created them |
| `ls -l` | Lists in detailed format: permissions, owner, size, date | Each file on its own line with extra details |
| `cd ..` | Moves to the parent folder | `pwd` showed the path without `terminal-practice` |
| `mkdir terminal-practice` | Creates a new folder | The new folder appeared in `ls` |
| `touch notes.txt` | Creates an empty file | `notes.txt` appeared in `ls` with size 0 |
| `cp notes.txt copy.txt` | Copies a file under a new name | Both files existed afterwards |
| `mv copy.txt renamed.txt` | Moves or renames a file | `copy.txt` disappeared and `renamed.txt` appeared |
| `cat notes.txt` | Displays a file's contents | Nothing at first because the file was empty |

### Task 2.2: Practising file changes
Inside `terminal-practice` I created `notes.txt`, wrote "line one" with `>`, added "line two" with `>>`, and checked with `cat` that both lines were there. I made a backup with `cp` and renamed it with `mv`.

- **Replacing vs adding to the end:** `>` replaces the whole contents of a file, while `>>` adds to the end and keeps the old lines.
- **Copying vs moving:** copying makes a duplicate and the original stays. Moving changes the name or location, so the original is gone from its old place.
- **What `pwd` provides:** the full path of my current folder, so I know where my commands will act.
- **Why listing is useful:** it shows which files and folders exist, and with `-l` it also shows permissions, sizes and dates.

### Task 2.3: Flags and pipes
I ran `ls`, `ls -l` and `ls -lah`. Plain `ls` shows only names. `-l` gives the detailed format, `-a` includes hidden files (names starting with `.`), and `-h` shows sizes in readable units like KB instead of bytes.

I also ran `ls -lah | head -5`. The pipe `|` takes the output of the command on its left and gives it as input to the command on its right. Here `ls -lah` produces the full detailed listing and `head -5` keeps only the first five lines.

### Task 2.4: Package managers
Homebrew is installed on my Mac. `brew --version` showed Homebrew 7.0.6 and `brew list` showed the packages it manages, such as `git` and `ffmpeg`. Many of the others are libraries that those tools depend on. I did not install or uninstall anything.

A package manager installs, updates and removes software from one command, and it also installs the other libraries that software needs. That saves me from finding downloads by hand and keeps everything updated in one place.

## 3. Commands / tools used
- `pwd`: prints the current folder's full path.
- `ls`, `ls -l`, `ls -lah`: list files, with flags for detail, hidden files and readable sizes.
- `cd`: changes folder.
- `mkdir`: creates a folder.
- `touch`: creates an empty file.
- `cp`: copies a file.
- `mv`: moves or renames a file.
- `cat`: shows a file's contents.
- `echo` with `>` and `>>`: writes text to a file, replacing it or adding to it.
- `head`: shows the first lines of its input.
- `|` (pipe): sends one command's output into another.
- `brew --version`, `brew list`: show the Homebrew version and installed packages.
- `git add`, `git commit`, `git push`: save and publish the mission.
- Tools: Terminal, TextEdit.

## 4. My understanding
The Terminal lets me work with files by typing commands instead of clicking. Each command does one small job, and flags change how it behaves. Pipes let me combine small commands, so the output of one becomes the input of the next. Before running a command I try to predict what it will do, then check the result.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-02-terminal/README.md`
- `mission-02-terminal/terminal-practice/` (contains `notes.txt`, `renamed.txt` and `backup-notes.txt`)

## 8. Commit details
- Commit message: "Complete Terminal and file management mission"
- Pushed to GitHub and verified:
