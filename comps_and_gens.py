
# 27
# Use comprehension instead of map and filter
# Because comprehension are clearer because they don't use lambdas

ints = range(1, 10)
square_ints = map(lambda i: i ** 2, ints)
even_square_ints = filter(lambda i: i % 2 == 0, square_ints)

# vs

esi = [
    i ** 2
    for i in range(1, 10)
    if i % 2 == 0
]


# 30
# Return generators over lists
# Generators use yield and bound the memory

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

# vs

def index_words_gene(text):
    # essentially stateful
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


# 32
# Consider generator expressions over lists

esi_generator = (
    i ** 2
    for i in range(1, 10)
    if i % 2 == 0
)


# 33
# Compose generators with yield from
# The result of the two animates are the same, but yield from reduces noise
# and runs significantly faster

def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def render(delta):
    print(f'Delta: {delta:.1f}')

def run(func):
    for delta in func():
        render(delta)

# run(animate)

def amimate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(4, 5.0)

# run(animate_composed)


# 36
# Use itertools
