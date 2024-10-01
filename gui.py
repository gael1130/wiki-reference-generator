import tkinter as tk
from tkinter import ttk, scrolledtext
from utils.reference_generator import WikipediaReferenceGenerator

class WikiReferenceGUI:
    def __init__(self, master):
        self.master = master
        master.title("Wikipedia Reference Generator")
        master.geometry("600x350")  # Adjusted the size to be slightly taller to fit the new arrangement

        self.create_widgets()

    def create_widgets(self):
        # URL Input Frame
        url_frame = ttk.Frame(self.master, padding="5")
        url_frame.pack(fill=tk.X, padx=5, pady=5)

        # URL Label and Entry
        url_label = ttk.Label(url_frame, text="Google News URL:")
        url_label.pack(anchor=tk.W, pady=(0, 5))

        self.url_entry = ttk.Entry(url_frame, width=50)
        self.url_entry.pack(fill=tk.X, expand=True, pady=(0, 10))

        # Generate Button
        generate_button = ttk.Button(url_frame, text="Generate Reference", command=self.generate_reference)
        generate_button.pack()

        # Output Text Area Frame
        output_frame = ttk.Frame(self.master, padding="5")
        output_frame.pack(expand=True, fill=tk.BOTH, padx=5, pady=(0, 5))

        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=70, height=10)
        self.output_text.pack(expand=True, fill=tk.BOTH)

        # Copy Button Frame
        button_frame = ttk.Frame(self.master, padding="5")
        button_frame.pack(fill=tk.X, padx=5, pady=(0, 5))

        copy_button = ttk.Button(button_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.pack(side=tk.RIGHT)

    def generate_reference(self):
        url = self.url_entry.get()
        if not url:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Please enter a Google News URL.")
            return

        try:
            generator = WikipediaReferenceGenerator(url)
            reference = generator.generate_reference()
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, reference)
        except Exception as e:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"An error occurred: {str(e)}")

    def copy_to_clipboard(self):
        reference = self.output_text.get(1.0, tk.END).strip()
        if reference:
            self.master.clipboard_clear()
            self.master.clipboard_append(reference)
            self.master.update()  # Keeps clipboard updated

def run_gui():
    root = tk.Tk()
    WikiReferenceGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
