# Calculator

*Last edited: 2024-01-12*

Based on the example of the book *Advanced C* by Herbert Schildt

A simple four-function calculator


```text/x-csrc
#include <stdio.h>

#define MAX 100

int * p;     // will point to a region of free memory
int * tos;   // points to top of stack
int * bos;   // points to bottom of stack

// Place an element on the stack
void push(int i) {
    if (p > bos) {
        printf("stack full\n");
        return;
    }
    * p = i;
    p++;
}

// Return the top element from the stack
int pop() {
    p--;
    if (p < tos) {
        printf("stack underflow\n");
        return 0;
    }
    return * p;
}


// Main routine
int main() {
    int a, b, c; // auxiliary variables
    char s[80];  // input buffer

    // get stack memory
    p = (int * ) malloc(MAX * sizeof(int));
    if (!p) {
        printf("allocation failure\n");
        exit(1);
    }
    tos = p;
    bos = p + MAX - 1;
    printf("Four Function Calculator\n");

    do {
        // fgets(s, sizeof s, stdin);
        scanf("%s", s);
        switch ( * s) {
        case '+':
            a = pop();
            b = pop();
            c = a + b;
            printf("%d\n", c);
            push(c);
            break;
        case '-':
            a = pop();
            b = pop();
            c = b - a;
            printf("%d\n", b - a);
            push(c);
            break;
        case '*':
            a = pop();
            b = pop();
            c = b * a;
            printf("%d\n", c);
            push(c);
            break;
        case '/':
            a = pop();
            if (a == 0) {
                printf("divide by 0\n");
                break;
            }
            b = pop();
            c = b / a;
            printf("%d\n", c);
            push(c);
            break;

        // show contents of top of stack
        case '.': 
            a = pop();
            push(a);
            printf("Current value on top of stack: %d\n", a);
            break;

        // If the input is a number
        default:
            a = atoi(s);
            push(a);
        }
    } while ( * s != 'q');
}
```

    Four Function Calculator


     10
     20
     .


    Current value on top of stack: 20


     +


    30


     .


    Current value on top of stack: 30


     50
     +


    80


     .


    Current value on top of stack: 80



```text/x-csrc

```
