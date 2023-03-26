#include <stdio.h>

// functia declarata in fisierul modul main.asm
void changebase(char sir1[], char sirRez[]);

int main_funct()
{
	char sir1[100], sirRez[100];
	printf("Introduceti sirul cu numere in baza 2: ");
	scanf("%100s", sir1);
	changebase(sir1, sirRez);
	printf("Sirul rezultat este: %s", sirRez);
	return 0;
}
