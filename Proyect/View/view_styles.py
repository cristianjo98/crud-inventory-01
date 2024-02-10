from tkinter import ttk
import tkinter as tk


class Styles():
    def __init__(self):
        self.styles = ttk.Style()
        self.styles.theme_use("clam")
        self.style_buttons()
        self.style_ButtonDelete()

    def style_buttons(self):
        self.styles.configure("styleButton.TButton", background="#8E8E8E",
                              foreground="#FFFFFF", font="Arial_Rounded_MT_Bold 9 bold",
                              relief="raised")
        self.styles.map("styleButton.TButton",background=[("active", "#FCFCFC")],
                        foreground=[("active", "#000000")])
    
    def style_ButtonDelete(self):
        self.styles.configure("styleButton_delete.TButton", background="#CE0000",
                              foreground="#FFFFFF", font="Arial_Rounded_MT_Bold 9 bold",
                              relief="raised")
        self.styles.map("styleButton_delete.TButton",background=[("active", "#CE0000")],
                        foreground=[("active", "#FFFFFF")])
