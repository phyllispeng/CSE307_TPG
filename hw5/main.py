# Name: Yuanyuan Peng
# ID: 108 734 720

import sys
import tpg

dict1 = {}


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


class Exe(Node):
    def __init__(self, stmt):
        self.stmt = stmt

    def execute(self):
        for statement in self.stmt:
            statement.execute()


class Value(Node):
    """
	A node representing integer literals.
	"""

    def __init__(self, value):

        if isinstance(value, list):
            self.value = list(value)
        elif value.isdigit():
            self.value = int(value)
        else:
            try:
                float(value)
                self.value = float(value)
            except ValueError:
                self.value = str(value)

    def evaluate(self):
        return self.value


class Variable(Node):
    """
	A node representing variables
	"""

    def __init__(self, variable):
        self.variable = str(variable)

    def evaluate(self):
        return self.variable


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
        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]
        if isinstance(left, str) and isinstance(right, str):
            left = left.replace('"', '')
            right = right.replace('"', '')

        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
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
        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]

        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
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

        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]

        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
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

        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]

        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
            raise SemanticError()
        if right == 0:
            raise SemanticError()
        return left / right


class Mod(Node):
    """
	A node representing Mod
	"""

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if left in dict1:
            left = dict1[left]
            
        if right in dict1:
            right = dict1[right]
            
        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
            raise SemanticError()
        if right == 0:
            raise SemanticError()
        return left % right


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

        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]

        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
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

        if left in dict1:
            left = dict1[left]
            
        if right in dict1:
            right = dict1[right]
           
        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
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

        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]

        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
            raise SemanticError()
        if left > right:
            return 1
        else:
            return 0


class LessEqual(Node):
    """
	A node representing LessEqual.
	"""

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate

        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]

        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
            raise SemanticError()
        if left <= right:
            return 1
        else:
            return 0


class NotEquals(Node):
    """
	A node representing NOTEquals.
	"""

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]
        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
            raise SemanticError()
        if left != right:
            return 1
        else:
            return 0


class GreatEqual(Node):
    """
	A node representing GreatEqual.
	"""

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]
        if (not isinstance(left, int)) and (not isinstance(left, float)):
            raise SemanticError()
        if (not isinstance(right, int)) and (not isinstance(right, float)):
            raise SemanticError()
        if left >= right:
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

        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]

        if left != 0:
            left = True
        else:
            left = False
        if right != 0:
            right = True
        else:
            right = False

        if left and right:
            return 1
        else:
            return 0


class bool_NOT(Node):
    """
	A node representing NOT.
	"""

    def __init__(self, node_b):
        self.node_b = node_b

    def evaluate(self):

        node_b = self.node_b.evaluate()
        if node_b in dict1:
            node_b = dict1[node_b]
        if node_b != 0:
            node_b = True
        else:
            node_b = False
        if node_b:
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
        if left in dict1:
            left = dict1[left]
        if right in dict1:
            right = dict1[right]
        if left != 0:
            left = True
        else:
            left = False
        if right != 0:
            right = True
        else:
            right = False

        if left or right:
            return 1
        else:
            return 0


class Index_Of(Node):
    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()

       
        if (isinstance(left ,list)):
        	if right in dict1:
        		right=dict1[right]
         
        	return left[right]
        else:
	        if left in dict1:
	        	left=dict1[left]
	        	
	        if right in dict1:
	        	right=dict1[right]
	        return left[right]


class saveVar(Node):
    def __init__(self, left, right):

        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()

    def execute(self):
       
        L = self.left.evaluate()
        R = self.right.evaluate()
        



        try:
         
            R = dict1[R]

            if (isinstance(L, int) or isinstance(L, float)):
            	for key in dict1:
            		key_value = dict1[key]
            		if (isinstance(key_value, list)):
            			i = 0
            			for ele in key_value:
            				if ele == L:
            					key_value[i]=R
            					break
            				else:
            					i=i+1
            else:
            	dict2 = {L: R}
            	dict1.update(dict2)
        except (KeyError, TypeError):
            dict2 = {L: R}
            dict1.update(dict2)


