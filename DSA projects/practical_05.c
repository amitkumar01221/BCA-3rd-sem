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
    if (top==-1)
    {
       printf("the stack is empty");

    }
    else{
    
       printf("elelments");
       for(i=top; i<0; i--){
       printf("\n%d",a[i]);}
    }
    
}
int main(){
    int n;
    while (1)
    {
    
    printf("1.push\n2.pop\n3.display\n");
    scanf("%d",&n);
    switch (n)
    {
    case 1:
        push();
    case 2:
        pop();
    case 3:
        display();
        break;
    }}
    return 0;

}