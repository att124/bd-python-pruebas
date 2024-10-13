#Main

from base_datos.conexion import Conexion

base_datos="base_datos/usuarios2.db"
conexion=Conexion(base_datos)

conexion.crear_tabla_usuario()

conexion.insertar_usuario(42138038,"Daniel","At","Administrador")

conexion.editar_usuario(42138038,"Dante","AAA","Usuario")

#conexion.eliminar_usuario(42138038)

usuarios = conexion.mostrar_usuario()




#Mostrar cliente

for fila in usuarios:
    print(fila)

conexion.cerrar_conexion()


