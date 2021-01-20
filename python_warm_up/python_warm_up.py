def is_multiple_of_9(n):
    """Return True if n is a multiple of 9; False otherwise."""
    if (n%9==0):
        return True
    else: return False


def next_prime(m):
    """Return the first prime number p that is greater than m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    # define a helper function to identify prime numbers
    def is_prime(n):
        # the smallest 2 prime numbers
        if (n <= 1):
            return False
        if (n <= 3):
            return True

        # the most obvious non-prime numbers
        if (n%2==0 or n%3==0):
            return False

        # because numbers that are multiple of 2 or 3 have been considered
        for i in range(5,n,2):
            if (n%i==0): return False
        return True
    # increase by 1 to search for the next prime number
    while not is_prime(m+1):
        m+=1
    return m+1



def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    # calculate the delta to consider different situations of the roots
    import math
    delta=b**2-4*a*c
    if delta<0: return "complex"
    elif delta==0: return (-b-math.sqrt(delta))*0.5
    else: return (float((-b-math.sqrt(delta))*0.5),float((-b+math.sqrt(delta))*0.5))




def perfect_shuffle(even_list):
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    For example, [0, 1, 2, 3, 4, 5, 6, 7] => [0, 4, 1, 5, 2, 6, 3, 7]"""
    n=len(even_list)
    ll=[]
    # slice the list to two parts
    for i in range(int(n/2)):
        # append the former part
        ll.append(even_list[i])
        # append the latter part
        ll.append(even_list[int(n/2)+i])
    return ll



def triples_list(input_list):
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 3."""
    # using list comprehension
    return [i*3 for i in input_list]



def double_consonants(text):
    """Return a new version of text, with all the consonants doubled.
    For example:  "The *BIG BAD* wolf!" => "TThhe *BBIGG BBADD* wwollff!"
    For this exercise assume the consonants are all letters OTHER
    THAN A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""
    # add a backspace to the skipwords list
    skip=['A','E','I','O','U','a','e','i','o','u',' ']
    output=""
    # import string library to exclude punctuations
    import string
    for i in text:
        if i in skip: output+=str(i)
        elif i in string.punctuation:output+=str(i)
        else: output+=str(i*2)
    return output




def count_words(text):
    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', '*', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ]  ).
    Convert all the letters to lower-case before the counting."""
    text = text.lower()
    stopsigns = [' ', '\n', '.', ',', ';', '!', '?', '&', '(', ')',
                 '[', ']', '\\', '_', '=',':','`','|','"','>','<','^',
                 '{','}','~','$']
    out_dict = {}
    j = 0
    def check_word(i, j):
        if text[j:i] in out_dict:
            out_dict[text[j:i]] += 1
        else:
            out_dict[text[j:i]] = 1

    for i in range(len(text)):
        if text[i] in stopsigns:
            if text[j:i] != "":
                check_word(i, j)
            j = i + 1
    if text[j:i+1] != "":
        check_word(i + 1, j)
    return out_dict



def make_cubic_evaluator(a, b, c, d):
    """When called with 4 numbers, returns a function of one variable (x)
    that evaluates the cubic polynomial
    a x^3 + b x^2 + c x + d.
    For this exercise Your function definition for make_cubic_evaluator
    should contain a lambda expression."""
    return lambda x: a*x**3+b*x**2+c*x+d



class Polygon:
    """Polygon class."""
    def __init__(self,n_sides,lengths=None, angles=None):
        self.n_sides=n_sides
        self.lengths=lengths
        self.angles=angles

    def is_rectangle(self):
        """ returns True if the polygon is a rectangle,
        False if it is definitely not a rectangle, and None
        if the angle list is unknown (None)."""
        if self.n_sides!=4: return False
        elif self.angles!=None and self.angles!=[90, 90, 90, 90]: return False
        elif self.angles==[90, 90, 90, 90]: return True
        else: return None

        pass

    def is_rhombus(self):
        if self.n_sides != 4:
            return False
        else:
            if self.lengths == None:
                return None
            else:
                if len(set(self.lengths)) != 1:
                    return False
                else:
                    return True
        pass

    def is_square(self):
        if self.n_sides == 4 and \
                self.lengths != None and len(set(self.lengths)) == 1 and \
                self.angles != None and self.angles == [90, 90, 90, 90]: return True
        if self.n_sides != 4: return False
        if self.n_sides == 4:
            if self.lengths == None:
                if self.angles != None and self.angles != [90, 90, 90, 90]:
                    return False
                else:
                    return None
            elif len(set(self.lengths)) == 1:
                if self.angles == None:
                    return None
                elif self.angles != [90, 90, 90, 90]:
                    return False
                else:
                    return True
            else:
                return False
        # if Polygon.is_rectangle(self) == True:
        #     if Polygon.is_rhombus(self) == True: return True
        #     if self.lengths == None: return None
        # else:
        #     return Polygon.is_rectangle(self)
        # pass
        pass

    def is_regular_hexagon(self):
        if self.n_sides == 6 and \
                self.lengths != None and len(set(self.lengths)) == 1 and \
                self.angles != None and self.angles == [120] * 6: return True
        if self.n_sides != 6: return False
        if self.n_sides == 6:
            if self.lengths == None:
                if self.angles != None and self.angles != [120] * 6:
                    return False
                else:
                    return None
            elif len(set(self.lengths)) == 1:
                if self.angles == None:
                    return None
                elif self.angles != [120] * 6:
                    return False
                else:
                    return True
            else:
                return False
        pass

    def is_isosceles_triangle(self):
        if self.n_sides != 3: return False
        else:
            if self.lengths == None:
                if self.angles == None: return None
                elif len(set(self.angles)) <= 2: return True
                else: return False
            elif len(set(self.lengths)) > 2: return False
            else:
                if self.angles != None and len(set(self.angles)) > 2: return False
                else: return True
        pass

    def is_equilateral_triangle(self):
        if Polygon.is_isosceles_triangle(self) == True:
            if self.lengths != None:
                if len(set(self.lengths)) == 1:
                    return True
                else:
                    return False
            elif self.angles != None:
                if self.angles != [60] * 3:
                    return False
                else:
                    return True
        else:
            return Polygon.is_isosceles_triangle(self)
        pass

    def is_scalene_triangle(self):
        if Polygon.is_isosceles_triangle(self) == False:
            if self.n_sides == 3:
                return True
            else:
                return False
        elif Polygon.is_isosceles_triangle(self) == True:
            return False
        else:
            return None
        pass