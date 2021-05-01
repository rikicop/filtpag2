# filtpag2
mejoramiento de filtro con paginacion

#HAY UN PROBLEMILLA
#Static Files & Admin

En:

pythonanywhere.com: Tengo la carpeta static en root
en este caso root es filtpag2

computador: Tengo que poner la carpeta static dentro de filtpag_project/
por que python busca los archivos es ahí, y ademas dejo también 
otra carpeta static en root(filtpag2), para "cuando lo suba
a pythonanywhere solo necesite borrar una carpeta"(la de filtpag_project/) si es necesario

El problema se resuelve en pythonanywhere en la sección web y 
llendo a la sección static cambias el directorio a :

--> /home/karinpena/filtpag2/filtpag_project/static
 

