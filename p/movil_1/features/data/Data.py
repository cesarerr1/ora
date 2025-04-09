import random
import csv
import string
import shutil
import unicodedata
import re


def limpiar_texto(texto):
    """Elimina acentos y caracteres especiales, dejando solo letras y números"""
    # Eliminar acentos
    texto_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    # Eliminar caracteres que no sean letras o números
    texto_limpio = re.sub(r'[^A-Za-z0-9 ]', '', texto_sin_acentos)
    return texto_limpio

def generar_nombre_aleatorio_hombre():
    nombres_hombres = [
        "Aaron", "Abel", "Abraham", "Adán", "Adrián", "Agustín", "Alberto", "Alejandro", "Alex", "Alfonso",
        "Alfredo", "Álvaro", "Amado", "Andrés", "Ángel", "Aníbal", "Antonio", "Ariel", "Armando", "Arturo",
        "Baltasar", "Benjamín", "Bernardo", "Blas", "Braulio", "Camilo", "Carlos", "César", "Christian", "Claudio",
        "Clemente", "Cristian", "Cristóbal", "Damián", "Daniel", "Dante", "David", "Demetrio", "Diego", "Dionisio",
        "Domingo", "Edgar", "Edmundo", "Eduardo", "Efraín", "Elías", "Emilio", "Enrique", "Ernesto", "Esteban",
        "Eugenio", "Eusebio", "Ezequiel", "Fabián", "Fabricio", "Federico", "Felipe", "Fernando", "Fidel", "Francisco",
        "Gabriel", "Gaspar", "Germán", "Gerardo", "Gilberto", "Gonzalo", "Gregorio", "Guillermo", "Gustavo", "Héctor",
        "Heriberto", "Hernán", "Homero", "Horacio", "Hugo", "Ignacio", "Isaac", "Isidro", "Ismael", "Iván",
        "Jacobo", "Jaime", "Javier", "Jerónimo", "Jesús", "Joaquín", "Jorge", "José", "Juan", "Julián",
        "Julio", "Justino", "Lautaro", "Leandro", "Leonardo", "Leopoldo", "Lorenzo", "Lucas", "Luciano", "Luis",
        "Manuel", "Mariano", "Mario", "Martín", "Mateo", "Matías", "Mauricio", "Maximiliano", "Miguel", "Narciso",
        "Néstor", "Nicolás", "Norberto", "Octavio", "Omar", "Orlando", "Oscar", "Pablo", "Pancho", "Patricio",
        "Pedro", "Rafael", "Ramiro", "Ramón", "Raúl", "Ricardo", "Roberto", "Rodrigo", "Rubén", "Salvador",
        "Samuel", "Santiago", "Saúl", "Sebastián", "Serafín", "Sergio", "Silvio", "Simón", "Tadeo", "Teodoro",
        "Tobías", "Tomás", "Valentín", "Vicente", "Victor", "Vladimir", "Wilfredo", "Xavier", "Yahir", "Zacarías",
        "Aarón", "Adalberto", "Alejo", "Alcides", "Amador", "Anastasio", "Aristides", "Arnaldo", "Artemio", "Atilio",
        "Baldomero", "Bartolomé", "Benedicto", "Bonifacio", "Borja", "Casimiro", "Celestino", "Ciriaco", "Crisóstomo",
        "Damian", "Desiderio", "Edelmiro", "Elpidio", "Eulogio", "Fausto", "Fortunato", "Gerónimo", "Gualberto",
        "Guido", "Heriberto", "Hilario", "Hipólito", "Honorato", "Isidoro", "Jesualdo", "Jovino", "León", "Lázaro",
        "Macario", "Marcelo", "Maximino", "Modesto", "Napoleón", "Pastor", "Primitivo", "Prudencio", "Raimundo",
        "Ramón", "Reinaldo", "Rogelio", "Rosendo", "Saturnino", "Simeón", "Timoteo", "Ubaldo", "Venancio",
        "Vespasiano", "Zacarías", "Evaristo", "Urbano", "Severino", "Zenón", "Bautista", "Valerio", "Filomeno",
        "Eusebio", "Ambrosio", "Germán", "Nicodemo", "Celso", "Sabas", "Melchor", "Gaspar", "Baltasar",
        "Alejandro","Álvaro","Andrés","Antonio","Arturo","Benjamín","Carlos","Cristian","Daniel","David","Diego","Eduardo","Emilio","Enrique",
        "Esteban","Fernando","Francisco","Gabriel","Gonzalo","Guillermo","Héctor","Hugo","Ignacio","Isaac","Iván","Javier","Jesús","Joaquín",
        "Jorge","José","Juan","Julián","Leonardo","Lucas","Luis","Manuel","Marcos","Mario","Martín","Mateo","Miguel","Nicolás","Óscar","Pablo",
        "Pedro","Rafael","Raúl","Ricardo","Roberto","Sergio"
    ]
    return random.choice(nombres_hombres)


