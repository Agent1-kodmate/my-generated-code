Here is a C++ code that finds the most occurring character from a string:

```cpp
#include <iostream>
#include <string>
#include <map>

char mostOccurringChar(const std::string& str) {
    std::map<char, int> charCount;
    for (char c : str) {
        if (charCount.find(c) != charCount.end()) {
            charCount[c]++;
        } else {
            charCount[c] = 1;
        }
    }

    char maxChar = ' ';
    int maxCount = 0;
    for (auto& pair : charCount) {
        if (pair.second > maxCount) {
            maxChar = pair.first;
            maxCount = pair.second;
        }
    }

    return maxChar;
}

int main() {
    std::string str;
    std::cout << "Enter a string: ";
    std::getline(std::cin, str);

    char mostOccurring = mostOccurringChar(str);
    std::cout << "Most occurring character: " << mostOccurring << std::endl;

    return 0;
}
```

This code uses a `std::map` to count the occurrences of each character in the string. It then iterates over the map to find the character with the maximum count.