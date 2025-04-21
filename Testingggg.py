Here is a C++ code that finds the least occurring character from a string:

```cpp
#include <iostream>
#include <string>
#include <map>

char findLeastOccurringChar(const std::string& str) {
    std::map<char, int> charCount;
    for (char c : str) {
        if (charCount.find(c) != charCount.end()) {
            charCount[c]++;
        } else {
            charCount[c] = 1;
        }
    }

    char leastOccurringChar = str[0];
    int minCount = charCount[str[0]];
    for (const auto& pair : charCount) {
        if (pair.second < minCount) {
            minCount = pair.second;
            leastOccurringChar = pair.first;
        }
    }

    return leastOccurringChar;
}

int main() {
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;

    char leastOccurringChar = findLeastOccurringChar(str);
    std::cout << "Least occurring character: " << leastOccurringChar << std::endl;

    return 0;
}
```

This code uses a `std::map` to count the occurrences of each character in the string. It then iterates over the map to find the character with the minimum count.