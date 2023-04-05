#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[]) {
	// For best results, run on webshell.picoctf.net with an offset of 0
	// If you can't get it to work try repeatedly running it with an offset of 0-2 seconds
	// An offset of 1 second is the best/most optimal one from my experience
	if (argc < 2) {
		puts("Usage: seed_spring_generator <offset in seconds>");
		return 0;
	}
	srand(time(NULL) + atoi(argv[1]));
	for (int i = 1; i <= 30; ++i) {
		printf("%d\n", rand() & 0xf);
	}
}

