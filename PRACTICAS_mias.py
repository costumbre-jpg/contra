import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("🔐 Generador de Contraseñas Seguras")
    try:
        longitud = int(input("¿Cuántos caracteres debe tener la contraseña? "))
        if longitud < 4:
            print("⚠️ La longitud mínima debe ser 4 caracteres.")
            return
        contraseña = generar_contraseña(longitud)
        print(f"✅ Tu contraseña segura es: {contraseña}")
    except ValueError:
        print("❌ Por favor ingresa un número válido.")

if __name__ == "__main__":
    main()
