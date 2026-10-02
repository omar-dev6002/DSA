#include <iostream>
#include <vector>
#include <string>

using namespace std;


class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> record;

        for (string op : operations){
            if (op == "C"){
                record.pop_back();
            }

            else if (op == "D"){
                int last = record.back();
                record.push_back(last * 2);
            }

            else if (op == "+"){
                int n = record.size();
                int sum = record[n-1] + record[n-2];
                record.push_back(sum);
            }

            else{
                int num = stoi(op);
                record.push_back(num);
            }
        }
      
        int total = 0;
        for (int score : record){
            total += score;
        }

        return total;
    }


};

// Time complexity: O(N)
// Space complexity: O(N)
// BYE, see you soon 🤗
