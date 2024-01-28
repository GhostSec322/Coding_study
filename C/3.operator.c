#include<stdio.h>
int main(void)
{
    //https://www.programiz.com/c-programming/c-operators 참고
    //산술연산
    int a=0;
    int b=3;
    printf("%d + %d = %d\n",a,b,a+b);
    printf("%d - %d = %d\n",a,b,a-b);
    printf("%d x %d = %d\n",a,b,a*b);
    printf("%d / %d = %d\n",a,b,a/b);
    printf("%d %% %d = %d\n",a,b,a%b);
    //관계연산
    printf("%d > %d = %d\n",a,b,a>b);
    printf("%d < %d = %d\n",a,b,a<b);
    printf("%d >= %d = %d\n",a,b,a>=b);
    printf("%d <= %d = %d\n",a,b,a<=b);
    printf("%d == %d = %d\n",a,b,a==b);
    printf("%d != %d = %d\n",a,b,a != b);
    //논리연산
    printf("%d and %d = %d\n",a,b,a&&b);
    printf("%d or %d = %d\n",a,b,a||b);
    printf("%d not %d = %d\n",a,b,!b);
    //증감연산
    printf("%d ++ = %d\n",a,b,a++);
    printf("%d -- = %d\n",a,b,a--);
    printf("++ %d = %d\n",a,b,++a);
    printf("-- %d = %d\n",a,b,--a);
    return 0;
}