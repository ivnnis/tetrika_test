def find_first_zero(numbers: str) -> int:
    return numbers.find('0')



tests = [
    {'data': '111111111110000000000000000', 'answer': 11},
    {'data': '111100000000', 'answer': 5}
]
if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = find_first_zero(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'