class ifStatement(Node):
    def __init__(self, expr, stmt):
        self.expr = expr
        self.stmt = stmt

    def execute(self):
        if (self.expr.evaluate()):
            self.stmt.execute()


class elseStatement(Node):
    def __init__(self, e, d, s):
        self.e = e
        self.d = d
        self.s = s

    def execute(self):
        statement_e = self.e.evaluate()
        if (statement_e == 1):
            self.d.execute()
        else:
            self.s.execute()


class whileLoop(Node):
    def __init__(self, expr, stmt):
        self.expr = expr
        self.stmt = stmt

    def execute(self):
        while (self.expr.evaluate()):
            self.stmt.execute()


class printStatement(Node):
    def __init__(self, stmt):
        self.stmt = stmt

    def execute(self):
        var = self.stmt.evaluate()
        if var in dict1:
            var = dict1[var]
        print(var)


# This is the TPG Parser that is responsible for turning our language into
# an abstract syntax tree.
class Parser(tpg.Parser):
    """
	token value "(\d+\.\d*|\d*\.\d+)|(\d+)|(\\"([^\\"])*\\")" Value
	token variable "([A-Za-z][A-Za-z0-9_]*)" Variable
	separator space "\s+";

	START/a -> statement/a;

	statement/a -> (
	"{" $ a = [] $
			(statement/b $ a.append(b) $)*
	"}" $ a = Exe(a) $
	| expression/b "=(?!=)" expression/c ";"  $ a = saveVar( b, c ) $
	| "print" "\(" expression/b "\)" ";" $ a = printStatement(b) $
	| "if" "\(" expression/e"\)" statement/d "else" statement/s $ a = elseStatement(e,d,s) $
	| "if" "\(" expression/b "\)" statement/a $ a = ifStatement(b,a)$
	| "while" "\(" expression/b "\)" statement/a $ a = whileLoop(b ,a) $
	);

	expression/a ->boolOR/a;
	boolOR/a -> boolAND/a ("or" boolAND/b $ a = bool_OR(a,b) $)*;
	boolAND/a -> boolNOT/a ("and" boolNOT/b $ a = bool_AND(a,b) $)*;
	boolNOT/a -> comparision/a |"not" expression/b $ a = bool_NOT(b) $;
	comparision/a -> addsub/a (
	"<>" addsub/b $ a = NotEquals(a,b) $
	|"==" addsub/b $ a = Equals(a,b) $
	|"<=" addsub/b $ a = LessEqual(a,b) $
	|"<" addsub/b $ a = Smaller(a,b) $
	|">=" addsub/b $ a = GreatEqual(a,b) $
	|">" addsub/b $ a = Greater(a,b) $)* ;

	addsub/a -> muldivmod/a ("\+" muldivmod/b $ a = Add(a, b) $
	| "\-" muldivmod/b $ a = Minus(a, b) $)* ;

	muldivmod/a -> index/a
	( "\*" index/b $ a = Multiply(a, b) $
	| "/"  index/b $ a = Divide(a, b) $
	| "\%" index/b  $ a = Mod(a,b) $
	)* ;

	index/a -> parens/a ("\[" expression/b "\]"  $ a = Index_Of(a,b) $ )*;
	parens/a -> "\(" expression/a "\)" | literal/a
	;

	literal/a -> value/a|array/a | variable/a;
	array/a -> "\[" $ a = Value([]) $
		expression/b $ a.value.append(b.evaluate()) $
	(","expression/b $ a.value.append(b.evaluate()) $ )*
	"\]"
	| "\[" "\]" $ a = Value([]) $;

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
inputfile = f.read()
try:
    # Try to parse the expression.
    node = parse(inputfile)
    # print(repr(node))
    # Try to get a result.
    node.execute()

# Print the representation of the result.
# print(repr(result))

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
# raise
 
f.close()
