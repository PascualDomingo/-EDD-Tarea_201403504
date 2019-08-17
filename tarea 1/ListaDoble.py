from graphviz import Digraph
class Nodo:
    def __init__(self, Valor = None):
        self.valor = Valor
        Nodo.siguiente = None
        Nodo.anterior = None


class listadoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.con = 0

    #inserta al final del nodo#
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo 
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo

    # inserta al final del nodo#
    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if self.primero == None:
            print("no se puede insertar el valor al final, Debe insertar primero al inicio")
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
    
    #insertar valor del nodo en la posicion indicada #
    def insertar_pos(self, pos, valor):
        nuevo = Nodo(valor)
        if self.primero == None:
            print("no se puede insertar el valor, no existe valor al inicio")
        else:
            if pos >= 0:
                con = 0 #es para contar cuantos nodos existe en la lista
                aux = self.primero
                while aux != None:
                    
                    if pos == con:
                        
                        if aux == self.primero:
                            self.insertar_inicio(valor)
                            break
                        else:
                            aux1 = aux.anterior
                            aux1.siguiente = nuevo
                            nuevo.anterior = aux1
                            nuevo.siguiente = aux
                            aux.anterior = nuevo
                            break
                    con += 1
                    aux = aux.siguiente
                    if aux == None:
                        print("la posicion insertada no existe, intente insertar otro numero")
                        break 
            else:
                print("la posicion insertada no existe, intente insertar otro numero") 

    #obtener el valor del nodo en la posicion indiciada#
    def obtener_pos(self, pos):
        if self.primero == None:
            print("la lista se encuentra vacia, inserte un valor")
        else:
            if pos >= 0:
                con = 0 #es para contar cuantos nodos existe en la lista
                aux = self.primero
                while aux != None:
                    
                    if pos == con:
                        return aux.valor

                    con += 1
                    aux = aux.siguiente
                    if aux == None:
                        print("la posicion insertada no existe, intente insertar otro numero")
                        break 
            else:
                print("la posicion insertada no existe, intente insertar otro numero")

#insertar valor del nodo en la posicion indicada #
    def eliminar(self, pos):
        if self.primero == None:
            print("no se puede elimiar, la lista esta vacia")
        else:
            if pos >= 0:
                con = 0 #es para contar cuantos nodos existe en la lista
                aux = self.primero
                while aux != None:
                    
                    if pos == con:
                        
                        if aux == self.primero:
                            self.primero = aux.siguiente
                            self.primero.anterior = None
                            break
                        elif aux == self.ultimo:
                            self.ultimo = aux.anterior
                            self.ultimo.siguiente = None
                            break
                        else:
                            aux.anterior.siguiente = aux.siguiente
                            aux.siguiente.anterior = aux.anterior
                            break
                    con += 1
                    aux = aux.siguiente
                    if aux == None:
                        print("la posicion insertada no existe, intente insertar otro numero")
                        break 
            else:
                print("la posicion insertada no existe, intente insertar otro numero") 


    def imprimir(self):
        aux = self.primero
        while aux != None:
            print(aux.valor)
            aux = aux.siguiente


    def graficar(self):
        dot = Digraph (comment="The round table", format = 'png')
        aux = self.primero
        self.con = 1 + self.con # para que cambie el numero de imagenes
        while aux != None:
            if aux == self.primero:
                dot.edge(str(aux.valor), str("null."))
                dot.edge(str(aux.valor), str((aux.siguiente.valor)), constraint='false')
                dot.edge(str(aux.siguiente.valor), str((aux.valor)), constraint='false')
            elif aux == self.ultimo:
                dot.edge(str(aux.valor), str("null"))
            else:
                dot.edge(str(aux.valor), str((aux.siguiente.valor)), constraint='false')
                dot.edge(str(aux.siguiente.valor), str((aux.valor)), constraint='false')
            aux = aux.siguiente
        dot.render("~\\lista doblemeente enlazada "+str(self.con)+".dot", view=True)
        


if __name__ == "__main__":
    listadoble = listadoble()
    # 5 inserciones al inicio
    listadoble.insertar_inicio(10)
    listadoble.insertar_inicio(20)
    listadoble.insertar_inicio(30)
    listadoble.insertar_inicio(40)
    listadoble.insertar_inicio(50)

    # 5 inserciones al final
    listadoble.insertar_final(100)
    listadoble.insertar_final(200)
    listadoble.insertar_final(300)
    listadoble.insertar_final(400)
    listadoble.insertar_final(500)

    # graficar
    listadoble.graficar()
    print("")
    #listadoble.imprimir()

    # insertar en posiciones
    listadoble.insertar_pos(5, 777)
    listadoble.insertar_pos(8, 999)

    #graficar
    print("")
    #listadoble.imprimir()
    listadoble.graficar()

    #obtener el valor de la lista
    print("")
    print(listadoble.obtener_pos(3))
    print("")
    listadoble.eliminar(0)
    listadoble.eliminar(4)
    #listadoble.imprimir()

    #graficar
    listadoble.graficar()
