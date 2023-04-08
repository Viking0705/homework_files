from pprint import pprint

def create_cook_book(file):
    cook_book = dict()   
    with open(file, 'rt', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            dish_count = int(f.readline().strip())
            ingredients = []
            for _ in range(dish_count):
                ingredient_name, quantity, measure = f.readline().strip().split('|')
                ingredients.append({'ingredient_name': ingredient_name.strip(), 
                                    'quantity': int(quantity.strip()), 
                                    'measure': measure.strip()})
            f.readline()
            cook_book[dish_name] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book('recipes.txt')
    pprint(cook_book, sort_dicts=False)
    shop_list = dict()
    for dish in dishes:
        for dish_in_cook_book in cook_book.keys():
            if dish in dish_in_cook_book:
                for ingredient in cook_book[dish]:                                      
                    if ingredient['ingredient_name'] in list(shop_list.keys()):
                        shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                    else:
                        shop_list[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'] * person_count, 
                                                                    'measure': ingredient['measure']}
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 3), sort_dicts=False)