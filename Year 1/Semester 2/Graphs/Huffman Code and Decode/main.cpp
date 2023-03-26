#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <queue>
using namespace std;
ifstream f("in.txt");
ofstream g("out.txt");

struct Node {
	char ch;
	int fr;
	Node* left;
	Node* right;
};

Node* getNode(char ch, int fr, Node* left, Node* right) {
	Node* nod = new Node();
	nod->ch = ch;
	nod->fr = fr;
	nod->left = left;
	nod->right = right;
	return nod;
}

struct comp {
	bool operator()(const Node* n1, const Node* n2) const {
		return n1->fr > n2->fr;
	}
};

bool isLeaf(Node* nod) {
	return nod->left == nullptr && nod->right == nullptr;
}

void encode(Node* nod, string str, unordered_map<char, string>& huffCode) {
	if (nod == nullptr) return;

	if (isLeaf(nod)) huffCode[nod->ch] = (str != "") ? str : "1";

	encode(nod->left, str + "0", huffCode);
	encode(nod->right, str + "1", huffCode);
}

void decode(Node* nod, int &index, string str) {
	if (nod == nullptr) return;

	if (isLeaf(nod)) {
		g << nod->ch;
		return;
	}

	index++;

	if (str[index] == '0') decode(nod->left, index, str);
	else decode(nod->right, index, str);
}

void buildHuffTree(string text) {
	if (text == "") return;

	unordered_map<char, int> freq;
	for (auto ch : text) {
		freq[ch]++;
	}

	priority_queue<Node*, vector<Node*>, comp> pq;
	for (auto pair : freq) {
		pq.push(getNode(pair.first, pair.second, nullptr, nullptr));
	}

	while (pq.size() != 1) {
		Node* n1 = pq.top(); pq.pop();
		Node* n2 = pq.top(); pq.pop();

		auto sum = n1->fr + n2->fr;
		pq.push(getNode('\0', sum, n1, n2));
	}

	Node* root = pq.top();
	unordered_map<char, string> huffCode;
	encode(root, "", huffCode);

	g << "Frequencies:\n ";
	for (auto ch : freq) {
		g << ch.first << " - " << ch.second << '\n';
	}

	g << "Huffman codes:\n";
	for (auto ch : huffCode) {
		g << ch.first << " = " << ch.second << '\n';
	}

	string word;
	g << "Original string: " << text << '\n';
	for (auto str : text) {
		word += huffCode[str];
	}

	g << "Encoded string is: " << word << '\n';
	g << "Decoded string is: ";
	if (isLeaf(root))
	{
		while (root->fr--) {
			cout << root->ch;
		}
	}
	else {
		int index = -1;
		while (index < (int)word.size() - 1) {
			decode(root, index, word);
		}
	}
}

int main() {

	string text;
	while (std::getline(f, text)) {
		buildHuffTree(text);
	}
	f.close();

	return 0;
}