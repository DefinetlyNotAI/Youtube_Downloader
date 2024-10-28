import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube
import threading
import logging
from colorlog_setup import *


class TextHandler(logging.Handler):
    def __init__(self, text_widget):
        logging.Handler.__init__(self)
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg + '\n')
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)


class YouTubeDownloaderApp:
    def __init__(self, root_YDA):
        self.root = root_YDA
        self.root.title("YouTube Downloader")

        self.url_label = tk.Label(root_YDA, text="YouTube URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(root_YDA, width=50)
        self.url_entry.pack()

        self.save_label = tk.Label(root_YDA, text="Save to:")
        self.save_label.pack()

        self.save_entry = tk.Entry(root_YDA, width=50)
        self.save_entry.pack()

        self.browse_button = tk.Button(root_YDA, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        self.download_button = tk.Button(root_YDA, text="Download", command=self.start_download)
        self.download_button.pack()

        self.progress = tk.Label(root_YDA, text="")
        self.progress.pack()

        self.log_text = tk.Text(root_YDA, height=10, width=60)
        self.log_text.pack()
        self.log_text.config(state=tk.DISABLED)

        text_handler = TextHandler(self.log_text)
        text_handler.setFormatter(formatter)
        logger.addHandler(text_handler)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.save_entry.delete(0, tk.END)
            self.save_entry.insert(0, directory)

    def start_download(self):
        url = self.url_entry.get()
        save_path = self.save_entry.get()

        if not url or not save_path:
            messagebox.showerror("Error", "Please provide both URL and save path.")
            return

        logger.info("Starting download thread")
        threading.Thread(target=self.download_video, args=(url, save_path)).start()

    def download_video(self, url, save_path):
        try:
            logger.info(f"Downloading video from URL: {url}")
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            video.download(save_path)
            self.progress.config(text=f"{yt.title} downloaded successfully.")
            logger.info(f"{yt.title} downloaded successfully.")
        except Exception as e:
            logger.debug(e)
            if str(e) == "get_throttling_function_name: could not find match for multiple":
                logger.critical("Video could not be downloaded due to an error with the API of YouTube")
            else:
                logger.error(f"Failed to download video: {e}")
            self.progress.config(text=f"Failed to download video: {e}")


if __name__ == "__main__":
    logger.warning("The GUI application is in BETA and may not work as expected.")
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
