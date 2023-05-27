#include <stdio.h>

int main()
{
    int cnt = 0;
    int N;
    scanf("%d", &N);
    for(int i=1; i<=N; i++){
        if(i%5==0)
            cnt++;
        if(i%25==0)
            cnt++;
        if(i%125==0)
            cnt++;
    }
    printf("%d\n", cnt);

    return 0;
}