#include <stdio.h>
#define Max 5

int a[Max];
int top = -1;

void push() {
    int data;
    if (top == Max - 1) {
        printf("Stack overflow or stack is full.\n");
    } else {
        printf("Enter element to push: ");
        scanf("%d", &data);
        top++;
        a[top] = data;
        printf("%d pushed to stack.\n", data);
    }
}

void pop() {
    if (top == -1) {
        printf("Stack underflow or stack is empty.\n");
    } else {
        printf("Popped element: %d\n", a[top]);
        top--;
    }
}

void display() {
    if (top == -1) {
        printf("The stack is empty.\n");
    } else {
        printf("Stack elements are:\n");
        for (int i = top; i >= 0; i--) {
            printf("%d\n", a[i]);
        }
    }
}

int main() {
    int n;
    while (1) {
        printf("\n1. Push\n2. Pop\n3. Display\n4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &n);

        switch (n) {
        case 1:
            push();
            break;
        case 2:
            pop();
            break;
        case 3:
            display();
            break;
        case 4:
            printf("Exiting...\n");
            return 0;
        default:
            printf("Invalid choice. Please try again.\n");
        }
    }
    return 0;
}
