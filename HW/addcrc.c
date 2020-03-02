#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
	char c;
	FILE* f = fopen(argv[1], "r");
	if (f == NULL) {
		fprintf(stderr, "Input file invalid\n");
		return 1;
	}

	int path_len = strlen(argv[1]);
	char* path = malloc(path_len + 4);
	path[0] = 0;
	strcat(path, argv[1]);
	strcat(path, ".crc");

	FILE* w = fopen(path, "w");

	while(fread(&c,1,1,f)) {
		fwrite(&c,1,1,w);
	}
	fseek(w, -4, SEEK_END);
	char crc;
	int x = atoi(argv[2]);
	for (int i = 3 ; i >= 0 ; i--) {
		char *buf = &x;
		fwrite(buf + i, 1, 1, w);
	}
	return 0;
}

