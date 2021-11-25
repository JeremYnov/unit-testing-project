

### Rappel : Qu'est-ce une docstring et quelles sont ses avantages ? 
## La docstring est un mécanisme de documentation du code (placée juste en dessous de la signature de la fonction, d'une class, au début du module). 
## Dans un shell Python/IPython, la documentation est accessible avec la commande help() ou encore __doc__
# from docstringtest import factorial
# help(factorial)
# print(factorial.__doc__)
# factorial(-1)
# factorial(30.1)
# factorial(1e100)

## Dans un IDE, la documentation est accessible en plaçant le curseur de la souris au dessus de la fonction/class (au début du module). 

## 2è focntionnalité : réaliser des tests unitaires (écrit dans un langage shell Python) => `doctest`
# On peut mettre des tests dans les docstrings, qui servent alors d’exemples d’utilisation


# Let's have `add` function to test with int, string and float values ? 
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """
    Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000

    n must be >= 0
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() not defined for negative values

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() only accepts integral values
    
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: factorial() argument should not exceed 2147483647
    """
    import math
    if not n >= 0:
        raise ValueError("factorial() not defined for negative values")
    if math.floor(n) != n:
        raise ValueError("factorial() only accepts integral values")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("factorial() argument should not exceed 2147483647")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

### Cmnt tester le doctest (plusieurs façons ...) ? 
## Rq importante : pas besoin d'importer pytest (lors d'un test sur docstring) !  

## 1è façon (manuelle), taper ds un shell Python : 
# >>> import doctest
# >>> doctest.testmod()

## 2è façon (automatique) : 
# Il est très facile de rendre automatique les tests et ainsi de ne plus avoir à faire appel explicitement (et manuellement) à la fonction testmod
# Ajouter à la fin du script : 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
# Lancer ds un CMD : python docstringtest.py -v

## 3è façon (tjrs automatique) et plus simple (sans écrire à la fin du module `if __name__ == ...`), taper ds un CMD : 
# python -m doctest -v docstringtest.py

## Ce qui peut être fait à l'aide de l'extension `pydoctestbtn`
# https://marketplace.visualstudio.com/items?itemName=NoahSyn10.pydoctestbtn

# Inconvénient des méthodes 2 et 3 : on teste tt le module (ttes les doctests qui y sont présentes) => test en lot (en batch)
# En d'autres termes, on ne peux pas réaliser un doctest d'une fonction/classe particulière (isolée)  

## 4è façon (en passant par pytest en CLI où à l'aide de l'extension Test Explorer UI) : 
# pytest --doctest-modules  -v ./docstringtest.py
# L'extension Test Explorer UI offre la possibilité de réaliser des doctests une par une, Super ! 

### La doctest n'est pas un outil `parfait` ! Ns devons faire par exemple au espace et ajouter souvent  des options (liste non exhaustive) : 

## 1) Les espaces sont significatifs dans la docstring

def whitespace_is_important_fail(n):
    """
    Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1,1,2,6,24,120]
    """
# En procédant au test, nous constatons un échec ! Le problème : ce sont les espaces que l’interpréteur place après chaque virgule dans l’énumération des éléments de la liste. Dans la docstring, ils n’y sont pas.   
# Cela vient du fait que la fonction testmod effectue une comparaison litérale entre la réponse fournie par la documentation (Expected) et celle fournie par l’interpréteur (Got).
# Comment corriger ce point ? C’est simple, il faut mettre des espaces entre les éléments d’une liste.

def whitespace_is_important_success(n):
    """
    Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    """


## 2) Normaliser les espaces (# doctest: +NORMALIZE_WHITESPACE)
# Mais ce n’est pas si simple. On peut facilement mettre plusieurs espaces, comme ci-dessous (et le test échoue) :
# https://stackoverflow.com/questions/17640416/doctest-normalize-whitespace-does-not-work
def normalize_whitespace_fail(n):
    """
    J'ai mis trop d'espaces et je réalise le test !
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2,     6, 24, 120]
    """

