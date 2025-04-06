# To-Do App (Beginner Project)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SimpleGUI](https://img.shields.io/badge/GUI-SimpleGUI-green)
![Streamlit](https://img.shields.io/badge/WebApp-Streamlit-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A beginner-friendly **To-Do application** with three user interfaces:
- **Command-Line Interface (CLI)**
- **Desktop GUI** using **SimpleGUI**
- **Web App** built with **Streamlit**

All versions share the same `todo.txt` file for simple file-based task storage. The project showcases basic programming, file I/O, GUI, and web development concepts in Python.

---

## Features

- Add, edit, remove, and view tasks
- Shared task data via `todo.txt`
- Minimalistic CLI for fast task entry
- SimpleGUI-powered desktop interface
- Streamlit-based modern web app
- Easy deployment with [Hokato](https://hokato.io/)

---

## Tech Stack

- **Programming Language:** Python 3
- **CLI:** Python standard input/output
- **GUI:** [SimpleGUI](https://simpleguics2pygame.readthedocs.io/)
- **Web App:** [Streamlit](https://streamlit.io/)
- **Deployment:** [Hokato](https://hokato.io/)

---

## Project Structure

```plaintext
todo-app/
│
├── cli_app.py        # Command-line interface
├── gui_app.py        # Desktop GUI using SimpleGUI
├── web_app.py        # Web interface using Streamlit
├── todo.txt          # Shared task storage
├── requirements.txt  # Python dependencies
└── README.md
