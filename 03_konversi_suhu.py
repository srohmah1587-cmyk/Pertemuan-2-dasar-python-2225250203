KELVIN_OFFSET: float = 273.15
celsius =float(input("Masukkan suhu dalam Celsius:0 "))
fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")

KELVIN_OFFSET = 273.15
celsius = float(input("Masukkan suhu dalam Celsius:100 "))
fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")