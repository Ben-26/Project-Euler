#include <iostream>
#include <vector>
#include <string>

class Date {
public:
	int d, w, m, y;
	std::vector<int> month_days = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	Date(int day, int weekday, int month, int year) {
		d = day;
		w = weekday;
		m = month;
		y = year;
	};
	int getDay() { return d; };
	int getMonth() { return m; };
	int getYear() { return y; };
	bool incrimentDate() {
		d++;
		w = w + 1 > 7 ? 1 : w + 1; // Weekday 
		if (m == 2 && (y % 100 == 0 ? (y % 400 == 0 ? true : false) : (y % 4 == 0 ? true : false))) { // Leap year February
			if (d > month_days.at(m - 1) + 1) { // New month
				d = 1;
				m++;
			}
		}
		else if (m == 12) { // December
			if (d > month_days.at(m - 1)) { // New Year
				d = 1;
				m = 1;
				y++;
			}
		}
		else { // Other months
			if (d > month_days.at(m - 1)) { // New month
				d = 1;
				m++;
			}
		}
		return w == 7 && d == 1 ? true : false;
	};
};

int main() {
	Date date = Date::Date(1, 1, 1, 1900);
	int t = 0;
	while (!(date.getDay() == 31 && date.getMonth() == 12 && date.getYear() == 2000)) {
		if (date.incrimentDate()) {
			t++;
		}
	}
	std::cout << t - 2; // - 2 to remove ones included in 1900
	return 0;
}
