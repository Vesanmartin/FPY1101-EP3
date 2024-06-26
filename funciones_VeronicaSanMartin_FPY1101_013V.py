import os
libreria=[]

def registrar_libro():  ##menu para registrar libros
    titulo= input("Favor ingresar titulo libro :").lower
    autor =input("Favor ingrese autor libro :")
    publicacion= input("Ingrese año de publicacion :")
    sku=input("Ingrese SKU :")

    libros={"titulo": titulo,
        "autor": autor,
        "publicacion": publicacion,
        "sku":sku
        }
    libreria.append(libros)
    print("Libro registrado exitosamente")

def prestamo_libros():
    sku=input("Ingrese SKU libro")
    usuario=input("Ingrese usuario")
    libro_disponible=input("ingrese libro")
    libro_ptmo= input("ingrese estado. 1 si se encuentra prestado")
    fecha_ptmo=input("Ingrese fecha ptmo")
    print(f"sku {sku}, usuario {usuario}, libro disponible {libro_disponible}, estado ptmo {libro_ptmo}, fecha_ptmo {fecha_ptmo}")


def listar_libros():
    if not prestamo_libros:
        print("No hay libros prestados")
        return
    for i, libros in enumerate(libreria, start=1):
        print(f"{i}, libros {libros['titulo']} Autor {libros['autor']} Año publicacion {libros['publicacion']} SKU {libros['sku']}")


    
def reporte_prestamos():
    print("*** Imprimir reporte libros prestamos de libreria")
    planilla=input("Ingrese reporte. Ingrese 0 para todos")
    if planilla=="0":
        nombre_archivo="informe libros prestamos.txt"
        with open (nombre_archivo,"w") as archivo:
            archivo.write ("**Imprimir reporte prestamos de libreria.{'prestamo_libros'.capiutalized()}**\n")
            archivo.write(f"usuario {prestamo_libros['usuario']}\n")
            archivo.write(f"Titulo {prestamo_libros['libro_ptmo']}\n")
            archivo.write(f"fecha ptmo {prestamo_libros['fecha_ptmo']}")
            print("se ha generado el archivo '{nombre_archivo}' con los libros prestados")

def menu ():   #menu principal
    while True:
        try: 
            print("Sistema de Gestion de libros biblioteca.")
            opcion=input("Favor ingrese su opcion: \n 1- Registrar libro  \n 2. Prestar libro \n 3. Listar todos los libros.\n 4.-Imprimir reporte de prestamos. \n 5.-Salir del programa. \nOpcion   :")
            if opcion=="1":
                registrar_libro()
            elif opcion=="2":
                prestamo_libros()
            elif opcion=="3":
                listar_libros()
            elif opcion=="4":
                reporte_prestamos()
            elif opcion=="5":
                print("Programa finalizado.\n Desarrollado por Veronica San Martin \n RUT: 15.461.735-3")
            else:
                print("Opcion no valida. Intente nuevamente.")
        except ValueError:
            print("Dato erroneo. Intente nuevamente")
          
if __name__=="__main__":
    menu()
