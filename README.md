# UFScrapper

Script creado con la finalidad de descargar las fichas de UniónFansub y meter todos sus datos de manera ordenada en un JSON. Se ha trabajado con python, recalcar que este no es un lenguaje con el que esté muy familiarizado, por eso pueden haber cosa que no sean tal y como las convenciones de este dice.

Para usar el script hace falta instalar las siguientes librerías con pip:

·beautifulsoup4
```
pip install beautifulsoup4
```
·tqdm (usada para mostrar el progreso)
```
pip install tqdm
```
## Sobre el login

Desde Octubre del 2021 es necesario estar logeado para poder ver el contenido de las fichas, el script ha sido actualizado para que se puede hacer. Antes de ejecutarlo solo hay que editar las líneas 111 y 112:
```python

        'username': 'miNombreDeUsuario',
        'password': 'miContraseñaSuperSegura',#
```