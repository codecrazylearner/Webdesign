
#include<string.h>
#include<cs50.h>
#include<ctype.h>
#include<stdio.h>
#include<stdlib.h>




int main(int argc, string argv[])
{
    if (argc != 2 )
    {
         printf("Usage: ./caesaar key");
         return 1;
    }
    if (strlen(argv[1])!=26)
    {
             printf("Must have all 26 letters of the alphabet");
         return 1;
    }

    for(int i=0;i<strlen(argv[1]);i++)
           {
               if (!isalpha(argv[1][i]))
               {
                  printf("Key must contain Alphabets");
                   return 1;

               }


               for(int j=i+1;j<strlen(argv[1]);j++)
                {
                   if (toupper(argv[1][i])==toupper(argv[1][j]))
                     {

                        printf("repeated value");
                           return 1;
                    }
               }
           }




    string ciphertext=argv[1];

    string gettext="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    int len1=strlen(gettext);

    string plaintext=get_string("\nPlaintext: ");

    int len2=strlen(plaintext);

    printf("ciphertext: ");
    for(int i=0;i<len2;i++)
    {

        char ch=plaintext[i];

        if (isalpha(ch))
        {
            if (islower(ch))
            {
                for(int j=0;j<len1;j++)
                {
                   if (tolower(gettext[j])==plaintext[i])
                   {
                       printf("%c",tolower(ciphertext[j]));

                    }
                }
            }
            if (isupper(ch))
            {
                for (int j=0;j<len1;j++)
                {


                  if (toupper(gettext[j])==plaintext[i])
                   {
                      printf("%c",toupper(ciphertext[j]));

                   }
                }
            }

        }

       else
          {
              printf("%c",plaintext[i]);

          }

    }
    printf("\n");
    return 0;

}







