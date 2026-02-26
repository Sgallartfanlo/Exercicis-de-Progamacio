contrasenya="secreta123"

intent=str(input("Introdueix la contrasenya per poder accedir: "))

if intent==contrasenya:
    print("Accés permès")
else:
    print("Accés denegat")