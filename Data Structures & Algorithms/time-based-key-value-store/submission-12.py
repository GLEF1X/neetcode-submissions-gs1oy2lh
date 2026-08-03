class TimeMap:

    def __init__(self):
        self._dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # put it into a dict as [(timestamp, value)]
        container = self._dict[key]
        container.append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        container = self._dict.get(key)
        if not container:
            return ""
        left = 0
        right = len(container) - 1
        result = ""

        while left <= right:
            middle = left + (math.ceil((right - left) / 2))
            probe = container[middle]
            probeTimestamp  = probe[0]

            if probeTimestamp == timestamp:
                return probe[1]
            elif probeTimestamp < timestamp:
                result = probe[1]
                # look for even smaller value
                left = middle + 1
            else:
                right = middle - 1
        
        return result
                
                
            
