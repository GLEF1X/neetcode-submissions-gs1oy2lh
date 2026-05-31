class TrieNode {
    children: Map<string, TrieNode> = new Map();
    isTerminal: boolean = false;
}

class WordDictionary {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    addWord(word: string): void {
        let node = this.root;

        for (let i = 0; i < word.length; i++) {
            const char = word[i];

            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }

            node = node.children.get(char)!;
        }

        node.isTerminal = true;
    }

    search(word: string): boolean {
        const dfs = (node: TrieNode, index: number): boolean => {
            if (index === word.length) {
                return node.isTerminal;
            }

            const char = word[index];

            if (char === ".") {
                for (const child of node.children.values()) {
                    if (dfs(child, index + 1)) {
                        return true;
                    }
                }

                return false;
            }

            const next = node.children.get(char);

            if (!next) {
                return false;
            }

            return dfs(next, index + 1);
        };

        return dfs(this.root, 0);
    }
}