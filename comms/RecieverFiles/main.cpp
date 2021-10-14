#include "nlohmann/json.hpp"
#include <string>
#include <vector>
using json = nlohmann::json;

struct Example {
    public:
        std::string s;
        int n;
        std::vector<int> ni;
        Example(std::string a, int b, std::vector<int> c) {
        s = a;
        n = b;
        ni = c;
    }
}

int main() {
    Example ex("re", 3, {3, 1, 4, 1, 5, 9, 2, 6});
    json j = ex;
    auto ex2 = j.get<Example>();
    return 0;
}