from rembg import remove
from tkinter import Tk, Button, filedialog, messagebox, Toplevel, Label
import os
import sys
import threading
from time import sleep

def resource_path(relative_path):
    """Permite acceder a archivos empaquetados dentro del .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def remove_background_gui():
    root = Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(
        title="Seleccioná una imagen",
        filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.webp;*.bmp")]
    )
    if not input_path:
        return

    output_path = filedialog.asksaveasfilename(
        title="Guardar imagen sin fondo como...",
        defaultextension=".png",
        filetypes=[("Imagen PNG", "*.png")]
    )
    if not output_path:
        return

    try:
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
            output_data = remove(input_data)

        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)

        messagebox.showinfo("¡Listo!", f"Imagen sin fondo guardada en:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")

def main_app():
    root = Tk()
    root.title("Quitar Fondo - Powered by Rembg")
    root.geometry("300x150")

    try:
        icon_path = resource_path("removebg.ico")
        root.iconbitmap(icon_path)
    except:
        pass  # No explota si no hay ícono

    btn = Button(root, text="Quitar fondo a imagen", font=("Arial", 12), command=remove_background_gui)
    btn.pack(expand=True, padx=20, pady=40)

    root.mainloop()

def show_splash_then_main():
    splash = Toplevel()
    splash.overrideredirect(True)
    splash.geometry("300x200+600+300")

    try:
        splash.iconbitmap(resource_path("removebg.ico"))
    except:
        pass

    Label(splash, text="Cargando Quitar Fondo...", font=("Arial", 14)).pack(expand=True)

    def delayed_start():
        sleep(1.5)
        splash.destroy()
        main_app()

    threading.Thread(target=delayed_start).start()

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    show_splash_then_main()
    root.mainloop()
