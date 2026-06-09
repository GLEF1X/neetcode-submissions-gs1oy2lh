class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
		const result = Array.from({length: temperatures.length}).fill(0)
		const stack = []
		for (let i = 0; i < temperatures.length; i++) {
			while (stack.length && temperatures[i] > temperatures[stack.at(-1)]) {
				const index = stack.pop()
				const distance = i - index
				result[index] = distance
			}
			stack.push(i)
		}
		return result
	}
}
