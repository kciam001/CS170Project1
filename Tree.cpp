#include "Tree.h"

Tree::Tree(Node *root)
{
     this->root = root;
}

void Tree::printRoot()
{
     root->printState();
}