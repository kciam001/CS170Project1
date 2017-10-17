#ifndef NODE_H
#define NODE_H
#include <iostream>
using namespace std;
#include <string>
class Node
{
     protected:
     Node * parent;
     int pathCost;
     int state[3][3];
     bool goalState;

     public:
     Node();
     Node(Node* parent, int pathCost, int state[3][3]);
     bool checkGoalState();
     bool moveLeft();
     bool moveUp();
     bool moveRight();
     bool moveDown();
     void printState();
};
#endif