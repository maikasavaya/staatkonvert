import tkinter as tk
from tkinter import filedialog, messagebox
import markdown

def convert_markdown_to_html(md_text):
    """convert markdown text to html."""
    return markdown.markdown(md_text)

def open_file():
    """open a markdown file and load its content into the text box."""
    file_path = filedialog.askopenfilename(filetypes=[("markdown files", "*.md")])
    if file_path:
        with open(file_path, 'r') as file:
            markdown_content = file.read()
        text_input.delete(1.0, tk.END)  
        text_input.insert(tk.END, markdown_content)

def save_file(html_text):
    """Save the converted HTML to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("html files", "*.html")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(html_text)
        messagebox.showinfo("success!", f"html content saved to {file_path}")

def convert():
    """convert the markdown text to html and display the result."""
    markdown_content = text_input.get(1.0, tk.END).strip()
    if markdown_content:
        html_content = convert_markdown_to_html(markdown_content)
        text_output.delete(1.0, tk.END)  
        text_output.insert(tk.END, html_content)  
    else:
        messagebox.showwarning("input error", "please provide markdown text or a markdown file.")

root = tk.Tk()
root.title("staatkonvert: markdown to html")

root.geometry("600x400")

label_input = tk.Label(root, text="your markdown:")
label_input.pack(pady=5)

text_input = tk.Text(root, height=10, wrap=tk.WORD)
text_input.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_load = tk.Button(frame_buttons, text="load markdown file", command=open_file)
button_load.grid(row=0, column=0, padx=5)

button_convert = tk.Button(frame_buttons, text="convert to html", command=convert)
button_convert.grid(row=0, column=1, padx=5)

label_output = tk.Label(root, text="your html:")
label_output.pack(pady=5)

text_output = tk.Text(root, height=10, wrap=tk.WORD)
text_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

button_save = tk.Button(root, text="save html file", command=lambda: save_file(text_output.get(1.0, tk.END)))
button_save.pack(pady=10)

root.mainloop()
