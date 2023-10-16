'''
TPRG 2131 Fall 2023 Assignment 1
Oct 15, 2023
Alex Burns <alexander.burns1@dcmail.ca #100885375>

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

    (Level 1)
    1. First Area/Volume* calulation
    2. Second Area/Volume* calculation
    3. Third Area/Volume* calculation
    4. Fourth Area/Volume* calculation
    5. Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''
# code taken from chatGPT on October 15th. Prompted by asking "Give me the python code for an A/V calculator. The calculator will start by asking user for 3 input options: V/v for the calculates view (shows formula and calculated result), D/d for default view (shows only the calculated result), and Q/q to quit the program and cancel the view. Then the calculator will give 5 calculation options: the area of a circle, the area of a triangle, the area of a rectangle, the volume of a pyramid, and the volume of a rectangular prism. Or q to quit. The program will only recognize numbers and will ask the user to input a number for everything else."
import math # the program is importing math math modules

def calculate_area_circle(radius=None):     # Code in brackets taken from chatGPT. Prompted from other question when asked to add assertions. 
    if radius is None:
        radius = input("Enter the radius of the circle: ")
        while not radius.isdigit():
            radius = input("Please input a number for the radius: ")
    assert float(radius) >= 0, "Radius should be non-negative"
    area = math.pi * float(radius) ** 2
    return area # program calculates area of a circle given a radius
 
def calculate_area_triangle(base=None, height=None):             # Code in brackets taken from chatGPT. Prompted from other question when asked to add assertions.
    if base is None or height is None:
        base = input("Enter the base of the triangle: ")
        height = input("Enter the height of the triangle: ")
        while not base.isdigit() or not height.isdigit():
            print("Please input numbers for base and height.")
            base = input("Enter the base of the triangle: ")
            height = input("Enter the height of the triangle: ")
    assert float(base) >= 0, "Base should be non-negative"
    assert float(height) >= 0, "Height should be non-negative"
    area = 0.5 * float(base) * float(height)
    return area  # program calculates area of a triangle given base and height

def calculate_area_rectangle():                    
    length = input("Enter the length of the rectangle: ")
    width = input("Enter the width of the rectangle: ")
    while not length.isdigit() or not width.isdigit():
        print("Please input numbers for length and width.")
        length = input("Enter the length of the rectangle: ")
        width = input("Enter the width of the rectangle: ")
    assert float(length) >= 0, "Length should be non-negative"
    assert float(width) >= 0, "Width should be non-negative"
    area = float(length) * float(width)
    return area # program calculates area of a rectangle using length and width

def calculate_volume_pyramid():
    length = input("Enter the base length of the pyramid: ")
    width = input("Enter the base width of the pyramid: ")
    height = input("Enter the height of the pyramid: ")
    while not length.isdigit() or not width.isdigit() or not height.isdigit():
        print("Please input numbers for base length, base width, and height.")
        length = input("Enter the base length of the pyramid: ")
        width = input("Enter the base width of the pyramid: ")
        height = input("Enter the height of the pyramid: ")
    volume = (float(length) * float(width) * float(height)) / 3
    return volume   # program calculates volume of a pyramid using length, width and height

def calculate_volume_rect_prism(length=None, width=None, height=None):           # Code in brackets taken from chatGPT. Prompted from other question when asked to add assertions.        
    if length is None or width is None or height is None:
        length = input("Enter the length of the rectangular prism: ")
        width = input("Enter the width of the rectangular prism: ")
        height = input("Enter the height of the rectangular prism: ")
        while not length.isdigit() or not width.isdigit() or not height.isdigit():
            print("Please input numbers for length, width, and height.")
            length = input("Enter the length of the rectangular prism: ")
            width = input("Enter the width of the rectangular prism: ")
            height = input("Enter the height of the rectangular prism: ")
    assert float(length) >= 0, "Length should be non-negative"
    assert float(width) >= 0, "Width should be non-negative"
    assert float(height) >= 0, "Height should be non-negative"
    volume = float(length) * float(width) * float(height)
    assert volume > 0, "Calculated volume should be positive."
    return volume   # program calculates volume of rectangular prism using length, width, and height.

def main():
    while True:
        print("\nA/V Calculator")
        print("Enter 'V' for calculated view with formula, 'D' for default view without formula, or 'Q' to quit.")
        user_choice = input("Choose an option: ").lower()

        if user_choice == 'q':
            break
        elif user_choice not in ['v', 'd']:
            print("Invalid option. Please enter 'V', 'D', or 'Q'.")
            continue     # this is the first loop of the program. User picks one of two views or quits.

        print("\nSelect a calculation:")
        print("1: Area of a Circle")
        print("2: Area of a Triangle")
        print("3: Area of a Rectangle")
        print("4: Volume of a Pyramid")
        print("5: Volume of a Rectangular Prism")
        print("Q: Quit")
        calculation_choice = input("Enter choice: ").lower() # this is the second loop where the user picks the calculation they want.

        if calculation_choice == 'q':
            break
        elif calculation_choice == '1':
            result = calculate_area_circle()
            formula = "π * radius^2" if user_choice == 'v' else ""
        elif calculation_choice == '2':
            result = calculate_area_triangle()
            formula = "0.5 * base * height" if user_choice == 'v' else ""
        elif calculation_choice == '3':
            result = calculate_area_rectangle()
            formula = "length * width" if user_choice == 'v' else ""
        elif calculation_choice == '4':
            result = calculate_volume_pyramid()
            formula = "(length * width * height) / 3" if user_choice == 'v' else ""
        elif calculation_choice == '5':
            result = calculate_volume_rect_prism()
            formula = "length * width * height" if user_choice == 'v' else ""
        else:
            print("Invalid choice. Please choose a number between 1 and 5, or 'Q' to quit.")
            continue     # depening on the number they pick, the program will select a calculation formula fitted for it.

        print(f"Formula: {formula}" if formula else "")
        print(f"Result: {result}")   # program will print results.

if __name__ == "__main__":
    main()                       # code taken from chatGPT on October 15th. Prompted by asking "Give me the python code for an A/V calculator. The calculator will start by asking user for 3 input options: V/v for the calculates view (shows formula and calculated result), D/d for default view (shows only the calculated result), and Q/q to quit the program and cancel the view. Then the calculator will give 5 calculation options: the area of a circle, the area of a triangle, the area of a rectangle, the volume of a pyramid, and the volume of a rectangular prism. Or q to quit. The program will only recognize numbers and will ask the user to input a number for everything else."





