class PrefixTree {
    #children: Map<string, PrefixTree>
    #isTerminal: boolean;

    constructor(isTerminal: boolean = false) {
        this.#children = new Map()
        this.#isTerminal = isTerminal
    }

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word: string): void {
        let currentTree = this as PrefixTree

        for (let i = 0; i < word.length; i++) {
            const char = word[i]

            let node = currentTree.#children.get(char)

            if (!node) {
                node = new PrefixTree()
                currentTree.#children.set(char, node)
            }

            currentTree = node
        }

        currentTree.#isTerminal = true
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word: string): boolean {
        let currentTree = this as PrefixTree
        for (let i = 0; i < word.length; i++) {
            const char = word[i]
            const isEndOfInput = i === word.length - 1
            let node = currentTree.#children.get(char)
            if (node) {
                if (isEndOfInput && node.#isTerminal) {
                    return true
                }

                currentTree = node
            } else {
                return false
            }
        }

        return false
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix: string): boolean {
        let currentTree = this as PrefixTree
        for (let i = 0; i < prefix.length; i++) {
            const char = prefix[i]
            let node = currentTree.#children.get(char)
            if (!node) {
                return false
            }

            currentTree = node
        }

        return true
    }
}
