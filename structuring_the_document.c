#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

struct word {
    char* data;
};

struct sentence {
    struct word* data;
    int word_count;//denotes number of words in a sentence
};

struct paragraph {
    struct sentence* data  ;
    int sentence_count;//denotes number of sentences in a paragraph
};

struct document {
    struct paragraph* data;
    int paragraph_count;//denotes number of paragraphs in a document
};
//r function to split a string by a delimiter
char** split_string(char* text, const char* delimiter, int* count) {
    char** result = NULL;
    char* token = strtok(text, delimiter);
    *count = 0;

    while (token) {
        result = realloc(result, sizeof(char*) * (*count + 1));
        result[*count] = token;
        (*count)++;
        token = strtok(NULL, delimiter);
    }

    return result;
}

struct document get_document(char* text) {
    struct document doc;

    int paragraph_count;
    char** paragraphs = split_string(text, "\n", &paragraph_count);
    doc.data = malloc(sizeof(struct paragraph) * paragraph_count);
    doc.paragraph_count = paragraph_count;

    for (int i = 0; i < paragraph_count; i++) {
        int sentence_count;
        char** sentences = split_string(paragraphs[i], ".", &sentence_count);
        doc.data[i].data = malloc(sizeof(struct sentence) * sentence_count);
        doc.data[i].sentence_count = sentence_count;

        for (int j = 0; j < sentence_count; j++) {
            int word_count;
            char** words = split_string(sentences[j], " ", &word_count);
            doc.data[i].data[j].data = malloc(sizeof(struct word) * word_count);
            doc.data[i].data[j].word_count = word_count;

            for (int k = 0; k < word_count; k++) {
                doc.data[i].data[j].data[k].data = words[k];
            }
            free(words);
        }
        free(sentences);
    }

    free(paragraphs);
    return doc;
}

struct paragraph kth_paragraph(struct document doc, int k) {
    return doc.data[k - 1];
}

struct sentence kth_sentence_in_mth_paragraph(struct document doc, int k, int m) {
    return doc.data[m - 1].data[k - 1];
}

struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document doc, int k, int m, int n) {
    return doc.data[n - 1].data[m - 1].data[k - 1];
}

void print_word(struct word w) {
    printf("%s", w.data);
}

void print_sentence(struct sentence sen) {
    for(int i = 0; i < sen.word_count; i++) {
        print_word(sen.data[i]);
        if (i != sen.word_count - 1) {
            printf(" ");
        }
    }
}

void print_paragraph(struct paragraph para) {
    for(int i = 0; i < para.sentence_count; i++){
        print_sentence(para.data[i]);
        printf(".");
    }
}

void print_document(struct document doc) {
    for(int i = 0; i < doc.paragraph_count; i++) {
        print_paragraph(doc.data[i]);
        if (i != doc.paragraph_count - 1)
            printf("\n");
    }
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

int main() 
{
    char* text = get_input_text();
    struct document Doc = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            struct word w = kth_word_in_mth_sentence_of_nth_paragraph(Doc, k, m, n);
            print_word(w);
        }

        else if (type == 2) {
            int k, m;
            scanf("%d %d", &k, &m);
            struct sentence sen= kth_sentence_in_mth_paragraph(Doc, k, m);
            print_sentence(sen);
        }

        else{
            int k;
            scanf("%d", &k);
            struct paragraph para = kth_paragraph(Doc, k);
            print_paragraph(para);
        }
        printf("\n");
    }     
}
