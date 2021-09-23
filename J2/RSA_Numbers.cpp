#include <iostream>
#include <stdio.h>

using namespace std;

int main();
int RSA(int a, int b);


int main(){
    int x;
    int y;
    cin>>x;
    cin>>y;
    cout<<"The number of RSA numbers between "<<x<<" and "<<y<<" is "<<RSA(x,y);

}

int RSA(int a, int b){
    int number_with_4_divisors = 0;
    for(int i = a; i <= b; ++i){
        int number_of_divisors = 0;
        for (int j = 1; j <= i; ++j){
            if ((i % j) == 0){
                ++number_of_divisors;
                //cout<<number_of_divisors<<" <- num of div\n";
            }
        }
        if (number_of_divisors == 4){
            number_with_4_divisors += 1;
        }
    }
    return number_with_4_divisors;
}