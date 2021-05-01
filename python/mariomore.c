
#include <stdio.h>
#include<cs50.h>

int main(void)
{
     int hgt= get_int("enter the height");
      while (hgt<1 || hgt>8)
          hgt= get_int("\n Invalid number -- enter the height again");
      for (int i=1;i <= hgt;i++)
       {
          for (int j = hgt-i; j > 0;j--)
             printf(" ");
          for(int k=1;k <= i+1; k++)
              printf("#");
          printf("\n");
      }
}
