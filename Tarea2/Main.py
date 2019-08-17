import os
import time
class mapeo_lexicografico:
    def __init__(self):
        self.matriz = []
        self.filas = 0
        self.columnas = 0
        self.linealizar_fila = 0
        self.linealizar_col = 0
        self.linealizar = 0


    def menu(self):
        print("***********************************")
        print("*         elija la opcion         *")
        print("*                                 *")
        print("*     1. mapeo por fila           *")
        print("*     2. mapeo por columna        *")
        print("*     3. salir                    *")
        print("*                                 *")
        print("*                                 *")
        print("***********************************")


    def mapeo_por_fila(self):
        print("********  eligio mapeo por fila   ******** \n")
        self.crear_matriz()
        self.imprimir_matriz()
        self.mostrar_pos_linealizar()
        self.linealizar = self.linealizar_fila*self.columnas + self.linealizar_col 
        print("posicion a linealizar: "+str(self.linealizar))
        self.graficar_matriz_x_fila()

    def mapeo_por_columna(self):
        print("********  eligio mapeo por columna    ******** \n")
        self.crear_matriz()
        self.mostrar_pos_linealizar()
        self.linealizar = self.linealizar_col*self.filas + self.linealizar_fila 
        print("posicion a linealizar: "+str(self.linealizar))
        self.graficar_matriz_x_columna()

    def crear_matriz(self):
        self.filas = int(input("ingrese el numero de fila: "))
        self.columnas = int(input("ingrese el numero de columna: "))

        #se crea la matriz con valores 0
        for i in range(self.filas):
            self.matriz.append([0]*self.columnas)

        # llenar la matriz con numeros del 0 al tam de la matriz
        contador = 0
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] = contador
                contador += 1

    def imprimir_matriz(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                print(self.matriz[i][j])

    def mostrar_pos_linealizar(self):
        print("\n\n********  ingrese la posicion a linealizar   ******** \n")
        self.linealizar_fila = int(input("fila: "))
        self.linealizar_col = int(input("columna: "))
        

    def graficar_matriz_x_fila(self):
        f = open("matriz.dot", "w")
        f.write("Digraph G{\n")
        f.write("subgraph cluster_gc_1 {\n")
        f.write("node [shape = plaintext] \n")
        f.write("some_node[ \n")
        f.write("label = < \n")
        f.write("<table border = \"0\" cellborder= \"1\" cellspacing = \"0\" > \n ")
        for i in range(self.filas):
            cadena = "<tr>"
            for j in range(self.columnas):
                if (self.linealizar is self.matriz[i][j]):
                     cadena += "<td bgcolor = 'yellow'>"+str(self.matriz[i][j])+"</td>"
                else:
                    cadena += "<td>"+str(self.matriz[i][j])+"</td>"
            cadena += "</tr>"
            f.write(cadena)
        f.write("</table>> \n")
        f.write("]; \n }")

        f.write("subgraph cluster_gc_2 {\n")
        f.write("node [shape = plaintext] \n")
        f.write("some_node1 [ \n")
        f.write("label = < \n")
        f.write("<table border = \"0\" cellborder= \"1\" cellspacing = \"0\" > \n ")
        cadena = "<tr>"
        for i in range(self.filas):
            for j in range(self.columnas):
                if (self.linealizar is self.matriz[i][j]):
                     cadena += "<td bgcolor = 'yellow'>"+str(self.matriz[i][j])+"</td>"
                else:
                    cadena += "<td>"+str(self.matriz[i][j])+"</td>"
        cadena += "</tr>"
        f.write(cadena)
        f.write("</table>> \n")
        f.write("]; \n }")
        f.write("}")
        f.close()
        os.system("dot -Tjpg matriz.dot  -o matriz.png")
        os.system("matriz.png")  # para abrir la imagen automaticamente

    def graficar_matriz_x_columna(self):
        f = open("matriz.dot", "w")
        f.write("Digraph G{\n")
        f.write("subgraph cluster_gc_1 {\n")
        f.write("node [shape = plaintext] \n")
        f.write("some_node[ \n")
        f.write("label = < \n")
        f.write("<table border = \"0\" cellborder= \"1\" cellspacing = \"0\" > \n ")
        for i in range(self.filas):
            cadena = "<tr>"
            for j in range(self.columnas):
                if (self.linealizar is self.matriz[i][j]):
                     cadena += "<td bgcolor = 'yellow'>"+str(self.matriz[i][j])+"</td>"
                else:
                    cadena += "<td>"+str(self.matriz[i][j])+"</td>"
            cadena += "</tr>"
            f.write(cadena)
        f.write("</table>> \n")
        f.write("]; \n }")

        f.write("subgraph cluster_gc_2 {\n")
        f.write("node [shape = plaintext] \n")
        f.write("some_node1 [ \n")
        f.write("label = < \n")
        f.write("<table border = \"0\" cellborder= \"1\" cellspacing = \"0\" > \n ")
        cadena = ""
        for i in range(self.columnas):
            for j in range(self.filas):
                if (self.linealizar is self.matriz[j][i]):
                     f.write("<tr><td bgcolor = 'yellow'>"+str(self.matriz[j][i])+"</td></tr>")
                else:
                    f.write("<tr><td>"+str(self.matriz[j][i])+"</td></tr>")

        f.write("</table>> \n")
        f.write("]; \n }")
        f.write("}")
        f.close()
        os.system("dot -Tjpg matriz.dot  -o matriz.png")
        os.system("matriz.png")  # para abrir la imagen automaticamente

        
                


ml = mapeo_lexicografico()  
while True:
    os.system("cls")
    try:
        ml.menu()
        select = int(input())
        os.system("cls")
        if select == 1:
            ml.mapeo_por_fila()
        if select == 2:
            ml.mapeo_por_columna()
        if select == 3:
            print("operacion exitosa")
            break
    except:
        print("Error, intente de nuevo")
           