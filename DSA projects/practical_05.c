// write  a c program perform push and pop operation in stack
#include<stdio.h>
#define Max 5
int a[Max];
int top=-1;
void push(){
    int data;
    if (top==Max-1){
        printf("stack overflow or stack is full");
    }
    else{
        printf("eneter element to push:");
        scanf("%d",&data);
        top++;
        a[top]=data;

    }
} 
void pop(){
    if (top==-1)
    {
        printf("underflow or stack is empty");
    }
    else
    {
        printf("pop element %d",a[top]);
        top--;

    }
}
void display(){
    int i;
    if (top==0)
    {
       printf("elelments");
       for(i=top; i>0; i--)
       printf("\n%d",a[i]);

    }
    else{
        printf("the stack is empty");
    }
    
}
int main(){
    int n;
    printf("1.push\n2.pop\n3.display");
    scanf("%d",&n);
    push();
}