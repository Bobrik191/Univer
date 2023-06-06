#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Segment {
    int start;
    int end;
};

vector<int> CountPoints(vector<Segment>& segments, vector<int>& points) {
    vector<int> counts(points.size());
    sort(segments.begin(), segments.end(), [](Segment& s1, Segment& s2) {
        return s1.end < s2.end;
    });
    for (int i = 0; i < points.size(); i++) {
        int count = 0;
        for (int j = 0; j < segments.size(); j++) {
            if (points[i] >= segments[j].start && points[i] <= segments[j].end) {
                count++;
                segments.erase(segments.begin() + j);
                j--;
            } else if (points[i] < segments[j].start) {
                break;
            }
        }
        counts[i] = count;
    }
    return counts;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<Segment> segments(n);
    for (int i = 0; i < n; i++) {
        cin >> segments[i].start >> segments[i].end;
    }
    vector<int> points(m);
    for (int i = 0; i < m; i++) {
        cin >> points[i];
    }
    vector<int> counts = CountPoints(segments, points);
    for (int i = 0; i < counts.size(); i++) {
        cout << counts[i] << " ";
    }
    cout << endl;
    return 0;
}
