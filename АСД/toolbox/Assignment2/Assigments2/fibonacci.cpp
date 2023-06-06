#include <cassert>
#include <iostream>

int fibonacci_naive(int n) {
    if (n <= 1) return n;

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2);
}

int fibonacci_fast(int n) {
    if (n <= 1) return n;

    long long previous = 0;
    long long current = 1;
    long long x = 0;
    for (size_t i = 0; i < n - 1; i++) {
        x = current;
        current += previous;
        previous = x;
    }
    return current;
}

void test_solution() {
    assert(fibonacci_fast(3) == 2);
    assert(fibonacci_fast(10) == 55);
    for (int n = 0; n < 20; ++n)
        assert(fibonacci_fast(n) == fibonacci_naive(n));
}

int main() {
    int n = 0;
    std::cin >> n;

    // std::cout << fibonacci_naive(n) << '\n';
    // test_solution();
    std::cout << fibonacci_fast(n) << '\n';
    return 0;
}