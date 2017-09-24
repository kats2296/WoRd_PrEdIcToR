#include <pthread.h>
#include <stdio.h>
#include <cstdlib>
#include<fstream>
#include<iostream>
#include <stdlib.h>
#include<string>
#include <stdio.h>
#include <stdlib.h>
#define NUM_THREADS	5
#define ALPHA_SIZE	26

using namespace std;

typedef struct trie_node
{
    struct trie_node *children[ALPHA_SIZE];
    int frequency;
    int isLeaf;
}trie;

trie *getnode();
void insert(trie * , string);

int char_to_index(char );

void frequency_display(trie * ,string);

int search(trie * , string);

int char_to_index(char c)
{
    int index;
    index = (int)c - (int)'a';

    return index;
}

void *ScanFile(void *root)
{
    trie *tid;
    tid = (trie *)root;
    printf("File Scanning by thread :\t1\n");

   ifstream rd;
	rd.open("sampletest.txt");

    string data;
 
	int k=0;

    string previousLine="";


    while(!rd.eof()) // To get you all the lines.
    {
        getline(rd,data); // Saves the line in STRING.
        if (data != previousLine)
        {
      		k++;
            previousLine=data;
	    insert(tid,data);
            //cout<<data<<endl; // Prints our STRING.
        }
	   //readfile>>data;

    }
	//cout<<"Done! Total Words: "<<k<<endl<<endl;
    rd.close();
    pthread_exit(NULL);
}


int main(int argc, char *argv[])
{
    pthread_t threads[NUM_THREADS];
    int rc;
    long t=1;
    trie *root = getnode();
    rc = pthread_create(&threads[t], NULL, ScanFile, (void *)root );
    if (rc)   
      {
            printf("ERROR; return code from pthread_create() is %d\n", rc);
            exit(-1);
       }
	
     string word_srch;
    cout<<"\n Enter the word you want to search\n";
    cin>>word_srch;

    int get_output=search(root,word_srch);

    if(get_output == 0)
        cout<<"\n WORD NOT FOUND IN TRIE";

    else

        {
            cout<<"\n WORD IS IN TRIE";
            cout<<"  with frequencies:\n";
            frequency_display(root,word_srch);
	}
            return 0;

  pthread_exit(NULL);
}

trie *getnode()
{
    trie *pnode = NULL;
    pnode = new trie;

    if(pnode)
    {
        for(int i=0;i<ALPHA_SIZE;i++)
        {
            pnode->children[i]=NULL;
        }
    }

    return pnode;

}

void insert(trie *root , string word)
{
    //int length = strlen(word);
        int length = word.length();

    int index;

    trie *pcrawl = root;

    for(int i=0;i<length;i++)
    {
        //index=char_to_index(word[i]);
        index=char_to_index(word.at(i));

        if(!pcrawl->children[index])
        {
           pcrawl->children[index]=getnode();

        }

         pcrawl->children[index]->frequency=(pcrawl->children[index]->frequency)+1;
        pcrawl=pcrawl->children[index];
    }

    pcrawl->isLeaf=1;

}

int search(trie *root , string word_srch)
{
    trie *pn = root;
    //int length=strlen(word_srch);
            int length = word_srch.length();

    int index;
    for(int i=0;i<length;i++)
    {
        //index = char_to_index(word_srch[i]);

                index = char_to_index(word_srch.at(i));

        if(!pn->children[index])
            return 0;

        pn=pn->children[index];
    }

    return (pn->isLeaf && pn !=NULL);
}

void frequency_display(trie *root , string word_srch)
{
    trie *pn = root;

    //int length=strlen(word_srch);
    int length=word_srch.length();
    int index;
    for(int i=0;i<length;i++)
    {
        index=char_to_index(word_srch.at(i));
        cout<<"\n"<<pn->children[index]->frequency;
        pn=pn->children[index];
    }

}
