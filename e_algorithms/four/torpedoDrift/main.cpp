//
// Created by Alec Mirambeau on 3/12/24.
//
#include <iostream>
#include <cstring>
#include <unordered_map>
#include <vector>

//
int torpedoDrift(std::vector<int> nums, int target){
    std::unordered_map<int, int> cache;
    cache[0] = 1;
    for( size_t i = 1; i <= target; ++i){
        cache[i] = 0;
        for (size_t j = 0; j < nums.size(); ++j){
            // have to debug this line below
            int sub = i - nums[j];
            if (sub >= 0){
                cache[i] += cache[sub];
            }
        }
    }
    return cache[target] % 1000000009;
}

int main(int argc, char** argv){
    int numTestCases;
//    std::string firstrowdata;
//    std::string secondRowData;
    int numBrickTypes;
    int targetLength;
    int temp;
    std::vector<int> bricks(0);
    std::cin >> numTestCases;
    std::vector<int> output(0);
    for(size_t i = 0; i < numTestCases; ++i){
        //getLine should get the entire line entered by user
//        std::getline(std::cin, firstrowdata);
//        std::getline(std::cin, secondRowData);
        std::cin >> numBrickTypes >> targetLength;
        for (size_t j = 0; j < numBrickTypes; ++j){
            std::cin >> temp;
            bricks.push_back(temp);
        }

        output.push_back(torpedoDrift(bricks, targetLength));
        bricks.clear();
        // We want to turn the input into tokens
//        char* token = std::strtok(firstrowdata, " ");
    }

    for (size_t i = 0; i < output.size(); ++i)
        std::cout << output[i] << "\n";






}

