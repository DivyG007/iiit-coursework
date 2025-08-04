#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

int main() {
    printf("This is parent. PID: %d\n",(int)getpid());
    int rc = fork();
    if(rc<0) {
        printf("Fork failed!\n");
        exit(1);
    }
    else if(rc == 0) {
        // sleep(5);
        printf("This is child. PID: %d\n",(int)getpid());
        char *myargs[3];
        myargs[0] = strdup("wc");
        myargs[1] = strdup("sample.txt");
        char *str[2];
        str[0] = strdup("sample2.txt");
        str[1] = NULL;
        myargs[2] = NULL;
        execvp(myargs[0], myargs);
        printf("There was an error. \n");
        return(1);
    }
    else {
        int rc_wait = wait(NULL);
        printf("This is parent my child is %d\n",rc);
    }
    printf("Who am I? PID:%d\n",(int)getpid());
    return 0;
}