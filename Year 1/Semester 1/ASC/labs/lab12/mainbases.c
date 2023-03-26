#include <stdio.h>

// functia declarata in fisierul modul main.asm
int changebase(char sir1[], int len);

int main()
{
	char sir1[100];

	int n = 4;
	for (int i = 0; i <= n; i++)
	{
		printf("Introduceti elementul in format binar: ");
		scanf("%hhd", sir1);
		int len = strlen(sir1[i]);
		int value = changebase(sir1, len);
		printf("Sirul rezultat este:%x ", value);
	}

	return 0;
}