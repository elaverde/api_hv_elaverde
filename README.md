# Instalación del paquete de idioma español en Linux con APT

Para instalar el paquete de idioma español en un sistema Linux que utiliza el gestor de paquetes APT (Advanced Package Tool), ejecuta el siguiente comando en una terminal:

```
sudo apt-get install language-pack-es
```
```
export LC_ALL=es_ES.UTF-8
```

Este comando descargará e instalará el paquete de idioma español en tu sistema.

# Activación del idioma español en el sistema

Para activar el idioma español en el sistema, sigue los siguientes pasos:

1. Abre el archivo de configuración de idioma de tu sistema con el siguiente comando:

    ```
    sudo nano /etc/default/locale
    ```

2. En el archivo, busca la línea que dice `LANG=` y cambia su valor a `es_ES.UTF-8`. Debería quedar algo como esto:

    ```
    LANG="es_ES.UTF-8"
    ```

3. Guarda los cambios y cierra el archivo.

4. Reinicia el sistema para que los cambios surtan efecto.

Después de estos pasos, el sistema debería estar configurado para usar el idioma español en diversas aplicaciones. Puedes verificar la configuración actual ejecutando el siguiente comando:

