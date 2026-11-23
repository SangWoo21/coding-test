#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1000001          // 크기가 큰 배열은 전역에 (스택 오버플로 방지)
int arr[MAX];

int cmp(const void *a, const void *b) { //오름차순 내림차순 등 cmp만 수정
    int x = *(const int *)a;
    int y = *(const int *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}
int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    qsort(arr, n, sizeof(int), cmp); //qsort(배열, 개수, 원소 하나 크기, 비교 함수)

    for (int i = 0; i < n; i++) printf("%d\n", arr[i]);
    return 0;

}