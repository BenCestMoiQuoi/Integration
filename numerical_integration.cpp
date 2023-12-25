#include <iostream>
using namespace std;

float f(float x)
{
    return 1-x*x;
}

int main()
{
    int n = 1000;
    float x_min = -1;
    float x_max = 1;

    float val = 0;
    float dx = (x_max-x_min)/n;

    for (float x1=x_min, x2=x_min+dx; x2<=x_max; x1=x1+dx, x2=x2+dx)
    {
        val = val+0.5*(f(x1)+f(x2))*dx;
    }
    cout<<val<<endl;
    system("PAUSE");
    return 0;
}