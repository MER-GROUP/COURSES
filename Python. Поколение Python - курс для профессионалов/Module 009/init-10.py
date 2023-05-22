print('------------------')

def greet(name):
    return f'Hello {name}!'

print('------------------')

def greet(name: str) -> str:
    return f'Hello {name}!'

print('------------------')

def greet(name: str = 'world') -> str:
    return f'Hello, {name}!'

print('------------------')

def print_hello(name: str, upper: bool = False) -> None:
    if upper:
        name = name.upper()
    print(f'Hello, {name}')

print('------------------')

def avg(num1: int, num2: int, num3: int) -> float:
    return (num1 + num2 + num3) / 3

print('------------------')

name: str = 'Timur'
age: int = 29
height: float = 171.5
is_married: bool = False

print('------------------')

def sum_square(nums: list) -> float:
    total = 0
    for i in nums:
        total += i ** 2
    return total

print('------------------')

numbers: list
person: tuple
prices: dict
answers: set

print('------------------')

from typing import List

def sum_square(nums: List[int]) -> float:
    total = 0
    for i in nums:
        total += i ** 2
    return total

print('------------------')

from typing import List, Tuple, Dict, Set

# тип всех элементов списка
numbers: List[int]      
# тип каждого элемента кортежа     
person: Tuple[str, int, bool]
# тип ключей, тип значений                     
prices: Dict[str, int] 
# тип всех элементов множества                           
answers: Set[float]                               

print('------------------')

# тип всех элементов списка
numbers: list[int]       
# тип каждого элемента кортежа                         
person: tuple[str, int, bool]  
# тип ключей, тип значений                   
prices: dict[str, int]   
# тип всех элементов множества                         
answers: set[float]                               

print('------------------')

def print_hello(num1: int, num2: int, num3: int) -> float:
    return (num1 + num2 + num3) / 3

print(print_hello.__annotations__)

print('------------------')

from typing import Union

def add_or_concatenate(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str]:
    return a + b

print('------------------')

from typing import Union

NumberOrStr = Union[int, float, str]

def add_or_concatenate(a: NumberOrStr, b: NumberOrStr) -> NumberOrStr:
    return a + b

print('------------------')

from typing import Union

name: Union[str, None]

print('------------------')

from typing import Optional

name: Optional[str]

print('------------------')

from typing import Any

def func(arg: Any) -> Any:
    return arg

print('------------------')

from typing import NoReturn

def stop() -> NoReturn:
    raise RuntimeError('no way')

print('------------------')