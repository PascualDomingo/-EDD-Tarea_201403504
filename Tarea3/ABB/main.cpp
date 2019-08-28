#include <QCoreApplication>
#include <iostream>
#include <QDebug>
#include "abb.h"

using namespace  std;

Abb *abb = new Abb();

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    /*insertar*/
    abb->insert(abb->raiz, NULL, "luigi");
    abb->insert(abb->raiz, NULL, "hammer");
    abb->insert(abb->raiz, NULL, "mario");
    abb->insert(abb->raiz, NULL, "peach");
    abb->insert(abb->raiz, NULL, "pow");
    abb->insert(abb->raiz, NULL, "fermin");

    /*graficar*/
    cout<<endl<<endl;
    abb->crear_archivo();

    /* eliminar nodo */
    abb->eliminar_Nodo(abb->raiz, "peach");

    /*graficar*/
    cout<<endl<<endl;
    abb->crear_archivo();

    /* insertar */
    abb->insert(abb->raiz, NULL, "shy_guy");
    abb->insert(abb->raiz, NULL, "edd");

    /*graficar*/
    cout<<endl<<endl;
    abb->crear_archivo();

    /* eliminar nodo */
    abb->eliminar_Nodo(abb->raiz, "pow");

    /*graficar*/
    cout<<endl<<endl;
    abb->crear_archivo();

    /* insertar */
    abb->insert(abb->raiz, NULL, "boo");
    abb->insert(abb->raiz, NULL, "kamek");
    abb->insert(abb->raiz, NULL, "star");
    abb->insert(abb->raiz, NULL, "whomp");

    /*graficar*/
    cout<<endl<<endl;
    abb->crear_archivo();

    /* eliminar nodo */
    abb->eliminar_Nodo(abb->raiz, "shy_guy");

    /*graficar*/
    cout<<endl<<endl;
    abb->crear_archivo();

    /* eliminar nodo */
    abb->eliminar_Nodo(abb->raiz, "mario");

    /*graficar*/
    cout<<endl<<endl;
    abb->crear_archivo();

    return a.exec();
}
