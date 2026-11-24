// BOJ 11650 좌표 정렬하기 (정렬)
// 아이디어: x, y를 구조체로 묶어 qsort → 짝이 깨지지 않음
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int x;
    int y;
} Point;

Point p[100001];      // 점 10만 개 (전역)

int cmp(const void *a, const void *b) {
    const Point *p1 = (const Point *)a;
    const Point *p2 = (const Point *)b;
    if (p1->x != p2->x)
        return (p1->x < p2->x) ? -1 : 1;
    if (p1->y != p2->y)
        return (p1->y < p2->y) ? -1 : 1;
    return 0;
}

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &p[i].x, &p[i].y);
    }
    qsort(p, n, sizeof(Point), cmp);
    
    for (int i =0; i < n; i++) {
        printf("%d %d\n", p[i].x, p[i].y);
    }
    return 0;
}