import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Función para instalar el APK
def install_apk():
    apk_path = filedialog.askopenfilename(title="Selecciona el APK", filetypes=[("APK files", "*.apk")])
    if apk_path:
        try:
            result = subprocess.run(["adb", "install", apk_path], capture_output=True, text=True)
            if "Success" in result.stdout:
                messagebox.showinfo("Éxito", "APK instalado correctamente.")
            else:
                messagebox.showerror("Error", f"Error al instalar el APK:\n{result.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")

# Función para desinstalar una app
def uninstall_apk():
    package_name = package_entry.get().strip()
    if package_name:
        try:
            result = subprocess.run(["adb", "uninstall", package_name], capture_output=True, text=True)
            if "Success" in result.stdout:
                messagebox.showinfo("Éxito", "APK desinstalado correctamente.")
            else:
                messagebox.showerror("Error", f"Error al desinstalar el APK:\n{result.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de APKs con ADB")

# Botón para instalar APK
install_button = tk.Button(root, text="Instalar APK", command=install_apk)
install_button.pack(pady=10)

# Entrada y botón para desinstalar APK
package_label = tk.Label(root, text="Nombre del paquete:")
package_label.pack(pady=5)
package_entry = tk.Entry(root, width=40)
package_entry.pack(pady=5)

uninstall_button = tk.Button(root, text="Desinstalar APK", command=uninstall_apk)
uninstall_button.pack(pady=10)

# Inicia el loop de la aplicación
root.mainloop()
