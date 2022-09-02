# Hashtable Left Join

## Collaborators: Jae and Brian
### Hashtable Left Join
- Write a function that LEFT JOINs two hashmaps into a single data structure.

- Write a function called left join
  - Arguments: two hash maps
  - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
  - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
  - Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
## Whiteboard Process
![left_join](whiteboard-hashtable-left-join.png)

## Approach & Efficiency
Time: O(n)
Space: O(n + m)
The first hashtable is iterated through. Each item is checked against the other hashtable for a match. If there is a match, that data is taken as well. The data is then formatted together and pushed into a matrix to be returned to the user.

## Link to Code:
[Code](hashtable_left_join.py)
## Link to tests:
[Tests](/tests/code_challenges/test_hashtable_left_join.py)
