func isPalindrome(s string) bool {
	leftPtr, rightPtr := 0, len(s) - 1

	for leftPtr < rightPtr {
		leftChar, rightChar := s[leftPtr], s[rightPtr]

		if !isAlnum(leftChar) {
			leftPtr++
			continue
		} else if !isAlnum(rightChar) {
			rightPtr--
			continue
		}

		if toLower(leftChar) != toLower(rightChar) {
			return false
		}

		leftPtr++
		rightPtr--
	}

	return true
}


func isAlnum(c byte) bool {
	return (c >= 'A' && c <= 'Z') ||
	       (c >= 'a' && c <= 'z') ||
	       (c >= '0' && c <= '9')
}

func toLower(b byte) byte {
	if b >= 'A' && b <= 'Z' {
		return b + ('a' - 'A')
	}
	return b
}