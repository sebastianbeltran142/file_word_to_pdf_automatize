import time as tm
import pyautogui as pg

# Configurar posiciones (Esto se realiza en pantalla de 1920 * 1080)
abrir_carpeta = 220,1054
pestana_review = 657,79
aceptar_1 = 1227,181
aceptar_2 = 1342,363
pestana_file = 35,79
button_saveAs = 76,411
selector_formato = 1490,214
pdf = 784,384
button_save = 1568,212
cerrar_ventanas = 1886,26
cambios_guardar = 860,592

# Mover mouse y dar click
def abrir(pos,click=1):
    pg.moveTo(pos)
    pg.click(clicks=click)

# Desplazamientos y ejecuciones
for i in range(29):
    abrir(abrir_carpeta,click=1)
    tm.sleep(1)
    abajo = pg.hotkey('down')
    intro = pg.hotkey('enter')
    tm.sleep(5)
    abrir(pestana_review,click=1)
    tm.sleep(1)
    abrir(aceptar_1,click=1)
    tm.sleep(1)
    abrir(aceptar_2,click=1)
    tm.sleep(1)
    abrir(pestana_file,click=1)
    tm.sleep(1)
    abrir(button_saveAs,click=1)
    tm.sleep(1)
    abrir(selector_formato,click=1)
    tm.sleep(1)
    abrir(pdf,click=1)
    tm.sleep(1)
    abrir(button_save,click=1)
    tm.sleep(15)
    abrir(cerrar_ventanas,click=1)
    tm.sleep(1)
    abrir(cerrar_ventanas,click=1)
    abrir(cambios_guardar,click=1)
    tm.sleep(1)
    abrir(abrir_carpeta,click=1)
    tm.sleep(0.5)
    
print ("Servicio realizado con éxito")

# Scrip por Grupo HDTC 2022 RPA