def generar_nombre_aleatorio_mujer():


    nombres_mujeres = [
        "Camila","Javiera","Francisca","Catalina","Valentina","Antonia","Daniela","Ignacia","Fernanda","Josefa",
        "Isidora","Trinidad","Barbara","Constanza","Paz","Carolina","Romina","Macarena","Tamara",
        "Emma","Sofia","Clara","Isabella","Amelia","Gabriella","Charlotte","Anais","Marta","Lea",     
       "Isabella","Emilia","Sofía","Anneliese","Margot","Eleonora","Tatiana","Ingrid","Katarina",
        "Abril", "Adriana", "Alejandra", "Alexa", "Alicia", "Alma", "Amalia", "Amanda", "Ana", "Andrea",
        "Ángela", "Angelica", "Antonia", "Ariadna", "Beatriz", "Belén", "Bianca", "Brenda", "Camila", "Carla",
        "Carmen", "Carolina", "Catalina", "Cecilia", "Celeste", "Clara", "Claudia", "Concepción", "Constanza", "Cristina",
        "Daniela", "Débora", "Diana", "Dolores", "Elena", "Elisa", "Elizabeth", "Elsa", "Emilia", "Esperanza",
        "Estefanía", "Estela", "Eugenia", "Eva", "Fabiana", "Fabiola", "Fernanda", "Fiorella", "Flor", "Francisca",
        "Gabriela", "Genoveva", "Georgina", "Gisela", "Gloria", "Graciela", "Guadalupe", "Hortensia", "Iliana", "Inés",
        "Irene", "Isabel", "Ivonne", "Jacqueline", "Jazmín", "Jennifer", "Jessica", "Jimena", "Johanna", "Josefina",
        "Juana", "Julia", "Julieta", "Karina", "Karla", "Laura", "Leticia", "Liliana", "Lorena", "Lourdes",
        "Luisa", "Luz", "Magdalena", "Manuela", "Marcela", "Margarita", "María", "Mariana", "Maricarmen", "Mariela",
        "Marina", "Marta", "Martina", "Mayra", "Melissa", "Mercedes", "Micaela", "Michelle", "Miranda", "Miriam",
        "Monserrat", "Montserrat", "Natalia", "Nayeli", "Nerea", "Nicole", "Nora", "Norma", "Olga", "Patricia",
        "Paula", "Paulina", "Pilar", "Raquel", "Rebeca", "Rita", "Rocío", "Romina", "Rosa", "Rosalía",
        "Rosario", "Sabrina", "Sandra", "Sara", "Silvia", "Sofía", "Sol", "Susana", "Tatiana", "Teresa",
        "Valentina", "Valeria", "Vanessa", "Verónica", "Victoria", "Virginia", "Viviana", "Ximena", "Yesenia", "Zaira",
        "Abigail", "Agustina", "Aída", "Ainhoa", "Alba", "Aleida", "Anahí", "Anastasia", "Angélica", "Anita",
        "Antonella", "Araceli", "Atenea", "Aurora", "Azucena", "Bárbara", "Betty", "Blanca", "Brigitte", "Candela",
        "Caridad", "Carina", "Cataleya", "Cintia", "Dafne", "Dayana", "Delfina", "Dina", "Domenica", "Dulce",
        "Edith", "Eglantina", "Eli", "Elvira", "Ema", "Emperatriz", "Esmeralda", "Ester", "Eulalia", "Evelyn",
        "Fátima", "Felicia", "Filomena", "Florencia", "Frida", "Gabriella", "Gladys", "Griselda", "Gretel", "Guillermina",
        "Herminia", "Hilda", "Indira", "Irasema", "Itzel", "Janeth", "Jennifer", "Jesusa", "Joana", "Jovita",
        "Juliana", "Justina", "Kassandra", "Katya", "Kelly", "Kiara", "Lara", "Leandra", "Lidia", "Lisette",
        "Lourdes", "Luján", "Magali", "Maite", "Mara", "Marciana", "Marlene", "Matilde", "Mavis", "Mercedes",
        "Milagros", "Mirna", "Modesta", "Mónica", "Myrna", "Nadia", "Nancy", "Nayara", "Neida", "Nelly",
        "Nieves", "Noelia", "Noemí", "Nuria", "Odalys", "Ofelia", "Olimpia", "Ornella", "Paloma", "Pamela",
        "Pascuala", "Pastora", "Perla", "Petra", "Priscila", "Queralt", "Quetzali", "Quirina", "Ramona", "Reina",
        "Renata", "Rocío", "Romilda", "Rosalinda", "Sabina", "Salomé", "Samanta", "Sarahi", "Serena", "Sheila",
        "Silvana", "Socorro", "Soraya", "Tamara", "Teodora", "Trinidad", "Ursula", "Vanina", "Venus", "Violeta",
        "Wendy", "Xiomara", "Yadira", "Yanet", "Yara", "Yasmin", "Yolanda", "Zenaida", "Zulema", "Zulma",
        "María","Camila","Valentina","Sofía","Isabella","Fernanda","Mariana","Alejandra","Sara","Lucía","Laura","Juliana",
        "Daniela","Carolina","Ana","Gabriela","Juana","María","Sofía","Antonella","Emma","Valeria","Natalia","Estefanía",
        "Paula","Andrea","Lina","Marcela","Gabriela","Isabel","Karla","Victoria","Julieta","Manuela","Camila","Andrea","Melanie",
        "Nicole","Alejandra","Patricia","Vanessa","Carolina","Valeria","Catalina","Luisa","Fernanda","Xiomara","Beatriz","Adriana",
        "Fabiola","Ángela","María","Diana","Milena","Carolina","Esther","Tatiana","Lorena","Jennifer","Daniela","Zaira","Melissa",
        "Nayeli","Cristina","Verónica","Alejandra","Génesis","Natalia","Estrella","Margarita","Fabiola","Consuelo","Rocío","Beatriz",
        "Marisol","Juliana","Susana","Viviana","Mónica","Yuliana","Cinthia","Alejandra","Luz","Elena","Mireya","Paulina","Geraldine",
        "Tatiana","Ximena","Valentina","Lourdes","Patricia","Magdalena","Teresa","Yolanda","Francisca","Esperanza","Carmen","Josefa","Milagros",
    ]
    

    return random.choice(nombres_mujeres)

