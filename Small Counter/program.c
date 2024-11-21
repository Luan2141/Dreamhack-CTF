// Name: debugee2.c
// Compile: gcc -o debugee2 debugee2.c -no-pie
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	char name[20];
	if( argc < 2 ) {
		printf("Give me the argv[1]!\n");
		exit(0);
	}
	memset(name, 0, sizeof(name));

	printf("argv[1] %s\n", argv[1]);

	read(0, name, sizeof(name)-1);
	printf("Name: %s\n", name);
	return 0;
} 
