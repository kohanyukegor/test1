hp = 20
def take_damage(damage):
    global hp
    hp -= damage
    print("Осталось "+str(hp)+" хп."+
          "Персонаж получил "+str(damage)+" урона.")

def count_damage(damage_type):
    if damage_type == "крипер":
        damage = 10
    elif damage_type == "лава":
        damage = 5
    return damage

x=input("Введите тип урона: ")
damage=count_damage(x)
take_damage(damage)


