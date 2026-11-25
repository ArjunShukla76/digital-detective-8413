# Mission 4: How programs run

## 1. Task / objective
Run a simple Python program and compare how compilers and interpreters work.

## 2. Work completed
Created hello.py containing one line that prints "Hello from Python" and ran it with python3. The message appeared.

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | The whole program is translated before it runs | The program is read and executed line by line while it runs |
| Typical output | A separate executable (machine code) file | No separate file; the result of running the code |
| One example | GCC for C | Python interpreter (python3) |
| One advantage | The finished program runs fast | Easy to test code quickly, no compile step |

A compiler translates the whole source code into another form, often machine code, before the program runs, so the result can be run again without translating. An interpreter reads the code and carries out instructions at runtime, so I can run a file straight away but it is usually slower. Python is usually run with an interpreter, though real implementations can mix both approaches.

## 3. Commands / tools used
- `echo` and `>`: wrote the one-line program into hello.py.
- `cat`: displayed the file to check it.
- `python3 hello.py`: ran the program with the Python interpreter.
- `git add`, `git commit`, `git push`: saved and published the mission.
- Tools: Terminal, nano.

## 4. My understanding
Source code has to be turned into instructions the processor can run. A compiler does that translation ahead of time, while an interpreter does it as the program runs. Running hello.py with python3 showed me the interpreter approach.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- mission-04-programs/hello.py
- mission-04-programs/README.md

## 8. Commit details
- Commit message: "Compare compilers and interpreters"
- Pushed to GitHub and verified: yes$
