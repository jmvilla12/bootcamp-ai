from collections import Counter

#1 Build a diccionary, show it in the screen with real data for an activity that you do in your daily life
gym_users = {
    "1004752617" : {
        "Nombre"   : "Jose"   ,
        "Edad"     : "24"     ,
        "Ciudad"   : "Pereira",
        "Gimnasio" : {
            "Nombre" : "Movifitness",
            "Sede"   : "El poblado",
        },
        "Intensidad" : {
            "Frecuencia" : "5 veces a la semana",
            "Duracion"   : "2 horas",
        },
    },
    "1193453911" : {
        "Nombre"   : "Sebastian"   ,
        "Edad"     : "24"     ,
        "Ciudad"   : "Pereira",
        "Gimnasio" : {
            "Nombre" : "Gimnasio UTP",
            "Sede"   : "UTP",
        },
        "Intensidad" : {
            "Frecuencia" : "5 veces a la semana",
            "Duracion"   : "2 horas",
        },
    },
}

#2 Build a diccionary that contains data that you can analize from 10 canpists (students from the bootcamp)
campistas = {
    "1004752617" : {
        "Nombre"   : "Jose"   ,
        "Edad"     : "24"     ,
        "Ciudad"   : "Pereira",
        "RH"       : "O+"     ,
        "Idiomas"  : ["Español", "Inglés", "Francés"],
        "Hobbies"  : ["Videojuegos", "Gimnasio", "Aprender idiomas"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria en Mecatronica",
            "Semestre" : "Graduado",
        },
    },
    "1193453911" : {
        "Nombre"   : "Sebastian"   ,
        "Edad"     : "24"     ,
        "Ciudad"   : "Pereira",
        "RH"       : "A+"     ,
        "Idiomas"  : ["Español", "Inglés"],
        "Hobbies"  : ["Lectura", "Ciclismo"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria de Sistemas",
            "Semestre" : "8",
        },
    },
    "1004752618" : {
        "Nombre"   : "Maria"   ,
        "Edad"     : "22"     ,
        "Ciudad"   : "Bogotá",
        "RH"       : "B+"     ,
        "Idiomas"  : ["Español", "Inglés", "Alemán"],
        "Hobbies"  : ["Pintura", "Natación"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria Industrial",
            "Semestre" : "6",
        },
    },
    "1004752619" : {
        "Nombre"   : "Carlos"   ,
        "Edad"     : "23"     ,
        "Ciudad"   : "Medellín",
        "RH"       : "AB+"     ,
        "Idiomas"  : ["Español", "Inglés"],
        "Hobbies"  : ["Fútbol", "Cine"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria Civil",
            "Semestre" : "7",
        },
    },
    "1004752620" : {
        "Nombre"   : "Laura"   ,
        "Edad"     : "21"     ,
        "Ciudad"   : "Cali",
        "RH"       : "O-"     ,
        "Idiomas"  : ["Español", "Inglés", "Italiano"],
        "Hobbies"  : ["Danza", "Viajar"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria Química",
            "Semestre" : "5",
        },
    },
    "1004752621" : {
        "Nombre"   : "Andres"   ,
        "Edad"     : "25"     ,
        "Ciudad"   : "Cartagena",
        "RH"       : "A-"     ,
        "Idiomas"  : ["Español", "Inglés"],
        "Hobbies"  : ["Pesca", "Cocina"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria Electrónica",
            "Semestre" : "9",
        },
    },
    "1004752622" : {
        "Nombre"   : "Diana"   ,
        "Edad"     : "24"     ,
        "Ciudad"   : "Bucaramanga",
        "RH"       : "B-"     ,
        "Idiomas"  : ["Español", "Inglés", "Portugués"],
        "Hobbies"  : ["Yoga", "Fotografía"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria Ambiental",
            "Semestre" : "10",
        },
    },
    "1004752623" : {
        "Nombre"   : "Jorge"   ,
        "Edad"     : "26"     ,
        "Ciudad"   : "Manizales",
        "RH"       : "O+"     ,
        "Idiomas"  : ["Español", "Inglés"],
        "Hobbies"  : ["Escalada", "Música"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria Mecánica",
            "Semestre" : "4",
        },
    },
    "1004752624" : {
        "Nombre"   : "Valentina"   ,
        "Edad"     : "20"     ,
        "Ciudad"   : "Pereira",
        "RH"       : "AB-"     ,
        "Idiomas"  : ["Español", "Inglés", "Francés"],
        "Hobbies"  : ["Lectura", "Viajar", "Moda"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria Industrial",
            "Semestre" : "8",
        },
    },
    "1004752625" : {
        "Nombre"   : "Luis"   ,
        "Edad"     : "22"     ,
        "Ciudad"   : "Cúcuta",
        "RH"       : "A+"     ,
        "Idiomas"  : ["Español", "Inglés"],
        "Hobbies"  : ["Ciclismo", "Videojuegos"],
        "Bootcamp" : {
            "Nombre" : "MisionTIC",
            "Ciudad" : "Pereira",
            "Sede"   : "UTP",
        },
        "Carrera" : {
            "Nombre" : "Ingenieria de Software",
            "Semestre" : "2",
        },
    }
}

#3 What operations could you perform to analyze the content?
# I can count the number of campistas, find the average age of the campistas, and count the number of campistas per city.


# 4. Build a dictionary and perform 3 operations
# 1. Count the number of campistas
num_campistas = len(campistas)
print(f"Number of campistas: {num_campistas}")

# 2. Find the average age of the campistas
total_age = sum(int(campista["Edad"]) for campista in campistas.values())
average_age = total_age / num_campistas
print(f"Average age of campistas: {average_age:.2f}")

# 3. Count the number of campistas per city
cities = [campista["Ciudad"] for campista in campistas.values()]
city_counts = Counter(cities)
print("Number of campistas per city:")
for city, count in city_counts.items():
    print(f"{city}: {count}")

# 5. Define if there's any difference between a list and a dictionary. And if there are different examples of each one. Please build 3 examples

# Lists are ordered collections of items that can be accessed by their index. They are defined using square brackets [].
# Dictionaries are unordered collections of key-value pairs that can be accessed by their keys. They are defined using curly braces {}.

# Examples of lists:
list_example1 = [1, 2, 3, 4, 5]
list_example2 = ["apple", "banana", "cherry"]
list_example3 = [True, False, True, False]

# Examples of dictionaries:
dict_example1 = {"name": "John", "age": 30, "city": "New York"}
dict_example2 = {"brand": "Ford", "model": "Mustang", "year": 1964}
dict_example3 = {"fruit": "apple", "color": "red", "quantity": 10}


# 6. Realize an example that uses all the concepts seen in the last steps


