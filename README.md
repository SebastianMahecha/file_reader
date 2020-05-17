# FILE READER

##Pasos para la instalacion del proyecto

1. Verificar si tienes instalado python3, si no entonces por favor instalalo.
2. Instalar pip
3. Instalar virtualenv
4. Crear virtualenv, puedes llamarlo httest
	`virtualenv -p python3 httest` 

5. Activar virtualenv
	`cd httest`
	`source bin/activate`
    
6. Crear fork desde este repositorio

7. En tu local, instalar git en caso no tenerlo.

8. Clonar el proyecto desde tu fork
	`git clone git@github.org:{USERNAME}/file_reader.git`	
9. Ir a la base del proyecto, en donde se encuentra el archivo manage.py
	`cd httest/file_reader`
10. Instalar requirements
	`pip install -r requirements.txt`
11. Instalar MySQL, en caso de no tenerlo
	
12. Crear DB para el proyecto
	`CREATE DATABASE file_reader;`
13. Correr las migraciones
    `python manage.py migrate`
14. Correr el proyecto
	`python manage.py runserver`
15. Ya podras visualizar la pagina desde el navegador con la url arrojada por el anterior comando.


	

