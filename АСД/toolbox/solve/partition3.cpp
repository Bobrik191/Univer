#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

bool partition_search(const vector<long long>& A, int index,
					  vector<long long>& partitions, long long target) {
	if (index >= A.size()) return true;
	for (size_t i = 0; i < partitions.size(); i++) {
		if (partitions[i] + A.at(index) <= target) {
			partitions[i] += A.at(index);
			if (partition_search(A, index + 1, partitions, target)) {
				return true;
			}
			partitions[i] -= A.at(index);
		}
	}
	return false;
}

bool partition3(vector<long long>& A) {
	long long n = accumulate(A.begin(), A.end(), 0);
	// cout << n << " " << *max_element(A.begin(), A.end()) << endl;
	if (n % 3 != 0 or A.size() < 3 or
		*max_element(A.begin(), A.end()) > n / 3) {
		// cout << "Invalid";
		return false;
	}

	sort(A.begin(), A.end());
	reverse(A.begin(), A.end());
	vector<long long> partitions(3, 0);
	return partition_search(A, 0, partitions, n / 3);
}

int main() {
	int n;
	std::cin >> n;
	vector<long long> A(n);
	for (size_t i = 0; i < A.size(); ++i) { std::cin >> A[i]; }
	std::cout << partition3(A) << '\n';
}
