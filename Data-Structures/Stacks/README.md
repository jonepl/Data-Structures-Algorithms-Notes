# Stacks

A stack is a linear list in which insertions (also called additions and pushes) and removals (also called deletions and pops) take place at the same end. This end is called the top; the other end of the list is called the bottom. As a result, a stack is a *last-in-first-out* data structure.


    AbstractDataType stack
    {
        instances
            linear list of elements; one end is called the bottom; the other is called the top

        operations
            empty() : Return true if the stack is empty, return false otherwise
            size() : Return the number of elements in the stack
            top() : Return the top element of the stack
            pop() : Remove the top element from the stack
            push() : Add element x at the top of the stack
    }

## Pros and Cons

PROS

* Good with *insertion* | Upperbound O(1)   | prepends elements to list
* Good with *deletions*  | Upperbound O(1)

CONS

* Bad with *accessings* | Upperbound O(n)
* Bad with *searching*  | Upperbound O(n).


<sup>1</sup> Abstract Data Type -  is an abstraction of a data structure which provides only the interface to which a data structure must adhere to.