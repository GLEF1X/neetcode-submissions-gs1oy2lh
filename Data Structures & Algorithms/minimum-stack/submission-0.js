class MinStack {
    #arr

    constructor() {
        this.#arr = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.#arr.push(val)
    }

    /**
     * @return {void}
     */
    pop() {
        this.#arr.pop()
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
        return  Math.min.apply(Math, this.#arr);
    }
}
