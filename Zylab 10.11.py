# Joel Sibi
# 1617077

class FoodItem:

    def __init__(self, name = 'None', fat = 0.00, carbs = 0.00, protein = 0.00):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print('Number of calories for {:.2f}'.format(p2), 'serving(s): {:.2f}'.format(self.get_calories(p2)))


p1 = FoodItem(input(), float(input()), float(input()), float(input()))
p2 = float(input())
p3 = FoodItem()
p3.print_info()
print()
p1.print_info()
