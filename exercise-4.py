# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


print('hey hottie, enter the lengths of 3 sides of a triangle in cm (number only):')

user_typed_a = input("a: ")  
user_typed_a = int(user_typed_a)

user_typed_b = input("b: ")
user_typed_b = int(user_typed_b)

user_typed_c = input("c: ") 
user_typed_c = int(user_typed_c)

while(True):
    if user_typed_a == user_typed_b and user_typed_a == user_typed_c and user_typed_b == user_typed_c: 
        print(f'a triangle with the sides of {user_typed_a} cm, {user_typed_b} cm and {user_typed_c} cm is an equalateral triangle')
        break 

    elif user_typed_a != user_typed_b and user_typed_c != user_typed_a and user_typed_b != user_typed_c: 
        print(f'a triangle with the sides of {user_typed_a} cm, {user_typed_b} cm and {user_typed_c} cm is a scalene triangle')
        break

    elif user_typed_a == user_typed_b or user_typed_a == user_typed_c or user_typed_b == user_typed_c:
        print(f'a triangle with the sides of {user_typed_a} cm, {user_typed_b} cm and {user_typed_c} cm is an isoceles triangle')
        break

