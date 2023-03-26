#include <iostream>
#include <fstream>
using namespace std;
ifstream f("date.in");
ofstream g("date.out");
int p[100],n, c[100], nr, v[100], init_l;
int determina_frunza_min(int p[]){
    int gasit;
    for(int i=0;i<init_l;i++)
    {
        if(p[i]!=-2){  //daca nodul mai exista in arbore
            gasit=0;
            for(int j=0;j<init_l;j++)
                if(i==p[j]) gasit=1;
            if(gasit==0)
            return i;
        }
    }
}

void elimina_frunza(int p[], int poz){
    p[poz]=-2; //marcam frunza ca stearsa
    n--;
}

void prufer(){
    while(n>1){
        int x= determina_frunza_min(p);
        //cout<<x<<endl;
        c[nr++]=p[x];
        elimina_frunza(p, x);
    }
}
int main()
{int i,j;
f>>n; init_l=n;
for(i=0;i<n;i++) f>>p[i];
prufer();
g<<nr<<endl;;
for(int i=0;i<nr;i++) g<<c[i]<<" ";
    return 0;
}
