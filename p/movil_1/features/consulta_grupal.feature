Feature: Agregar integrantes a un grupo
  
  Background:
    Given el usuario está en la pantalla principal
    When Selecciona la opcion: Consulta grupal

  @genera-nuevo-grupo
  Scenario Outline: Colocar el nombre a un grupo.
  
    Then Genera un nuevo grupo con el nombre: "<nombre_grupo>"
    # Then Agregar integrante dando clic en icono mas
    # Then Seleccionar btn prospecto existente
    # Then Buscar al integrante: "<usuario>" para agregar al grupo

    Then Volver al inicio

 @validar-duplicidad-de-nuevo-grupo
  Scenario Outline: Validar que no exista la posibilidad de crear un grupo con el mismo nombre.
    Then Genera un nuevo grupo con el nombre: "<nombre_grupo>"
    Then Validacion de duplicidad de grupo
    Then Volver al inicio


      
      # Las Pulqueras Poderosas
      # Espuma Sagrada
      # Espuma milagrosa
      # Las Teporingas
      # Hijas del Maguey
      # Guerreras deñ Pulque 
      # Las Tlachiqueras
      # Las Curadas
      # Agave Divino
      # Agave helado
      # Fuerza Pulquera
      # Las Diosas del Néctar
      # Huracanas
      # Las ninjas
      # Atlético corazon
      # Las de cobre
      # Gladiadoras
      # Gigantes de acero
      # Muñecas de porcelana
      # Nenas raptor
      # Deportivo venus
      # Deportivo estrella de plata
      # Nenas de venus
      # AFFRODITAS
      # Vengadoras del balón
      # Mujeres del zodiaco
      # Diosas del amor
      # Atlético burbuja
      # Las estrellas rosadas
      # Destellos de pinol| Atlético de pulque |
      # | Sangre de Pulque   |
      # Chicas del amor| nombre_grupo       |
      # | Atlético de pulque |
      # | Sangre de Pulque   |
      # Rayos de luz
      # Golondrinas de oro   # Las Pulqueras Poderosas
      # Espuma Sagrada
      # Espuma milagrosa
      # Las Teporingas
      # Hijas del Maguey
      # Guerreras deñ Pulque 
      # Las Tlachiqueras
      # Las Curadas
      # Agave Divino
      # Agave helado
      # Fuerza Pulquera
      # Las Diosas del Néctar
      # Huracanas
      # Las ninjas
      # Atlético corazon
      # Las de cobre
      # Gladiadoras
      # Gigantes de acero
      # Muñecas de porcelana
      # Nenas raptor
      # Deportivo venus
      # Deportivo estrella de plata
      # Nenas de venus
      # AFFRODITAS
      # Vengadoras del balón
      # Mujeres del zodiaco
      # Diosas del amor
      # Atlético burbuja
      # Las estrellas rosadas
      # Destellos de pinol
      # Chicas del amor| nombre_grupo       |
      # | Atlético de pulque |
      # | Sangre de Pulque   |
      # Rayos de luz
      # Golondrinas de oro
      # Cebras veloces
      # Furia de unicornio
      # Soñadas
      # Las rebeldes
      # Águilas de fuego
      # Hormigas de fuego
      # Hormigas de humo
      # Las mágicas
      # Las chicas del barrio
      # Jugadoras con honor
      # Las princesas del universo
      # Las chicas
      # Estrellas del paraiso
      # Las correcaminos
      # Guerreras de la cancha
      # Las supergoleadoras
      # Las futbolísimas
      # Las mexicas
      # Las Valkirias
      # Estrellas Guerreras
      # Amazonas del Sol
      # Las Águilas Doradas
      # Tormenta Rosa
      # Las Fieras
      # Guerreras del Alba
      # Las Emperatrices
      # Rayo de Luna
      # Furia Violeta
      # Sirenas del Norte
      # Lobas Plateadas
      # Intrépidas
      # Felinas
      # Cenoza de hielo
      # Combustion del comal
      # Fuego Eterno
      # Halconas Doradas
      # Las Vencedoras
      # Estrellas Brillantes
      # Las Invencibles
      # Las Adelitas
      # Guerreras Aztecas
      # Las Catrinas
      # Diosas del Maíz
      # Las Jaguaras
      # Princesa del Maíz
      # Fuerza Maya
      # Águilas Tonantzin
      # Las Tehuanas
      # Corazón Mexica
      # Las Quetzales
      # Valkirias de Oaxaca
      # Las Nahualas
      # Fuego Zapoteco
      # Guerreras Huastecas
      # Las Tlatoanis
      # Hijas del Nopal
      # Hijas del Maíz
      # Templarias del Sol
      # Coyotas
      # Herencia Azteca
      # Rayo Mixteco
      # Tamaleras
      # Poderosas Enchiladas
      # Las Salsas Bravas
      # Las Tostadas de Oro
      # Chicas del Mole
      # Chapulinas
      # Furia Tapatía
      # Tortilleras
      # Quesadillocas
      # Las Huaraches
      # Guacamoleras
      # Picantes y Sabrosas
      # Flautas Doradas
      # Hijas del Maíz
      # Sopesitas
      # Raspaditas
      # Chamoyadas
      # Fuerza Taquera
      # Las Picositas
      # Poder y Tacos
      # Las Catrinas Valientes
      # Almas Eternas
      # Las Flor de Cempasúchil
      # Guardianas del Inframundo
      # Las Almas Libres
      # Luz y Calaveras
      # Las Xoloitzcuintles
      # Espíritu de Cempasúchil
      # Las Calaveritas
      # Guerreras del Mictlán
      # Las Altarinas
      # Almas Ancestrales
      # Las Ofrendas
      # Calaveras y Fuego
      # Las 
      # Almas de Azúcar
      # Las Guardianas de las Velas
      # Catrinas y Mictlantecuhtli
      # Las Mariposas del Alma
      # Luces del Mictlán
      # Cebras veloces
      # Furia de unicornio
      # Soñadas
      # Las rebeldes
      # Águilas de Fuego
      # Hormigas de fuego
      # Hormigas de humo
      # Las mágicas
      # Las chicas del barrio
      # Jugadoras con honor
      # Las princesas del universo
      # Las chicas
      # Estrellas del paraiso
      # Las correcaminos
      # Guerreras de la cancha
      # Las supergoleadoras
      # Las futbolísimas
      # Las mexicas
      # Las Valkirias
      # Estrellas Guerreras
      # Amazonas del Sol
      # Las Águilas Doradas
      # Tormenta Rosa
      # Las Fieras
      # Guerreras del Alba
      # Las Emperatrices
      # Rayo de Luna
      # Furia Violeta
      # Sirenas del Norte
      # Lobas Plateadas
      # Intrépidas
      # Felinas
      # Cenoza de hielo
      # Combustion del comal
      # Fuego Eterno
      # Halconas Doradas
      # Las Vencedoras
      # Estrellas Brillantes
      # Las Invencibles
      # Las Adelitas
      # Guerreras Aztecas
      # Las Catrinas
      # Diosas del Maíz
      # Las Jaguaras
      # Princesa del Maíz
      # Fuerza Maya
      # Águilas Tonantzin
      # Las Tehuanas
      # Corazón Mexica
      # Las Quetzales
      # Valkirias de Oaxaca
      # Las Nahualas
      # Fuego Zapoteco
      # Guerreras Huastecas
      # Las Tlatoanis
      # Hijas del Nopal
      # Hijas del Maíz
      # Templarias del Sol
      # Coyotas
      # Herencia Azteca
      # Rayo Mixteco
      # Tamaleras
      # Poderosas Enchiladas
      # Las Salsas Bravas
      # Las Tostadas de Oro
      # Chicas del Mole
      # Chapulinas
      # Furia Tapatía
      # Tortilleras
      # Quesadillocas
      # Las Huaraches
      # Guacamoleras
      # Picantes y Sabrosas
      # Flautas Doradas
      # Hijas del Maíz
      # Sopesitas
      # Raspaditas
      # Chamoyadas
      # Fuerza Taquera
      # Las Picositas
      # Poder y Tacos
