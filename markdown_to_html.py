import tkinter as tk
from tkinter import filedialog, messagebox
import markdown

def convert_markdown_to_html(md_text):
    """Convert Markdown text to HTML."""
    return markdown.markdown(md_text)

def open_file():
    """Open a Markdown file and load its content into the text box."""
    file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    if file_path:
        with open(file_path, 'r') as file:
            markdown_content = file.read()
        text_input.delete(1.0, tk.END)  # Clear existing text
        text_input.insert(tk.END, markdown_content)

def save_file(html_text):
    """Save the converted HTML to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(html_text)
        messagebox.showinfo("Success", f"HTML content saved to {file_path}")

def convert():
    """Convert the Markdown text to HTML and display the result."""
    markdown_content = text_input.get(1.0, tk.END).strip()
    if markdown_content:
        html_content = convert_markdown_to_html(markdown_content)
        text_output.delete(1.0, tk.END)  # Clear existing output
        text_output.insert(tk.END, html_content)  # Show HTML output
    else:
        messagebox.showwarning("Input Error", "Please provide some Markdown text or load a Markdown file.")

# Create the main window
root = tk.Tk()
root.title("Markdown to HTML Converter")

# Set the window size
root.geometry("600x400")

# Text input (Markdown)
label_input = tk.Label(root, text="Enter or load Markdown:")
label_input.pack(pady=5)

text_input = tk.Text(root, height=10, wrap=tk.WORD)
text_input.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Buttons for file operations and conversion
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_load = tk.Button(frame_buttons, text="Load Markdown File", command=open_file)
button_load.grid(row=0, column=0, padx=5)

button_convert = tk.Button(frame_buttons, text="Convert to HTML", command=convert)
button_convert.grid(row=0, column=1, padx=5)

# Text output (HTML)
label_output = tk.Label(root, text="Converted HTML:")
label_output.pack(pady=5)

text_output = tk.Text(root, height=10, wrap=tk.WORD)
text_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Button to save HTML to file
button_save = tk.Button(root, text="Save HTML File", command=lambda: save_file(text_output.get(1.0, tk.END)))
button_save.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
