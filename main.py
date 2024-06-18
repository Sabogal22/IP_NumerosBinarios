# Función para encriptar una cadena de números binarios
def encrypt_binary(binary_string):
  # Invertir cada bit: '0' se convierte en '1' y '1' se convierte en '0'
  encrypted = ''.join('1' if bit == '0' else '0' for bit in binary_string)
  return encrypted

# Función para desencriptar una cadena de números binarios encriptados
def decrypt_binary(encrypted_string):
  # Invertir cada bit: '0' se convierte en '1' y '1' se convierte en '0'
  decrypted = ''.join('1' if bit == '0' else '0' for bit in encrypted_string)
  return decrypted

# Función para convertir una lista de números binarios en una dirección IP
def binary_to_ip(binary_numbers):
  ip_parts = []
  for binary in binary_numbers:
    # Convertir cada grupo de 8 bits en un número decimal
    decimal_value = int(binary, 2)
    ip_parts.append(str(decimal_value))
  # Unir los números decimales con puntos para formar la dirección IP
  ip_address = '.'.join(ip_parts)
  return ip_address

def main():
  # Solicitar al usuario que ingrese la secuencia de números binarios encriptados
  encrypted_bin = input("Ingrese la secuencia de números binarios encriptados: ")
    
  # Verificar si la longitud de la cadena es múltiplo de 8
  if len(encrypted_bin) % 8 != 0:
    raise ValueError("La secuencia de números binarios encriptados debe ser divisible por 8 para formar octetos.")

  # Desencriptar la secuencia de números binarios
  decrypted_bin = decrypt_binary(encrypted_bin)

  # Dividir los binarios desencriptados en grupos de 8 bits
  binary_groups = [decrypted_bin[i:i + 8] for i in range(0, len(decrypted_bin), 8)]
    
  # Convertir los grupos de 8 bits en una dirección IP
  ip_address = binary_to_ip(binary_groups)
    
  # Imprimir la dirección IP resultante
  print(f"La dirección IP es: {ip_address}")

if __name__ == "__main__":
  main()
