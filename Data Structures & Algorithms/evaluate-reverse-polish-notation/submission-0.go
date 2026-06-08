func evalRPN(tokens []string) int {
    ops := map[string]func(a, b int) int{
        "+": func(a, b int) int { return a + b },
        "-": func(a, b int) int { return a - b },
        "*": func(a, b int) int { return a * b },
        "/": func(a, b int) int { return a / b },
    }

    stack := []string{}
    for i := 0; i < len(tokens); i++ {
        currToken := tokens[i]
        if opFunc, ok := ops[currToken]; ok {
            operand1, operand2 := stack[len(stack) - 2], stack[len(stack) - 1]
            stack = stack[:len(stack) - 2]
            
            operand1AsInteger, _ := strconv.ParseInt(operand1, 10, 64)
            operand2AsInteger, _ := strconv.ParseInt(operand2, 10, 64)
            result := opFunc(int(operand1AsInteger), int(operand2AsInteger))
            stack = append(stack, strconv.FormatInt(int64(result), 10))

            fmt.Println(result, stack, operand1AsInteger, operand2AsInteger, currToken)
            continue
        }
        stack = append(stack, currToken)
    }

    resParsed, _ := strconv.ParseInt(stack[0], 10, 64)
    return int(resParsed)
}