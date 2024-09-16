import mysql.connector #pip install mysql-connector-python→ instalar libreria

'''
#1)INSERT EN TABLA PROVEEDORES
conexion1=mysql.connector.connect(host="127.0.0.1", user="root",passwd="3929",database="ejer_2_SQL") #variable de conexion.
cursor=conexion1.cursor()
sql1="insert into Proveedores(Nombre, Direccion , Telefono, Email) values(%s,%s,%s,%s)"#los values deben coincidir con la cantidad de %s
datos1= ("Proveedor K","Avenida k78, Ciudad k","888888888","proveedork@example.com")#variable de datos a insertar
cursor.execute(sql1,datos1)

conexion1.commit()     #subida del insert a la base de datos
print("Datos insertados correctamente en ambas tablas.")

#INSERT EN TABLA PRODUCTOS
sql2="insert into Productos(Nombre, Descripcion , Tipo, Precio,Stock,ProveedorID) values(%s,%s,%s,%s,%s,%s)"#los values deben coincidir con la cantidad de %s
datos2= ("Producto 11","Descripción del producto 11","Tipo B","17.45","35","10")#variable de datos a insertar
cursor.execute(sql2,datos2)
conexion1.commit()#subida del insert a la base de datos
print("Datos insertados correctamente en ambas tablas.")

cursor.close()

'''
#2)NOMBRE DE PRODUCTO CON CONDICION 
conexion3=mysql.connector.connect(host="127.0.0.1", user="root",passwd="3929",database="ejer_2_SQL") #variable de conexion.
cursor=conexion3.cursor()
cursor.execute("SELECT d.Nombre , v.TotalVenta FROM Productos d JOIN Ventas v ON d.ProductoID = v.ProductoID HAVING v.TotalVenta > 30.00;")
for tabla in cursor:                      
    print(tabla)
conexion3.close()


'''
#UPDATE
#Prueba actualizacion de una columna

conexion4=mysql.connector.connect(host="127.0.0.1", user="root",passwd="3929",database="ejer_2_SQL") #variable de conexion.
cursor=conexion4.cursor()
datos4="UPDATE Administradores SET Nombre = 'alexis Linares' WHERE AdministradorID= 1;"
cursor.execute(datos4)
conexion4.commit()#subida del insert a la base de datos
print("Dato actualizado")

cursor.execute("SELECT * FROM Administradores")
for tabla in cursor:                      
    print(tabla)

cursor.close()
'''
#3)Actualizacion de un registro
conexion5=mysql.connector.connect(host="127.0.0.1", user="root",passwd="3929",database="ejer_2_SQL") #variable de conexion.
cursor=conexion5.cursor()

sql5 = """  
        UPDATE Administradores 
        SET Nombre = %s, Ubicacion = %s, Celular = %s, Email = %s 
        WHERE AdministradorID = 1
        """
dato5=('Sergio Linares','Ciudad S','3205639841','tsergio@gmail.com')
cursor.execute(sql5,dato5)
conexion5.commit()
print("Dato actualizado")

cursor.execute("SELECT * FROM Administradores")
for tabla in cursor:                      
    print(tabla)
cursor.close()

#DELETE
#eliminar los registros relacionados en la tabla PRODUCTOS
conexion6=mysql.connector.connect(host="127.0.0.1", user="root",passwd="3929",database="ejer_2_SQL")
cursor=conexion6.cursor()
sql6= "DELETE from Productos WHERE ProveedorID=%s" #eliminamos la relacion  de proveedores en prodcutos
borrar=18
cursor.execute(sql6,(borrar,))
#eliminar el registro en la tabla 'Administradores'
delete_adm = "DELETE FROM Proveedores WHERE ProveedorID= %s"
cursor.execute(delete_adm,(borrar,))
conexion6.commit()
print("Dato actualizado")

cursor.execute("SELECT * FROM Proveedores")
for tabla in cursor:                      
    print(tabla)
cursor.close()
