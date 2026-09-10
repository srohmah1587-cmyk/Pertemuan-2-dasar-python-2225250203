print("KALKULATOR KOORDINAT DUA TITIK")
x_A = float(input("x titik A:0 "))
y_A = float(input("y titik A:0 "))
x_B = float(input("x titik B:3 "))
y_B = float(input("y titik B:4 "))

dx = x_B - x_A
dy = y_B - y_A

jarak_a_ke_b = ((dx ** 2) + (dy ** 2)) ** 0.5

titik_tengah_x = (x_A + x_B) / 2
titik_tengah_y = (y_A + y_B) / 2

print()
print(f"Titik A        : ({x_A:.2f}, {y_A:.2f})")
print(f"Titik B        : ({x_B:.2f}, {y_B:.2f})")
print(f"Perubahan      : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B   : {jarak_a_ke_b:.2f}")
print(f"Titik tengah   : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")

print("TEST CASE KASUS 2")
x_A = float(input("x titik A:-2 "))
y_A = float(input("y titik A:1 "))
x_B = float(input("x titik B:4 "))
y_B = float(input("y titik B:1 "))

dx = x_B - x_A
dy = y_B - y_A

jarak_a_ke_b = ((dx ** 2) + (dy ** 2)) ** 0.5

titik_tengah_x = (x_A + x_B) / 2
titik_tengah_y = (y_A + y_B) / 2

print()
print(f"Titik A        : ({x_A:.2f}, {y_A:.2f})")
print(f"Titik B        : ({x_B:.2f}, {y_B:.2f})")
print(f"Perubahan      : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B   : {jarak_a_ke_b:.2f}")
print(f"Titik tengah   : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")

print("TEST CASE KASUS 3")
x_A = float(input("x titik A:2.5 "))
y_A = float(input("y titik A:-1 "))
x_B = float(input("x titik B:2.5 "))
y_B = float(input("y titik B:3 "))

dx = x_B - x_A
dy = y_B - y_A

jarak_a_ke_b = ((dx ** 2) + (dy ** 2)) ** 0.5

titik_tengah_x = (x_A + x_B) / 2
titik_tengah_y = (y_A + y_B) / 2

print()
print(f"Titik A        : ({x_A:.2f}, {y_A:.2f})")
print(f"Titik B        : ({x_B:.2f}, {y_B:.2f})")
print(f"Perubahan      : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B   : {jarak_a_ke_b:.2f}")
print(f"Titik tengah   : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")