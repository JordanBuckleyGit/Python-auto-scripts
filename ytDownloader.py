import customtkinter as ctkapp
from customtkinter import CTkButton, CTkEntry, CTkLabel, CTkFrame
from pytube import YouTube
import os
import threading
from tkinter import messagebox

def download_video():
    url = url_entry.get()
    download_path = path_entry.get()

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if stream:
            download_button.configure(state="disabled")
            download_thread = threading.Thread(target=download_video_thread, args=(stream, download_path))
            download_thread.start()
        else:
            messagebox.showerror("Error", "No progressive stream available for this video.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def download_video_thread(stream, download_path):
    try:
        stream.download(output_path=download_path)
        messagebox.showinfo("Success", "Download successful!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        download_button.configure(state="normal")

# Create the main window
root = ctkapp.CTk()
root.geometry("500x300")
root.title("YouTube Downloader")

# Create a stylish frame for content
content_frame = CTkFrame(master=root, width=480, height=260, corner_radius=10)
content_frame.pack(padx=10, pady=10)

# Create labels with improved styling
url_label = CTkLabel(master=content_frame, text="Enter YouTube Video URL:")
url_label.pack(pady=5)

# Create entry box for URL
url_entry = CTkEntry(master=content_frame, width=60)
url_entry.pack(pady=5)

path_label = CTkLabel(master=content_frame, text="Enter Download Path:")
path_label.pack(pady=5)

# Create entry box for download path
path_entry = CTkEntry(master=content_frame, width=60)
path_entry.pack(pady=5)

# Create a stylish button with hover effect
download_button = CTkButton(master=content_frame, text="Download", command=download_video, hover_color="#303F9F")
download_button.pack(pady=10)

root.mainloop()
