class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < temperature:
                indexOfLesserTemperature = stack.pop()
                result[indexOfLesserTemperature] = i - indexOfLesserTemperature

            stack.append(i)

        return result