import pygame
import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()

# Initialize pygame mixer
pygame.mixer.init()

# Create the main window
window = tk.Tk()
window.title("Music Player")

# Create the menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Create the Controls frame
controls_frame = tk.Frame(window)
controls_frame.pack()

# Create the buttons
button_open = tk.Button(controls_frame, text="Open", command=open_file)
button_open.pack(side=tk.LEFT)

button_pause = tk.Button(controls_frame, text="Pause", command=pause)
button_pause.pack(side=tk.LEFT)

button_resume = tk.Button(controls_frame, text="Resume", command=resume)
button_resume.pack(side=tk.LEFT)

button_stop = tk.Button(controls_frame, text="Stop", command=stop)
button_stop.pack(side=tk.LEFT)

# Start the application
window.mainloop()