def normalize_whitespace_success(n):
    """
    J'ai mis par erreur trop d'espace ! J'indique alors la directive appropriée !
    
    >>> [factorial(n) for n in range(6)] # doctest: +NORMALIZE_WHITESPACE
    [1, 1, 2,     6, 24, 120]
    """


## 3) Raccourcir le return de la fonction ds le doctest (# +ELLIPSIS) ? 
# Le return de la fonction est trop long, on ne peux pas s'amuser à écrire des centaines de lignes dans la docstring ! 
# L'idée est de tronquer le return => Il faut accompagner la docstring d'un magic comment `# +ELLIPSIS` ? 
# https://stackoverflow.com/questions/17092215/how-enable-ellipsis-when-calling-python-doctest

def ellipsis_success(n):
    """
    Je tronque le résultat : au lieu de saisir [1, 1, 2, 6, 24, 120]
    j'ai raccourci en [1, ..., 24, 120] 

    >>> [factorial(n) for n in range(6)] # doctest: +ELLIPSIS
    [1, ..., 24, 120]
    """

def ellipsis_fail(n):
    """
    Au lieu de saisir 

    >>> [factorial(n) for n in range(6)] # doctest: +ELLIPSIS
    [1, 1, ..., 24, 12]
    """    

def ellipsis_too_long_list_success():
    """
    On souhaite se dispenser d’énumérer explicitement tous les éléments de la liste [0, ..., 999] ?
    En d'autres termes, cmnt préciser qu’on veut tester une sortie tronquée ?
    => La directive `# +ELLIPSIS` est idéale pour les longs textes.
    >>> list(range(1000)) # doctest: +ELLIPSIS 
    [0, ..., 999]
    """
    return list(range(1000))

def ellipsis_too_long_text_success():
    '''
    >>> 'foobarbaz' # doctest: +ELLIPSIS
    'foo...baz'
    '''
    # return 'foobarbaz'

## 4) Combiner plusieurs directives :     
def combine_many_options_success(n):
    """
    Je peux indiquer plusieurs flag ! La bonne pratique ess de retourner à la ligne et de les indiquer (les ... sont important : shell Python) !
    
    >>> [factorial(n) for n in range(6)] 
    ... # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [1, ..., 24,     120]
    """

## 5) Cmnt gérer les exceptions (ds le doctest) ?
# Vous le savez, le déclenchement d’une exception produit un message plus ou moins long affiché sur plusieurs lignes.     
# Si on veut les inclure ds un doctest, est-on obligé de reproduire intégralement de tels messages qui peuvent être excessivement longs ?!
# Heureusement non. Il suffit de se limiter à : 

# `Traceback (most recent call last):
#         ...
# ValueError: factorial() not defined for negative values`


# Exécuter le code suivant dans un shell IPython pour examiner les exceptions soulevées par notre fonction factorial()
# from docstringtest import factorial
# factorial(-1)
# factorial(30.1)
# factorial(1e100)


# In [2]: factorial(-1)
#    ...: 
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-2-5aae425d6a8b> in <module>()
# ----> 1 factorial(-1)

# C:\Users\bejao\OneDrive\TipsPyR\TipsPy\Flask\1-HelloWorldColor\tests\tests_unit\docstringtest.py in factorial(n)
#      59     import math
#      60     if not n >= 0:
# ---> 61         raise ValueError("factorial() not defined for negative values")
#      62     if math.floor(n) != n:
#      63         raise ValueError("factorial() only accepts integral values")

# ValueError: factorial() not defined for negative values


def exception_success(n):
    """
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() not defined for negative values

    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() only accepts integral values

    # >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    factorial() argument should not exceed 2147483647
    """

# Le test suivant échouera parce que sur l'exception soulevée par factorial(30.1) n'est pas conforme à la docstring.
# Il manque Traceback (most recent call last): et les ... 
def exception_fail(n):
    """
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() not defined for negative values

    >>> factorial(30.1)
    ValueError: factorial() only accepts integral values
    """    