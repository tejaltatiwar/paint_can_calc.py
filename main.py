import math
test_h=int(input("Height of wall:"))
test_w = int(input("width of wall:"))
coverage=int(input("how much one can can paint?"))
def paint_calc(height,width):
   no_of_cans=math.ceil((test_h*test_w)/coverage)
   print(f"You need {no_of_cans} cans of paint.")
paint_calc(test_h,test_w,)