#include <string>
#include <iostream>
#include <algorithm>
#include <memory.h>

using namespace std;

extern "C" char ** perm(char * txt){
    string str = txt;
    char **ret = (char**) malloc(5 * sizeof(char*));
    int i = 0;
    sort(str.begin(), str.end());

    do {
        ret[i]= strdup(str.c_str());
//        cout << str << endl;
        i++;
    } while (next_permutation(str.begin(), str.end()));

    return ret;
}


int main() {
    return 0;
}