# Mission 3: Understand the operating system

## Task 3.1
| Information | What it tells you | Observation |
|---|---|---|
| OS / system details | Which OS, version and kernel the computer runs | macOS [version from sw_vers], Darwin, [arm64 or x86_64] |
| Current account | Which user account is logged in | [redacted] |
| Storage | Total, used and free disk space | Size [x], Used [x], Available [x] |
| System activity | Snapshot of CPU, memory and busiest processes | CPU [x]% in use |

## Task 3.2
- Process: a program that is currently running.
- PID: a unique number the OS gives each running process so it can identify and manage it.
- Two examples: launchd (1923, background system process) and Terminal (TextEdit).

## Task 3.3
- Absolute path: full path from the root /, works from anywhere. Example: /Users/[redacted]/digital-detective-8413/mission-02-terminal
- Relative path: path from where I am now. Example: mission-02-terminal/terminal-practice
- notes.txt permissions are -rw-r--r--. The owner has rw-, so the owner can read and write but not execute.

## Task 3.4
| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Decides which programs run and for how long | Brave and Spotify running together |
| Memory management | Gives each program its own RAM and keeps them separate | One app crashing doesn't freeze others |
| Device management | Controls hardware through drivers | Keyboard input appearing on screen |
| File management | Organises how files are stored and found | Folders in Finder |
| User interface / shell | How I interact with the computer | Desktop and Terminal |
| Security and permissions | Controls who can read, write or run what | The rw- letters on a file
