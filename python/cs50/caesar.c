
#include<string.h>
#include<cs50.h>
#include<ctype.h>
#include<stdio.h>
#include<stdlib.h>
bool checkdigit(string s);



int main(int argc, string argv[])
{
    if (argc != 2 ||  !checkdigit(argv[1]))
    {
         printf("Usage: ./caesaar key");
         return 1;
    }




    int key = atoi(argv[1]);

    string plaintext=get_string("Plaintext : ");
    printf("Ciphertext : ");

    for(int i=0; i < strlen(plaintext); i++)
      {
         if (isalpha(plaintext[i]))
         {
             
                  char m='A';
              
              if (islower(plaintext[i]))
              {   m='a';}
              printf("%c",(plaintext[i] - m + key) % 26 + m);
         }   
         else
               { printf("%c",plaintext[i]);}


       }
       
}



bool checkdigit(string s) 
{

     for(int i = 0; i<strlen(s); i++) 
     {
        if(!isdigit(s[i])) 
        {

           return false;
        }
     }
     return true;
  }
