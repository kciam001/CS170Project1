#include "Node.h"

class Tree
{
     private:
     Node* root;
     Node* curr;

     public:
     Tree(Node*);
     void buildTree();
     void printRoot();
};