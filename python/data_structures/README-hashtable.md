# Hashtables

A hashtable is a way of organizing large amounts of data so that it's efficient to access. It stores each key-value pair in a list of linkedlists. The index that it's stored at is deterministic and based on an arbitrary equation performed on the key. Therefore, when searching for a value of a given key, the index that it is stored at can be quickly accessed without the lengthy O(n) search that would be required in a regular list.

## Challenge
Write a working hashtable implementation.

## Approach
The hash is found by converting characters into their unicode values, then multiplying and adding them all together, then multiplying by a prime, then doing a modulus of the size of the hashtable to ensure the index is in range.

## Efficiency
* set
  * time: O(1)
    * Once the hashing calculation is finished, no time is spent on searching the list as the index is known. No time is spent on traversal either as the new key-value pair is inserted into the head of the linkedlist.
  * space: O(1):
    * no new data structures are being created. A single new node is being added to a linkedlist.
* get
  * time: O(1 + ?)
    * Once the hashing calculation is finished, no time is spent on searching the list as the index is known. However, depending on the size and fullness of the hashtable, some time may need to be spent traversing the linkedlist (i.e. 10,000 items in a hashtable with 1 bucket = 10,000 traversals). This may be O(h), but I'm not sure on the correct terminology for this efficiency.
  * space: O(1):
    * No new data is being created.
* contains
  * time: O(1 + ?)
    * see the explanation for get. The algorithm is exactly the same but a boolean is returned instead of a value.
  * space: O(1)
    * No new data is being created.
* keys:
  * time: O(n)
    * The entire hashtable must be traversed, so it expands linearly with the size of the hashtable.
  * space: O(n)
    * A list with the contents of the entire hashtable is created, so it expands linearly with the size of the hashtable.
* hash:
  * time: O(n)
    * N being the number of characters in the key, because math must be performed on each one.
  * space: O(1)
    * No new data structures are being created.




## API
* Hashtable()
  * Arguments: size, prime
    * size: number of buckets in the hashtable. Note: this is not the upper limit for the number of key-value pairs that can be stored in the table; each bucket has a linkedlist which can hold any number of items. Default: 64
    * prime: seed for the hashing algorithm. Should probably be a prime number, but doesn't have to be. Default: 811
* set()
  * Arguments: key, value
  * Returns: nothing
* Add a new key-value pair to the hashtable. If the key already exists in the table, its previous value will be replaced with the new value supplied in arguments.
* get()
  * Arguments: key
  * Returns: that key's corresponding value
* contains()
  * Arguments: key
  * Returns: True if the key exists in the table already, false if it does not.
* keys()
  * Arguments: none
  * Returns: list with all keys in the hashtable.
* hash ()
  * Arguments: key
  * Returns: the index that a key-value pair with the given key would be stored in if it were entered into the list.
