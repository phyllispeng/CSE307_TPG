import sys
import tpg

class SemanticError(Exception):

    """
    This is the class of the exception that is raised when a semantic error
    occurs.
    """

# These are the nodes of our abstract syntax tree.
class Node(object):
    """
    A base class for nodes. Might come in handy in the future.
    """

    def evaluate(self):
        """
        Called on children of Node to evaluate that child.
        """
        raise Exception("Not implemented.")

class Value(Node):
     """
     A node representing integer literals.
     """

     def __init__(self, value):
         value_type = type(value)
         print(value_type)
         self.value = int(value)


     def evaluate(self):
         return self.value

class Add(Node):
    """
    A node representing addition
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right
    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return left + right

class Minus(Node):
    """
    A node representing minus
    """
    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right
    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return left - right

class Multiply(Node):
    """
    A node representing multiplication.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return left * right

class Divide(Node):
    """
    A node representing division.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        if right == 0:
            raise SemanticError()
        return left / right

class Smaller(Node):
    """
    A node representing Smaller.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        if left < right:
            return 1
        else:
            return 0


class Equals(Node):
    """
    A node representing Equals.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        if left == right:
            return 1
        else:
            return 0

class Greater(Node):

    """
    A node representing Larger.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        if left > right:
            return 1
        else:
            return 0



class bool_AND(Node):
    """
    A node representing Larger.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right


    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if  left !=0:
            left = True
        else:
            left = False
        if  right != 0:
            right = True
        else:
            right = False

        if left and right:
            return 1
        else:
            return 0

class bool_NOT(Node):
    """
    A node representing Larger.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        #self.left = left
        self.right = right


    def evaluate(self):
        #left = self.left.evaluate()
        right = self.right.evaluate()

        if  right != 0:
            right = True
        else:
            right = False

        if  right:
            return 0
        else:
            return 1

class bool_OR(Node):
    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right


    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if  left !=0:
            left = True
        else:
            left = False
        if  right != 0:
            right = True
        else:
            right = False

        if left or right:
            return 1
        else:
            return 0
# This is the TPG Parser that is responsible for turning our language into
# an abstract syntax tree.
class Parser(tpg.Parser):
    """
    token value "(\d+)|(\d+\.\d*|\d*\.\d+)|(\\"([^\\"])*\\")" Value
    separator space "\s+";

    START/a -> expression/a
    ;

    expression/a -> boolOR/a;
    boolOR/a -> boolNOT/a ("or" boolNOT/b $ a = bool_OR(a,b) $)*;
    boolNOT/a -> boolAND/a ("not" boolAND/b $ a = bool_NOT(b,b) $)*;
    boolAND/a -> comparision/a ("and" comparision/b $ a = bool_AND(a,b) $)*;
    comparision/a -> addsub/a ("<" addsub/b $ a = Smaller(a,b) $
     | "==" addsub/b $ a = Equals(a,b) $
     | ">" addsub/b $ a = Greater(a,b) $)* ;

    addsub/a -> muldiv/a ("\+" muldiv/b $ a = Add(a, b) $
    | "\-" muldiv/b $ a = Minus(a, b) $)* ;

    muldiv/a -> parens/a
    ( "\*" parens/b $ a = Multiply(a, b) $
    | "/"  parens/b $ a = Divide(a, b) $
    )* ;

    parens/a -> "\(" expression/a "\)" | literal/a
    ;

    literal/a -> value/a;
    """

# Make an instance of the parser. This acts like a function.
parse = Parser()

# This is the driver code, that reads in lines, deals with errors, and
# prints the output if no error occurs.

# Open the file containing the input.
try:
    f = open(sys.argv[1], "r")
except(IndexError, IOError):
    f = open("input1.txt", "r")

# For each line in f
for l in f:
    try:
        # Try to parse the expression.
        node = parse(l)

        # Try to get a result.
        result = node.evaluate()

        # Print the representation of the result.
        print(repr(result))

    # If an exception is thrown, print the appropriate error.
    except tpg.Error:
        print("SYNTAX ERROR")
        # Uncomment the next line to re-raise the syntax error,
        # displaying where it occurs. Comment it for submission.
        # raise

    except SemanticError:
        print("SEMANTIC ERROR")
        # Uncomment the next line to re-raise the semantic error,
        # displaying where it occurs. Comment it for submission.
        #raise

f.close()
