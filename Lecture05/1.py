import circle
import rectangle
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICB = 2
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5
def main():
    choice = 0 
    while choice != QUIT_CHOICE:
        display_menu()
        choice =  int(input('Enter your choice:'))
        if choice == AREA_CIRCLR_CHOICE:
            radiius = 
            ptinr('The area is', circle.area(radius))
