"""
❓ PROMPT
You found a note from your brother when you got home from school:

"Doofus, go to the store to pick up some ingredients for my recipe. Don't buy anything we already have at home like last time. I didn't make the grocery list so you'll have to do it yourself and then go to the store to buy the missing ingredients, you lazy bum. Use your own money to pay for it; you owe me for only pranking you 5 times this week anyway. Get it done before dinnertime, loser."

Your brother's a jerk and gave you the recipe in the hardest possible way to decipher: one long line of all the quantities followed by all the ingredients. Meanwhile, the ingredients at home are in tabular format, ugh!

Example(s)
Recipe: "12 3 3 1 egGs baCon sAusaGe souRdoughBread"
At home: {"SauSage": 6, "EGgs": 4, "BACoN": 3, "banAnA": 1}
Grocery list: {"eggs": 8, "sourdoughbread": 1}

You need 12 eggs but you only have 4 at home, so you need 8 more, dweeb.
You need 3 bacon and you have 3 at home, so you don't need anymore, dweeb.
You need 3 sausage and you have 6 at home, so you don't need anymore, dweeb.
You need 1 sourdoughbread but you have none at home, so you need 1 more, dweeb.
The banana isn't a part of the recipe, so it doesn't matter, dweeb.

Your brother swears he could do this so much faster than you, but he's got more important things to do like go grind the half-pipe with some gnarly shredz.
'''
"""

def get_grocery_list(bros_recipe: str, ingredients_at_home: dict) -> dict:
    grocery_list = dict()
    
    recipe = bros_recipe.split(" ")
    print(recipe)
    midpoint = len(recipe) // 2
    
    for i in range(midpoint):
        item = recipe[midpoint + i].lower()
        if item in ingredients_at_home:
            print(item)
            amount_at_home = ingredients_at_home[item]
            amount_needed = int(recipe[i]) - amount_at_home
            if amount_needed > 0:
                grocery_list[item] = amount_needed
        else:
            grocery_list[item] = int(recipe[i])
                
    print(grocery_list)
    return grocery_list

get_grocery_list("12 3 3 1 egGs baCon sAusaGe souRdoughBread", {"sausage": 6, "eggs": 4, "bacon": 3, "banana": 1})