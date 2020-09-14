#include <stdio.h>

int main(int argc, char* argv[])
{
    
    FILE *fp1,*fp2,*fp3;
    int c;

    fp1 = fopen(argv[1], "r");
    fp2 = fopen(argv[2], "r");
    fp3 = fopen(argv[3], "a+");

    while ((c = fgetc(fp1)) != EOF) {
        printf("%c", c);
    }

    fputs("来吧，换行。\n第二行。",fp3);
    
    fclose(fp3);
    fclose(fp2);
    fclose(fp1);
    return 0;
}
