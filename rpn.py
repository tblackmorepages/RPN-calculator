import re
from word2number import w2n


class Calculator:
    """
    This is a stack-based RPN calculator
    It uses Reverse Polish Notation to determine the order of operation
    Supports addition, subtraction, multiplication, integer division, and remainder or modulo
    Input expression must contain only whole numbers.
    """

    def evaluate(self, string):
        """
        Evaluates input expression and returns whole number.
        """
        current = -1
        stack = []
        for sub_str in string:
            # Store number in current variable
            if sub_str.isdigit():
                if current > 0:
                    current = int(sub_str) + current*10
                else:
                    current = int(sub_str)
            # If next character is a space and a number is stored in current add number to the stack
            elif sub_str == " ":
                if current >= 0:
                    stack.append(current)
                    current = -1
            # Apply operator to last two numbers in the stack
            elif sub_str in ["+", "-", "*", "/", "%"]:
                if len(stack) < 2:
                    return "Error: Expression invalid"
                b = stack.pop()
                a = stack.pop()
                if sub_str == "+":
                    stack.append(a + b)
                elif sub_str == "-":
                    stack.append(a - b)
                elif sub_str == "*":
                    stack.append(a * b)
                elif sub_str == "/":
                    stack.append(a // b)
                else:
                    stack.append(a % b)
            else:
                return "Exiting RPN Calculator..."
        # Check that correct number of operators has been given
        if len(stack) > 1:
            return "Error: Expression invalid"
        result = stack.pop()
        return result

    def text_to_numbers(self, string):
        """
        Converts input text into numbers.
        """
        result = []
        # Split string at each text number
        str_split = string.split('  ')
        # If no text numbers return original string
        if len(str_split) == 1:
            return string
        # Replace text numbers with digits
        else:
            for sub_str in str_split:
                word_char_search = re.search('[^a-zA-Z ]', sub_str)
                if word_char_search == None:
                    try:
                        w2n.word_to_num(sub_str)
                    except:
                        return "Please enter a valid expression:"
                    else:
                        number = str(w2n.word_to_num(sub_str))
                        result.append(number)
                else:
                    result.append(sub_str)
        return ' '.join(result)


print("Launching RPN calculator...")
rpn_calc = Calculator()
user_input = ""
# To exit calculator use following expressions:
while user_input not in ["exit", "quit", "q", "close"]:
    # Get user input
    # regex = re.search('[a-zA-Z]', user_input)
    # if regex != None:
    #     print("Please enter a valid expression:")
    user_input = input("> ")
    number_input = rpn_calc.text_to_numbers(user_input)
    output = rpn_calc.evaluate(number_input)
    print(output)