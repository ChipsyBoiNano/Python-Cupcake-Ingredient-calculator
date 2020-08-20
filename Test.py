#  THE CUPKAKE ITSELF:
# this is for 5 vanilla flavored cupcakes


batch = 5


answer = input('Hey, do you want to make some cupcakes?\n')
if answer == 'yes':
    print('Sure!')
elif answer == 'no':
    print('Jeez, okay.')
    quit()
else:
    print('I did not understand.')
    quit()

answer2 = input('Let\'s start with the cupcake itself, are you ready?\n')
if answer2 == 'yes':
    print('Let\'s do this!')
elif answer2 == 'no':
    print('Jeez, okay.')
    quit()
else:
    print('Sorry, i did not understand that!')
    quit()

#-------FLOUR--------------------------------------------------------------  
required_flour = 64
flour = input('You need {} grams of flour,'' '
              'how much do you have?\n' .format(required_flour))
needed_flour = required_flour - int(flour)
if int(flour) >= required_flour:
    print('Nice, you have enough!')
else:
    print('You need {} more grams, go get it.' .format(needed_flour))
#-------BAKING POWDER------------------------------------------------------
required_baking_powder = 2
baking_powder = input('You need {} grams of baking powder or a 1/2 teaspoon,'' '
                        'how much do you have?\n' .format(required_baking_powder))
needed_baking_powder = required_baking_powder - float(baking_powder)
if float(baking_powder) >= required_baking_powder:
    print('You have enough, you can proceed')
else:
    print(f'You need {needed_baking_powder:.2f} more grams, go get it.')
#-------SALT---------------------------------------------------------------
required_salt = 0.75
salt = input('You need {} grams of salt or a 1/8 teaspoon,'' '
            'how much do you have?\n' .format(required_salt))
needed_salt = required_salt - float(salt)
if float(salt) >= required_salt:
    print('You have enough salt, precoeed')
else:
    print(f'You need {needed_salt:.2f} more grams, go get it.')
#-------EGG-----------------------------------------------------------------
required_eggs = 1
eggs = input('You need {} egg, do you have an egg?\n' .format(required_eggs))
if eggs == 'yes':
    print('Nice, you have an egg')
else:
    print('Go get an egg then.')
#-------GRANULATED SUGAR----------------------------------------------------
required_granulated_sugar = 50
granulated_sugar = input('You need {} grams of granulated sugar or 1/4 cup,'' '
                        'how much do you have?\n' .format(required_granulated_sugar))
needed_granulated_sugar = required_granulated_sugar - int(granulated_sugar)
if int(granulated_sugar) >= required_granulated_sugar:
    print('You have enough sugar, lets continue')
else:
    print('You need {} more grams, go get that' .format(needed_granulated_sugar))
#-------BUTTER---------------------------------------------------------------
required_butter = 57
butter = input('You need {} grams of butter or 4 tablespoons,'' '
               'how much do you have?\n' .format(required_butter))
needed_butter = required_butter - int(butter)
if int(butter) >= required_butter:
    print('You have enough butter!')
else:
    print('You need {} more grams, go get it' .format(needed_butter))
#-------PURE VANILLA EXTRACT-------------------------------------------------
required_vanilla = 8.4
vanilla = input('You need {} grams of pure vanilla extract or 2 teaspoons,'' '
                'how much do you have?\n' .format(required_vanilla))
needed_vanilla = required_vanilla - float(vanilla)
if float(vanilla) >= required_vanilla:
    print('Good, you have enough, proceed')
else:
    print(f'You need {needed_vanilla:.2f} more grams, go get it')
#-------MILK-----------------------------------------------------------------
required_milk = 59
milk = input('You need {} milliliters of milk or 1/4 a cup,'' '
            'how much do you have?\n' .format(required_milk))
needed_milk = required_milk - int(milk)
if int(milk) >= required_milk:
    print('Nice, you have enough, proceed')
else:
   print('You need {} more milliliters, go get it' .format(needed_milk))



answer3 = input('Type "yes" to continue, Type "no" to exit.\n')
if answer3 == 'yes':
    print('Sure, we\'ll continue!')
elif answer3 == 'no':
    quit()

answer4 = input('Now, we\'re going to make the frosting, are you ready?\n')
if answer4 == 'yes':
    print('Lets continue then shall we')
else:
    quit()
#-------SUGAR----------------------------------------------------------------
required_sugar = 75
sugar = input('You need {} grams of powdered sugar or 3/4 a cup,'' '
              'how much do you have?\n' .format(required_sugar))
needed_sugar = required_sugar - int(sugar)
if int(sugar) >= required_sugar:
    print('Good, you have enough sugar, you can continue')
else:
    print('You need {} more grams, go get it' .format(needed_sugar))
#-------BUTTER---------------------------------------------------------------
required_butter1 = 43
butter1 = input('You need {} grams of butter or 3 tablespoons,'' '
              'how much do you have?\n' .format(required_butter1))
needed_butter1 = required_butter1 - int(butter1)
if int(butter1) >= required_butter1:
    print(' you have enough, continue')
else:
    print('You need {} more grams, go get it' .format(needed_butter1))
#-------VANILLA--------------------------------------------------------------
required_vanilla1 = 1
vanilla1 = input('You need {} grams of pure vanilla extract or 1/4 a teaspoon,'' '
                 'how much do you have?\n' .format(required_vanilla1))
needed_vanilla1 = required_vanilla1 - float(vanilla1)
if float(vanilla1) >= required_vanilla1:
    print('You have enough, go ahead')
else:
    print(f'You need {needed_vanilla1:.2f} more grams, go get it')
#-------MILK-----------------------------------------------------------------
required_milk1 = 2.5
milk1 = input('You need {} grams of milk or 1/2 a teaspoon,'' '
              'how much do you have?\n' .format(required_milk1))
needed_milk1 = required_milk1 - float(milk1)
if float(milk1) >= required_milk1:
    print('You have enough, proceed')
else:
    print(f'You need {required_milk1:.2f} more milligrams of mik, go get it')




print('Now, if you have all the ingredients in the right ammounts you can start making cupcakes,\n'
      'so first of all: \n'
      '1/Preheat oven to 350°F. Spray 5 muffin cups or place 5 liners in a muffin pan.\n'
      '2/In a small bowl, combine flour, baking powder, and the salt. Set it aside\n'
      '3/In a large bowl, whisk the egg and sugar for about 30 seconds.\n'
      'Add the vanilla extract and melted butter and whisk until well combined\n'
      '4/Add half the dry ingredients to the wet ingredients and whisk until just combined.\n'
      'Add the milk, and whisk until just combined. Add the remaining dry ingredients and whisk\n'
      'until combined (being careful not to overmix)\n'
      '5/Divide the batter evenly between 5 muffin cups (each cup will be between 2/3 and 3/4 full).\n'
      'Bake for 14-16 minutes, until a toothpick inserted into the center of a cupcake comes out clean.\n'
      'Cool completely before frosting\n')


exit1 = input('So, this is the end, type "exit" to exit the program\n')
if exit1 == 'exit':
  quit()
