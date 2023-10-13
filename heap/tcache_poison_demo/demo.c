#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
#define STORAGE_SIZE 10
int main(void) {
	system("echo tcache poisoning demo");
	int opt;
	char* storage[STORAGE_SIZE];
	size_t sizes[STORAGE_SIZE];

	//for (int i = 0; i < STORAGE_SIZE; ++i) exists[i] = false;
	printf("1: alloc\n2: read\n3: free\n> ");	
	int top;
	while (1) {
		scanf("%d", &opt);
		if (opt == 1) {
			int next_top;
			size_t sz;
			printf("idx=\n");
			scanf("%d", &next_top);
			//printf("next_top=%d",next_top);
			printf("size=\n");
			scanf("%d", &sz);
			sizes[next_top] = sz;
			storage[next_top] = malloc(sz);
			//printf("%p", storage[next_top]);
			assert(storage[next_top] != NULL);
			printf("contents=\n");
			read(0, storage[next_top], sz);
			printf("leak: %p\n", storage[next_top]);
			//exists[next_top] = true;
			top = next_top;
		} else if (opt == 2) {
			printf("idx=\n");
			int idx;
			scanf("%d", &idx);
			write(1, storage[idx], sizes[idx]);
		} else if (opt == 3) {
			printf("idx=\n");
			int idx;
			scanf("%d", &idx);
			free(storage[idx]);
		}
		printf("> ");
		fflush(stdout);
	}
}
