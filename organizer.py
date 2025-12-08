import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Python Files": [".py", ".ipynb"],
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"]
}

def organize_files(source_path):
    if not source_path:
        messagebox.showerror("Error", "Please select a folder first!")
        return

    files_moved = 0
    
    try:
        files = os.listdir(source_path)
        
        for file in files:
            file_path = os.path.join(source_path, file)
            
            if os.path.isdir(file_path):
                continue

            _, extension = os.path.splitext(file)
            extension = extension.lower()

            found_category = False
            
            for category, ext_list in FILE_CATEGORIES.items():
                if extension in ext_list:
                    dest_folder = os.path.join(source_path, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    files_moved += 1
                    found_category = True
                    break
            
            if not found_category and extension:
                dest_folder = os.path.join(source_path, "Others")
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file))
                files_moved += 1

        messagebox.showinfo("Success", f"Done! Organized {files_moved} files.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_selected)

def run_organizer():
    path = entry_path.get()
    organize_files(path)

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x150")

label_instr = tk.Label(root, text="Select a folder to organize:")
label_instr.pack(pady=5)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

entry_path = tk.Entry(frame_input, width=40)
entry_path.pack(side=tk.LEFT, padx=5)

btn_browse = tk.Button(frame_input, text="Browse", command=browse_folder)
btn_browse.pack(side=tk.LEFT)

btn_run = tk.Button(root, text="Organize Files", command=run_organizer, bg="lightblue", width=20)
btn_run.pack(pady=20)

root.mainloop()