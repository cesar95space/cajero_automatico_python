# ==============================
#        CAJERO AUTOMÁTICO
# ==============================

# Diccionario donde se guardan los usuarios
usuarios = {}

# -------- REGISTRAR USUARIO --------
def registrar():
    print("\n=== 📝 REGISTRO DE USUARIO ===")

    nombre = input("Ingrese un nombre de usuario: ")

    # verificar si el usuario ya existe
    if nombre in usuarios:
        print("❌ El usuario ya existe")
        return

    clave = input("Cree una clave de 4 dígitos: ")

    # validar clave de 4 números
    if not clave.isdigit() or len(clave) != 4:
        print("❌ La clave debe tener exactamente 4 números")
        return

    # permitir saldo inicial (puede ser 0)
    try:
        saldo_inicial = int(input("Ingrese saldo inicial (puede ser 0): "))
    except ValueError:
        print("❌ Debe ingresar un número")
        return

    # guardar usuario en el diccionario
    usuarios[nombre] = {"clave": clave, "saldo": saldo_inicial}

    print(f"✅ Usuario creado con saldo: ${saldo_inicial}")

# -------- LOGIN --------
def login():
    print("\n=== 🔐 LOGIN ===")

    nombre = input("Usuario: ")
    clave = input("Clave: ")

    # validar usuario y clave
    if nombre in usuarios and usuarios[nombre]["clave"] == clave:
        print(f"\n✅ Bienvenido {nombre}")
        menu(nombre)
    else:
        print("❌ Usuario o clave incorrectos")

# -------- MENÚ PRINCIPAL --------
def menu(usuario):
    while True:
        print("\n==============================")
        print("🏧      MENÚ CAJERO")
        print("==============================")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_saldo(usuario)

        elif opcion == "2":
            retirar(usuario)

        elif opcion == "3":
            depositar(usuario)

        elif opcion == "4":
            print("🔒 Sesión cerrada")
            break

        else:
            print("❌ Opción inválida")

# -------- CONSULTAR SALDO --------
def consultar_saldo(usuario):
    saldo = usuarios[usuario]["saldo"]
    print(f"\n💰 Su saldo actual es: ${saldo}")

# -------- RETIRAR DINERO --------
def retirar(usuario):
    saldo_actual = usuarios[usuario]["saldo"]

    try:
        monto = int(input("Ingrese monto a retirar: "))

        if monto <= 0:
            print("❌ El monto debe ser mayor a 0")

        elif monto > saldo_actual:
            print(f"❌ Fondos insuficientes. Su saldo es: ${saldo_actual}")

        else:
            # restar dinero al saldo
            usuarios[usuario]["saldo"] -= monto

            print("✅ Retiro exitoso")
            print(f"💰 Usted retiró: ${monto}")
            print(f"💰 Saldo restante: ${usuarios[usuario]['saldo']}")

    except ValueError:
        print("❌ Ingrese un número válido")

# -------- DEPOSITAR DINERO --------
def depositar(usuario):
    try:
        monto = int(input("Ingrese monto a depositar: "))

        if monto <= 0:
            print("❌ El monto debe ser mayor a 0")

        else:
            # sumar dinero al saldo
            usuarios[usuario]["saldo"] += monto

            print("✅ Depósito exitoso")
            print(f"💰 Usted depositó: ${monto}")
            print(f"💰 Saldo actual: ${usuarios[usuario]['saldo']}")

    except ValueError:
        print("❌ Ingrese un número válido")

# -------- MENÚ INICIAL DEL SISTEMA --------
def inicio():
    while True:
        print("\n==============================")
        print("🏧  CAJERO AUTOMÁTICO APP")
        print("==============================")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar()

        elif opcion == "2":
            login()

        elif opcion == "3":
            print("👋 Gracias por usar el cajero")
            break

        else:
            print("❌ Opción inválida")

# -------- EJECUTAR APP --------
inicio()