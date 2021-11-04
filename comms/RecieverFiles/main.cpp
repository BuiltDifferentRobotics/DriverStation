#include "nlohmann/json.hpp"
#include <string>
#include <iostream>
#include <sstream>
using json = nlohmann::json;

struct Example {
    public:
        std::string l;
        int n;
        std::vector<int> v;
        Example() {}
        Example(std::string a, int b, std::vector<int> c) {
        n = b;
        l = a;
        v = c;
    }
};
void to_json(json& j, const Example& p) {
    j = json{{"l", p.l}, {"n", p.n}, {"v", p.v}};
}

void from_json(const json& j, Example& p) {
    j.at("l").get_to(p.l);
    j.at("n").get_to(p.n);
    j.at("v").get_to(p.v);
}
int main() {
    Example ex("hoHohoHo", 3, {2, 2, 3});
    json j;
    to_json(j, ex);
    std::stringstream message;
    message << j;
    json j2;
    message >> j2;
    //std::cout << j2 << std::endl;
    Example ex2;
    from_json(j2, ex2);
    //std::cout << ex2.l << ex2.n << ex2.v << std::endl;
    return 0;
}