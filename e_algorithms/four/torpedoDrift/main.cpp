//
// Created by Alec Mirambeau on 3/12/24.
//
#include <iostream>
#include <cstring>

//
int torpedoDrift(std::vector<int> nums, int target){
    std::vector<int> cache(target + 1, 0);
    cache[0] = 1;
    for( size_t i = 1; i <= target; ++i){
        for (size_t j = 0; j < nums.size(); ++j){
            int sub = i - nums[j];
            if (sub >= 0){
                cache[i] += cache[sub];
            }
        }
    }
    return cache[target];
}

int main(int argc, char** argv){
    int numTestCases;
//    std::string firstrowdata;
//    std::string secondRowData;
    int numBrickTypes;
    int targetLength;
    std::cin >> numTestCases;
    for(size_t i = 0; i < numTestCases; ++i){
        //getLine should get the entire line entered by user
//        std::getline(std::cin, firstrowdata);
//        std::getline(std::cin, secondRowData);

        // We want to turn the input into tokens
//        char* token = std::strtok(firstrowdata, " ");

    }




}

