func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

    m := make(map[int]struct{})
    for _, num := range nums {
        m[num] = struct{}{}        
    }

    var longestLength int
    for _, num := range nums {
        if _, ok := m[num-1]; ok {
            continue
        }

        innerMaxLength := 1
        for {
            _, ok := m[num+1]
            if !ok {
                break
            }
            innerMaxLength++
            num++
        }

        longestLength = max(innerMaxLength, longestLength)

    }

    return longestLength
}
