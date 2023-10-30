#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "out.h"
void decrypt(char* buf, int n) {
	for (int i = 0; i < n; ++i) {
		//printf("%d\n",i);
		//printf("yes %x\n",buf[0]);
		for (int j = 0; j <= i; ++j) {
			buf[i] = buf[i] ^ ((char)(rand()) & 0xff);
		}
	}
}
int main(void) {
	char* start = "ictf{";
	int start_len = 4;
	// 4/1/2023 0:0:0
	char tmp[out_bin_len];
	for (unsigned long i = 1680321600; i <= 4294967295; ++i) {
		srand(i);
		memcpy(tmp, out_bin, out_bin_len);
		//puts("before segfault");
		decrypt(tmp, start_len);
		bool works=true;
		//puts("yes");
		for (int j = 0; j < start_len; ++j) {
			if (tmp[j] != start[j]) {
				works=false;
				break;
			}
		}
		//printf("%lu ",i);
		//puts("before");
		if (works) {
			printf("found seed=%lu\n", i);
			srand(i);
			memcpy(tmp, out_bin, out_bin_len);
			decrypt(tmp,out_bin_len);
			for (int j = 0; j < out_bin_len; ++j) {
				putchar(tmp[j]);
			}
			puts("");
			break;
		}
		//printf("done\n");
	}
}
