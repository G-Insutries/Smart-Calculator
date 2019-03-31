import Operations.algebra
import Operations.sqroot
import Text_Recognizing.text_recognizing
import Text_Recognizing.algebra
import Text_Recognizing.sqroot

usrinput = ""
txtrecog = [0, [], 0]  # [Question Kind] [Calculation Transformed] [Level]

def recognizing():
    print()

while True:
    usrinput = input(">: ")
    txtrecog = Text_Recognizing.text_recognizing.recognize(usrinput)

    if txtrecog[0] == 0:
        if txtrecog[2] == 0:
            txtrecog[1] = Operations.algebra.calculate(txtrecog[1])
        elif txtrecog[2] == 1:
            txtrecog[1] = Operations.sqroot.calculate(txtrecog[1])
        else:
            print('ERROR 1')