def generar_nombre_aleatorio():
    """Genera un nombre aleatorio."""
    nombres = [
        "JUAN", "MARIA", "LUIS", "ANA", "PEDRO", "LAURA", "JOSE", "SOFIA", "ELENA",
        "HABIBAH","ESPERANZA","LEMURY","UMELDA","PNTITLAN","LEOBARDO","MORTANDAD","BRAZILIA","YADIRA","UADALUPANO",
        "CASIMIRO","MIRANDA","JACABRIA","CRIPTONIANA","PAMELOTA","VICTORIA","ZELDA","JESSICA","LUPE","ROSA",
        "RITA","XIMENA","BEBA","ULTRANA","GAMALIELA","KARIAN","LORETIANA","DIANA ISABEL","GABRIELA FERNANDA","MONICA ALEJANDRA",
        "SOFIA MARIANA","DENISS","EMILIA","FERNANDA","GUADALUPE","HORACIA","IMELDA","JAZMIN","KAREN","MONICA",
        "NADIA","OSCARINA","PETRONILA","ROCIO","SABRINA","TARINKA","UVALDA","CRISTOBAL","ELIZABETH","CARLOS",
        "AURORA","EMMA","ALICE","OISIN","RORY","TIERNAN","CONOR","LEOKON","APOLONIO","BULMARO", "MARIANA", "RENATA",
        "DOROTEO","TRISTAN","APOLONIA","BULMARA","CIFORA","DOROTEA","EVELARDA","FREMIDA","GUSABIA","HILARIA",
        "INDONECIA","NILLORA","JEREMIOS","KAZAMIA","LORETANA","MONIQUILLA","NIONDIDA","OPOLINA","PULPANA","QUESADIRIA",
        "RAMONA","SAMILA","TRIGULA","ULARIA","VIVIANA","XINA","YOYIS","FILIBERTA","REGANA","HADANIS","UMILDADA",
        "OTRILLA","GENEBRAS","ZAMILA","WENDY","HADA","HADARA","HADASSAH","HADDIE","HADI","HADIYA","HADLEIGH",
        "HADLEY","HADRIA","HABIBI","MAXIMILIANO", "LUCIA","ARMITA","LIAM","JAKATULIA","KENIA","TRINIDAD", "DOMINGA",
        "FRANCESCA", "AMANDA","MATIAS", "BENJAMIN", "ISIDORA", "AGUSTINA", "FELIPE", "CONSTANZA", "VALENTINA", "NICOLAS",
        "JAVIERA","CAMILA", "TOMAS", "MARTINA", "FRANCISCO", "JOAQUIN", "ALEJANDRO", "ANTONIA", "GABRIEL", "DANIELA",
        "RODRIGO", "LUCAS", "IGNACIO", "PAULA", "PATRICIO", "ALONSO", "DIEGO", "ANDRES", "CLEMENTE", "PABLO", "RICARDO",
        "FLORENCIA",  "MONTSERRAT","MARTIN", "FRANCO", "AGUSTIN", "FACUNDO", "BAUTISTA", "HUGO", "RAUL", "OSCAR",
        "BRUNO", "FEDERICO", "EMILIANO", "SANTIAGO", "LEANDRO", "DAMIAN", "MILTON", "JORGE", "GONZALO", "LUCIANO",
        "IVAN", "EZEQUIEL", "SERGIO", "ANGEL", "MANUEL", "RENZO", "ALBERTO","RAMIRO", "VALENTIN", "MARIANO", "ENZO",
        "SEBASTIAN", "LEO", "ADRIAN","BEATRIZ","CAMILO","DAFNE","ESTEBAN","FABIOLA","GERARDO","HUGUETTE","INÉS","JONATHAN",
        "KATIA","LORENZO","MARCO","NATALIA","OCTAVIO","PASCUAL","QUINTIN","SALVADOR","URIEL","VANESSA","WALTER","XAVIER","ZULEMA",
        "BRIGITTE","DARIO","EVANGELINA","FELICIANO","RAFAEL","SALVADOR","TAMARA",
        "APIO","CAYO","LUCIO","MARCO","MANIO","QUINTO","SERVIO","SEXTO","ESPURIO","TITO","TIBERIO","ANTISTIA","ANTONIA",
        "ATIA","AURELIA","DRUSILLA","HELENA","HELVIA","HONORIA","HOSTIA","IRA",
        "LEONTIA","LEPIDA","LICINIA","MARCIANA","MARINIARA","MATIDIA","MESSALINA","MINERVINA",
        "BRUNO","AURELIO","ARTURO","ARMANDO","ARISTIDE","ANTONIO","AMADEO","ALONZO","ALESSANDRO","ALDO","CESARE","DANIELE",
        "DANTE","DARIO","DINO","EDOARDO","ELIO","ENNIO","ENZO","FEDERICO","FRANCESCO","FRANCO","GABRIELE","GENNARO","GERARDO",
        "GIANNI","GINO","GIOVANNI","GIULIO","LEONARDO","LEANDRO","LEOPOLDO","LORENZO","LUIGI","MANUELE","MARCELLO","MATTEO","MATTIA",
        "MAURO","NARCISO","NICO","RENATO","RENZO","RICCARDO","RICO","ROCCO","ROLANDO","ROMEO","SALVATORE","SANTO",
        "VINCENT AMAURI","ANA ALICIA","SANTOS JONATAN","LINDA STEPHANIE","LAURA CECILIA",
        "JACQUELINE","MARCO ANTONIO","PAOLA","DIANA","OLYMPIA","OSVALDO MISAEL","MARIA GUADALUPE",
        "MARIO ALBERTO","ALEJANDRO","LIZBETH ISABEL","CARLOS ALBERTO","KEIMBERLY SOFIA","AMERICA",
        "NAYELI ITZEL","ANGEL TADEO","CYNTHIA MELISSA","JOSE LUIS","ALEJANDRA","SELMA","MARIA SELINA","PALOMA ISABEL",
        "VICTOR MANUEL","LUCIA WENDOLYNE","MAYRA PALOMA","BEATRIZ GRACIELA","DORIS ESTEFANIA","ROSARIO JAQUELINE",
        "BEATRIZ GRACIELA","DORIS ESTEFANIA","ROSARIO JAQUELINE","MARIA DE LOS ANGELES","ADALI","LUIS ALBERTO","EDITH",
        "SOFIA ELIZABETH","RICARDO FRANCISCO","IVANIA GUADALUPE","ANA VIOLETA","GENESIS","DANIEL AUGUSTO","JESUS ALBERTO",
        "DIANA LAURA","KAREN YANNIRA","OLGA", "BERENICE","VIVIANA DEL ROCIO","JESSICA INGRID","GABRIEL","IMELDA SARAY","ANDREA",
        "KAREN YANNIRA","OLGA BERENICE","VIVIANA DEL ROCIO","JESSICA INGRID","GABRIEL","IMELDA SARAY","ANDREA","MARIA FERNANDA","JAZMIN PAOLA",
        "Alejandro","Álvaro","Andrés","Antonio","Arturo","Benjamín","Carlos","Cristian","Daniel","David","Diego","Eduardo","Emilio","Enrique",
        "Esteban","Fernando","Francisco","Gabriel","Gonzalo","Guillermo","Héctor","Hugo","Ignacio","Isaac","Iván","Javier","Jesús","Joaquín",
        "Jorge","José","Juan","Julián","Leonardo","Lucas","Luis","Manuel","Marcos","Mario","Martín","Mateo","Miguel","Nicolás","Óscar","Pablo",
        "Pedro","Rafael","Raúl","Ricardo","Roberto","Sergio"
    ]
  
    return random.choice(nombres)

