#include <iostream>
#include <string>
#include <fstream>
#include "abb.h"

using namespace std;

Abb::Abb(){
    raiz = NULL;
    cuerpo_graph = "";
    con = 0;

}

void Abb::insert(Nodo *&raiz, Nodo *padre, string dato){
    Nodo *nuevo = new Nodo(dato, padre);
    if(raiz == NULL){
        raiz = nuevo;
    }else{
        if(dato < raiz->dato){
            insert(raiz->izquierda, raiz, dato);
        }else{
            insert(raiz->derecha, raiz, dato);
        }
    }
}

void Abb::reemplazar(Nodo *&raiz, Nodo *nuevo){
    if(raiz->padre){ /*si existe padre del nodo*/
        /*si existe izquieda del padre*/
        if(raiz->padre->izquierda){
            if(raiz->dato == raiz->padre->izquierda->dato){
                raiz->padre->izquierda = nuevo;
            }
        }
        /*si existe derecha del padre*/
        if(raiz->padre->derecha){
            if(raiz->dato == raiz->padre->derecha->dato){
                raiz->padre->derecha = nuevo;
            }
        }
    }

    /*asignarle padre al nuevo nodo*/
    if(nuevo){
        nuevo->padre = raiz->padre;
    }

}

void Abb::eliminar(Nodo *raiz){
    if(raiz->izquierda && raiz->derecha){ /* si tiene dos hijos */
        Nodo *menor = NodoMenor(raiz->derecha); /*retorna nodo menor*/
        raiz->dato = menor->dato; /*solo cambia el dato nada mas*/
        eliminar(menor);

    }else if(raiz ->izquierda){ /*si tiene hijo derecho*/
        reemplazar(raiz, raiz->izquierda);
        destruir_nodo(raiz);    /*destruir nodo*/
    }else if(raiz->derecha){ /*si tiene hijo izquierdo*/
        reemplazar(raiz, raiz->derecha);
        destruir_nodo(raiz);    /*destruir nodo*/
    }else{
        reemplazar(raiz, NULL); /*reemplazar*/
        destruir_nodo(raiz);    /*destruir nodo*/
    }


}

/* funcion para determinar el nodo mas izquierdo posible*/

Abb::Nodo *Abb::NodoMenor(Nodo *arbol){
    if(arbol == NULL){
        return NULL;
    }
    if(arbol->izquierda){
        return NodoMenor(arbol->izquierda);
    }else{
        return  arbol;
    }
}

void Abb::eliminar_Nodo(Nodo *&raiz, string dato){
    if(raiz == NULL){
        return;
    }else if(dato < raiz->dato){
         eliminar_Nodo(raiz->izquierda, dato);
    }else if(dato > raiz->dato){
         eliminar_Nodo(raiz->derecha, dato);
    }else{
        eliminar(raiz);
    }

}

void Abb::destruir_nodo(Nodo *eliminarNodo){
    eliminarNodo->derecha = NULL;
    eliminarNodo->izquierda = NULL;
    delete eliminarNodo;
}

void Abb::crear_archivo(){
    cuerpo_graph = "";
    con++;
    string contador = std::to_string(con);
    ofstream file;
    file.open(contador+"abb.dot", ios::out);
    if(file.fail()){
        cout<<"error al crear archivo dot";
    }

    /*escribir en el archivo*/
    string cabeza = "digraph grafica{ \nnode [shape = record, style = filled, splines= line, location = none, fillcolor = seashell2]; \n";
    string cuerpo = graficar_abb(raiz);
    string cola = "\n}\n";
    file<<cabeza+cuerpo+cola;
    file.close(); /*cerrar el archivo*/
    string salida = "dot "+ contador +"abb.dot -o " + contador + "abb.png -Tpng";
    const char *comand = salida.c_str(); /*convertir string a char*/
    system(comand);
}

string Abb::graficar_abb(Nodo *&arbol){
    if(arbol == raiz){
        string mi_node = arbol->dato;
        cout<<mi_node+"\n";
        cuerpo_graph += mi_node+" [ label = \"<iz>|"+mi_node+"|<der>\"] \n\n";
    }

        if(arbol->izquierda){
            string mi_node = arbol->izquierda->dato;
            cout<<mi_node+"\n";
            cuerpo_graph += arbol->dato+":iz -> "+mi_node+"\n";
            cuerpo_graph += mi_node+" [ label = \"<iz>|"+mi_node+"|<der>\"] \n\n";
            graficar_abb(arbol->izquierda);
        }

        if(arbol->derecha){
            string mi_node = arbol->derecha->dato;
            cout<<mi_node+"\n";
            cuerpo_graph += arbol->dato+":der -> "+mi_node+"\n";
            cuerpo_graph += mi_node+" [ label = \"<iz>|"+mi_node+"|<der>\"] \n\n";
            graficar_abb(arbol->derecha);
        }


    return  cuerpo_graph;
}
