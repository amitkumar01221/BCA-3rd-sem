// intillize an array with element and calculate it's length
#include<stdio.h>
int main()
{
    int arr[5]={10,20,30,40,50};
    int i;
    printf("array element are:");
    for(i=0; i<5; i++)
    {
        printf("%d",arr[i]);
        printf("\n");

    }
    // calculate it's lenght 
    int len=sizeof(arr)/sizeof(arr[0]);
    printf("the lenght of this array is %d\n",len);
    return 0;
}