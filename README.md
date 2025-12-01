# Aplicaciones multiplataforma con FLET

En este repositorio estare documentando lo aprendido con FLET, de las explicaciones con CHATGPT y mis propias modificaciones y experiencias. Tambien documentare las instrucciones iniciales, como las formas de instalr FLET y los primeros pasos para crear una aplicacion sencilla.

## ¿Qué es FLET?

FLET es un framework de código abierto que permite crear aplicaciones multiplataforma utilizando Python. Con FLET, puedes desarrollar aplicaciones web, de escritorio y móviles con una sola base de código, lo que facilita el proceso de desarrollo y mantenimiento.

## Requisitos Previos

### Instalación de Python

Flet recomienda tener instalado Python 3.7 o superior. De preferencia utiliza la version 3.12.x. También es recomendable crear un entorno virtual con la version de python especifica, por ejemplo:

```bash
python -3.12 -m venv venv
.\venv\Scripts\activate
```

### Instalar Flutter

Flet utiliza Flutter para compilar aplicaciones móviles. Sigue estos pasos para instalar Flutter:

1. Descarga Flutter desde su [sitio oficial](https://docs.flutter.dev/get-started/quick).
2. Activar las licencias de Flutter:

      ```bash
      flutter doctor --android-licenses
      ```

3. Verificar flutter en terminal:

      ```bash
      flutter doctor
      ```

Esto mostrará el estado de tu instalación de Flutter y te indicará si hay algún componente faltante.

### Generar APK

- Tener Java JDK 17 o superior
- Tener instalado Android SDK / Android Studio
- Aceptar las licencias del SDK

## Instalación de FLET

Es recomendable crear un entorno virtual para tu proyecto. Puedes hacerlo utilizando `venv`:

```bash
pip install flet
```

## Primeros pasos con FLET

La primer aplicacion que se creó es [Hola Mundo](./hello_world.py)

### Ejecución de la aplicación

Para ejecutar la aplicación, utiliza el siguiente comando en tu terminal:

```bash
python hello_world.py
```

Esto iniciará una aplicación de escritorio que muestra un mensaje de "Hola, Mundo!" en la ventana.

---

### Ejecutar en el navegador

Para ejecutar la aplicación en el navegador, utiliza el siguiente comando en tu terminal:

```bash
python hello_world.py --web
```

Esto iniciará un servidor local y abrirá la aplicación en tu navegador web predeterminado.
Tambien se puede definir en el codigo pa forma de ejecucion, en este caso para web:
En lugar de usar:

```python
ft.app(target=main)
```

Utiliza los siguientes parametros:

```python
ft.app(target=main, view=ft.WEB_BROWSER)
```

---

## Exportar a Android APK

Flet usa una herramienta llamada Flet Build para empaquetar tu app. Instala la herramienta:

```bash
pip install flet-cli
```

Ahora ejecuta el “build”:

```bash
flet build apk
```

Esto generará una carpeta:

```JSON
build/
 └── apk/
      └── app-release.apk
```

**Ese es tu instalador de Android.**

### Notas adicionales

Al ejecutar el comando `flet build apk`, Flet busca por defecto el archivo `main.py` en el directorio actual. Si tu archivo principal tiene un nombre diferente o está ubicado en otra carpeta, debes especificar la ruta correcta utilizando el parámetro `--module-name`. Por ejemplo, si tu archivo principal se llama `mi_app.py`, el comando sería:

```bash
flet build apk --module-name mi_app.py
```
