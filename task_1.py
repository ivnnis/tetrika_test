def task(numbers: str) -> int:
    return numbers.find('0')


print(task('111111111110000000000000000')) # 11
print(task('111100000000')) # 4
