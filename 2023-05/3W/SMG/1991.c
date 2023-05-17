#include <stdio.h>
#include <stdlib.h>

typedef struct __node{
    char data;
    struct __node *left, *right;
}Node;
typedef struct __tree{
    struct __node *root;
}Tree;

Node *getNode(char data){
    if(data == '.')
        return NULL;

    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;

    return newNode;
}
void setNode(Node *node, char parent, char left, char right){
    node->data = parent;
    if(left != '.')
        node->left = getNode(left);
    if(right != '.')
        node->right = getNode(right);
}
Node *searchNode(Node *node, char data){
    if(node == NULL)
        return NULL;
    else if(node->data == data)
        return node;
    else{
        Node *ret = searchNode(node->left, data);
        if(ret != NULL)
            return ret;
    }
    return searchNode(node->right, data);
}
void preOrder(Node *node){
    if(node){
        printf("%c", node->data);
        preOrder(node->left);
        preOrder(node->right);
    }
}
void inOrder(Node *node){
    if(node){
        inOrder(node->left);
        printf("%c", node->data);
        inOrder(node->right);
    }
}
void postOrder(Node *node){
    if(node){
        postOrder(node->left);
        postOrder(node->right);
        printf("%c", node->data);
    }
}
void freeNode(Node *node){
    if(node){
        freeNode(node->left);
        freeNode(node->right);
        free(node);
    }
}

int main()
{
    Tree t;
    char parent, leftdata, rightdata;
    int N;
    scanf("%d", &N);
    getchar();

    t.root = getNode(NULL);

    for(int i=0; i<N; i++){
        scanf("%c %c %c", &parent, &leftdata, &rightdata);
        getchar();
        Node *ptr = searchNode(t.root, parent);
        if(ptr != NULL)
            setNode(ptr, parent, leftdata, rightdata);
        else
            setNode(t.root, parent, leftdata, rightdata);
    }
    preOrder(t.root);
    printf("\n");
    inOrder(t.root);
    printf("\n");
    postOrder(t.root);
    printf("\n");

    freeNode(t.root);

    return 0;
}