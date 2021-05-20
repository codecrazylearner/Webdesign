#include "helpers.h"
#include <cs50.h>
#include <stdio.h>
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{    // loop over rows of bitmap
    for (int i = 0; i < height; i++)
    {
        // loop over each pixel in the row
        for (int j = 0; j < width; j++) {

            // get rgb values of original pixel, find average, and round using float
            int rgb_value = 0;
            rgb_value += image[i][j].rgbtRed;
            rgb_value += image[i][j].rgbtGreen;
            rgb_value += image[i][j].rgbtBlue;
            rgb_value = round(((float) rgb_value) / 3);

            // set each color value to the average
            image[i][j].rgbtRed = rgb_value;
            image[i][j].rgbtGreen = rgb_value;
            image[i][j].rgbtBlue = rgb_value;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{// loop over rows of bitmap
    for (int i = 0; i < height; i++)
    {
        // loop over each pixel in the row
        for (int j = 0; j < width; j++)
        {
           // get rgb values of original pixel, apply formula, and round using float
            BYTE originalRed = image[i][j].rgbtRed;
            BYTE originalGreen = image[i][j].rgbtGreen;
            BYTE originalBlue = image[i][j].rgbtBlue;

            float sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
            float sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
            float sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;

            int s_red = roundf(sepiaRed);
            int s_green = roundf(sepiaGreen);
            int s_blue = roundf(sepiaBlue);

            if (s_red > 255)
            {
                s_red = 255;

            }

            if (s_green > 255)
            {
               s_green = 255;
            }

            if (s_blue > 255)
            {
                s_blue = 255;
            }

            // set each color value to the sepia value
            image[i][j].rgbtRed = s_red;
            image[i][j].rgbtGreen = s_green;
            image[i][j].rgbtBlue = s_blue;


        }

    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    // loop over rows of bitmap
    for (int i = 0; i<height; i++)
    {

         for (int j = 0; j<width/2; j++)
        {
            RGBTRIPLE temp_red = image[i][j];
            image[i][j] = image[i][width-1-j];
            image[i][width-1-j] =  temp_red;

            RGBTRIPLE temp_green = image[i][j];
             image[i][j] = image[i][width-1-j];
             image[i][width-1-j] =  temp_green;

             RGBTRIPLE temp_blue = image[i][j];
             image[i][j] = image[i][width-1-j];
             image[i][width-1-j] =  temp_blue;


        }
    }
        //int first=0;
        //int last=width-1;
        //int mid_element = round(width/2);
        // loop over each pixel in the row

        // while (first<last)

        //     RGBTRIPLE temp_red = image[i][first];
        //     image[i][first] = image[i][last];
        //     image[i][last] =  temp_red;

        //     RGBTRIPLE temp_green = image[i][first];
        //     image[i][first] = image[i][last];
        //     image[i][last] =  temp_green;

        //     RGBTRIPLE temp_blue = image[i][first];
        //     image[i][first] = image[i][last];
        //     image[i][last] =  temp_blue;

        //     first++;
        //     last--;

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE newImage[height][width];
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {

            newImage[i][j] = image[i][j];
        }

    }
    
    for(int h=0;h<height;h++)
    {
        for(int w=0;w<width;w++)
        {
            int totalCounter=0;
            int avgR = 0;
            int avgG = 0;
            int avgB = 0;

            for(int ii=-1;ii<2;ii++)
            {
              for(int jj=-1;jj<2;jj++)
              {
                //if ((h+ii!=-1 && h+ii!=height && w+jj!=0 && w+jj!=width))
                if (h+ii < 0 || h+ii >= height || w+jj < 0 || w+jj >= width)
                 {

                 }
                else {
                       //totalRed += newImage[h+ii][w+jj].rgbtRed;
                       //totalBlue += newImage[h+ii][w+jj].rgbtBlue;
                       //totalGreen += newImage[h+ii][w+jj].rgbtGreen;
                       avgR += newImage[h+ii][w+jj].rgbtRed;
                       avgB += newImage[h+ii][w+jj].rgbtBlue;
                       avgG += newImage[h+ii][w+jj].rgbtGreen;
                       totalCounter++;
                   }

              }

            }
               //calculate average and repace r,g,b values

            image[h][w].rgbtRed = round(avgR /(float)totalCounter);
            image[h][w].rgbtBlue = round(avgB / (float)totalCounter);
            image[h][w].rgbtGreen = round(avgG / (float)totalCounter);



        }
    }



    return;
}
