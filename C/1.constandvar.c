// 변수: 변할수 있는 데이터
// 상수: 변할 수 없는 데이터
#include<stdio.h>
int main(void){
    // 변수 선언 => 자료형 데이터이름= 값; 
    int a= 10;
    /*
    기본적인 자료형
    int =>정수형
    long long => 숫자가 긴 정수형
    double => 일반적인 실수형을 표현
    string => c++에서 많이 사용됨 , 문자열을 표현할때 사용
    bool => 참/거짓을 표현할때 사용
    char =>한문자를 표현할때 사용함
    */
    printf("The number is .. %d!",a);
    return 0;
}