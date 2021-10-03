#include <iostream>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <cmath>

using namespace std;

int main();
int sqrt_finder(int x, int y);

int main(){
    int a{};
    int b{};
    cin>>a;
    cin>>b;

    cout<<sqrt_finder(a,b);
}

int sqrt_finder(int x, int y){
    int num_found{0};
    double holder{};
    for(int i = x; i <= y; ++i){
        holder = i;
        bool sqrt_checker = true;
        for (int j = 0; j < 3; ++j){
            if (fmod(sqrt(holder), 1.0) != 0.0){
                holder = sqrt(i);
                sqrt_checker = false;
            }else{
                break;
            }   
        }
        if (sqrt_checker){
            num_found += 1;
        }
    }
    return num_found;
}