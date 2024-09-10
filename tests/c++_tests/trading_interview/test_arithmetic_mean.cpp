#include <iostream>
#include <vector>
#include "arithmetic_mean.h"
using namespace std;

void testGetArithmeticMeanContiguousFragmentsCount(const vector<int>& arr, int target, int expected) {
    int result = getArithmeticMeanContiguousFragmentsCount(arr, target);
    if (result == expected) {
        cout << "Test passed!" << endl;
    } else {
        cout << "Test failed! Expected " << expected << " but got " << result << endl;
    }
}

int main() {
    // Test case 1
    vector<int> arr1 = {3, 2, 4};
    int target1 = 3;
    int expected1 = 3;
    testGetArithmeticMeanContiguousFragmentsCount(arr1, target1, expected1);

    // Test case 2
    vector<int> arr2 = {-1, 3, 2, -2};
    int target2 = 1;
    int expected2 = 2;
    testGetArithmeticMeanContiguousFragmentsCount(arr2, target2, expected2);

    // Test case 3
    vector<int> arr3 = {2, 3, 6};
    int target3 = 5;
    int expected3 = 0;
    testGetArithmeticMeanContiguousFragmentsCount(arr3, target3, expected3);

    // Test case 4: Single element array
    vector<int> arr4 = {5};
    int target4 = 5;
    int expected4 = 1;
    testGetArithmeticMeanContiguousFragmentsCount(arr4, target4, expected4);

    // Test case 5: All elements are the same
    vector<int> arr5 = {2, 2, 2, 2};
    int target5 = 2;
    int expected5 = 10; // All possible subarrays have mean 2
    testGetArithmeticMeanContiguousFragmentsCount(arr5, target5, expected5);

    // Test case 6: No subarray with the target mean
    vector<int> arr6 = {1, 2, 3, 4, 5};
    int target6 = 10;
    int expected6 = 0;
    testGetArithmeticMeanContiguousFragmentsCount(arr6, target6, expected6);

    // Test case 7: Negative numbers
    vector<int> arr7 = {-3, -2, -1, 0, 1, 2, 3};
    int target7 = 0;
    int expected7 = 3; // Subarrays: [-3, -2, -1, 0, 1, 2, 3], [-2, -1, 0, 1, 2], [-1, 0, 1]
    testGetArithmeticMeanContiguousFragmentsCount(arr7, target7, expected7);
}