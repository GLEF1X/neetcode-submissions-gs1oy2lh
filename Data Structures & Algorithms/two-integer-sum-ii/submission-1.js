class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let [leftPtr, rightPtr] = [0, numbers.length - 1]

        while (leftPtr < rightPtr) {
            const [leftNum, rightNum] = [numbers[leftPtr], numbers[rightPtr]]

            const sum = leftNum + rightNum

            if (sum === target) {
                return [leftPtr+1, rightPtr+1]
            } else if (sum < target) {
                leftPtr++
            } else {
                rightPtr--
            }
        }

    }
}
