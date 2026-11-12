import customtkinter as ctk

# Configuración inicial de la apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class ZeroLimitApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ZERO LIMIT - Terminal de Diagnóstico")
        self.geometry("850x650")

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(expand=True, fill="both")

        self.mostrar_menu_principal()

    def limpiar_pantalla(self):
        """Elimina todos los widgets de la pantalla actual para dibujar la siguiente."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def mostrar_menu_principal(self):
        self.limpiar_pantalla()

        label_titulo = ctk.CTkLabel(self.main_frame, text="ZERO LIMIT", 
                                    font=("Consolas", 200, "bold"), text_color="#00FF00", justify="left")
        label_titulo.pack(pady=(40, 5))

        subtitulo = ctk.CTkLabel(self.main_frame, text="PROYECTO: METODOS NUMERICOS (MODULO DE DIAGNOSTICO)", font=("Consolas", 14), text_color="#00FF00")
        subtitulo.pack(pady=(0, 30))

        # Botones Principales
        ctk.CTkButton(self.main_frame, text="[ MODO PRACTICA ]", font=("Consolas", 30, "bold"), fg_color="transparent", 
                      border_width=2, text_color="#00FF00", border_color="#00FF00", hover_color="#003300", 
                      command=self.mostrar_instrucciones_practica).pack(pady=10)

        ctk.CTkButton(self.main_frame, text="[ MODO DESAFIO ]", font=("Consolas", 30, "bold"), fg_color="transparent", 
                      border_width=2, text_color="#00FF00", border_color="#00FF00", hover_color="#003300").pack(pady=10)

        ctk.CTkLabel(self.main_frame, text="NOTA: Requiere conocimiento básico de álgebra y cálculo.", font=("Consolas", 15), text_color="gray").pack(side="bottom", pady=20)

    def mostrar_instrucciones_practica(self):
        self.limpiar_pantalla()

        ctk.CTkLabel(self.main_frame, text="ADVERTENCIA - MODO PRACTICA", font=("Consolas", 30, "bold"), text_color="yellow").pack(pady=(50, 20))

        instrucciones = (
            "SISTEMA EN MODO SEGURO.\n\n"
            "> Tómese su tiempo para analizar la telemetría.\n"
            "> Herramientas externas (calculadoras/apuntes) PERMITIDAS.\n"
            "> Protocolos de estrés (Temporizador y Escudos) DESACTIVADOS.\n\n"
            "Seleccione un expediente de falla para comenzar el diagnóstico."
        )
        ctk.CTkLabel(self.main_frame, text=instrucciones, font=("Consolas", 20), text_color="white", justify="center").pack(pady=20)

        ctk.CTkButton(self.main_frame, text="[ ACCEDER AL SISTEMA ]", font=("Consolas", 25, "bold"), fg_color="transparent", 
                      border_width=2, text_color="#00FF00", border_color="#00FF00", hover_color="#003300", 
                      command=self.mostrar_lista_errores).pack(pady=20)

        ctk.CTkButton(self.main_frame, text="[ CANCELAR ]", font=("Consolas", 25), fg_color="transparent", text_color="gray", hover_color="#333333", command=self.mostrar_menu_principal).pack(pady=10)

    def mostrar_lista_errores(self):
        self.limpiar_pantalla()

        ctk.CTkLabel(self.main_frame, text="C:\\> DIRECTORIO DE FALLAS DEL SISTEMA", font=("Consolas", 20, "bold"), text_color="#00FF00").pack(pady=(40, 30))

        # Usamos lambda para pasar el ID del problema al método siguiente
        ctk.CTkButton(self.main_frame, text="[ ERROR 01: Falla de Módulo de Descenso ]", font=("Consolas", 25), fg_color="transparent", 
                      border_width=1, text_color="white", border_color="gray", hover_color="#003300", width=400,
                      command=lambda: self.mostrar_diagnostico("ERR_01")).pack(pady=10)

        ctk.CTkButton(self.main_frame, text="[ ERROR 02: Telemetría Espaciada (Interpolación) ]", font=("Consolas", 25), fg_color="transparent", 
                      border_width=1, text_color="white", border_color="gray", hover_color="#003300", width=400,
                      command=lambda: self.mostrar_diagnostico("ERR_02")).pack(pady=10)

        ctk.CTkButton(self.main_frame, text="[ REGRESAR AL MENU ]", font=("Consolas", 25), fg_color="transparent", text_color="gray", hover_color="#333333", command=self.mostrar_menu_principal).pack(side="bottom", pady=30)

    def mostrar_diagnostico(self, id_error):
        self.limpiar_pantalla()

        if id_error == "ERR_01":
            titulo = "ERROR 01: ESTABILIZACION DE CAPSULA"
            datos = "Se requiere alcanzar velocidad terminal de 40 m/s a los 10s.\nMasa: 68.1 kg | Gravedad: 9.81 m/s²\n\nModelo: f(c) = [9.81(68.1)/c][1 - e^(-10c/68.1)] - 40 = 0"
            metodos = ["BISECCION", "FALSA POSICION"]
            
        elif id_error == "ERR_02":
            titulo = "ERROR 02: RECONSTRUCCION DE SENAL"
            datos = "Sensor falló en x=2. Se conservan puntos de calibración:\nx | 1 | 3 | 4 | 6\ny | 0.00 | 1.09 | 1.38 | 1.79\n\nEstime la señal en x=2."
            metodos = ["LAGRANGE", "NEWTON DIFERENCIAS DIVIDIDAS", "INTERPOLACION LINEAL"]

        ctk.CTkLabel(self.main_frame, text=f"> LEYENDO EXPEDIENTE: {titulo}", font=("Consolas", 18, "bold"), text_color="#00FF00").pack(pady=(30, 20))
        
        # Caja de datos del problema
        frame_datos = ctk.CTkFrame(self.main_frame, fg_color="#111111", border_width=1, border_color="#00FF00")
        frame_datos.pack(pady=10, padx=50, fill="x")
        ctk.CTkLabel(frame_datos, text=datos, font=("Consolas", 14), text_color="white", justify="left").pack(pady=20, padx=20)

        ctk.CTkLabel(self.main_frame, text="ANALISIS: PROTOCOLOS DE RECUPERACION VIABLES DETECTADOS", font=("Consolas", 14, "bold"), text_color="yellow").pack(pady=(20, 10))

        # Generar botones de métodos dinámicamente según el problema
        for metodo in metodos:
            ctk.CTkButton(self.main_frame, text=f"[ EJECUTAR PROTOCOLO: {metodo} ]", font=("Consolas", 14), fg_color="transparent", 
                          border_width=1, text_color="#00FF00", border_color="#00FF00", hover_color="#003300", width=350,
                          command=lambda m=metodo: self.iniciar_calculo(id_error, m)).pack(pady=5)

        ctk.CTkButton(self.main_frame, text="[ VOLVER AL DIRECTORIO ]", font=("Consolas", 20), fg_color="transparent", text_color="gray", hover_color="#333333", command=self.mostrar_lista_errores).pack(side="bottom", pady=20)

    def iniciar_calculo(self, id_error, metodo_elegido):
        print(f"Lanzando motor de cálculo: Problema {id_error} usando {metodo_elegido}")
        # Aquí conectaremos la siguiente pantalla donde el jugador ingresa sus iteraciones o respuestas.

if __name__ == "__main__":
    app = ZeroLimitApp()
    app.mainloop()