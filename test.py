def lengthOfLongestSubstring(s):
    unrepeated_substring = []
    string_list = list(s)
    substring = ""
    for i, j in enumerate(string_list):
        if substring.count(j) == 0:
            substring = substring + j
        else:
            unrepeated_substring.append(substring)
            substring = j
    unrepeated_substring.append(substring)
    max_count = 0
    for i, j in enumerate(unrepeated_substring):
        x = len(unrepeated_substring[i])
        if x > max_count:
            max_count = x
    return max_count


if __name__ == "__main__":
    string01: str = "abcabcbb"
    string02 = " "
    string03 = "dvdf"
    lengthOfLongestSubstring(string03)
