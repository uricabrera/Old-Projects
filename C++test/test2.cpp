#include <iostream>

using namespace std;
int add(int x, int y)
{
	return x + y;
}


int main()
{
	int a = add(3+4);
	std::cout << "the add of 3+4 is " << a;
	return 0;
}
