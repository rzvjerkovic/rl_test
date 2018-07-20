# Test if the text has balanced brackets
text_to_test = "Blalsa{llsffaslfsalf"
open_brackets = "{[("
closed_brackets = "}])"
bracket_map = { "{" : "}", "[" : "]", "(" : ")" }

def is_balanced(text):
        stack = []
        for char in text_to_test:
                if char in open_brackets:
                        stack.append(char)
                elif char in closed_brackets:
                        try:
                                poped = stack.pop()
                        except:
                                # If no matching open brace on stack, text is not balanced
                                return False
                        else:
                                if char != bracket_map[poped]:
                                        # Braces not balanced
                                        return False
                else:
                        # Non brace char, skip
                        continue

        # If all matched without error and no open braces on stack, text is balanced
        return len(stack) == 0