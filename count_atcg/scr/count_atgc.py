import sys

# Verifica que se haya proporcionado el nombre del archivo como argumento
if len(sys.argv) < 2:
    print("Uso: Python count_atcg.py nombre_del_archivo [nucleotidos]")
    sys.exit(1)

nombre_archivo = sys.argv[1]

try:
    # Abre el archivo en modo lectura
    with open(nombre_archivo, 'r') as file:
        # Lee la cadena de ADN del archivo
        dna_sequence = file.read()

        # Verifica si el archivo está vacío
        if not dna_sequence.strip():
            print(f"Sorry, the file '{nombre_archivo}' is empty")
            sys.exit(1)

        # Verifica si el archivo contiene caracteres no válidos
        invalid_characters = set(dna_sequence) - {'A', 'C', 'G', 'T'}
        if invalid_characters:
            print(f"Error: The file '{nombre_archivo}' contains invalid characters: {', '.join(invalid_characters)}")
            sys.exit(1)

except FileNotFoundError:
    print(f"Sorry, couldn´t find the file: '{nombre_archivo}'")
    sys.exit(1)

# Obtener los nucleótidos específicos, si se proporcionan
nucleotidos_especificos = set(arg.upper() for arg in sys.argv[2:]) if len(sys.argv) > 2 else {'A', 'C', 'G', 'T'}

# Si se proporcionaron argumentos de nucleótidos inválidos, mostrar un mensaje de error y salir
nucleotidos_invalidos = set(arg.upper() for arg in sys.argv[2:]) - {'A', 'C', 'G', 'T'}
if nucleotidos_invalidos:
    print(f"Error: invalid base argument: {', '.join(nucleotidos_invalidos)}")
    sys.exit(1)

# Inicializa contadores para cada símbolo
count_A = 0
count_C = 0
count_G = 0
count_T = 0

# Itera sobre la cadena de ADN y cuenta las ocurrencias de cada símbolo
for symbol in dna_sequence:
    if symbol not in {'A', 'T', 'C', 'G'}:
        print(f"Error: Sequence contains '{symbol}', it is an invalid character")
        sys.exit(1)
    elif symbol == 'A':
        count_A += 1
    elif symbol == 'C':
        count_C += 1
    elif symbol == 'G':
        count_G += 1
    elif symbol == 'T':
        count_T += 1

# Imprime el resultado para los nucleótidos específicos o para todos si no se especifican
if nucleotidos_especificos:
    for nucleotido in nucleotidos_especificos:
        count = 0
        if nucleotido == 'A':
            count = count_A
        elif nucleotido == 'C':
            count = count_C
        elif nucleotido == 'G':
            count = count_G
        elif nucleotido == 'T':
            count = count_T
        print(f'La base {nucleotido} aparece {count} veces.')
else:
    print(f'La base A aparece {count_A} veces.')
    print(f'La base C aparece {count_C} veces.')
    print(f'La base G aparece {count_G} veces.')
    print(f'La base T aparece {count_T} veces.')

