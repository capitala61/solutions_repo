import os

# Lista nazw plików
table_of_contents = [
    "Logic",
    "Set Theory",
    "Relations",
    "Functions",
    "Combinatorics",
    "Sequences and Series",
    "Induction",
    "Number Theory",
    "Recurrence",
    "Graph Theory"
]

# Tworzenie plików z numerami porządkowymi
for i, topic in enumerate(table_of_contents, start=1):
    # Zamiana spacji na podkreślenia w nazwach plików
    filename = f"_{i:02d} {topic.replace(' ', '_')}.md"
    
    # Tworzenie pliku
    with open('docs/3 Discret_Mathematics/'+filename, "w") as file:
        file.write(f"# {i:02d} {topic}\n\n")  # Dodanie tytułu w pliku
    print(f"Stworzono plik: {filename}")

print("Wszystkie pliki zostały utworzone!")
