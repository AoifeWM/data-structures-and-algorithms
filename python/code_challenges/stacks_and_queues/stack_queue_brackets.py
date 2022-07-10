from queue import Queue
from stack import Stack

# def multi_bracket_validation(string):
#     # Stack to make sure brackets line up properly
#     st = Stack()
#     # Dictionary so we can reference which characters are supposed to match up for valid brackets.
#     type = {"(": ")", "{": "}", "[": "]"}
#     # Iterate through the string character by character
#     for char in string:
#         # If the character is a key, it means it's an open bracket, and we want to keep it in the stack, so that we
#         # can see what bracket sets still need to be fulfilled.
#         if char in type.keys():
#             st.push(char)
#         # If the character is a value that means it's a closing bracket and there's a few behaviors we will implement
#         # below.
#         elif char in type.values():
#             # If the stack is empty, it means there's no possible corresponding open bracket, and so it's invalid.
#             if not st.top:
#                 return False
#             # If we hit a close bracket, and it's not closing the most recent open bracket, then it's invalid. (ie,
#             # we don't want "[ { ] }" to return valid. If the code encounters "]" but the most recent unclosed open
#             # bracket is "{", then it's not valid. By popping (instead of peeking, for instance) we also
#             # automatically remove from the stack open brackets which have been properly closed, without having to
#             # add any extra statements to do so.
#             elif type[st.pop()] != char:
#                 return False
#     # If any dangling open bracket is left over, the string is invalid.
#     if st.top:
#         return False
#     # Our failure conditions are exhaustive, so if we are able to iterate through the entire string without
#     # triggering one of them, then the string must be valid, and we can return True.
#     return True


# This is the optimized version, which is less readable but takes fewer lines and has functionally the exact same code.
def multi_bracket_validation(string):
    st, type = Stack(), {"(": ")", "{": "}", "[": "]"}
    for char in string:
        if char in type.keys():
            st.push(char)
        elif char in type.values() and (not st.top or type[st.pop()] != char):
            return False
    if st.top:
        return False
    return True
