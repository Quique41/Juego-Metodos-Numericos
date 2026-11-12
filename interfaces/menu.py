import customtkinter as ctk

class VistaMenu(ctk.CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="transparent")
        self.controlador = controlador
        self.construir_ui()

    def construir_ui(self):
        ctk.CTkLabel(self, text="ZERO LIMIT", font=("Consolas", 100, "bold"), text_color="#00FF00").pack(pady=(40, 5))
        ctk.CTkLabel(self, text="PROYECTO: METODOS NUMERICOS (MODULO DE DIAGNOSTICO)", font=("Consolas", 14), text_color="#00FF00").pack(pady=(0, 30))

        # El botón ahora le dice al controlador que cambie a la vista de práctica
        ctk.CTkButton(self, text="[ MODO PRACTICA ]", font=("Consolas", 40, "bold"), fg_color="transparent", 
                      border_width=2, text_color="#00FF00", border_color="#00FF00", hover_color="#003300", 
                      command=lambda: self.controlador.mostrar_vista("practica")).pack(pady=10)

        ctk.CTkButton(self, text="[ MODO DESAFIO ]", font=("Consolas", 40, "bold"), fg_color="transparent", 
                      border_width=2, text_color="#00FF00", border_color="#00FF00", hover_color="#003300").pack(pady=10)

        ctk.CTkLabel(self, text="NOTA: Para poder prácticar se requieren conocimientos básicos de álgebra y cálculo.", font=("Consolas", 20), text_color="gray").pack(side="bottom", pady=20)
        
        ctk.CTkButton(self, text="[ MANUAL DEL INGENIERO ]", font=("Consolas", 20, "bold"), fg_color="transparent", 
                      border_width=2, text_color="yellow", border_color="yellow", hover_color="#333300",
                      command=lambda: self.controlador.mostrar_vista("manual")).pack(pady=(30, 10))