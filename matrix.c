#include<stdio.h>
#include<math.h>
int main()
{
   int mat1[100][100],mat2[100][100],r,r2,c,c2;
    printf("enter matrix 2 row:");
    scanf("%d",&r);
    printf("enter matrix 2 colume:");
    scanf("%d",&c);
   for(int i=0;i<r;i++)
   {
    for (int j = 0; j < c; j++)
    {
        scanf("%d",&mat1[i][j]);
    }
    printf("enter matrix 2 row:");
    scanf("%d",&r2);
    printf("enter matrix 2 colume:");
    scanf("%d",&c2);
    for(int k=0;k<r;k++)
   {
    for (int l = 0; l< c; l++)
    {
        scanf("%d",&mat2[k][l]);
    }
   }
   for (int i = 0; i < r; i++)
   {
    for (int j = 0; j < c; j++)
    {
        printf("%d",mat1[i][j]);
    }
    
   }
   

    return 0;
}
}