def generar_apellido_aleatorio():
    """Genera un apellido aleatorio."""
    apellidos = [
        "GARCIA","RODRIGUEZ","GONZALEZ","LOPEZ","MARTINEZ","SANCHEZ","GOMEZ","MARTIN","JIMENEZ","HERNANDEZ",
        "RUIZ","DIAZ","MORENO","MUÑOZ","ALVAREZ","ROMERO","GUTIERREZ","ALONSO","NAVARRO","TORRES","DOMINGUEZ",
        "RAMOS","VAZQUEZ","GIL","SERRANO","MORALES","MOLINA","SUAREZ","BLANCO","ORTIZ","MARIN",
        "RUBIO","NUÑEZ","MEDINA","CASTILLO","SANZ","CORTES","IGLESIAS","SANTOS","GARRIDO","LOZANO","CANO","CRUZ",
        "FLORES","MENDEZ","HERRERA","PRIETO","PEÑA","LEON","MARQUEZ","CABRERA","GALLEGO","CALVO","VIDAL","REYES","CAMPOS",
        "FUENTES","CARRASCO","AGUILAR","CABALLERO","DIEZ","NIETO","VARGAS","SANTANA","GIMENEZ","HIDALGO","MONTERO","PASCUAL",
        "HERRERO","LORENZO","SANTIAGO","BENITEZ","DURAN","ARIAS","MORA","IBAÑEZ","FERRER","CARMONA","VICENTE","SOTO",
        "CRESPO","ROMAN","PARRA","PASTOR","VELASCO","RIVERA","SAEZ","SILVA","BRAVO","MOYA","GALLARDO","ZAMORA","COLIBRI",
        "ROJINI","PINEDA","JORRON","KILOS","MONTES","PEZ","PIEDRA","CARRASCO","VALDEZ","TERRENOS","CHONGOS","CAZARES",
        "TRAMOS","JULY", "COLMAN", "FRANCO", "PAZ","VEGA","ALVAREZ", "ARAYA", "BUSTOS", "CAMPOS", "CASTRO", "CONTRERAS", "CORNEJO", "DELGADO",
        "GALVEZ", "GARCIA", "GODOY", "GUERRERO", "HERNANDEZ", "IBARRA", "MORALES", "ORTEGA", 
        "PEREZ", "REYES", "ROJAS", "SALAZAR", "SANCHEZ", "TORRES", "VALENZUELA", "ZAMORANO",
        "FERNANDEZ", "GONZALEZ", "GOMEZ", "SANCHEZ", "ROMERO", "LOPEZ","RODRIGUEZ",
        "ALVAREZ", "TORRES", "RAMIREZ", "ACOSTA", "BENITEZ", "AGUILAR", "GUTIERREZ", 
        "MORALES", "MUÑOZ", "ORTEGA", "FLORES", "PONCE", "MEDINA", "ARAYA", "NAVARRO", "VALDEZ", 
        "VARGAS", "QUIROGA", "VERA", "CABRERA", "CARRASCO", "CARDENAS", "ESCOBAR", "PERALTA", "RIOS", 
        "SALAZAR", "SALINAS", "VILLALBA", "BRAVO", "FIGUEROA", "PEREYRA", "MALDONADO", "PALACIOS",
        "RUIZ","DIAZ","MORALES","PLASCENCIA","COLLAZO","CONTRERAS","HERNANDEZ","ALVARADO","SAUCEDO","GARCIA","DELGADO",
        "LUCAS","SALAZAR","TORRES","AMEZCUA","OLGUIN","MARTINEZ","MIRANDA","ROMO",
        "SANTINI","MARTINEZ","PEREZ","CORONADO","PEREZ","ALEMAN","MEJIA","SERRANO",
        "GUERRA","MARTINEZ","LINARES","CAMPA","GARCIA","TOLEDO","VIÑA","GALICIA","VAZQUEZ",
        "GUTIERREZ","RAMIREZ","VILLA","ALCALA","ACOSTA","CHAVEZ","CADENA","VEGA","MIRELES","DAVAR",
        "LOPEZ","LOZADA","MAQUEO","MARIN","MOYA","PORRAS","RAMIREZ","RAZO","RIVERA","ROLDAN","SERENO",
        "SOTO","VILLALOBOS","VILLANUEVA","ABUNDIS","ACUÑA","AGUILAR","ANDRADE","ARAGON","BALDERAS","BARAJAS",
        "BASAÑEZ","BUSTOS","CARMONA","CEPEDA","CONTRERAS","CORDOVA","CORNEJO","CORONADO","DIAZ","EGUIA","ESQUIVEL",
        "FERNANDEZ","GALLARDO","GALVEZ","GARCIA","GUZMAN","HERNANDEZ","HUERTA","JIMENEZ",   
    ]
    
    """ #FIXME: falta agragar la regla de apellidos compuestos en la generacion de CURP.

    "DEL VALLE","DEL PINO","DEL CAMPO","DEL CASTILLO","DEL OLMO","DEL MORAL","DEL AMO","DEL BARRIO","DEL REY","DEL VAL",
    "DEL OLMO","DEL MORAL","DEL AMO","DEL BARRIO","DEL REY","DEL VAL"
    """
    
    return random.choice(apellidos)



