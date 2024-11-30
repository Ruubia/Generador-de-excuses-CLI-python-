import random

# Listas de partes de una excusa
subjects = ["Mi perro", "El vecino", "Un hacker", "Un fantasma", "Mi profesor"]
verbs = ["comió", "rompió", "escondió", "robó", "destruyó"]
objects = ["mi tarea", "mi computadora", "mis llaves", "el proyecto", "mi celular"]
circumstances = [
    "justo antes de entregarlo.",
    "mientras dormía.",
    "durante una tormenta.",
    "cuando nadie estaba viendo.",
    "al intentar arreglarlo."
]

def generate_excuse():
    """
    Genera una excusa al azar combinando elementos de las listas.
    """
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object_ = random.choice(objects)
    circumstance = random.choice(circumstances)
    return f"{subject} {verb} {object_} {circumstance}"

def main():
    print("¡Bienvenido al Generador de Excusas CLI! 🎲")
    while True:
        print("\nGenerando una excusa aleatoria...")
        excuse = generate_excuse()
        print(f"📝 Excusa: {excuse}")
        
        user_input = input("\n¿Quieres otra excusa? (s/n): ").strip().lower()
        if user_input == "n":
            print("¡Hasta luego! 🖐️")
            break

if __name__ == "__main__":
    main()
