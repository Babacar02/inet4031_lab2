#include <stdio.h>


int main(){

	int a = 2;
	int b=2;
	int c = a+b;
	const char* array_users[3] ={ "User1", "User2", "User3"};
	

	for(int i = 0; i < 3; i++){
		printf("%s\n",array_users[i]);
	}

	printf("\n");
	printf("C says: Hello, World!\n");
	printf("%d + %d = %d\n",a,b,c);

	return 0;

}
