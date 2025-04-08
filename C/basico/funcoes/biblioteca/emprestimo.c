#include <stdio.h>
#include <string.h>

#define MAX_EMPRESTIMOS 3

// Define o enum para o status do livro: DISPONIVEL ou EMPRESTADO.
typedef enum {
    DISPONIVEL,
    EMPRESTADO
} StatusLivro;

// Estrutura que representa um livro.
typedef struct {
    char autor[100];
    char titulo[100];
    int total_emprestimos; // Número de vezes que o livro foi emprestado (máximo 3).
    StatusLivro status;
} Livro;

// Função para imprimir os dados do livro de forma formatada.
void imprimirLivro(Livro *livro) {
    printf("\n--- Dados do Livro ---\n");
    printf("Título: %s\n", livro->titulo);
    printf("Autor: %s\n", livro->autor);
    printf("Total de Empréstimos: %d\n", livro->total_emprestimos);
    printf("Status: %s\n", (livro->status == DISPONIVEL) ? "Disponível" : "Emprestado");
    printf("----------------------\n");
}

// Função para imprimir o resultado das operações de empréstimo ou devolução.
void imprimirOperacao(const char *operacao, int sucesso) {
    if (sucesso) {
        printf("Operação de %s realizada com sucesso!\n", operacao);
    } else {
        printf("Operação de %s falhou!\n", operacao);
    }
}

// Função para realizar o empréstimo do livro.
// Verifica se o livro está disponível e se não atingiu o número máximo de empréstimos.
int emprestarLivro(Livro *livro) {
    if (livro == NULL)
        return 0;
   
    if (livro->total_emprestimos >= MAX_EMPRESTIMOS) {
        printf("Este livro já atingiu o número máximo de empréstimos (%d).\n", MAX_EMPRESTIMOS);
        return 0;
    }
   
    if (livro->status == DISPONIVEL) {
        livro->status = EMPRESTADO;
        livro->total_emprestimos++;
        return 1;
    } else {
        printf("O livro não está disponível para empréstimo no momento.\n");
        return 0;
    }
}

// Função para realizar a devolução do livro.
// Verifica se o livro está emprestado.
int devolverLivro(Livro *livro) {
    if (livro == NULL)
        return 0;
   
    if (livro->status == EMPRESTADO) {
        livro->status = DISPONIVEL;
        return 1;
    } else {
        printf("O livro não está emprestado e, portanto, não pode ser devolvido.\n");
        return 0;
    }
}

int main() {
    Livro meuLivro;

    // Inicialização dos dados do livro.
    strcpy(meuLivro.autor, "Autor Exemplo");
    strcpy(meuLivro.titulo, "Título Exemplo");
    meuLivro.total_emprestimos = 0;
    meuLivro.status = DISPONIVEL;
   
    int opcao;
   
    do {
        printf("\n============================\n");
        printf("   Sistema de Empréstimo de Livros\n");
        printf("============================\n");

        // Exibe os dados do livro.
        imprimirLivro(&meuLivro);
       
        // Exibe o menu de operações.
        printf("\nEscolha uma operação:\n");
        printf("1 - Emprestar Livro\n");
        printf("2 - Devolver Livro\n");
        printf("0 - Sair\n");
        printf("Opção: ");
        scanf("%d", &opcao);
       
        switch (opcao) {
            case 1:
                // Tenta emprestar o livro.
                if (emprestarLivro(&meuLivro))
                    imprimirOperacao("Empréstimo", 1);
                else
                    imprimirOperacao("Empréstimo", 0);
                break;
            case 2:
                // Tenta devolver o livro.
                if (devolverLivro(&meuLivro))
                    imprimirOperacao("Devolução", 1);
                else
                    imprimirOperacao("Devolução", 0);
                break;
            case 0:
                printf("Encerrando o programa...\n");
                break;
            default:
                printf("Opção inválida. Tente novamente.\n");
        }
    } while (opcao != 0);
   
    return 0;
}