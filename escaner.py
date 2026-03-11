import socket
from datetime import datetime

# Definimos el objetivo (Importante: solo escanea equipos autorizados)
# Usaremos 'localhost' que es tu propia computadora.
objetivo = "127.0.0.1" 

print("-" * 50)
print(f"Iniciando escaneo en el objetivo: {objetivo}")
print(f"Hora de inicio: {datetime.now()}")
print("-" * 50)

try:
    # Escanearemos los puertos del 1 al 1024 (los más comunes)
    for puerto in range(1, 1025):
        # AF_INET significa que usamos IPv4, SOCK_STREAM significa que usamos TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Un tiempo de espera corto (1 segundo) para no demorar demasiado
        s.settimeout(1)
        
        # connect_ex devuelve 0 si la conexión es exitosa (puerto abierto)
        resultado = s.connect_ex((objetivo, puerto))
        
        if resultado == 0:
            print(f"[*] El puerto {puerto} está ABIERTO")
            
        s.close()

except KeyboardInterrupt:
    print("\nSaliendo del programa...")
except socket.error:
    print("\nNo se pudo conectar al servidor.")