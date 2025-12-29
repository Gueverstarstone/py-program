try:
    raise MemoryError('memory error')
except MemoryError as e:
    print(e)