#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// int main(int argc, char*argv[]){

//     for(int i = 0; i<argc;i++){
//         printf("Arg[%i]%s\n",i,argv[i]);
//     }
//     //printf ("%i/n",argc);
//     return 0;
// }

// float inToFloat(int n){
//     return n;
// }
// void halfConvert(int n){
    
//    // float half = n *0.5;
//     float half = inToFloat(n) *0.5;
//     printf("Metade 2: %.2f\n", half);
// }
// void tema(){
//     printf("=================================Menu===================================\n");
//     halfConvert(10);
//     printf("=================================----===================================\n");
// }

#define MAX_STR 50

typedef struct{
    char name[MAX_STR];
    float power;
    int lives;
    bool alive;

}Player;

void imprimePlayer(Player *p){
    printf("======Game Over==========\n");
    printf("%s\n",p ->name);
    printf("%.4f\n",p ->power);
    printf("%d\n",p ->lives);
    printf("%i\n",p ->alive);
    printf("=========================\n");
}

int main(){

    Player p1 = {
        .name = "brunão",
        .power = 1500.0,
        .lives = 5,
        .alive = true
    };
    imprimePlayer(&p1);
    // tema();
    return 0;
}