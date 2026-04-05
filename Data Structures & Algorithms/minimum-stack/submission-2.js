class MinStack {
    #arr
    #minStack

    constructor() {
        this.#arr = []
        this.#minStack = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.#arr.push(val)
        const topOfMinStack = this.#minStack.at(-1)
        const min = topOfMinStack !== undefined ? Math.min(val, topOfMinStack) : val
        this.#minStack.push(min)
    }

    /**
     * @return {void}
     */
    pop() {
        this.#arr.pop()
        this.#minStack.pop()
    }

    /**
     * @return {number}
     */
    top() {
        return this.#arr[this.#arr.length - 1]
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.#minStack.at(-1);
    }

    // 0 -> min(0,1) = 0 is min
    // 2 -> min(1, 2) = 1 is min
    // 1 -> min(1,nothing) = 1 is min
}
