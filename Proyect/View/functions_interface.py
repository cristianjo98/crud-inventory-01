import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Functions():
    def __init__(self, rott, my_frame, model):
        self.model = model
        self.root = rott
        self.my_frame = my_frame

    def showHide_bahias(self, box_medium_storage, my_storageType,
                        my_bahias, label_bahias, entry_bahias):

        box_medium_storage.select_clear()

        if my_storageType.get() == "Sata":
            label_bahias.grid(row=3, column=2, padx=2, pady=5, sticky=tk.E)
            entry_bahias.grid(row=3, column=3, padx=2, pady=5, sticky=tk.W)
            my_bahias.set("")
        else:
            label_bahias.grid_forget()
            entry_bahias.grid_forget()
            entry_bahias.delete(0, tk.END)
            my_bahias.set("N/A")

    def showHide_modulos(self, entry_dataCenter, my_dataCenter,
                         my_modulo, label_modulos, entry_modulos):

        entry_dataCenter.select_clear()

        if my_dataCenter.get() == "Jupiter data" or my_dataCenter.get() == "Saturno data":
            label_modulos.grid(row=0, column=7, padx=2, pady=5, sticky=tk.E)
            entry_modulos.grid(row=0, column=8, padx=2, pady=5, sticky=tk.W)
            my_modulo.set("")
        else:
            label_modulos.grid_forget()
            entry_modulos.grid_forget()
            entry_modulos.delete(0, tk.END)
            my_modulo.set("N/A")

    def clear_fields(self, list_stringVar):
        for variable in list_stringVar:
            variable.set("")

    def clear_table(self, table):
        iids = table.get_children()

        for id in iids:
            table.delete(id)

    def open_popup_window(self, list_stringVar):
        pos_x = self.root.winfo_x()
        pos_y = self.root.winfo_y()
        
        popup_w = tk.Toplevel(master=self.my_frame)
        popup_w.geometry(f"250x120+{pos_x}+{pos_y + 50}")
        popup_w.resizable(False, False)

        label_serialCode = ttk.Label(
            master=popup_w, text="Ingresar serial - codigo:", font=(12), background="#F0F0F0")
        label_serialCode.grid(row=0, column=0, padx=40, pady=35)

        label_save = ttk.Label(
            master=popup_w, text="Guardado con exito", font=(12), background="#F0F0F0")

        # ENTRY_SERIAL
        box_serialCode = ttk.Entry(
            master=popup_w, textvariable=list_stringVar[3], width=30)
        box_serialCode.place(x=30, y=65)
        box_serialCode.focus()
        box_serialCode.icursor(tk.END)
        box_serialCode.bind(
            "<Return>", lambda event: self.model.save_data(list_stringVar, label_save=label_save))
        
    def doubleClic_setFields(self, table, list_stringVar,
                             label_bahias, entry_bahias,
                             label_modulos, entry_modulos):

        get_iid = table.selection()
        get_values = table.item(get_iid, "values")

        if not get_values:
            pass


        if get_values[5] != "N/A":
            label_bahias.grid(row=3, column=2, padx=2, pady=5, sticky=tk.E)
            entry_bahias.grid(row=3, column=3, padx=2, pady=5, sticky=tk.W)

        if not get_values[7] == "N/A":
            label_modulos.grid(row=0, column=7, padx=2, pady=5, sticky=tk.E)
            entry_modulos.grid(row=0, column=8, padx=2, pady=5, sticky=tk.W)
        
        for index in range(11):
            list_stringVar[index].set(get_values[index])
        table.delete(get_iid[0])

    def about(self):
        text = """
        Inventario de medios de almacenamiento
        
        Versión: 1.0
        Tecnologia: Python/Tkinter
        """
        messagebox.showinfo(title="Acerca de", message=text)

    def Exit(self):
        question = messagebox.askyesno(
            title="Salir", message="¿Desea salir de la aplicación?")

        if question:
            self.root.destroy()
        else:
            pass
