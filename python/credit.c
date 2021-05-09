#include<stdio.h>
#include<math.h>
#include<cs50.h>

int length(long count_num)
{   int count=0;
    while (count_num!=0)
    {
         count_num=count_num/10;
         count++;
    }
    return(count);
}

bool cardlen(int len)
{
    if (len==13 || len==15 || len ==16 )
        return true;
   return false;
}

bool digitsum(long number,int len)
{
        int ctr=0;
        int prod=0;
        int sum=0;
        for (ctr=0;ctr<len;ctr++)
        {

            if(ctr%2 == 0)
            {
                sum=sum + (number%10);
            }
            else
             {
                prod= 2*(number%10);
                sum = sum+(prod%10)+(prod/10);
             }
            number/=10;
        }
         if (sum%10==0)
            return true;

       return false;
}

void cardname(long card)

{
        if ((card >= 340000000000000 && card < 350000000000000) || (card >= 370000000000000 && card < 380000000000000))
              {
                  printf("AMEX\n");

              }

        else if (card >= 5100000000000000 && card < 5600000000000000)
             {
                  printf("MASTERCARD\n");
             }
        else if((card >= 4000000000000 && card < 5000000000000) || (card >= 4000000000000000 && card < 5000000000000000))
            {

                  printf("VISA\n") ;

            }
        else
            printf("INVALID\n");

}



void checkcard(long ccard)
{

       int len=length(ccard);
       if (!(cardlen(len) && digitsum(ccard,len) ))
         {
             printf("INVALID\n");
             return;
         }

       cardname(ccard);


}



int main(void)
{
    long ctcard=1;

    do
    {

      ctcard=get_long("Enter the number");

    } while(ctcard < 0);

    checkcard(ctcard);
}