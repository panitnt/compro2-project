from window_app import WindowApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scan Your Netflix")
    root.geometry("800x1440")
    app = WindowApp(root)
    app.run()
