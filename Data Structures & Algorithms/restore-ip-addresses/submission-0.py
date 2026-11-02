class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        # 255255111235
        curr = []
        result = []

        def backtrack(i):
            if len(curr) > 4:
                return
            if i == len(s) and len(curr) == 4:
                result.append(".".join([str(a) for a in curr]))
                return

            
            for j in range(i, i + 3):
                if j > len(s) - 1:
                    continue
                possibleOctet = s[i:j+1]
                octet = int(possibleOctet)
                if octet > 255 or (len(possibleOctet) > 1 and possibleOctet[0] == "0"):
                    continue

                curr.append(octet)
                backtrack(j + 1)
                curr.pop()


        backtrack(0)
        return result