def generar_cp_aleatorio():
    cp_aleatorios   = ["56600", "56604", "56605", "56606", "56607", "56608", "56609", "56620", "56624", "56625", "56640", "56641", 
        "56643", "56644", "56646", "56620", "56624", "56625", "56640", "56641", "56643", "56644", "56646","52775","52776","52777",
        "54000","54009","54010","54015","54016","54017","54020","54021","54022","54023","54025","54026","54028","54030","54033",
        "54037","54038","54040","54049","54050","54054","54055","54057","54059","54060","54063","54067","54068","54069","54070",
        "54073","54075","54076","54080","54090","54092","54093","54094","54098","54100","54108","54109","52770","52773","52774",
        "52140","52143","52144","52145","52146","52147","52148","52149","52150","52154","52155","52156","52157","52158","52159",
        "52160","52161","52163","52164","52165","52166","52167","52760","52763","52764","52765","52766","52767","52768","52769",
        "52778","52779","52780","52783","52784","52785","52786","52787","52788","52789","52790","52793","52794","52795","52967"
        "52500","52503","52504","52505","52506","52900","52909","52910","52915","52916","52918","52919","52920","52923","52924",
        "52925","52926","52927","52928","52929","52930","52934","52936","52937","52938","52940","52945","56236","56237",
        "52946","52947","52948","52949","52950","52953","52956","52957","52958","52959","52960","52965","52966","56240","56243",
        "54600","54602","54603","54604","54605","54607","54608","54610","54614","54615","54616","54615","54616","56223","56224",
        "56100","56103","56105","56106","56110","56120","56130","56140","56150","56160","56170","56200","56225","56226","56227",
        "56203","56204","56205","56207","56208","56210","56213","56214","56215","56216","56217","56220","56230","56233","56235",
        "53000","53010","53030","53040","53050","53060","53070","53100","53110","53115","53116","53117","53119","53120","53124",
        "53125","53126","53127","53128","53129","53130","53138","53140","53150","53160","53170","53177","53178","53179","53200",
        "53215","53216","53217","53218","53219","53220","53224","53227","53228","53229","53230","53237"
    ]
    return random.choice(cp_aleatorios)



def primera_vocal_ap_paterno(apellido):
    vocales = "aeiouAEIOU"

    apellido = apellido.strip().upper()
    
    # Recorrer el apellido y buscar la primera vocal
    # for letra in apellido.strip():
    for letra in apellido[1:]:
        if letra in vocales:
            return letra  # Retorna la primera vocal encontrada
    
    return None  # Si no hay vocales, retorna None


def primera_consonante_interna(apellido):
    vocales = "aeiouAEIOU"
    
    # Eliminar espacios en blanco alrededor del apellido
    apellido = apellido.strip()
    
    # Verificar que el apellido tenga al menos dos letras
    if len(apellido) < 2:
        return None  # No hay suficiente longitud para una consonante interna

    # Recorrer el apellido desde la segunda letra en adelante
    for i in range(1, len(apellido)):  # Comienza en índice 1 para omitir la inicial
        if apellido[i].isalpha() and apellido[i] not in vocales:
            return apellido[i]  # Retorna la primera consonante interna encontrada
    
    return None # Si no encuentra consonantes internas, retorna None


def primera_consonante_interna_segundo_apellido(apellido):
    vocales = "aeiouAEIOU"
    
    # Eliminar espacios en blanco y asegurar que hay suficientes caracteres
    apellido = apellido.strip()
    
    # Recorrer el apellido desde la segunda letra para evitar la inicial
    for i in range(1, len(apellido)):
        if apellido[i].isalpha() and apellido[i] not in vocales:
            return apellido[i]  # Retorna la primera consonante interna encontrada
    
    return None  # Si no encuentra consonantes internas, retorna None


def primera_consonante_interna_nombre(nombre):
    vocales = "aeiouAEIOU"
    
    # Eliminar espacios en blanco y asegurar que hay suficientes caracteres
    nombre = nombre.strip()
    
    # Recorrer el nombre desde la segunda letra para evitar la inicial
    for i in range(1, len(nombre)):
        if nombre[i].isalpha() and nombre[i] not in vocales:
            return nombre[i]  # Retorna la primera consonante interna encontrada
    
    return None  # Si no encuentra consonantes internas, retorna None




def numeros_aleatorios():
    num1 = random.randint(0, 99)
    
    return f"{num1:02}"  # Formato de dos dígitos



def generar_curp(nombre, genero, ap_paterno, ap_materno):
    """Genera un CURP basado en el nombre y apellidos."""
    primera_vocal_paterno = primera_vocal_ap_paterno(ap_paterno)
    entidad_federativa = "AS"
    # fecha_nacimiento = f"{random.randint(50, 99)}{random.randint(1, 12):02d}{random.randint(1, 28):02d}"
    fecha_nacimiento = f"070101"
    # consonantes = "".join(random.choices(string.ascii_uppercase, k=3))
    consonante_interna_ap_paterno= primera_consonante_interna(ap_paterno)
    consonante_interna_ap_materno = primera_consonante_interna_segundo_apellido(ap_materno)
    consonante_interna_nombre = primera_consonante_interna_nombre(nombre)
    if genero == "H":
        sexo = "H"
    elif genero == "M":
        sexo = "M"
    else:
        sexo = random.choice("HM")
    
    return f"{ap_paterno[:1].upper()}{primera_vocal_paterno}{ap_materno[:1].upper()}{nombre[:1].upper()}{fecha_nacimiento}{sexo}{entidad_federativa}{consonante_interna_ap_paterno}{consonante_interna_ap_materno}{consonante_interna_nombre}{numeros_aleatorios()}"





