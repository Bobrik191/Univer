#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>

using namespace std;

int Partition(vector<int>& arr, int left, int right) {
    int pivot = arr[right];
    int i = left - 1;
    for (int j = left; j < right; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[right]);
    return i + 1;
}

void RandomizedQuickSort(vector<int>& arr, int left, int right) {
    if (left >= right) {
        return;
    }
    srand(time(NULL));
    int random = left + rand() % (right - left + 1);
    swap(arr[random], arr[right]);
    int pivot_index = Partition(arr, left, right);
    RandomizedQuickSort(arr, left, pivot_index - 1);
    RandomizedQuickSort(arr, pivot_index + 1, right);
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    RandomizedQuickSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
