class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [4, -4]
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            asteriod = asteroids[i]
            # signs are different meaning it collides
            if stack and stack[-1] >= 0 and asteriod <= 0:
                while stack and stack[-1] >= 0 and asteriod <= 0:
                    if abs(asteriod) > abs(stack[-1]):
                        stack.pop()
                        if not stack or stack[-1] < 0: 
                            stack.append(asteriod)
                    elif abs(stack[-1]) == abs(asteriod):
                        # collide and destroy each other
                        stack.pop()
                        # the processed asteriod is gone
                        break
                    else:
                        # the asteriod on the stack survived
                        break
            else:
                stack.append(asteriod)
        
            
        return stack