grupos = ["Alfa", "Beta", "Gamma", "Delta", "Epsilon",
    "LAS_PULQUERAS_PODEROSAS","ESPUMA_SAGRADA","ESPUMA_MILAGROSA","LAS_TEPORINGAS","HIJAS_DEL_MAGUEY","GUERRERAS_DE_PULQUE",
    "LAS_TLACHIQUERAS","LAS_CURADAS","AGAVE_DIVINO","AGAVE_HELADO","FUERZA_PULQUERA","LAS_DIOSAS_DEL_N_CTAR","HURACANAS",
    "LAS_NINJAS","ATL_TICO_CORAZON","LAS_DE_COBRE","GLADIADORAS","GIGANTES_DE_ACERO","MU_ECAS_DE_PORCELANA","NENAS_RAPTOR",
    "DEPORTIVO_VENUS", "DEPORTIVO_ESTRELLA_DE_PLATA", "NENAS_DE_VENUS", "AFFRODITAS", "VENGADORAS_DEL_BAL_N", "MUJERES_DEL_ZODIACO", 
    "DIOSAS_DEL_AMOR", "ATL_TICO_BURBUJA", "LAS_ESTRELLAS_ROSADAS", "DESTELLOS_DE_PINOL", "ATL_TICO_DE_PULQUE", "SANGRE_DE_PULQUE",
    "CHICAS_DEL_AMOR", "ATL_TICO_DE_PULQUE", "SANGRE_DE_PULQUE", "RAYOS_DE_LUZ", "GOLONDRINAS_DE_ORO", "LAS_PULQUERAS_PODEROSAS",
    "ESPUMA_SAGRADA", "ESPUMA_MILAGROSA","HALCONAS_DORADAS","LAS_VENCEDORAS","ESTRELLAS_BRILLANTES","LAS_INVENCIBLES","LAS_ADELITAS",
    "LAS_TEPORINGAS", "HIJAS_DEL_MAGUEY", "GUERRERAS_DE_PULQUE", "LAS_TLACHIQUERAS", "LAS_CURADAS", "AGAVE_DIVINO", "AGAVE_HELADO", 
    "FUERZA_PULQUERA", "LAS_DIOSAS_DEL_N_CTAR", "HURACANAS", "LAS_NINJAS", "ATL_TICO_CORAZON", "LAS_DE_COBRE", "GLADIADORAS", 
    "GIGANTES_DE_ACERO", "MU_ECAS_DE_PORCELANA", "NENAS_RAPTOR", "DEPORTIVO_VENUS","GUERRERAS_AZTECAS","LAS_CATRINAS","DIOSAS_DEL_MA_Z",
    "DEPORTIVO_ESTRELLA_DE_PLATA", "NENAS_DE_VENUS", "AFFRODITAS", "VENGADORAS_DEL_BAL_N", "MUJERES_DEL_ZODIACO", "DIOSAS_DEL_AMOR",
    "ATL_TICO_BURBUJA", "LAS_ESTRELLAS_ROSADAS", "DESTELLOS_DE_PINOL", "CHICAS_DEL_AMOR", "ATL_TICO_DE_PULQUE", "SANGRE_DE_PULQUE", 
    "RAYOS_DE_LUZ", "GOLONDRINAS_DE_ORO", "CEBRAS_VELOCES","CENOZA_DE_HIELO", "COMBUSTION_DEL_COMAL", "FUEGO_ETERNO",
    "FURIA_DE_UNICORNIO","SO_ADAS","LAS_REBELDES","GUILAS_DE_FUEGO","HORMIGAS_DE_FUEGO","HORMIGAS_DE_HUMO",
    "LAS_M_GICAS","LAS_CHICAS_DEL_BARRIO","JUGADORAS_CON_HONOR","LAS_PRINCESAS_DEL_UNIVERSO","LAS_CHICAS","ESTRELLAS_DEL_PARAISO",
    "LAS_CORRECAMINOS","GUERRERAS_DE_LA_CANCHA","LAS_SUPERGOLEADORAS","LAS_FUTBOL_SIMAS","LAS_MEXICAS","LAS_VALKIRIAS","ESTRELLAS_GUERRERAS",
    "AMAZONAS_DEL_SOL","LAS_GUILAS_DORADAS","TORMENTA_ROSA","LAS_FIERAS","GUERRERAS_DEL_ALBA","LAS_EMPERATRICES","RAYO_DE_LUNA",
    "FURIA_VIOLETA","SIRENAS_DEL_NORTE","LOBAS_PLATEADAS","INTR_PIDAS","FELINAS",
    "LAS_JAGUARAS","PRINCESA_DEL_MA_Z","FUERZA_MAYA","GUILAS_TONANTZIN","LAS_TEHUANAS",
    "CORAZ_N_MEXICA","LAS_QUETZALES","VALKIRIAS_DE_OAXACA","LAS_NAHUALAS","FUEGO_ZAPOTECO",
    "GUERRERAS_HUASTECAS","RAYO_MIXTECO", "LAS_FLOR_DE_CEMPAS_CHIL",
    "LAS_TLATOANIS","HIJAS_DEL_NOPAL","HIJAS_DEL_MA_Z","TEMPLARIAS_DEL_SOL","COYOTAS","HERENCIA_AZTECA","ALMAS_ETERNAS",
    "TAMALERAS", "PODEROSAS_ENCHILADAS", "LAS_SALSAS_BRAVAS", "LAS_TOSTADAS_DE_ORO", "CHICAS_DEL_MOLE", "CHAPULINAS", "FURIA_TAPAT_A",
    "TORTILLERAS", "QUESADILLOCAS", "LAS_HUARACHES", "GUACAMOLERAS", "PICANTES_Y_SABROSAS", "FLAUTAS_DORADAS", "HIJAS_DEL_MA_Z",
    "SOPESITAS", "RASPADITAS", "CHAMOYADAS", "FUERZA_TAQUERA", "LAS_PICOSITAS", "PODER_Y_TACOS", "LAS_CATRINAS_VALIENTES", 
    "GUARDIANAS_DEL_INFRAMUNDO","LAS_ALMAS_LIBRES","LUZ_Y_CALAVERAS","LAS_XOLOITZCUINTLES","ESP_RITU_DE_CEMPAS_CHIL","LAS_CALAVERITAS",
    "GUERRERAS_DEL_MICTL_N","LAS_ALTARINAS","ALMAS_ANCESTRALES","LAS_OFRENDAS","CALAVERAS_Y_FUEGO","ALMAS_DE_AZ_CAR",
    "LAS_GUARDIANAS_DE_LAS_VELAS","CATRINAS_Y_MICTLANTECUHTLI","LAS_MARIPOSAS_DEL_ALMA","LUCES_DEL_MICTL_N","CEBRAS_VELOCES",
    "FURIA_DE_UNICORNIO","SO_ADAS","LAS_REBELDES","GUILAS_DE_FUEGO","HORMIGAS_DE_FUEGO","HORMIGAS_DE_HUMO","LAS_M_GICAS","LAS_CHICAS_DEL_BARRIO",
    "JUGADORAS_CON_HONOR","LAS_PRINCESAS_DEL_UNIVERSO","LAS_CHICAS","ESTRELLAS_DEL_PARAISO","LAS_CORRECAMINOS","GUERRERAS_DE_LA_CANCHA",
    "LAS_SUPERGOLEADORAS","LAS_FUTBOL_SIMAS","LAS_MEXICAS","LAS_VALKIRIAS","ESTRELLAS_GUERRERAS","AMAZONAS_DEL_SOL","LAS_GUILAS_DORADAS",
    "TORMENTA_ROSA","LAS_FIERAS","GUERRERAS_DEL_ALBA","LAS_EMPERATRICES","RAYO_DE_LUNA","FURIA_VIOLETA","SIRENAS_DEL_NORTE",
    "LOBAS_PLATEADAS","INTR_PIDAS","FELINAS","CENOZA_DE_HIELO","COMBUSTION_DEL_COMAL","FUEGO_ETERNO","HALCONAS_DORADAS","LAS_VENCEDORAS",
    "ESTRELLAS_BRILLANTES","LAS_INVENCIBLES","LAS_ADELITAS","GUERRERAS_AZTECAS","LAS_CATRINAS","DIOSAS_DEL_MA_Z","LAS_JAGUARAS",
    "PRINCESA_DEL_MA_Z","FUERZA_MAYA","GUILAS_TONANTZIN","LAS_TEHUANAS","CORAZ_N_MEXICA","LAS_QUETZALES","VALKIRIAS_DE_OAXACA",
    "LAS_NAHUALAS","FUEGO_ZAPOTECO","GUERRERAS_HUASTECAS","LAS_TLATOANIS","HIJAS_DEL_NOPAL","CHICAS_DEL_MOLE","CHAPULINAS",
    "HIJAS_DEL_MA_Z","TEMPLARIAS_DEL_SOL","COYOTAS","HERENCIA_AZTECA","RAYO_MIXTECO","FURIA_TAPAT_A","TORTILLERAS","QUESADILLOCAS","LAS_HUARACHES",
    "TAMALERAS","PODEROSAS_ENCHILADAS","LAS_SALSAS_BRAVAS","LAS_TOSTADAS_DE_ORO",
    "GUACAMOLERAS","PICANTES_Y_SABROSAS","FLAUTAS_DORADAS","HIJAS_DEL_MA_Z","SOPESITAS","RASPADITAS","CHAMOYADAS",
    "FUERZA_TAQUERA","LAS_PICOSITAS","PODER_Y_TACOS"
]



