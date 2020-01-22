#include <iostream>
#include <cfloat>

int main()
{
  using namespace std;

  cout.setf(ios_base::fixed, ios_base::floatfield);

  float flt = 10.0 / 3.0;
  double dbl = 10.0 / 3.0;

  float million = 1e6;

  cout << flt << " " << million * flt << endl;
  cout << million * flt * 1000 << endl;
  cout << dbl << " " << million * dbl << endl;
  cout << million * dbl * 1000 << endl;
}