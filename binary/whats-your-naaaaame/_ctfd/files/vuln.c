/* gcc -m32 -fno-stack-protector vuln.c -o vuln */

#include <stdio.h>
#include <stdlib.h>

#define MAX_NAME_LEN 20
#define FALSE 0

int main(int argc, char **argv) {
    int name_len = 0;
    volatile int is_admin = FALSE;

    printf("How long is your name? ");
    fflush(stdout);
    scanf("%d", &name_len);

    if (name_len > MAX_NAME_LEN) {
        printf("Your name is too long for us!\n");
        fflush(stdout);
        exit(EXIT_FAILURE);
    }

    char name[MAX_NAME_LEN];

    printf("Enter your name: ");
    fflush(stdout);
    scanf("%s", name);

    if (is_admin != FALSE) {
        printf("OWEEK{now try this on the server to get the real flag!}\n");
    } else {
        printf("You are not authorised to view this flag!\n");
    }

    fflush(stdout);

    return EXIT_SUCCESS;
}
