#ifndef ABB_H
#define ABB_H
#include <string>
#include <iostream>

using namespace std;
class Abb{
public:

    class Nodo{
    public:
        string dato;
        Nodo *izquierda;
        Nodo *derecha;
        Nodo *padre;

        Nodo();

        Nodo(string n, Nodo *m){
            dato = n;
            padre = m;
            izquierda = NULL;
            derecha = NULL;
        }

    };

    Nodo *raiz;
    string cuerpo_graph;
    int con;

    Abb();
    void insert(Nodo *&, Nodo *, string);
    void crear_archivo();
    string graficar_abb(Nodo *&);
    void eliminar_Nodo(Nodo *&, string);
    void eliminar(Nodo *);
    void destruir_nodo(Nodo *);
    void reemplazar(Nodo*&, Nodo *);
    Nodo *NodoMenor(Nodo *);
};


#endif //ABB_H
