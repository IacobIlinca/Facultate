#include <stdio.h>
#include <string.h>
#pragma comment(linker, "/INCLUDE:_scanf")
#pragma comment(lib, "legacy_stdio_definitions.lib")
#pragma comment(linker, "/INCLUDE:_printf")


void sufix_comun(char sir1[100], char sir2[100], char sufix[100])
{   int i,k,j;
    char inversat [100];
    i = strlen(sir1)-1;
    j = strlen(sir2)-1;
    k = 0;
    while ((sir1[i] == sir2[j]) && (i>=0) && (j>=0))
    {   
        inversat[k]=sir1[i];
        k++;
        i--;
        j--;
    }
    inversat[k] = 0;
    k=0;
    for (i=strlen(inversat)-1;i>=0;i--)
    {
        sufix[k] = inversat[i];
        k++;
    }
    sufix[k] = 0; 
}

void citire(char sir1[100],char sir2[100], char sir3[100]);


int main()
{   
    
    char sir1[100], sir2[100], sir3[100], sufix[100];
    citire(sir1,sir2,sir3);
    sufix_comun(sir1,sir2,sufix);
    printf("Sufixul comun sir1 sir2: %s",sufix);
    
    sufix_comun(sir1,sir3,sufix);
    printf("Sufixul comun sir1 sir3:%s",sufix);
    
    sufix_comun(sir2,sir3,sufix);
    printf("Sufixul comun sir2 sir3:%s",sufix);
    
return 0;
}