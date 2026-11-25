# Mission 3: Understand the Operating System

## 1. Task / objective
Learn what an operating system does and review system information, processes, paths, file permissions, and operating system responsibilities.

## 2. Work completed

### Task 3.1: System information
| Information | What it tells you | Observation |
|---|---|---|
| Operating system | OS and version | macOS 26.5 |
| Architecture | Processor architecture | arm64 |
| Current account | Which user account is logged in | [redacted] |
| Storage on `/` | Total, used, and available space | 460Gi total, 19Gi used, 319Gi available; 6% capacity used |
| System activity | Snapshot of processor activity | 3.26% user, 9.5% system, 87.68% idle |

### Task 3.2: Processes and PIDs
A process is a program that is running. A PID is the number the operating system assigns to identify a process. Examples of processes include `launchd`, a background system process, and Terminal, an application.

### Task 3.3: Paths and permissions
- An absolute path starts at the root `/` and describes the full location. Example: `/Users/[redacted]/digital-detective-8413/mission-02-terminal`.
- A relative path describes a location from the current folder. Example: `mission-02-terminal/terminal-practice`.
- The `notes.txt` permissions were `-rw-r--r--`. The owner can read and write the file; group members and others can read it.

### Task 3.4: Operating system responsibilities
| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Schedules programs and shares processor time | Running a browser and music player at the same time |
| Memory management | Allocates memory to programs | Keeping applications running without overwriting each other's memory |
| Device management | Coordinates communication with hardware | Sending keyboard input to an application |
| File management | Organizes files and folders | Finding documents through Finder |
| User interface / shell | Lets users interact with the computer | Desktop, Finder, and Terminal |
| Security and permissions | Controls access to files and system resources | File read and write permissions |

## 3. Commands / tools used
- `sw_vers -productVersion`
- `uname -m`
- `df -h /`
- `top -l 1 -n 0 | head -n 8`
- Terminal

## 4. My understanding
The operating system manages programs, memory, devices, files, user interaction, and permissions. Processes are running programs, and a PID identifies each process. Absolute paths begin at `/`; relative paths depend on the current folder.

## 5. Difficulties faced
I needed to interpret the storage and CPU output and distinguish absolute paths from relative paths.

## 6. How I resolved them
I used the system information commands to check the values and compared how each path is written.

## 7. Evidence / files
- `README.md` with system information, process and path notes, permissions, and operating system responsibilities
- Account name: [redacted]

## 8. Commit details
- Original mission commit message: `Document operating system and file management`
- Correction commit message: `Complete operating system mission details`