def obtener_calles_aleatorias():
    """Devuelve una lista con 100 nombres de calles de la Ciudad de México."""
    calles = [
        "Avenida Insurgentes", "Paseo de la Reforma", "Calzada de Tlalpan", "Avenida Revolución", "Eje Central Lázaro Cárdenas",
        "Viaducto Miguel Alemán", "Avenida Chapultepec", "Avenida Patriotismo", "Circuito Interior", "Avenida de los Insurgentes Sur",
        "Calzada Ignacio Zaragoza", "Avenida Universidad", "Avenida Tláhuac", "Eje 5 Sur Eugenia", "Avenida Juárez",
        "Avenida División del Norte", "Avenida Constituyentes", "Avenida Miguel Ángel de Quevedo", "Avenida San Antonio Abad",
        "Calzada México-Tacuba", "Calzada Vallejo", "Avenida Ejército Nacional", "Avenida Horacio", "Calzada de los Misterios",
        "Calzada de Guadalupe", "Calzada Legaria", "Avenida Cuitláhuac", "Avenida Marina Nacional", "Calzada Ermita Iztapalapa",
        "Avenida de las Granjas", "Calzada Acoxpa", "Avenida de los Poetas", "Avenida Vasco de Quiroga", "Eje 10 Sur Copilco",
        "Avenida Lomas Verdes", "Eje 8 Sur Popocatépetl", "Eje 6 Sur Angel Urraza", "Eje 3 Oriente Eduardo Molina",
        "Eje 2 Norte Canal del Norte", "Eje 4 Sur Xola", "Eje 1 Norte Mosqueta", "Eje 7 Sur Municipio Libre",
        "Eje 9 Sur Río Mixcoac", "Avenida Churubusco", "Viaducto Tlalpan", "Avenida Centenario", "Avenida Hidalgo",
        "Avenida Morelos", "Avenida Fray Servando Teresa de Mier", "Avenida Montevideo", "Avenida Politécnico Nacional",
        "Calzada San Juan de Aragón", "Avenida Río Churubusco", "Calzada del Hueso", "Avenida Taxqueña", "Avenida Tezozómoc",
        "Avenida 608", "Eje 1 Oriente Anillo de Circunvalación", "Eje 2 Sur Av. del Taller", "Eje 3 Sur Av. Baja California",
        "Eje 4 Norte Talismán", "Avenida Montevideo", "Avenida Instituto Politécnico Nacional", "Avenida Eduardo Molina",
        "Avenida Plutarco Elías Calles", "Calzada Tenorios", "Avenida Miguel Hidalgo", "Avenida Ferrocarril de Cuernavaca",
        "Eje 5 Oriente Javier Rojo Gómez", "Calzada del Desierto de los Leones", "Avenida 5 de Mayo", "Avenida Presidente Masaryk",
        "Avenida Constituyentes", "Eje 5 Norte Manuel Salazar", "Avenida San Fernando", "Calzada de los Leones",
        "Eje 1 Poniente Guerrero", "Avenida Adolfo López Mateos", "Avenida Santa Lucía", "Eje 7 Oriente Troncoso",
        "Eje 8 Oriente Calzada de la Viga", "Avenida 20 de Noviembre", "Avenida Ricardo Flores Magón",
        "Avenida Hangares", "Calzada México-Xochimilco", "Calzada Ticomán", "Avenida Eje 6 Norte", "Calzada Chivatito",
        "Avenida 16 de Septiembre", "Avenida Camarones", "Calzada Atzacoalco", "Calzada Emiliano Zapata", "Avenida Madero",
        "Eje 3 Norte Avenida Cien Metros", "Eje 4 Oriente Avenida Congreso de la Unión", "Eje 6 Norte Misterios",
        "Calzada de la Ronda", "Avenida México", "Avenida Hidalgo", "Calzada San Cosme", "Calzada Tacuba",
        "Eje 2 Oriente H. Congreso de la Unión", "Eje 4 Oriente Francisco del Paso y Troncoso", "Calzada del Peñón"
    ]
    return random.choice(calles)


