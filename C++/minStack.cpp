#include<iostream>
#include<stack>
using namespace std;

class MinStack {

private:
    stack<int> mainStack;
    stack<int> minStack;

public:
    MinStack() {
        
    }
    
    void push(int value) {
        mainStack.push(value);
        if (minStack.empty() || value <= minStack.top()){
            minStack.push(value);
        }
    }
    
    void pop() {
        if(!mainStack.empty()){
            int topVal = mainStack.top();
            mainStack.pop();
            if (topVal == minStack.top()){
                minStack.pop();
            }
        }
    }
    
    int top() {
        return mainStack.top();
    }
    
    int getMin() {
        return minStack.top();      
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */


 /*
 Time: O(1) for all operations.
 Space: O(n) (two stacks, but still linear).
 Bye 😊
 */
