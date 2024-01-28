// 기본 입출력
#include<stdio.h>
int main(void){
    int a;
    scanf("%d",&a);// &는 특정한 변수의 주소를 의미한다.
    printf("입력한 숫자는 %d",a);
    /*
    형식 지정자
    1. int 형 %d
    2. longlong %lld
    3. double %lf
    4.float %f
    5.string %s
    6. char %c
    */
    return 0;
}