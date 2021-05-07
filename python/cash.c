#include<cs50.h>
#include<stdio.h>
#include<math.h>

int main(void)
{
  float change_owed;
    do
    {    
         change_owed = get_float("enter the change owed :  ");
         
    }while(change_owed < 0);
    int  coins = (int)round (change_owed*100);
 
 
    int sum=(coins/25)+((coins%25)/10)+(((coins%25)%10)/5)+((((coins%25)%10)%5)/1);
    
    printf("sum %d\n:  ",sum);
}
