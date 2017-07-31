"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""

# =================== stack ================
# Time: init - O(n), next - O(1), hasNext - O(n)
# Sapce: O(n)
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {

    private Stack<NestedInteger> s;
    
    public NestedIterator(List<NestedInteger> nestedList) {
        s = new Stack<>();
        for ( int i = nestedList.size() - 1; i >= 0; i-- ) {
            s.push(nestedList.get(i));
        }
    }

    @Override
    public Integer next() {
        if ( s.empty() ) {
            return null;
        }
        
        return s.pop().getInteger();
    }

    @Override
    public boolean hasNext() {
        while ( !s.empty() && !s.peek().isInteger() ) {
            NestedInteger cur = s.pop();
            List<NestedInteger> curList = cur.getList();
            for ( int i = curList.size() - 1; i >= 0; i-- ) {
                s.push(curList.get(i));
            }
        }
        
        return !s.empty();
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
