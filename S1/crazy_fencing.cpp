#include <iostream>
#include <cmath>

int main();
void area(double area_before_div);

int main(){
    unsigned int num_traps;

    std::cin >> num_traps;

    unsigned int side_lengths[num_traps + 1];
    unsigned int base_lengths[num_traps];

    for(unsigned int i{0}; i <= num_traps; ++i){
        std::cin >> side_lengths[i];
    }
    for(unsigned int i{0}; i < num_traps; ++i){
        std::cin >> base_lengths[i];
    }

    double area_b_d{0};

    for(unsigned int i{0}; i < num_traps; i++){
        area_b_d += ((side_lengths[i] + side_lengths[i + 1]) * base_lengths[i]);
    }
    area(area_b_d);
}

void area(double area_before_div){
    std::cout<< std::fixed << (area_before_div / 2);
}