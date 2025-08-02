#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    printf("This is parent. PID: %d\n",(int)getpid());
    int rc = fork();
    if(rc<0) {
        printf("Fork failed!\n");
        exit(1);
    }
    else if(rc == 0) {
        printf("This is child. PID: %d\n",(int)getpid());
    }
    else {
        printf("This is parent my child is %d\n",rc);
    }
    printf("Who am I? PID:%d\n",(int)getpid());
    return 0;
}