def main():
    my_list = [1,"Hello", True, 4.5]
    my_dict ={"firstname": "Hector", "lastname": "Sanchez"}

    super_list = [
        {"firstname": "Hector", "lastname": "Sanchez"},
        {"firstname": "Caro", "lastname": "Illa"},
        {"firstname": "Adonis", "lastname": "Quilimaco"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 1.2, 1.3, 1.4, 1.5]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for i in super_list:
        for key01, value01 in i.items():
            print(key01, "-", value01)

if __name__ == '__main__':
    main()