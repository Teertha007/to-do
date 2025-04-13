import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
from tkcalendar import DateEntry
import uuid

class TodoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        style = ttk.Style()
        style.configure("Custom.TButton", padding=5, font=('Helvetica', 10))
        style.configure("Custom.TLabel", font=('Helvetica', 10))
        style.configure("Custom.TEntry", padding=5)
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Task input section
        input_frame = ttk.LabelFrame(main_frame, text="Add New Task", padding="10")
        input_frame.pack(fill=tk.X, pady=5)
        
        # Task description
        ttk.Label(input_frame, text="Task:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.task_entry = ttk.Entry(input_frame, width=40)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Category
        ttk.Label(input_frame, text="Category:").grid(row=0, column=2, sticky=tk.W, pady=5)
        self.category_var = tk.StringVar()
        categories = ["Personal", "Work", "Shopping", "Health", "Other"]
        self.category_combo = ttk.Combobox(input_frame, textvariable=self.category_var, values=categories, width=15)
        self.category_combo.grid(row=0, column=3, padx=5, pady=5)
        self.category_combo.set("Personal")
        
        # Priority
        ttk.Label(input_frame, text="Priority:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.priority_var = tk.StringVar()
        priorities = ["High", "Medium", "Low"]
        self.priority_combo = ttk.Combobox(input_frame, textvariable=self.priority_var, values=priorities, width=15)
        self.priority_combo.grid(row=1, column=1, padx=5, pady=5)
        self.priority_combo.set("Medium")
        
        # Due Date
        ttk.Label(input_frame, text="Due Date:").grid(row=1, column=2, sticky=tk.W, pady=5)
        self.due_date = DateEntry(input_frame, width=15, background='darkblue', foreground='white', borderwidth=2)
        self.due_date.grid(row=1, column=3, padx=5, pady=5)
        
        # Add button
        add_btn = ttk.Button(input_frame, text="Add Task", command=self.add_task, style="Custom.TButton")
        add_btn.grid(row=2, column=0, columnspan=4, pady=10)
        
        # Task list section
        list_frame = ttk.LabelFrame(main_frame, text="Tasks", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Treeview for tasks
        columns = ("ID", "Task", "Category", "Priority", "Due Date", "Status")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        self.tree.column("Task", width=200)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Buttons frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        # Action buttons
        ttk.Button(btn_frame, text="Edit", command=self.edit_task, style="Custom.TButton").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_task, style="Custom.TButton").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Mark Complete", command=self.mark_completed, style="Custom.TButton").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.refresh_tasks, style="Custom.TButton").pack(side=tk.LEFT, padx=5)
        
        self.refresh_tasks()
        
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                self.tasks = []
                
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
            
    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Warning", "Please enter a task description!")
            return
            
        new_task = {
            'id': str(uuid.uuid4())[:8],
            'task': task,
            'category': self.category_var.get(),
            'priority': self.priority_var.get(),
            'due_date': self.due_date.get_date().strftime("%Y-%m-%d"),
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'completed': False
        }
        
        self.tasks.append(new_task)
        self.save_tasks()
        self.refresh_tasks()
        self.task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully!")
        
    def edit_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to edit!")
            return
            
        task_id = self.tree.item(selected_item[0])['values'][0]
        for task in self.tasks:
            if task['id'] == task_id:
                # Create edit window
                edit_window = tk.Toplevel(self.root)
                edit_window.title("Edit Task")
                edit_window.geometry("400x350") # Increased height for date entry
                
                ttk.Label(edit_window, text="Task:").pack(pady=5)
                task_entry = ttk.Entry(edit_window, width=40)
                task_entry.insert(0, task['task'])
                task_entry.pack(pady=5)
                
                ttk.Label(edit_window, text="Category:").pack(pady=5)
                category_var = tk.StringVar(value=task['category'])
                category_combo = ttk.Combobox(edit_window, textvariable=category_var, values=["Personal", "Work", "Shopping", "Health", "Other"])
                category_combo.pack(pady=5)
                
                ttk.Label(edit_window, text="Priority:").pack(pady=5)
                priority_var = tk.StringVar(value=task['priority'])
                priority_combo = ttk.Combobox(edit_window, textvariable=priority_var, values=["High", "Medium", "Low"])
                priority_combo.pack(pady=5)
                
                # Add Due Date editing
                ttk.Label(edit_window, text="Due Date:").pack(pady=5)
                # Convert stored string date back to datetime object for DateEntry
                current_due_date = None
                try:
                    current_due_date = datetime.strptime(task.get('due_date', ''), "%Y-%m-%d").date()
                except ValueError:
                    pass # Handle cases where due_date might be empty or invalid
                
                due_date_entry = DateEntry(edit_window, width=15, background='darkblue', foreground='white', borderwidth=2)
                if current_due_date:
                    due_date_entry.set_date(current_due_date)
                due_date_entry.pack(pady=5)
                
                def save_changes():
                    task['task'] = task_entry.get().strip()
                    task['category'] = category_var.get()
                    task['priority'] = priority_var.get()
                    # Save the updated due date
                    task['due_date'] = due_date_entry.get_date().strftime("%Y-%m-%d")
                    self.save_tasks()
                    self.refresh_tasks()
                    edit_window.destroy()
                    messagebox.showinfo("Success", "Task updated successfully!")
                
                ttk.Button(edit_window, text="Save Changes", command=save_changes).pack(pady=20)
                break
                
    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return
            
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this task?"):
            task_id = self.tree.item(selected_item[0])['values'][0]
            self.tasks = [task for task in self.tasks if task['id'] != task_id]
            self.save_tasks()
            self.refresh_tasks()
            messagebox.showinfo("Success", "Task deleted successfully!")
            
    def mark_completed(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to mark as completed!")
            return
            
        task_id = self.tree.item(selected_item[0])['values'][0]
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                self.save_tasks()
                self.refresh_tasks()
                status = "completed" if task['completed'] else "uncompleted"
                messagebox.showinfo("Success", f"Task marked as {status}!")
                break
                
    def refresh_tasks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for task in self.tasks:
            status = "✓" if task.get('completed', False) else " "
            self.tree.insert("", tk.END, values=(
                task.get('id', ''),
                task.get('task', ''),
                task.get('category', 'Personal'),
                task.get('priority', 'Medium'),
                task.get('due_date', ''),
                status
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListGUI(root)
    root.mainloop() 