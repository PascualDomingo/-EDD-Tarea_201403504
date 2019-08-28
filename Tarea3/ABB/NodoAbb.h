#ifndef NODOABB_H
#define NODOABB_H
#include <string>

using namespace std;


class NodoAbb{
public:
    string dato;
    NodoAbb *izquierda;
    NodoAbb *derecha;
    NodoAbb *padre;

    NodoAbb(string, NodoAbb*);


};




#endif //NODOABB_H
