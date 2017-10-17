using namespace std;
#include "Node.h"
#include "Tree.h"
int main()
{



     int initialState[3][3] = {{0}};



     Node* test = new Node(0,0,initialState);

     //test.printState();

     Tree searchSpace(test);

     searchSpace.printRoot();
}