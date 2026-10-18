CLI Task & Project Manager

A Python-based Command-Line Interface (CLI) application designed for administrators to manage users, projects, and tasks with local JSON data persistence.

Features

User Management: Add and view system users.

Project Tracking: Associate projects with specific users, including descriptions and due dates.

Task Delegation: Assign tasks to specific projects with status tracking (e.g., Pending, Completed).

Status Updates: Modify the status of existing tasks directly via CLI options.

Data Persistence: Automatically stores and loads data locally in JSON format with built-in error recovery for corrupted files.

Rich Terminal Output: Visualizes views using structured, color-coded tables.

Project Structure

project_root/
│
├── main.py              # Main CLI entry point (Typer commands)
├── requirements.txt     # Third-party dependencies
├── README.md            # Documentation
│
├── models/              # Object-Oriented Domain Models
│   ├── __init__.py
│   ├── user.py          # Person and User classes
│   ├── project.py       # Project class definition
│   └── task.py          # Task class definition
│
├── utils/               # File handling and utility helpers
│   ├── __init__.py
│   └── file_handler.py  # JSON storage reader/writer logic
│
└── data/                # Local data persistence
    └── storage.json     # Saved users, projects, and tasks


Setup Instructions

Prerequisites

Python 3.8 or higher installed on your machine.

Installation

Clone the repository:

git clone <your-repository-url>
cd <your-repository-folder>


Create and activate a virtual environment (Optional):

macOS/Linux:

python3 -m venv venv
source venv/bin/activate


Windows:

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


How to Run CLI Commands

1. User Commands

Add a user:

python main.py add-user --name "Cliff" --email "cliff@example.com"


View all users:

python main.py view users


2. Project Commands

Add a project for a user:

python main.py add-project --user "Cliff" --title "CLI Tool" --description "Python CLI app project" --due-date "2026-10-19"


View all projects:

python main.py view projects


3. Task Commands

Add a task to a project:

python main.py add-task --project "CLI Tool" --title "Implement add-task" --assigned-to "Cliff" --status "In Progress"


View all tasks:

python main.py view tasks


Update task status:

python main.py update-task-status --title "Implement add-task" --status "Completed"
