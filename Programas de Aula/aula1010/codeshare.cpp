#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 80

int strequal(char string1[MAX], char string2[MAX]){
	char aux[80];
	int i,j;
	
	for(i=0;i<strlen(string2);i++){
		aux[i]=tolower(string2[i]);
	}
	if (strlen(string1)!= strlen(aux)){
		return 1;
	}
	for(i=0;string1[i]!='\0';i++){
		if(string1[i] != aux[i]){
			return 1;
		}
		
	}
	return 0;
}


void main(){
	int i,j;
	char entrada[MAX];
	char original[MAX] = "cervo";
	
	scanf("%s", &entrada);	
	
	if(strequal(original,entrada)==0){
		printf("%s eh patrono do Harry Potter\n", entrada);
	}else{
		printf("%s nao eh patrono do Harry Potter\n", entrada);
	}
	

}





