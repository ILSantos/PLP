#include <stdio.h>
#include <string.h>
#define MAX 100
#define MAX_VET 101

struct Musica {
	char autor[MAX];
	char titulo[MAX];
	char arquivo[MAX];
	int duracao;
};
struct MusicaLista {
	char autor[MAX];
	char titulo[MAX];
	char arquivo[MAX];
	int duracao;
	int indice;
};

int buscar_musica(struct Musica *base, int tam_base, char *autor, char *titulo)
{
	int i;
	int k=-1;
	char vetAutor[MAX_VET];
	char vetTitulo[MAX_VET];
	strcpy(vetAutor,autor);
	strcpy(vetTitulo,titulo);
	for(i=0;i<tam_base;i++){
		if(strcmp(vetAutor,base[i].autor)==0 && strcmp(vetTitulo,base[i].titulo)==0){
			k=i;
		}
	}
	return k;
}


int main(void)
{
	struct Musica base[MAX];
	struct MusicaLista lista[MAX];
	char tempoAutor[MAX_VET];
	char tempoTitulo[MAX_VET];
	int duracaoLista,contadorLista,contadorImpressao,contIndice;
	duracaoLista=0;
	contadorLista=0;
	contadorImpressao=0;
	contIndice=0;
	int musicaBase,musicaLista,i,cont;

	scanf("%d",&musicaBase);

	for(i=0;i<musicaBase;i++){
		scanf("%s",&base[i].autor);
		scanf("%s",&base[i].titulo);
		scanf("%s",&base[i].arquivo);
		scanf("%d",&base[i].duracao);
	}

	scanf("%d",&musicaLista);
	int indiceTempo[musicaLista];
	for(i=0;i<musicaLista;i++){
		
		scanf("%s",&tempoAutor);
		scanf("%s",&tempoTitulo);
		indiceTempo[i]=buscar_musica(base,musicaBase,tempoAutor,tempoTitulo);
	}

	for(i=0;i<musicaLista;i++){
		if(indiceTempo[i]!=-1){
			strcpy(lista[contadorLista].titulo,base[indiceTempo[i]].titulo);
			strcpy(lista[contadorLista].autor,base[indiceTempo[i]].autor);
			strcpy(lista[contadorLista].arquivo,base[indiceTempo[i]].arquivo);
			lista[contadorLista].duracao=base[indiceTempo[i]].duracao;
			lista[contadorLista].indice=contIndice;
			contIndice++;
			duracaoLista=duracaoLista+lista[contadorLista].duracao;
			if(duracaoLista>3600){
				duracaoLista=duracaoLista-lista[contadorLista].duracao;
				strcpy(lista[contadorLista].autor,"");
				strcpy(lista[contadorLista].titulo,"");
				strcpy(lista[contadorLista].arquivo,"");
				lista[contadorLista].duracao=-1;
				lista[contadorLista].indice=-1;
				contadorImpressao--;
			}
			contadorLista++;
			contadorImpressao++;
		}
	}
	printf("Lista gerada com %d musicas e duracao %d:%02d\n",contadorImpressao,(duracaoLista/60),(duracaoLista%60));
		
	for(i=0;i<musicaLista;i++){
		if(lista[i].duracao!=-1){
			printf("%s\n",lista[i].arquivo);
		}
	}
	return 0;
}
