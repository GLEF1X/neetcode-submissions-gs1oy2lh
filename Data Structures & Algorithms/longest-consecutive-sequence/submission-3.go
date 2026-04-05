func longestConsecutive(nums []int) int {
    m := make(map[int]struct{})
    for _, num := range nums {
        m[num] = struct{}{}
    }

    var longestLength int
    for _, num := range nums {
        // does the number have a preceding number
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