def generar_nombre_grupo():
    # Seleccionar un grupo aleatorio del array
    grupo_seleccionado = random.choice(grupos)
    # Generar un número aleatorio de 4 dígitos
    numero_aleatorio = random.randint(1000, 9999)
    # Concatenar el nombre del grupo con el número
    nombre_final = f"{grupo_seleccionado}{"_"}{numero_aleatorio}"
    return nombre_final


def reemplazar_ñ_por_x(texto):
    return texto.replace("ñ", "x").replace("Ñ", "X")



def generar_numero_10_digitos():
    # Genera un número aleatorio de 10 dígitos
    numero_aleatorio = random.randint(1000000000, 9999999999)  # Rango de 10 dígitos
    
    return numero_aleatorio


def generar_registros(numero_registros, tipo):
    """Genera una lista de registros con nombre, apellidos y CURP."""
    nombre_grupo = generar_nombre_grupo()
    registros = []
    for _ in range(numero_registros):

        if tipo == "h":
            nombre = generar_nombre_aleatorio_hombre()
            genero = "H"
        elif tipo == "m":
            nombre = generar_nombre_aleatorio_mujer()
            genero = "M"
        else:  # Mixto
            if random.choice([True, False]):
                nombre = generar_nombre_aleatorio_hombre()
                genero = "H"
            else:
                nombre = generar_nombre_aleatorio_mujer()
                genero = "M"

        
        
        # nombre = generar_nombre_aleatorio()
        ap_paterno = generar_apellido_aleatorio()
        ap_materno = generar_apellido_aleatorio()
        curp = generar_curp(nombre, genero, ap_paterno, ap_materno)
        # Ejemplo de uso
        curp_remplazado = reemplazar_ñ_por_x(curp)
        curp_remplazado = curp_remplazado.upper()
        numero_aleatorio = generar_numero_10_digitos()
        
        nombre = nombre.upper()
        nombre = limpiar_texto(nombre)

        nombre_referencia = generar_nombre_aleatorio()
        nombre_referencia = nombre_referencia.upper()


        nombre_referencia2 = generar_nombre_aleatorio()
        nombre_referencia2 = nombre_referencia2.upper()

        ap_paterno = ap_paterno.upper()
        ap_materno = ap_materno.upper()
        cp = generar_cp_aleatorio()
        calle = obtener_calles_aleatorias()
        registros.append({
            "prospecto": nombre,
            "ap_paterno": ap_paterno,
            "ap_materno": ap_materno,
            "curp": curp_remplazado,
            "lugar_nacimiento": 'AGUASCALIENTES',
            "telefono": '7293886370',
            "confirmacion": '7293886370',
            "cp": cp,
            "calle": calle,
            "num_ext": '1055',
            "estado_civil_soltera": 'SOLTERA',
            "escolaridad": 'SECUNDARIA',
            "ine": 'SI',
            "parentesco": 'PROPIO',
            "nombre_familiar": 'PALOMA RINCON RAMOS',
            "tel_familiar": numero_aleatorio,
            "caracteristicas_vivienda": 'FACHADA PIEDRA VOLCANICA',
            "referencia_ubicacion": 'FRENTE A PARQUE',
            "direccion_del_negocio": 'SAN JOSE',
            "ganancia_semanal": '4008',
            "otros_ingresos": '2508',
            "monto_pago_semanal": '1200',
            "nombre_referencia": nombre_referencia,
            "tel_referencia_celular": '5525820280',
            "nombre_referencia2": nombre_referencia2,
            "tel_referencia_celular2": '5513195062',
            "monto_credito": '15000',
            "origen_recursos_credito": 'NEGOCIO FAMILIAR',
            "destino_recursos_credito": 'CRECIMIENTO DE NEGOCIO FAMILIAR',
            "nombre_grupo": nombre_grupo  
        })
        
    return registros

#  /home/cr/Documentos/Podemos/Proyectos/POD/p/movil_1/features/data/consulta_rapida_basica.csv

def guardar_registros_csv(registros, nombre_archivo="consulta_rapida_basica.csv"):
    """Guarda los registros en un archivo CSV."""
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        campos = ["prospecto", "ap_paterno", "ap_materno", "curp","lugar_nacimiento","telefono","confirmacion","cp","calle","num_ext","estado_civil_soltera","escolaridad","ine","parentesco","nombre_familiar","tel_familiar","caracteristicas_vivienda","referencia_ubicacion","direccion_del_negocio","ganancia_semanal","otros_ingresos","monto_pago_semanal","nombre_referencia","tel_referencia_celular","nombre_referencia2","tel_referencia_celular2","monto_credito","origen_recursos_credito","destino_recursos_credito","nombre_grupo"]
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(registros)
        print(f"Registros guardados en el archivo {nombre_archivo}")

    if registros:
        ultimo_registro = registros[-1] 

    # Guardar solo la columna "nombre_grupo" en grupo.csv
        with open("grupo.csv", mode='w', newline='', encoding='utf-8') as archivo_grupo:
            escritor_grupo = csv.DictWriter(archivo_grupo, fieldnames=["nombre_grupo"])
            escritor_grupo.writeheader()
            # escritor_grupo.writerows([{"nombre_grupo": registro["nombre_grupo"]} for registro in registros])
            escritor_grupo.writerow({"nombre_grupo": ultimo_registro["nombre_grupo"]})









def main():
    print("Generador de nombres y CURP")
    try:
        numero_registros = int(input("¿Cuántos registros deseas generar? "))
        tipo = input("¿Deseas generar nombres de 'h', 'm' o 'x'? ").strip().lower()

        if tipo not in ["h", "m", "x"]:
            print("Opción inválida. Debes escribir 'h', 'm' o 'x'.")
            return
        
        registros = generar_registros(numero_registros, tipo)
        # registros = generar_registros(numero_registros, tipo)
        guardar_registros_csv(registros)
        print("Registros generados con éxito:")

        for registro in registros:
            print(registro)
    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()



