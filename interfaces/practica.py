import customtkinter as ctk
from logica.gestor_problemas import GestorProblemas
from logica.gestor_practica import GestorPractica

class VistaPractica(ctk.CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="transparent")
        self.controlador = controlador
        self.gestor = GestorPractica()
        
        # Arrancamos mostrando las instrucciones en lugar del directorio
        self.mostrar_instrucciones()

    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def mostrar_instrucciones(self):
        self.limpiar_frame()

        ctk.CTkLabel(self, text="ADVERTENCIA - MODO PRACTICA", font=("Consolas", 30, "bold"), text_color="yellow").pack(pady=(50, 20))

        instrucciones = (
            "SISTEMA EN MODO SEGURO.\n\n"
            "> Tómese su tiempo para analizar la telemetría.\n"
            "> Herramientas externas (calculadoras/apuntes) PERMITIDAS.\n"
            "> Protocolos de estrés (Temporizador y Escudos) DESACTIVADOS.\n\n"
            "Seleccione un expediente de falla para comenzar el diagnóstico."
        )
        ctk.CTkLabel(self, text=instrucciones, font=("Consolas", 20), text_color="white", justify="center").pack(pady=20)

        # Este botón ahora nos lleva al directorio de problemas
        ctk.CTkButton(self, text="[ ACCEDER AL SISTEMA ]", font=("Consolas", 25, "bold"), fg_color="transparent", 
                      border_width=2, text_color="#00FF00", border_color="#00FF00", hover_color="#003300", 
                      command=self.mostrar_directorio).pack(pady=20)

        # Regresa al menú principal usando el enrutador
        ctk.CTkButton(self, text="[ CANCELAR ]", font=("Consolas", 25), fg_color="transparent", text_color="gray", hover_color="#333333", 
                      command=lambda: self.controlador.mostrar_vista("menu")).pack(pady=10)

    def mostrar_directorio(self):
        self.limpiar_frame()
        ctk.CTkLabel(self, text="C:\\> DIRECTORIO DE FALLAS", font=("Consolas", 20, "bold"), text_color="#00FF00").pack(pady=(40, 30))

        ctk.CTkButton(self, text="[ PB_03: Falla de Módulo de Descenso ]", font=("Consolas", 25), fg_color="transparent", 
                      border_width=1, text_color="white", border_color="gray", hover_color="#003300", width=400,
                      command=lambda: self.iniciar_diagnostico("PB_03")).pack(pady=10)

        ctk.CTkButton(self, text="[ REGRESAR AL MENU ]", font=("Consolas", 20), fg_color="transparent", text_color="gray", hover_color="#333333", 
                      command=lambda: self.controlador.mostrar_vista("menu")).pack(side="bottom", pady=30)

    def iniciar_diagnostico(self, id_problema):
        problema = GestorProblemas.obtener_problema(id_problema)
        if not problema:
            return 

        if not self.gestor.inicializar_sesion(problema):
            return 

        self.limpiar_frame()
        ctk.CTkLabel(self, text=f"> {problema['titulo']}", font=("Consolas", 20, "bold"), text_color="#00FF00").pack(pady=(30, 10))
        ctk.CTkLabel(self, text=problema["contexto"], font=("Consolas", 14), text_color="white").pack(pady=10)
        
        self.frame_juego = ctk.CTkFrame(self, fg_color="#111111", border_width=1, border_color="#00FF00")
        self.frame_juego.pack(pady=20, padx=50, fill="x")

        self.label_instruccion = ctk.CTkLabel(self.frame_juego, text="", font=("Consolas", 16), text_color="yellow")
        self.label_instruccion.pack(pady=20)

        self.entrada_jugador = ctk.CTkEntry(self.frame_juego, font=("Consolas", 18), width=150, justify="center")
        self.entrada_jugador.pack(pady=10)

        self.label_feedback = ctk.CTkLabel(self.frame_juego, text="", font=("Consolas", 14))
        self.label_feedback.pack(pady=10)

        ctk.CTkButton(self.frame_juego, text="[ ENVIAR DATOS ]", font=("Consolas", 16, "bold"), fg_color="transparent", 
                      border_width=2, text_color="#00FF00", border_color="#00FF00", hover_color="#003300", 
                      command=self.procesar_respuesta).pack(pady=20)
        
        # --- NUEVO CONTENEDOR PARA LOS BOTONES INFERIORES ---
        frame_botones_inferiores = ctk.CTkFrame(self, fg_color="transparent")
        frame_botones_inferiores.pack(side="bottom", pady=20)

        ctk.CTkButton(frame_botones_inferiores, text="[ CONSULTAR MANUAL ]", font=("Consolas", 14), fg_color="transparent", 
                      border_width=1, text_color="yellow", border_color="yellow", hover_color="#333300", 
                      command=lambda: self.controlador.mostrar_vista("manual")).pack(side="left", padx=10)

        ctk.CTkButton(frame_botones_inferiores, text="[ ABORTAR DIAGNOSTICO ]", font=("Consolas", 14), fg_color="transparent", 
                      text_color="gray", hover_color="#333333", command=self.mostrar_directorio).pack(side="left", padx=10)

        self.actualizar_paso()

    def actualizar_paso(self):
        datos_paso = self.gestor.obtener_datos_paso_actual()
        if not datos_paso:
            self.label_instruccion.configure(text="¡MÓDULO ESTABILIZADO! Diagnóstico completado.")
            self.entrada_jugador.configure(state="disabled")
            return

        texto = f"ITERACIÓN {datos_paso['iteracion']} | a = {datos_paso['a']}, b = {datos_paso['b']}\nIngrese el valor del punto medio (x):"
        self.label_instruccion.configure(text=texto)
        self.entrada_jugador.delete(0, 'end')
        self.label_feedback.configure(text="")

    def procesar_respuesta(self):
        try:
            valor = float(self.entrada_jugador.get())
        except ValueError:
            self.label_feedback.configure(text="Error: Ingrese un numérico válido.", text_color="red")
            return

        correcto, valor_real = self.gestor.verificar_respuesta(valor)
        if correcto:
            self.label_feedback.configure(text=f"¡Correcto! x = {valor_real}", text_color="#00FF00")
            self.after(1500, self.actualizar_paso)
        else:
            self.label_feedback.configure(text="Datos incorrectos. Revisa tus cálculos.", text_color="red")