#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int ch = 0, ai = 0;
    printf("Rock Paper Scissors\n");

    srand(time(0)); // Seed the random number generator

    while (1) {
        printf("rock - 1 \npaper - 2 \nscissors - 3 \n");
        scanf("%d", &ch);

        ai = rand() % 3 + 1; // Random number between 1 and 3

        if (ch == 1 && ai == 2) {
            printf("AI wins\n");
        } else if (ch == 2 && ai == 3) {
            printf("AI wins\n");
        } else if (ch == 3 && ai == 1) {
            printf("AI wins\n");
        } else {
            printf("Player wins\n");
            printf("%d %d\n", ch, ai);
        }
    }

    return 0;
}
