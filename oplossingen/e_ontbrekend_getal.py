def ontbrekend_getal(lijst):
    return 55 - sum(lijst)


print(ontbrekend_getal([2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 1
print(ontbrekend_getal([5, 3, 8, 9, 10, 4, 1, 6, 7]))  # 2
print(ontbrekend_getal([7, 2, 3, 6, 5, 9, 1, 4, 8]))  # 10
print(ontbrekend_getal([10, 5, 1, 2, 4, 6, 8, 3, 9]))  # 7

# Andere mogelijke oplossingen:

# def ontbrekend_getal(lijst):
#     for n in range(1,11):
#         if n not in lijst:
#             return n

# def ontbrekend_getal(lijst):
#     lijst.sort()
#     nummer = 1
#     for item in lijst:
#         if item != nummer:
#             return nummer
#         nummer += 1
#     return 10 # Als 1 t.e.m. 9 erin zaten