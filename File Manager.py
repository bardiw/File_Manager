from tkinter import filedialog, messagebox, Button, Tk, Label
import shutil
import os
import easygui


def file_open_box():
    path = easygui.fileopenbox()
    return path


def directory_open_box():
    path = filedialog.askdirectory()
    return path


def open_file():
    path = file_open_box()
    try:
        os.startfile(path)
    except TypeError:
        messagebox.showinfo("Error!", "The desired file was not found!")


def copy_file():
    source = file_open_box()
    destination = directory_open_box()
    try:
        shutil.copy(source, destination)
        messagebox.showinfo("Successful!", "File copied successfully!")
    except:
        messagebox.showinfo("Error!", "Copy failed!")


def delete_file():
    path = file_open_box()
    try:
        os.remove(path)
        messagebox.showinfo("Successful!", "File deleted successfully!")
    except:
        messagebox.showinfo("Error!", "The file was not deleted!")


def rename_file():
    try:
        file = file_open_box()
        path1 = os.path.dirname(file)
        extention = os.path.splitext(file)[1]
        new_name = input("New name: ")
        path2 = os.path.join(path1, new_name + extention)
        os.rename(file, path2)
        messagebox.showinfo("Successful!", "File name changed successfully!")
    except:
        messagebox.showinfo("Error!", "Rename failed!")


def move_file():
    source = file_open_box()
    destination = directory_open_box()
    if source == destination:
        messagebox.showinfo("Error!", "The transfer path has not changed!")
    else:
        try:
            shutil.move(source, destination)
            messagebox.showinfo("Successful!", "File transferred successfully!")
        except:
            messagebox.showinfo("Error!", "File transfer failed!")


def make_directory():
    path = directory_open_box()
    name = input("Name: ")
    path = os.path.join(path, name)
    try:
        os.mkdir(path)
        messagebox.showinfo("Successful!", "Directory created successfully!")
    except:
        messagebox.showinfo("Error!", "Directory not created!")


def remove_directory():
    path = directory_open_box()
    try:
        os.rmdir(path)
        messagebox.showinfo("Successful!", "Directory deleted successfully!")
    except:
        messagebox.showinfo("Error!", "Directory not deleted!")


def list_files():
    path = directory_open_box()
    file_list = sorted(os.listdir(path))
    for i in file_list:
        print(i)


window = Tk()
window.title("File Management")
window.configure(bg="black")
window.geometry("500x400")
Label(window, text="what should i do").pack()
Button(window, command=open_file, text="Open the file", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=copy_file, text="Copy the file", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=delete_file, text="Delete the file", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=rename_file, text="Rename the file", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=move_file, text="File transfer", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=make_directory, text="Create folder", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=remove_directory, text="Delete folder", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=list_files, text="List of all files", fg="blue", activebackground="red", bg="white").pack()

window.mainloop()
