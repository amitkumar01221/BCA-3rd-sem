//write a program to revese an array element
#include<stdio.h>
int  main(){
    int a[5];
    printf("eneter array element");
    for(int i=0; i<5; i++)
    {
        scanf("%d",&a[i]);
        printf("reverse array elelment\n");
    }
    for (int i = 4; i >= 0; i--)
    {
        printf("%d\n",a[i]);
    }
    return 0;
    
}