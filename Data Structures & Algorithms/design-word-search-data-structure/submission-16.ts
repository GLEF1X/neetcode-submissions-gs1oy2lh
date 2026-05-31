class WordDictionary {
    #map: Map<string, WordDictionary>;
    #isTerminal: boolean;

    constructor() {
        this.#map = new Map();
        this.#isTerminal = false;
    }

    /**
     * @param {string} word
     * @return {void}
     */
    addWord(word: string): void {
        let currCharMap = this.#map;
        for (const [index, letter] of [...word].entries()) {
            const currentLetterDictionary = currCharMap.get(letter);
            const isLastChar = index === word.length - 1;
            if (currentLetterDictionary) {
                if (isLastChar && !currentLetterDictionary.#isTerminal) {
                    // terminate, since we found an appropriate letter
                    // but it's not marked as terminal
                    currentLetterDictionary.#isTerminal = true;
                    currCharMap.set(letter, currentLetterDictionary);
                    continue;
                }
                // go to next letter
                currCharMap = currentLetterDictionary.#map;
                continue;
            }
            // character did not exist in dictionary so we changed it
            const dict = new WordDictionary()
            if (isLastChar) {
                dict.#isTerminal = true
            }
            currCharMap.set(letter, dict);
            currCharMap = dict.#map
        }
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word: string): boolean {
        let currCharMap = this.#map;
        console.log(word, currCharMap)
        for (const [index, letter] of [...word].entries()) {
            const isWildCard = letter === ".";
            const isLastChar = index === word.length - 1;
            if (isWildCard) {
                // since it could be anywhere in any letter of the current letter
                // we have to search all of them, and the cleanest way to do so is recursion
                for (let [letter, dictionary] of currCharMap.entries()) {
                    if (isLastChar && dictionary.#isTerminal) {
                        return true
                    }
                    // does the letter at the current level have an appropriate suffix
                    const suffix = word.slice(index+1)
                    if (dictionary.search(suffix)) {
                        return true
                    }
                }
                break
            } else {
                const currentLetterDictionary = currCharMap.get(letter);
                if (currentLetterDictionary) {
                    if (isLastChar && currentLetterDictionary.#isTerminal) {
                        return true
                    }
                    // go to next letter
                    currCharMap = currentLetterDictionary.#map;
                    continue;
                }
                // we didn't find char, so we return false
                return false
            }
        }

        return false;
    }
}
