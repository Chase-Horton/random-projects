#include <stdio.h>
int main(void){
float numbers;
float a;
float b;
float C;
printf("How many Fibonacci Numbers would you like?\n");
if(0 == scanf("%f", &numbers)) {
numbers = 0;
scanf("%*s");
}
printf("\n");
a=0;
b=1;
while(numbers>0){
printf("%.2f\n", (float)(a));
C=a+b;
a=b;
b=C;
numbers=numbers-1;
}
return 0;
}
