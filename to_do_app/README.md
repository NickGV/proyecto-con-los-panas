# To-Do List App con Django y MongoDB

## Descripción del Proyecto

Esta es una aplicación simple de **Lista de Tareas** desarrollada con **Django** y **MongoDB**, donde los usuarios pueden gestionar sus tareas pendientes de manera eficiente. El proyecto está diseñado para practicar la integración de Django con bases de datos NoSQL, como MongoDB.

### Funcionalidades principales:
- **Crear tareas**: Añade nuevas tareas con un título y una descripción.
- **Editar tareas**: Modifica el contenido de una tarea existente.
- **Eliminar tareas**: Borra las tareas que ya no necesites.
- **Marcar tareas como completadas**: Gestiona el estado de una tarea (completada o pendiente).
- **Visualización de tareas**: Muestra todas las tareas en la lista, filtradas por estado.

Este proyecto sigue el patrón **MTV (Model-Template-View)**, que es la implementación de Django del patrón **MVC (Model-View-Controller)**, haciendo que la lógica de la aplicación esté bien organizada y sea fácil de mantener.

## Tecnologías utilizadas:
- **Django**: Framework web basado en Python para construir la lógica del servidor y el sistema de plantillas.
- **MongoDB**: Base de datos NoSQL utilizada para almacenar las tareas.

## Cómo ejecutar el proyecto:
1. Clona este repositorio.
2. Instala las dependencias listadas en `requirements.txt`.
3. Configura tu conexión a MongoDB en `settings.py`.
4. Ejecuta las migraciones para inicializar la base de datos.
5. Inicia el servidor de desarrollo con el comando:
   ```bash
   python manage.py runserver
