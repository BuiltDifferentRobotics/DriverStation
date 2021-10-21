//#include "nlohmann/json.hpp"
#include <string>
#include <iostream>
//using json = nlohmann::json;

struct Example {
    public:
        int n;
        Example(int b) {
        n = b;
    }
};

int main() {
    Example ex(3);
    // json j;
    // j["s"] = ex.s;
    // j["n"] = ex.n;
    // //auto ex2 = j.get<Example>();
    std::cout << "ee\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" << std::endl;
    return 0;
}