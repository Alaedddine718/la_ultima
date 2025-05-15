class CLIController:
    def __init__(self, poll_service, user_service, nft_service):
        self.poll_service = poll_service
        self.user_service = user_service
        self.nft_service = nft_service
        self.usuario_actual = None
        self.token_sesion = None

    def ejecutar(self):
        while True:
            comando = input(">> ").strip().lower()
            if comando == "registrar":
                u = input("usuario: ")
                p = input("contraseña: ")
                self.user_service.registrar(u, p)
                print("Registrado correctamente.")
            elif comando == "login":
                u = input("usuario: ")
                p = input("contraseña: ")
                token = self.user_service.login(u, p)
                self.usuario_actual = u
                self.token_sesion = token
                print("Sesión iniciada.")
            elif comando == "crear_encuesta":
                if not self.usuario_actual:
                    print("Primero inicia sesión.")
                    continue
                pregunta = input("Pregunta: ")
                opciones = input("Opciones separadas por coma: ").split(",")
                duracion = int(input("Duración en segundos: "))
                eid = self.poll_service.crear_encuesta(pregunta, opciones, duracion)
                print(f"Encuesta creada con ID {eid}")
            elif comando == "votar":
                pid = input("ID de encuesta: ")
                opcion = input("Opción: ")
                try:
                    self.poll_service.votar(pid, self.usuario_actual, opcion)
                    self.nft_service.generar_token(self.usuario_actual, pid, opcion)
                    print("Voto registrado y token generado.")
                except Exception as e:
                    print(f"Error: {e}")
            elif comando == "resultados":
                pid = input("ID de encuesta: ")
                resultados = self.poll_service.obtener_resultados(pid)
                for op, val in resultados.items():
                    print(f"{op}: {val}")
            elif comando == "cerrar_encuesta":
                pid = input("ID de encuesta: ")
                self.poll_service.cerrar_encuesta(pid)
                print("Encuesta cerrada.")
            elif comando == "mis_tokens":
                tokens = self.nft_service.obtener_tokens_usuario(self.usuario_actual)
                for t in tokens:
                    print(t)
            elif comando == "salir":
                break
            else:
                print("Comando no reconocido.")
