#include <stdio.h>
#ifndef CLEAR
#define CLEAR

#ifdef _WIN32
    #deifine CLEAR_CMD "cls"

    #else
        #define CLEAR_CMD "clear"

#endif

void clear (){

    system(CLEAR_CMD);
};
#endif