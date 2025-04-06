#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

char* kth_word_in_mth_sentence_of_nth_paragraph(char**** document, int k, int m, int n) {
    return document[n-1][m-1][k-1];
}

char** kth_sentence_in_mth_paragraph(char**** document, int k, int m) { 
    return document[m-1][k-1];
}

char*** kth_paragraph(char**** document, int k) {
    return document[k-1];
}

char**** get_document(char* text) {
    char* text_copy = strdup(text);
    int paragraph_count = 0;
    char* temp_text = strdup(text);
    char* p_token = strtok(temp_text, "\n");
    while (p_token != NULL) {
        paragraph_count++;
        p_token = strtok(NULL, "\n");
    }
    free(temp_text);
    char**** document = (char****)malloc((paragraph_count + 1) * sizeof(char***));
    char* saveptr1, *saveptr2, *saveptr3;
    char* text_ptr = text_copy;
    int p_index = 0;
    char* paragraph = strtok_r(text_ptr, "\n", &saveptr1);
    while (paragraph != NULL) {
        char* temp_paragraph = strdup(paragraph);
        int sentence_count = 0;
        char* s_token = strtok(temp_paragraph, ".");
        while (s_token != NULL) {
            sentence_count++;
            s_token = strtok(NULL, ".");
        }
        free(temp_paragraph);
        document[p_index] = (char***)malloc((sentence_count + 1) * sizeof(char**));
        char* paragraph_copy = strdup(paragraph);
        int s_index = 0;
        
        char* sentence = strtok_r(paragraph_copy, ".", &saveptr2);
        while (sentence != NULL) {
            char* temp_sentence = strdup(sentence);
            int word_count = 0;
            char* w_token = strtok(temp_sentence, " ");
            while (w_token != NULL) {
                word_count++;
                w_token = strtok(NULL, " ");
            }
            free(temp_sentence);
            document[p_index][s_index] = (char**)malloc((word_count + 1) * sizeof(char*));
            char* sentence_copy = strdup(sentence);
            int w_index = 0;
            char* word = strtok_r(sentence_copy, " ", &saveptr3);
            while (word != NULL) {
                while (*word == ' ' && *word != '\0') word++;
                if (*word != '\0') {
                    document[p_index][s_index][w_index] = (char*)malloc((strlen(word) + 1) * sizeof(char));
                    strcpy(document[p_index][s_index][w_index], word);
                    w_index++;
                }
                word = strtok_r(NULL, " ", &saveptr3);
            }
            document[p_index][s_index][w_index] = NULL;
            free(sentence_copy);
            s_index++;
            sentence = strtok_r(NULL, ".", &saveptr2);
        }
        document[p_index][s_index] = NULL;
        free(paragraph_copy);
        p_index++;
        paragraph = strtok_r(NULL, "\n", &saveptr1);
    }
    document[p_index] = NULL;
    free(text_copy);
    return document;
}

char* get_input_text() {	
    int paragraph_count;
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    for (int i = 0; i < paragraph_count; i++) {
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char* returnDoc = (char*)malloc((strlen (doc)+1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    return returnDoc;
}

void print_word(char* word) {
    printf("%s", word);
}

void print_sentence(char** sentence) {
    int word_count;
    scanf("%d", &word_count);
    for(int i = 0; i < word_count; i++){
        printf("%s", sentence[i]);
        if( i != word_count - 1)
            printf(" ");
    }
} 

void print_paragraph(char*** paragraph) {
    int sentence_count;
    scanf("%d", &sentence_count);
    for (int i = 0; i < sentence_count; i++) {
        print_sentence(*(paragraph + i));
        printf(".");
    }
}

int main() 
{
    char* text = get_input_text();
    char**** document = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            char* word = kth_word_in_mth_sentence_of_nth_paragraph(document, k, m, n);
            print_word(word);
        }

        else if (type == 2){
            int k, m;
            scanf("%d %d", &k, &m);
            char** sentence = kth_sentence_in_mth_paragraph(document, k, m);
            print_sentence(sentence);
        }

        else{
            int k;
            scanf("%d", &k);
            char*** paragraph = kth_paragraph(document, k);
            print_paragraph(paragraph);
        }
        printf("\n");
    }     
}
