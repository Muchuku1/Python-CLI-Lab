import typer
from rich.console import Console
from rich.table import Table

from models.user import User
from models.project import Project
from models.task import Task
from utils.file_handler import load_data, save_data

app = typer.Typer(help="CLI Tool for managing Users, Projects, and Tasks.")
console = Console()

# --- ADD COMMANDS ---

@app.command()
def add_user(
    name: str = typer.Option(..., help="User's name"), 
    email: str = typer.Option(..., help="User's email")
):
    """Add a new user."""
    data = load_data()
    if any(u["name"] == name for u in data["users"]):
        console.print(f"[bold red]Error:[/bold red] User '{name}' already exists.")
        raise typer.Exit(code=1)
    
    new_user = User(name=name, email=email)
    data["users"].append(new_user.to_dict())
    save_data(data)
    console.print(f"[bold green]Success:[/bold green] Added user '{name}'.")

@app.command()
def add_project(
    user: str = typer.Option(..., help="Project owner username"), 
    title: str = typer.Option(..., help="Project title"), 
    description: str = typer.Option("", help="Project description"), 
    due_date: str = typer.Option("TBD", help="Due date")
):
    """Add a new project for a user."""
    data = load_data()
    if not any(u["name"] == user for u in data["users"]):
        console.print(f"[bold red]Error:[/bold red] User '{user}' does not exist.")
        raise typer.Exit(code=1)
    
    new_proj = Project(title=title, description=description, due_date=due_date, username=user)
    data["projects"].append(new_proj.to_dict())
    save_data(data)
    console.print(f"[bold green]Success:[/bold green] Added project '{title}' for user '{user}'.")

@app.command()
def add_task(
    project: str = typer.Option(..., help="Project title"), 
    title: str = typer.Option(..., help="Task title"), 
    assigned_to: str = typer.Option("Unassigned", help="Assigned person"), 
    status: str = typer.Option("Pending", help="Task status")
):
    """Add a new task to a project."""
    data = load_data()
    if not any(p["title"] == project for p in data["projects"]):
        console.print(f"[bold red]Error:[/bold red] Project '{project}' does not exist.")
        raise typer.Exit(code=1)
    
    new_task = Task(title=title, status=status, assigned_to=assigned_to, project_title=project)
    data["tasks"].append(new_task.to_dict())
    save_data(data)
    console.print(f"[bold green]Success:[/bold green] Added task '{title}' to project '{project}'.")

# --- VIEW COMMANDS ---

@app.command()
def view(entity: str):
    """View entities: users, projects, or tasks."""
    data = load_data()
    
    if entity == "users":
        table = Table(title="System Users")
        table.add_column("Name", style="cyan")
        table.add_column("Email", style="magenta")
        for u in data["users"]:
            table.add_row(u["name"], u["email"])
        console.print(table)
        
    elif entity == "projects":
        table = Table(title="Projects")
        table.add_column("Title", style="cyan")
        table.add_column("Description", style="white")
        table.add_column("Due Date", style="yellow")
        table.add_column("Owner", style="green")
        for p in data["projects"]:
            table.add_row(p["title"], p["description"], p["due_date"], p["username"])
        console.print(table)
        
    elif entity == "tasks":
        table = Table(title="Tasks")
        table.add_column("Title", style="cyan")
        table.add_column("Project", style="green")
        table.add_column("Assigned To", style="magenta")
        table.add_column("Status", style="yellow")
        for t in data["tasks"]:
            table.add_row(t["title"], t["project_title"], t["assigned_to"], t["status"])
        console.print(table)
    else:
        console.print("[bold red]Invalid entity.[/bold red] Choose from: users, projects, tasks.")

# --- UPDATE COMMANDS ---

@app.command()
def update_task_status(
    title: str = typer.Option(..., help="Task title"), 
    status: str = typer.Option(..., help="New status")
):
    """Update the status of an existing task."""
    data = load_data()
    updated = False
    for t in data["tasks"]:
        if t["title"] == title:
            t["status"] = status
            updated = True
            break
            
    if updated:
        save_data(data)
        console.print(f"[bold green]Success:[/bold green] Updated task '{title}' status to '{status}'.")
    else:
        console.print(f"[bold red]Error:[/bold red] Task '{title}' not found.")

if __name__ == "__main__":
    app()