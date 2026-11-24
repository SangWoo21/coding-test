// 아이디어: 단어를 char 2차원 배열에 저장 → qsort로 정렬 → 중복 건너뛰며 출력
//          cmp: 길이가 다르면 짧은 순(strlen), 같으면 사전 순(strcmp)
//          strcmp는 이미 "앞이면 음수, 뒤면 양수, 같으면 0"이라 그대로 반환
// 중복 제거: 정렬하면 같은 단어가 붙어 있음 → 바로 앞 단어와 다를 때만 출력
//          i == 0을 먼저 확인 (words[-1]은 범위 밖, ||는 앞이 참이면 뒤를 계산 안 함)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char words[20000][51];

int cmp(const void *a, const void *b) {
    const char *s1 = (const char *)a;
    const char *s2 = (const char *)b;
    int len1 = strlen(s1), len2 = strlen(s2);
    if (len1 != len2) return (len1 < len2) ? -1 : 1;
    return strcmp(s1, s2);
}

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%s", words[i]);

    qsort(words, n, sizeof(words[0]), cmp);

    for (int i = 0; i < n; i++) {
        if (i == 0 || strcmp(words[i], words[i - 1]) != 0)
            printf("%s\n", words[i]);
    }
    return 0;
}