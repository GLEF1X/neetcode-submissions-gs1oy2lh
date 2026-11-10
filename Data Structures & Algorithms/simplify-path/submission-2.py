class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = []
        for i, char in enumerate(path):
            if char == "/" or i == len(path) - 1:
                if i == len(path) - 1 and char != "/":
                    curr.append(char)
                if len(curr) > 1:
                    # prev directory reference
                    if len(curr) == 3 and curr[1] == "." and curr[2] == ".":
                        if stack:
                            # pop prev directory
                            stack.pop()
                    elif len(curr) == 2 and curr[1] == ".":
                        curr.clear()
                    else:
                        stack.append("".join(curr[1:]))

                curr = ["/"]
                continue
            elif char == ".":
                curr.append(".")
                continue
            else:
                curr.append(char)
        
        return "/" + "/".join(stack)