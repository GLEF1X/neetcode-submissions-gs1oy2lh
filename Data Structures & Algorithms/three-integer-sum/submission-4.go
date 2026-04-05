func threeSum(nums []int) [][]int {
    sort.SliceStable(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
    // [-4,-1,-1,0,1,2]
    triplets := make([][]int, 0)
    for i := 0; i < len(nums); i++ {
        // [-4,-1,-1,0,0,0,0,0,1,1,2]
        if i >= 1 && nums[i-1] == nums[i] {
            continue
        }
        leftPtr, rightPtr := i+1, len(nums)-1
        for leftPtr < rightPtr {
            sum := nums[i] + nums[leftPtr] + nums[rightPtr]
            if sum == 0 {
                triplets = append(triplets, []int{nums[i], nums[leftPtr], nums[rightPtr]})
                // [-4,-1,-5,1,2,3,4]
                // [-4,-1,-5,1,1,4,4]
                // [-4,-1,-5,1,2,2,4]

                // [-2,0,0,2,2]
                // [-2,0,0,1,2]
                // is the next number same as current
                for leftPtr < rightPtr && nums[leftPtr] == nums[leftPtr+1] {
                    leftPtr++
                }
                for leftPtr < rightPtr && nums[rightPtr] == nums[rightPtr-1] {
                    rightPtr--
                }

                leftPtr++
                rightPtr--
            } else if sum > 0  {
                // too big
                rightPtr--
            } else {
                leftPtr++
            }
        }
    }
    return triplets
}
// (-1,0,...)
// (-1,1,...)
// (-1,2,...)
// (-1,-1,...)
// (-1,-4, ...)

// (0,1,...)
// (0,2,...)
// (0,-1,...)
// (0,-4,...)
// (1,2, ...)
// (1,-1,...)
// (1,-4,...)

// (2,-1,...)
// (2,-4,...)
// (-1,-4,...)
