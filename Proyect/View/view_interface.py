import os
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from .functions_interface import Functions
from .view_styles import Styles

# 1296


class View():
    __width = 1300
    __height = 705
    __list_r_u = ["N/A"]
    __list_data = ["Jupiter data", "Saturno data",
                   "Wbp-01", "Wbp-02", "Wbp-oficina"]
    __list_storageType = ["USB", "Sata", "Cinta"]
    __list_bahias = ["13", "14", "15", "16", "17",
                     "18", "19", "20", "21", "22",
                     "23", "N/A"]
    __list_modulos = ["A", "B", "C", "D", "N/A"]
    __list_estado = ["Conectado", "Desconectado",
                     "Recibido", "Retirado"]

    def __init__(self, root, model):

        self.root = root
        self.path_icono = os.path.join(os.path.dirname(__file__),
                                       "..", "Images", "logo.ico")
        self.my_frame = ttk.Frame(master=self.root)
        self.table = ttk.Treeview(master=self.my_frame)

        self.my_id = tk.StringVar()
        self.my_fecha = tk.StringVar()
        self.my_cliente = tk.StringVar()
        self.my_serial = tk.StringVar()
        self.my_storageType = tk.StringVar()
        self.my_dataCenter = tk.StringVar()
        self.my_bahias = tk.StringVar()
        self.my_modulo = tk.StringVar()
        self.my_rackUnidad = tk.StringVar()
        self.my_estado = tk.StringVar()
        self.my_comments = tk.StringVar()
        self.list_stringVar = [

            self.my_id, self.my_fecha, self.my_cliente, self.my_serial,
            self.my_storageType, self.my_bahias, self.my_dataCenter,
            self.my_modulo, self.my_rackUnidad, self.my_estado, self.my_comments
        ]
        self.label_bahias = None
        self.entry_bahias = None
        self.label_modulos = None
        self.entry_modulos = None

        self.model = model
        self.functions = Functions(self.root, self.my_frame, model)
        self.styles = Styles()

        self.config_root()
        self.menu_root()
        self.labels_entrys()
        self.buttons()
        self.table_data()

    def config_root(self):
        self.root.title("Inventario de medios de almacenamiento")
        self.root.geometry(f"{self.__width}x{self.__height}+0+0")
        self.root.iconbitmap(self.path_icono)
        self.my_frame.pack(fill=tk.BOTH, expand=True)

    def menu_root(self):
        bar_menu = tk.Menu(self.my_frame)
        inicio = tk.Menu(bar_menu, tearoff=0)

        inicio.add_command(label="Crear BD",
                           command=lambda: self.model.conection_dataBase())
        inicio.add_command(label="Borrar BD",
                           command=lambda: self.model.delete_dataBase())
        inicio.add_command(
            label="Salir", command=lambda: self.functions.Exit())
        bar_menu.add_cascade(label="Inicio", menu=inicio)

        ayuda = tk.Menu(bar_menu, tearoff=0)
        ayuda.add_command(label="Limpiar campos",
                          command=lambda: self.functions.clear_fields(self.list_stringVar))
        ayuda.add_command(label="Limpiar tabla",
                          command=lambda: self.functions.clear_table(self.table))
        ayuda.add_command(label="Acerca de",
                          command=lambda: self.functions.about())
        bar_menu.add_cascade(label="Ayuda", menu=ayuda)

        self.root.config(menu=bar_menu)

    def labels_entrys(self):
        # FRAME LABELS & ENTRYS
        frame_labelsEntrys = ttk.Frame(master=self.my_frame)
        frame_labelsEntrys.place(
            x=0, y=-280, relx=0.5, rely=0.5, anchor="center")

        # FECHA
        label_date = ttk.Label(master=frame_labelsEntrys,
                               text="Fecha", font=(10))
        label_date.grid(row=0, column=0, padx=2, pady=5, sticky=tk.E)
        entry_date = DateEntry(master=frame_labelsEntrys, textvariable=self.my_fecha, width=10,
                               background="darkblue", foreground="white", borderwidth=2,
                               date_pattern="dd-mm-yyyy")
        entry_date.grid(row=0, column=1, padx=2, pady=5, sticky=tk.W)

        # CLIENTE
        label_customer = ttk.Label(
            master=frame_labelsEntrys, text="Cliente", font=(10))
        label_customer.grid(row=1, column=0, padx=2, pady=5, sticky=tk.E)
        entry_customer = ttk.Entry(
            master=frame_labelsEntrys, textvariable=self.my_cliente, width=29)
        entry_customer.grid(row=1, column=1, padx=2,
                            pady=5, sticky=tk.W, columnspan=3)

        # SERIAL
        label_serialNumber = ttk.Label(
            master=frame_labelsEntrys, text="Serial / codigo", font=(12))
        label_serialNumber.grid(row=2, column=0, padx=2, pady=5, sticky=tk.E)
        entry_serialNumber = ttk.Entry(
            master=frame_labelsEntrys, textvariable=self.my_serial, width=29)
        entry_serialNumber.grid(row=2, column=1, padx=2,
                                pady=5, sticky=tk.W, columnspan=3)

        # BAHIAS SATA
        self.label_bahias = ttk.Label(
            master=frame_labelsEntrys, text="Bahia", font=(12))
        self.entry_bahias = ttk.Combobox(
            master=frame_labelsEntrys, textvariable=self.my_bahias, width=4, values=self.__list_bahias)
        self.entry_bahias.bind("<<ComboboxSelected>>",
                               lambda event: self.entry_bahias.select_clear())

        # TIPO DE MEDIO
        label_mediaType = ttk.Label(master=frame_labelsEntrys, text="Tipo de medio",
                                    font=(12))
        label_mediaType.grid(row=3, column=0, padx=2, pady=5, sticky=tk.E)
        entry_mediumStorage = ttk.Combobox(master=frame_labelsEntrys, textvariable=self.my_storageType,
                                           values=self.__list_storageType, width=10,)
        entry_mediumStorage.grid(row=3, column=1, padx=2, pady=5, sticky=tk.W)
        entry_mediumStorage.bind("<<ComboboxSelected>>",
                                 lambda event: self.functions.showHide_bahias(entry_mediumStorage, self.my_storageType,
                                                                              self.my_bahias, self.label_bahias, self.entry_bahias)
                                 )

        # -----------------------------------------------------------------------------------
        # LABEL SPACE
        label_space = ttk.Label(master=frame_labelsEntrys, text=" "*25)
        label_space.grid(row=0, column=4, padx=30, pady=5)

        # MODULOS DATA CENTER
        self.label_modulos = ttk.Label(
            master=frame_labelsEntrys, text="Modulo", font=(12))
        self.entry_modulos = ttk.Combobox(master=frame_labelsEntrys, textvariable=self.my_modulo,
                                          values=self.__list_modulos, width=4)
        self.entry_modulos.bind("<<ComboboxSelected>>",
                                lambda event: self.entry_modulos.select_clear())

        # DATA CENTER
        label_dataCenter = ttk.Label(
            master=frame_labelsEntrys, text="Data center", font=(12))
        label_dataCenter.grid(row=0, column=5, padx=2, pady=5, sticky=tk.E)
        entry_dataCenter = ttk.Combobox(
            master=frame_labelsEntrys, textvariable=self.my_dataCenter, values=self.__list_data, width=13)
        entry_dataCenter.grid(row=0, column=6, padx=2, pady=5, sticky=tk.W)
        entry_dataCenter.bind("<<ComboboxSelected>>",
                              lambda event: self.functions.showHide_modulos(entry_dataCenter, self.my_dataCenter,
                                                                            self.my_modulo, self.label_modulos,
                                                                            self.entry_modulos))

        # RACK / UNIDAD
        label_rack = ttk.Label(master=frame_labelsEntrys,
                               text="Rack / Unidad", font=(12))
        label_rack.grid(row=1, column=5, padx=2, pady=5, sticky=tk.E)
        entry_rack = ttk.Combobox(
            master=frame_labelsEntrys, textvariable=self.my_rackUnidad, values=self.__list_r_u, width=13)
        entry_rack.grid(row=1, column=6, padx=2, pady=5, sticky=tk.W)
        entry_rack.bind("<<ComboboxSelected>>",
                        lambda event: entry_rack.select_clear())

        # ESTADO
        label_state = ttk.Label(
            master=frame_labelsEntrys, text="Estado", font=(12))
        label_state.grid(row=2, column=5, padx=2, pady=5, sticky=tk.E)
        entry_state = ttk.Combobox(master=frame_labelsEntrys, textvariable=self.my_estado,
                                   values=self.__list_estado, width=13)
        entry_state.grid(row=2, column=6, padx=2, pady=5, sticky=tk.W)
        entry_state.bind("<<ComboboxSelected>>",
                         lambda event: entry_state.select_clear())

        # COMENTARIOS
        label_comments = ttk.Label(
            master=frame_labelsEntrys, text="Comentarios", font=(12))
        label_comments.grid(row=3, column=5, padx=2, pady=5, sticky=tk.E)
        entry_comments = ttk.Combobox(
            master=frame_labelsEntrys, textvariable=self.my_comments, width=35,
            values=self.__list_r_u)
        entry_comments.bind("<<ComboboxSelected>>",
                            lambda event: entry_comments.select_clear())
        entry_comments.grid(row=3, column=6, padx=2,
                            pady=5, sticky=tk.W, columnspan=3)

    def buttons(self):
        # GUARDAR EN MASIVO
        button_add_massive = ttk.Button(
            master=self.my_frame, text="Guardar en masivo", padding=(4, 4),
            command=lambda: self.functions.open_popup_window(
                self.list_stringVar),
            style="styleButton.TButton")
        button_add_massive.config(takefocus=False)
        button_add_massive.bind("<Enter>",
                                lambda event: button_add_massive.config(cursor="hand2"))
        button_add_massive.bind("<Leave>",
                                lambda event: button_add_massive.config(cursor=""))
        button_add_massive.place(
            x=-582, y=-180, relx=0.5, rely=0.5, anchor="center")

        # FRAME BUTTONS
        frame_buttons = ttk.Frame(master=self.my_frame)
        frame_buttons.place(x=0, y=-180, relx=0.5, rely=0.5, anchor="center")

        # BUSCAR
        button_search = ttk.Button(
            master=frame_buttons, text="Buscar", padding=(0, 4),
            command=lambda: self.model.search_data(
                self.list_stringVar, self.table),
            style="styleButton.TButton")
        button_search.grid(row=0, column=0, padx=5, pady=5)
        button_search.config(takefocus=False)
        button_search.bind("<Enter>",
                           lambda event: button_search.config(cursor="hand2"))
        button_search.bind("<Leave>",
                           lambda event: button_search.config(cursor=""))

        # GUARDAR
        button_save = ttk.Button(master=frame_buttons, text="Guardar",
                                 padding=(0, 4), command=lambda:
                                 self.model.save_data(
                                     self.list_stringVar, event="button_save"),
                                 style="styleButton.TButton")
        button_save.grid(row=0, column=1, padx=5, pady=5)
        button_save.config(takefocus=False)
        button_save.bind("<Enter>",
                         lambda event: button_save.config(cursor="hand2"))
        button_save.bind("<Leave>",
                         lambda event: button_save.config(cursor=""))

        # ACTUALIZAR
        button_update = ttk.Button(master=frame_buttons, text="Actualizar",
                                   padding=(0, 4), command=lambda:
                                   self.model.update_data(self.list_stringVar),
                                   style="styleButton.TButton")
        button_update.grid(row=0, column=2, padx=5, pady=5)
        button_update.config(takefocus=False)
        button_update.bind("<Enter>",
                           lambda event: button_update.config(cursor="hand2"))
        button_update.bind("<Leave>",
                           lambda event: button_update.config(cursor=""))

        # LIMPIAR TABLA
        button_clearTable = ttk.Button(master=frame_buttons, text="Limpiar tabla",
                                       padding=(4, 4), command=lambda:
                                       self.functions.clear_table(self.table),
                                       style="styleButton.TButton")
        button_clearTable.grid(row=0, column=3, padx=5, pady=5)
        button_clearTable.config(takefocus=False)
        button_clearTable.bind("<Enter>",
                               lambda event: button_clearTable.config(cursor="hand2"))
        button_clearTable.bind("<Leave>",
                               lambda event: button_clearTable.config(cursor=""))

        # LIMPIAR CAMPOS
        button_clearFields = ttk.Button(
            master=frame_buttons, text="Limpiar campos", padding=(4, 4), command=lambda:
            self.functions.clear_fields(self.list_stringVar), style="styleButton.TButton")
        button_clearFields.grid(row=0, column=4, padx=5, pady=5)
        button_clearFields.config(takefocus=False)
        button_clearFields.bind("<Enter>",
                                lambda event: button_clearFields.config(cursor="hand2"))
        button_clearFields.bind("<Leave>",
                                lambda event: button_clearFields.config(cursor=""))

        # ELIMINAR REGISTROS
        button_delete = ttk.Button(master=self.my_frame, text="Eliminar registros",
                                   padding=(4, 4), command=lambda:
                                   self.model.delete_data(
                                       self.list_stringVar),
                                   style="styleButton_delete.TButton")
        button_delete.place(
            x=585, y=-180, relx=0.5, rely=0.5, anchor="center")
        button_delete.config(takefocus=False)
        button_delete.bind("<Enter>",
                           lambda event: button_delete.config(cursor="hand2"))
        button_delete.bind("<Leave>",
                           lambda event: button_delete.config(cursor=""))

    def table_data(self):
        scroll_table = ttk.Scrollbar(
            master=self.my_frame, command=self.table.yview, orient="vertical")
        scroll_table.place(x=636, y=107, relx=0.5, rely=0.5,
                           anchor="center", height=483)
        self.table.configure(yscrollcommand=scroll_table.set)

        self.table.config(columns=["ID", "Fecha", "N_cliente", "N°_serial",
                                   "t_medio", "Bahia", "D_center", "Modulo",
                                   "Rack_Unidad", "Estado", "comentarios"],
                          height=24, show="headings")

        self.table.place(x=0, y=94, relx=0.5, rely=0.5, anchor="center")

        # COLUMNA ID
        self.table.heading(column="ID", text="ID", anchor="w")
        self.table.column(column="ID", width=1, minwidth=1)

        # COLUMNA FECHA
        self.table.heading(column="Fecha", text="Fecha", anchor="center")
        self.table.column(column="Fecha", width=100,
                          stretch="yes", anchor="center")

        # COLUMNA CLIENTE
        self.table.heading(
            column="N_cliente", text="Nombre del cliente", anchor="center")
        self.table.column(column="N_cliente", width=200,
                          stretch="yes", anchor="center")

        # COLUMNA SERIAL
        self.table.heading(column="N°_serial",
                           text="N° Serial", anchor="center")
        self.table.column(column="N°_serial", width=200,
                          stretch="yes", anchor="center")

        # COLUMNA CONEXIÓN
        self.table.heading(
            column="t_medio", text="Tipo/medio", anchor="center")
        self.table.column(column="t_medio", width=75,
                          stretch="yes", anchor="center")

        # COLUMNA BAHIA
        self.table.heading(column="Bahia", text="Bahia", anchor="center")
        self.table.column(column="Bahia", width=50,
                          stretch="yes", anchor="center")

        # COLUMNA DATA CENTER
        self.table.heading(column="D_center",
                           text="Data center", anchor="center")
        self.table.column(column="D_center", width=150,
                          stretch="yes", anchor="center")

        # COLUMNA MODULO
        self.table.heading(column="Modulo", text="Modulo", anchor="center")
        self.table.column(column="Modulo", width=65,
                          stretch="yes", anchor="center")

        # COLUMNA RACK / UNIDAD
        self.table.heading(column="Rack_Unidad",
                           text="Rack Unidad", anchor="center")
        self.table.column(column="Rack_Unidad", width=100,
                          stretch="yes", anchor="center")

        # COLUMNA ESTADO
        self.table.heading(column="Estado", text="Estado", anchor="center")
        self.table.column(column="Estado", width=120,
                          stretch="yes", anchor="center")

        # COLUMNA COMENTARIOS

        self.table.heading(column="comentarios",
                           text="Comentarios", anchor="center")
        self.table.column(column="comentarios", width=225,
                          stretch="yes", anchor="center")

        self.table.bind("<Double-Button-1>",
                        lambda event: self.functions.doubleClic_setFields(self.table, self.list_stringVar,
                                                                          self.label_bahias, self.entry_bahias,
                                                                          self.label_modulos, self.entry_modulos))

        self.table.bind("<MouseWheel>",
                        lambda event: self.table.yview_scroll(int(-1*(event.delta/120)), "units"))
