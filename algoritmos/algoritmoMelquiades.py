import random #se importa la librería de python random

sujetos = ["Queridos compatriotas", "Apreciados conciudadanos", "Distinguidos amigos",
           "Honorables coterraneos","Estimados opartidarios","Respetados electores"]; #se define una lista
intenciones = ["trabajare por", "yo puedo", "yo vengo a", "voy a"];
verbos = ["eliminar","vencer", "acabar", "luchar contra","combatir"];
advs = [""];
complementos_uno = ["la educacion", "el empleo", "la seguridad", "la paz",
                    "la igualdad","la salud"];
complementos_dos = ["dependiendo de la cantidad de votos"
                , "del pais", "de la ciudad", "de la comunidad","de la poblacion",
                    "para toda la gente","de cada colombiano"];

sujeto_seleccionado = random.choice(sujetos) #se utiliza la librería para seleccionar un elemento al azar de la lista sujetos
intencion_seleccionada = random.choice(intenciones)
verbo_seleccionado = random.choice(verbos)
adv_seleccionado = random.choice(advs)
compl1s_seleccionado = random.choice(complementos_uno)
compl2s_seleccionado = random.choice(complementos_dos)

print("letra generada: " + sujeto_seleccionado + " " + intencion_seleccionada + " " + verbo_seleccionado + " "
      + adv_seleccionado + " " + compl1s_seleccionado + " " + compl2s_seleccionado) #se imprime la canción