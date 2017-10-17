#include "Node.h"

Node::Node(Node* parent, int pathCost, int state[3][3])
{
     this->parent = parent;
     this->pathCost = pathCost;

     for(unsigned i = 0; i < 3; i++)
     {
          for(unsigned j = 0; j < 3; j++)
          {
               this->state[i][j] = state[i][j];
          }
     }

}

Node::Node()
{

}

void Node::printState()
{
     cout << "-------" << endl;
     for(unsigned i = 0; i < 3; i++)
     {
          cout << "|";
          for(unsigned j = 0; j < 3; j++)
          {
               cout << state[i][j] << "|";
          }
          cout << endl;
     }
     cout << "-------" << endl;
}