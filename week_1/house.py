name = input("Whats's your name ? ")

match name:
    # case "Harry":
    #     print("Gryfinder")
    # case "Hermione":
    #     print("Gryfinder")
    # orrrrrr
    case "Harry" | "Hermione" | "Ron":
      print("Gryfinder")
    case "Draco":
        print("Slynther")
    case _:
        print("who ?")