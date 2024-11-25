// write a program in c to find the sum of all element of an array
#include<stdio.h>
int main()
{
    int n,i;
    int sum=0;
    printf("enter no of element in array");
    scanf("%d",&n);
    int arr[n]; 
    for(i=0; i<n; i++){
    printf("enter the element value");
    scanf("%d",&arr[i]);}
    for(i=0; i<n; i++)
    sum+=arr[i];
// print the result
    printf("the sum of the element is %d",sum);
    return 0;
}