#include <iostream>
#include <vector>

using namespace std;

int BinarySearch(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            // handle duplicates
            while (mid > 0 && arr[mid - 1] == target) {
                mid--;
            }
            return mid;
        } else if (arr[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int target;
        cin >> target;
        int index = BinarySearch(arr, target);
        cout << index << " ";
    }
    cout << endl;
    return 0;
}
