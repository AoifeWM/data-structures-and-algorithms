# Data Structures and Algorithms

## Language: `Python`

### Table of Contents

- [Challenge 01: Array Reverse](./code_challenges/array_reverse/README.md)
- [Challenge 02: Array insert shift](./code_challenges/array_insert_shift/README.md)
- [Challenge 03: Binary Search of Sorted Array](./code_challenges/array_binary_search/README.md)
- [Challenges 05 - 07: Linked Lists](./code_challenges/linked_list/README.md)
- [Challenge 08: linkedlist zip](./code_challenges/README-linked-list-zip.md)
- [Challenge 10: stacks and queues](./code_challenges/stacks_and_queues/README.md)
- [Challenge 11: Pseudoqueue](./code_challenges/stack_queue_pseudo/README.md)
- [Challenge 15: trees](./code_challenges/trees/README-trees.md)
- [Challenge 16: treesmax](./code_challenges/trees/README-treemax.md)
- [Challenge 18: fizz buzz tree](./code_challenges/trees/README-tree-fizz-buzz.md)
- [Challenge 26: insertion sort](./code_challenges/sorting/insertion/README.md)
- [Challenge 30: Hashtables](./data_structures/README-hashtable.md)
- [Challenge 31: First Repeated Word using hashtable](./code_challenges/README-hashtable-repeated-word.md)
- [Challenge 32: Tree intersection](./code_challenges/README-tree-intersection.md)
- [Challenge 33: Hashmap Left Join](./code_challenges/README-hashtable-left-join.md)

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`
