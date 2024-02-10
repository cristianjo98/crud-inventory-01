import os
from tkinter import *
from tkinter import messagebox
import sqlite3


class Model():
    marker_db = None
    path_db = os.path.join(os.path.dirname(
        __file__), "..", "Data", "DDBB_inventory_disk.db")
    my_conection = sqlite3.connect(path_db)
    my_cursor = my_conection.cursor()
        
    def conection_dataBase(self):
        try:
            self.my_cursor.execute("""        
            CREATE TABLE DDBB_inventory_disk(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Fecha VARCHAR(50) NOT NULL,
            N_cliente VARCHAR(50) NOT NULL,
            Serial VARCHAR(50) NOT NULL,
            T_medio VARCHAR(50) NOT NULL,
            Bahias VARCHAR(4) NOT NULL,
            Data_center VARCHAR(50) NOT NULL,
            Modulo VARCHAR(3) NOT NULL,
            Rack_Unidad VARCHAR(10) NOT NULL,
            Estado VARCHAR(50) NOT NULL,
            Comentarios VARCHAR(50) NOT NULL)
            """)
            self.marker_db = True
            self.my_conection.commit()
            messagebox.showinfo(
                title="Base de datos", message="Base de datos creada con exito")
        except:
            messagebox.showerror(
                title="Error", message="La base de datos ya fue creada")

    def delete_dataBase(self):
        try:
            question = messagebox.askyesno(
                title="Base de datos",
                message="¿Esta seguro de eliminar la base de datos?")

            if question:
                question = messagebox.askyesno(title="Base de datos",
                                               message="¿Esta completamente seguro de eliminar definitivamente la base de datos?")
                if question:
                    self.my_cursor.execute("DROP TABLE DDBB_inventory_disk")
                    messagebox.showinfo(
                        title="Base de datos", message="Base de datos eliminada con exito")
                    self.marker_db = False
                else:
                    pass
            else:
                pass
        except:
            messagebox.showerror(
                title="Error", message="La base de datos que intenta eliminar no existe.")

    def save_data(self, list_stringVar, label_save="", event=""):
        try:
            tup_values = tuple()
            for index, sVar in enumerate(list_stringVar):
                if index == 0:
                    continue
                elif not sVar.get():
                    messagebox.showwarning(title="Guardar",
                                           message="No se admiten campos vacios, por favor completar todos los campos")
                    break

            else:
                for index in range(1, 11):
                    tup_values += (list_stringVar[index].get(),)

                if self.marker_db == False:
                    messagebox.showerror(title="Buscar",
                                         message="Base de datos inexistente, por favor crear una base de datos")
                else:
                    self.my_cursor.execute("""INSERT INTO DDBB_inventory_disk VALUES
                                            (NULL,?,?,?,?,?,?,?,?,?,?)""", tup_values)
                    self.my_conection.commit()

                    if event == "button_save":
                        messagebox.showinfo(
                            title="Guardar", message="Guardado con exito")
                        self.clear_fields(list_stringVar)
                    else:
                        list_stringVar[3].set("")

                    if not label_save:
                        pass
                    else:
                        label_save.place(x=45, y=95)
        except:
            messagebox.showerror(
                title="Error",
                message="Ocurrio un error al intentar guardar, Por favor verificar la conexión con la base de datos")

    def search_data(self, list_stringVar, table):
        for iid in table.get_children():
            table.delete(iid)

        if self.marker_db == False:
            messagebox.showerror(title="Buscar",
                                 message="Base de datos inexistente, Por favor crear una base de datos")
        else:
            my_conection = sqlite3.connect(self.path_db)

            keys = ("Id", "Fecha", "N_cliente", "Serial", "T_medio", "Bahias",
                    "Data_center", "Modulo", "Rack_Unidad", "Estado", "Comentarios")

            dict_stringVar = dict()
            for index, value in enumerate(list_stringVar):
                if index == 0:
                    continue
                else:
                    dict_stringVar.update({keys[index]: value.get()})

            dict_filter = {key: value for key,
                           value in dict_stringVar.items() if value}

            if not dict_filter.values():
                messagebox.showwarning(title="Buscar",
                                       message="No se admiten campos vacios, por favor completar todos los campos")
            else:
                query = "SELECT * FROM DDBB_inventory_disk WHERE"
                condictions = []
                values = []

                try:
                    if "N_cliente" in dict_filter:
                        for index, value in dict_filter.items():
                            condictions.append(f"{index} LIKE ?")
                            values.append(f"{value[0]}%")

                        if len(condictions) == 1:
                            query += " " + condictions[0]
                        elif len(condictions) > 1:
                            query += " " + " AND ".join(condictions)

                        self.my_cursor.execute(query, tuple(values))
                        result_ddbb = self.my_cursor.fetchall()

                        if self.marker_db == False:
                            messagebox.showerror(title="Buscar",
                                                 message="Base de datos inexistente, Por favor crear una base de datos")
                        elif not result_ddbb:
                            messagebox.showerror(title="Buscar",
                                                   message="Los registros buscados no existen en la base de datos")
                        else:
                            for data in result_ddbb:
                                table.insert(
                                    parent="", index="end", values=data)
                            my_conection.close()

                    else:
                        for index, value in dict_filter.items():
                            condictions.append(f"{index} = ?")
                            values.append(value)

                        if len(condictions) == 1:
                            query += " " + condictions[0]
                        elif len(condictions) > 1:
                            query += " " + " AND ".join(condictions)

                        self.my_cursor.execute(query, tuple(values))
                        result_ddbb = self.my_cursor.fetchall()

                        if self.marker_db == False:
                            messagebox.showerror(title="Buscar",
                                                 message="Base de datos inexistente, Por favor crear una base de datos")
                        elif not result_ddbb:
                            messagebox.showwarning(title="Buscar",
                                                   message="Los registros buscados no existen en la base de datos")
                        else:
                            for data in result_ddbb:
                                table.insert(
                                    parent="", index="end", values=data)
                            my_conection.close()
                except:
                    messagebox.showerror(
                        title="Error",
                        message="Ocurrio un error con la busqueda, por favor verificar la conexión con la base de datos")

    def update_data(self, list_stringVar):

        column_DDBB = (" Id = ?", " Fecha = ?,", " N_cliente = ?,", " Serial = ?,",
                       " T_medio = ?,", " Bahias = ?,", " Data_center = ?,",
                       " Modulo = ?,", " Rack_Unidad = ?,", " Estado = ?,",
                       " Comentarios = ?")

        try:
            query = "UPDATE DDBB_inventory_disk SET"
            values = tuple()
            id_data = list_stringVar[0].get()

            for sVar in list_stringVar:
                if list_stringVar[0] == sVar:
                    continue
                if not sVar.get():
                    messagebox.showwarning(title="Actualizar",
                                           message="No se admiten campos vacios, por favor completar todos los campos")
                    break

            else:
                for index in range(1, 11):
                    query += column_DDBB[index]
                    values += (list_stringVar[index].get(),)
                query += " WHERE " + column_DDBB[0]

                if self.marker_db == False:
                    messagebox.showerror(title="Actualizar",
                                         message="Base de datos inexistente, Por favor crear una base de datos")
                elif id_data.isdigit():
                    values += (int(id_data),)
                    self.my_cursor.execute(query, values)
                    self.my_conection.commit()

                    messagebox.showinfo(title="Actualizar",
                                        message="Datos actualizados con exito")
                    self.clear_fields(list_stringVar)
                else:
                    messagebox.showerror(title="Actualizar",
                                         message="No es posible actualizar estos registros, Registros no encontrados en la base de datos")
        except:
            messagebox.showerror(
                title="Error",
                message="Ocurrio un error al intentar actualizar, Por favor validar la conexión con la base de datos")

    def delete_data(self, list_stringVar):
        try:
            for index, sVar in enumerate(list_stringVar):
                if not index:
                    continue
                elif not sVar.get():
                    messagebox.showwarning(title="Eliminar registros",
                                           message="No se admiten campos vacios, por favor completar todos los campos")
                    break
            else:
                if self.marker_db == False:
                    messagebox.showerror(title="Eliminar registros",
                                         message="Base de datos inexistente, Por favor crear una base de datos")
                elif not list_stringVar[0].get().isdigit():
                    messagebox.showerror(
                        title="Eliminar registros",
                        message="No es posible eliminar estos registros, registros no encontrados en la base de datos")

                else:
                    id_data = int(list_stringVar[0].get())

                    question = messagebox.askyesno(
                        title="Eliminar registro",
                        message="¿Seguro que desea eliminar el registro de la base de datos?")

                    if question:
                        self.my_cursor.execute(
                            "DELETE FROM DDBB_inventory_disk WHERE Id = ?", (id_data,))
                        self.my_conection.commit()
                        messagebox.showinfo(
                            title="Eliminar registro", message="Registros eliminados con exito")
                        self.clear_fields(list_stringVar)
                    else:
                        pass
        except:
            messagebox.showerror(
                title="Error",
                message="Ocurrio un error al intentar eliminar los registros," /
                "Por favor validar la conexión con la base de datos")

    def clear_fields(self, list_stringVar):
        for variable in list_stringVar:
            variable.set("")
