def answer(petya, vasya, tolia):
    place1 = "Петя" if petya > vasya and petya > tolia else "Вася" if vasya > petya and vasya > tolia else "Толя"
    place3 = "Петя" if petya < vasya and petya < tolia else "Вася" if vasya < petya and vasya < tolia else "Толя"
    place2 = "ПетяВасяТоля"
    place2 = place2.replace(place1, "")
    place2 = place2.replace(place3, "")
    print(f'''          {place1}          
  {place2}  
                  {place3}  
   II      I      III   ''')


def main():
    petya = int(input())
    vasya = int(input())
    tolia = int(input())
    answer(petya, vasya, tolia)


if __name__ == "__main__":
    main()
