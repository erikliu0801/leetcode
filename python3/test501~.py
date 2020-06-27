# 501
def findMode(root):
    pass


# 504
def convertToBase7(num):
    negative = False
    if num < 0:
        negative = True
        num = abs(num)
    elif num == 0:
        return '0'
    import math
    digits = int(math.log(num, 7))
    sevenbasenum = ''
    while digits != -1:
        sevenbasenum = sevenbasenum + str(num // (7 ** digits))
        num = num % (7 ** digits)
        digits -= 1
    if negative:
        return '-' + sevenbasenum
    return sevenbasenum


# 507
def checkPerfectNumber(num):
    divisors = set([1])
    import math
    divisor = int(math.sqrt(num))
    while divisor != 1:
        if num % divisor == 0:
            divisors.add(divisor)
            divisors.add(num // divisor)
        divisor -= 1
    divisors.discard(num)
    return num == sum(divisors)


# 509
def fib(N):
    if N < 1:
        return 0
    elif N == 1:
        return 1
    else:
        return fib(N - 1) + fib(N - 2)


def main509():
    for i in range(1, 31):
        print(fib(i))


# 532
def findPairs(nums, k):
    s = set(nums)
    count = 0
    if k > 0:
        for e in s:
            if e + k in s:
                count += 1
    elif k == 0:
        for e in s:
            if nums.count(e) > 1:
                count += 1
    return count


def main532():
    input_nums = [[3, 1, 4, 1, 5], [1, 2, 3, 4, 5], [1, 3, 1, 5, 4], [1, 3, 1, 5, 4, 1, 1]]
    input_k = [2, 1, 0, 0]
    expected_output = [2, 4, 1, 1]
    for i in range(len(input_nums)):
        if findPairs(input_nums[i], input_k[i]) != expected_output[i]:
            print(
            "Wrong!!!", ' Output:', findPairs(input_nums[i], input_k[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(findPairs(input_nums[-1], input_k[-1]))

# 599
def findRestaurant(list1, list2):
    res = []
    common = set(list1) & set(list2)
    common_priority = {}
    for r in common:
        common_priority[r] = list1.index(r) + list2.index(r)
    first = min(common_priority.values())
    for r, p in common_priority.items():
        if p == first: res.append(r)
    return res


def main599():
    input_list1 = [["Shogun", "Tapioca Express", "Burger King", "KFC"],
                   ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                   ["Shogun", "Tapioca Express", "Burger King", "KFC"]]
    input_list2 = [["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
                   ["KFC", "Shogun", "Burger King"], ["KFC", "Burger King", "Tapioca Express", "Shogun"]]
    expected_output = [["Shogun"], ["Shogun"], ["KFC", "Burger King", "Tapioca Express", "Shogun"]]
    for i in range(len(input_list1)):
        if findRestaurant(input_list1[i], input_list2[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', findRestaurant(input_list1[i], input_list2[i]), '; Expected Output:',
                  expected_output[i])
        else:
            print("Right")
    print(findRestaurant(input_list1[-1], input_list2[-1]))


# 605
def canPlaceFlowers(flowerbed, n):
    rest_place = []
    max_added_flowers = 0
    existed_flowers = flowerbed.count(1)
    while flowerbed:
        if flowerbed[0] == 1:
            flowerbed = flowerbed[2:]
            existed_flowers -= 1
            continue
        if existed_flowers > 0:
            rest_place.append(flowerbed[:flowerbed.index(1) - 1])
            flowerbed = flowerbed[flowerbed.index(1) + 2:]
            existed_flowers -= 1
        else:
            rest_place.append(flowerbed)
            break
    for place in rest_place:
        max_added_flowers += (len(place) + 1) // 2
    return n <= max_added_flowers


def main605():
    input_flowerbed = [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 0, 1],
                       [1, 0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0]]
    input_n = [1, 2, 1, 1, 1, 2]
    expected_output = [True, False, False, False, True, True]
    for i in range(len(input_flowerbed)):
        if canPlaceFlowers(input_flowerbed[i], input_n[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', canPlaceFlowers(input_flowerbed[i], input_n[i]), '; Expected Output:',
                  expected_output[i])
        else:
            print("Right")


# 	print(canPlaceFlowers(input_flowerbed[-1], input_n[-1]))

# 633
def judgeSquareSum(c):
    import math
    limit = math.sqrt(2) / 2
    for a in range(int(c * limit) + 1):
        if a**2 >= c: break
        if math.sqrt(abs(c - a ** 2)) % 1 == 0: return True
    return False


def main633():
    input1 = [5, 3, 4]
    expected_output = [True, False, True]
    for i in range(len(input1)):
        if judgeSquareSum(input1[i]) != expected_output[i]:
            print("Wrong!!!,  Output:", judgeSquareSum(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    print(judgeSquareSum(input1[-1]))


# 643
def findMaxAverage(nums, k):
    if k == 1: return max(nums)
    max_sum = sum(nums[:k]) / k
    rest_prob = len(nums) - k
    mean = max_sum
    for i in range(rest_prob):
        mean += (nums[k + i] - nums[i]) / k
        max_sum = max(max_sum, mean)
    return max_sum


def main643():
    input_nums = [[1, 12, -5, -6, 50, 3]]
    input_k = [4]
    expected_output = [12.75]
    for i in range(len(input_nums)):
        if findMaxAverage(input_nums[i], input_k[i]) != expected_output[i]:
            print(
            "Wrong!!!", ' Output:', findMaxAverage(input_nums[i], input_k[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(findMaxAverage(input_nums[-1], input_k[-1]))

# 645
def findErrorNums(nums):
    repetition = []
    missing = []
    nums.sort()
    pre = 0
    for c in nums:
        if c != pre + 1:
            if c == pre:
                if c not in repetition:
                    repetition.append(c)
                continue
            else:
                while pre + 1 != c:
                    pre += 1
                    missing.append(pre)
        pre = c
    return repetition + missing


def main645():
    input1 = [[1, 2, 2, 4], [1, 2, 2, 2, 4], [1, 2, 2, 2, 5]]
    expected_output = [[2, 3], [2, 3], [2, 3, 4]]
    for i in range(len(input1)):
        if findErrorNums(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', findErrorNums(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    print(findErrorNums(input1[-1]))


# 665
def checkPossibility(nums):
    nums0 = nums.copy()
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            nums[i - 1] = nums[i]
            new_nums_sorted = nums.copy()
            new_nums_sorted.sort()
            nums0[i] = nums0[i - 1]
            new_nums0_sorted = nums0.copy()
            new_nums0_sorted.sort()
            return nums == new_nums_sorted or nums0 == new_nums0_sorted
    return True


def main665():
    input_nums = [[1, 2, 3], [4, 2, 3], [4, 2, 1], [3, 4, 2, 3], [2, 3, 3, 2, 4]]
    expected_output = [True, True, False, False, True]
    for i in range(len(input_nums)):
        if checkPossibility(input_nums[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', checkPossibility(input_nums[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# 	print(checkPossibility(input_nums[-1]))

# 674
def findLengthOfLCIS(nums):
    if len(nums) < 2:
        return len(nums)
    count = 1
    nums_count = []
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
            if i == len(nums) - 1:
                nums_count.append(count)
        else:
            nums_count.append(count)
            count = 1
    return max(nums_count)


def main674():
    input_nums = [[1, 3, 5, 4, 7], [2, 2, 2, 2, 2], [1, 3, 5, 7]]
    expected_output = [3, 1, 4]
    for i in range(len(input_nums)):
        if findLengthOfLCIS(input_nums[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', findLengthOfLCIS(input_nums[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(findLengthOfLCIS(input_nums[-1]))


# 680
def validPalindrome(s):
    if s == s[::-1]: return True
    i = 0
    while i <= len(s) // 2:
        if s[i] != s[-1 - i]:
            s1 = s[:i] + s[i + 1:]
            s2 = s[:-1 - i] + s[len(s) - i:]
            return s1 == s1[::-1] or s2 == s2[::-1]
        i += 1


def main680():
    input_s = ["abccba", "dabccba", "abccbad", "dabcdfcba"]
    expected_output = [True, True, True, False]
    for i in range(len(input_s)):
        if validPalindrome(input_s[i]) != expected_output[i]:
            print("Wrong!!! Output:", validPalindrome(input_s[i]))
        else:
            print("Right")


# 	print(validPalindrome(input_s[2]))

# 717
def isOneBitCharacter(bits):
    cd = False
    for bit in bits[:-1]:
        if cd:
            cd = False
            continue
        if bit == 1:
            cd = True
    return not cd


def main717():
    input_bits = [[1, 0, 0], [1, 1, 1, 0], [0], [1, 0], [0, 0]]
    expected_output = [True, False, True, False, True]
    for i in range(len(input_bits)):
        if isOneBitCharacter(input_bits[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', isOneBitCharacter(input_bits[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# 	print(isOneBitCharacter(input_bits[1]))

# 720
def longestWord(words):
    words.sort(reverse=True)
    res = []
    alph = []
    longest = 0
    for w in words:
        if len(w) == 1:
            alph.append(w)
        if longest > len(w):
            continue
        for j in range(1, len(w)):
            if w[:j] not in words:
                break
            if j == len(w) - 1:
                res.append(w)
                longest = len(w)
    if res:
        return res[-1]
    elif alph:
        return alph[-1]
    else:
        return ''


def main720():
    input1 = [["w", "wo", "wor", "worl", "world"],
              ["a", "banana", "app", "appl", "ap", "apply", "apple"],
              ["b", "br", "bre", "brea", "break", "breakf", "breakfa", "breakfas", "breakfast", "l", "lu", "lun",
               "lunc", "lunch", "d", "di", "din", "dinn", "dinne", "dinner"],
              ["ts", "e", "x", "pbhj", "opto", "xhigy", "erikz", "pbh", "opt", "erikzb", "eri", "erik", "xlye", "xhig",
               "optoj", "optoje", "xly", "pb", "xhi", "x", "o"]]
    expected_output = ["world", "apple", "breakfast", "e"]
    for i in range(len(input1)):
        if longestWord(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', longestWord(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    print(longestWord(input1[-1]))


# 724
def pivotIndex(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]): return i
    return -1


def main724():
    input_nums = [[1, 7, 3, 6, 5, 6], [1, 2, 3], [1, 2, -2]]
    expected_output = [3, -1, 0]
    for i in range(len(input_nums)):
        if pivotIndex(input_nums[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', pivotIndex(input_nums[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    #print(pivotIndex(input_nums[-1]))

#728
def selfDividingNumbers(left, right):
    res = []
    for i in range(left, right +1):
        sdnum = True
        for j in str(i):
            if j == '0' or i % int(j) != 0:
                sdnum = False
                break
        if sdnum: res.append(i)
    return res

def main728():
    input1 = [1]
    input2 = [22]
    expected_output = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]]
    for i in range(len(input1)):
        if selfDividingNumbers(input1[i], input2[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', selfDividingNumbers(input1[i], input2[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
	# print(selfDividingNumbers(input1[-1], input2[-1]))

# 744
def nextGreatestLetter(letters, target):
    t_num = ord(target)
    close_num = float('inf')
    smallest_num = float('inf')
    for c in letters:
        c_num = ord(c)
        if c_num > t_num and c_num < close_num:
            close_num = c_num
        if c_num < smallest_num:
            smallest_num = c_num
    if close_num != float('inf'):
        return chr(close_num)
    return chr(smallest_num)


def main744():
    input_letters = [["c", "f", "j"], ["c", "f", "j"], ["c", "f", "j"], ["c", "f", "j"], ["c", "f", "j"],
                     ["c", "f", "j"]]
    inpurt_target = ["a", "c", "d", "g", "j", "k"]
    expected_output = ["c", "f", "f", "j", "c", "c"]
    for i in range(len(input_letters)):
        if nextGreatestLetter(input_letters[i], inpurt_target[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', nextGreatestLetter(input_letters[i], inpurt_target[i]), '; Expected Output:',
                  expected_output[i])
        else:
            print("Right")


# print(nextGreatestLetter(input_letters[-1], inpurt_target[-1]))

# 747
def dominantIndex(nums):
    a = max(nums)
    i = nums.index(a)
    nums.remove(a)
    return i if a >= (max(nums) * 2) else -1


def main747():
    input_nums = [[3, 6, 1, 0], [1, 2, 3, 4], [0, 0, 0, 1]]
    expected_output = [1, -1, 3]
    for i in range(len(input_nums)):
        if dominantIndex(input_nums[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', dominantIndex(input_nums[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(dominantIndex(input_nums[0]))

# 748
def shortestCompletingWord(licensePlate, words):
    licensePlate = licensePlate.lower()
    alph = set([chr(x) for x in range(97, 123)])
    truely = ''
    for c in licensePlate:
        if c in alph:
            truely += c

    res = []
    shortest = float('inf')
    from collections import Counter
    t = Counter(truely)
    for w in words:
        if not (t - Counter(w.lower())) and shortest > len(w):
            res.append(w)
            shortest = len(w)
    for w in res:
        if len(w) == shortest: return w


def main748():
    input1 = ["1s3 PSt", "1s3 456"]
    input2 = [["step", "steps", "stripe", "stepple"], ["looks", "pest", "stew", "show"]]
    expected_output = ["steps", "pest"]
    for i in range(len(input1)):
        if shortestCompletingWord(input1[i], input2[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', shortestCompletingWord(input1[i], input2[i]), '; Expected Output:',
                  expected_output[i])
        else:
            print("Right")


# print(shortestCompletingWord(input1[-1], input2[-1]))

# 766
def isToeplitzMatrix(matrix):
    array = []
    for i, arr in enumerate(matrix):
        if i == 0:
            array = arr
            continue
        for j, val in enumerate(arr):
            if j == 0:
                array.insert(0, val)
                continue
            if array[j] != val: return False
    return True


def main766():
    input_matrix = [
        [[1, 2, 3, 4],
         [5, 1, 2, 3],
         [9, 5, 1, 2]],
        [[1, 2],
         [2, 2]]]
    expected_output = [True, False]
    for i in range(len(input_matrix)):
        if isToeplitzMatrix(input_matrix[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', isToeplitzMatrix(input_matrix[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(isToeplitzMatrix(input_matrix[-1]))

# 804
def uniqueMorseRepresentations(words):
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alph = [chr(x) for x in range(97, 123)]
    m_a = {alph[i]: morse[i] for i in range(26)}
    morse_strs = []
    for word in words:
        morse_str = ''
        for w in word.lower():
            morse_str += m_a[w]
        morse_strs.append(morse_str)
    return len(set(morse_strs))


def main804():
    input_words = [["gin", "zen", "gig", "msg"]]
    expected_output = [2]
    for i in range(len(input_words)):
        if uniqueMorseRepresentations(input_words[i]) != expected_output[i]:
            print("Wrong!!!")
            print(uniqueMorseRepresentations(input_words[i]))
        else:
            print("Right")


# print(uniqueMorseRepresentations(input_words[-1]))

# 811
def subdomainVisits(cpdomains):
    subdomains_cp = {}
    for cp_domain in cpdomains:
        cp, domain = cp_domain.split(' ')
        cp = int(cp)
        sub = domain.split('.')
        for i in range(len(sub)):
            subdomain = '.'.join(sub[i:])
            if subdomain not in subdomains_cp:
                subdomains_cp[subdomain] = cp
            else:
                subdomains_cp[subdomain] += cp
    res = []
    for subdomain, cp in subdomains_cp.items():
        res.append(''.join([str(cp), ' ', subdomain]))
    return res


def main811():
    input1 = [["9001 discuss.leetcode.com"], ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]]
    expected_output = [["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"],
                       ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org",
                        "1 intel.mail.com", "951 com"]]
    for i in range(len(input1)):
        if subdomainVisits(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', subdomainVisits(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    print(subdomainVisits(input1[-1]))


# 819
def mostCommonWord(paragraph, banned):
    from collections import Counter
    alph = [chr(x) for x in range(97, 123)]
    words = []
    word = ''
    for w in paragraph:
        if w.lower() in alph:
            word += w.lower()
        elif word != '':
            words.append(word)
            word = ''
    if word != '':
        words.append(word)
    frequence = Counter(words)
    while frequence:
        frequentest, _ = frequence.most_common(1)[0]
        if frequentest not in banned:
            return frequentest
        frequence.pop(frequentest)
    return ''


def main819():
    input_paragraph = ["Bob hit a ball, the hit BALL flew far after it was hit.", "Bob"]
    input_banned = [["hit"], []]
    expected_output = ["ball", "bob"]
    for i in range(len(input_paragraph)):
        if mostCommonWord(input_paragraph[i], input_banned[i]) != expected_output[i]:
            print("Wrong!!!")
            print(mostCommonWord(input_paragraph[i], input_banned[i]))
        else:
            print("Right")

#821
def shortestToChar(S, C):
    def  mountainNums(num):
        nums = [i for i in(range(1, num//2 + 1))]
        numsRight = nums[::-1]
        if num % 2 == 1:
            nums += [ num//2 + 1 ]
        nums += numsRight
        return nums


    # first part: increase
    Cindex = S.index(C)
    dist = [i for i in range(Cindex, -1, -1)]
    if not S[Cindex+1:]: return dist

    # middle part : first increase then decrease
    step = 0
    for i in range(Cindex+1, len(S)):
        if S[i] == C:
            if step == 0:
                dist += [0]
                continue
            dist += mountainNums(step) + [0]

            step = 0
        else:
            step += 1

    # last part : decrease
    dist += [i for i in range(1, step+1)]
    return dist

def main821():
    S = "loveleetcode"
    C = 'e'

    return shortestToChar(S, C)


# 824
def toGoatLatin(S):
    word = ''
    w_end = ''
    transed_S = ''
    index = 1
    vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    up = set([chr(x) for x in range(65, 91)])
    low = set([chr(x) for x in range(97, 123)])
    for c in (S + ' '):
        if word == '' and w_end == '':
            if c in vowel:
                word = c
            if c in ((up | low) - vowel):
                w_end = c
        elif c in (up | low):
            word += c
        else:
            if word != '' or w_end != '':
                transed_S += word + w_end + 'ma' + ('a' * index)
                index += 1
                word, w_end = '', ''
            transed_S += c
    return transed_S[:-1]


def main824():
    input_S = ["I speak Goat Latin", "The quick brown fox jumped over the lazy dog", "HZ sg L"]
    expected_output = ["Imaa peaksmaaa oatGmaaaa atinLmaaaaa",
                       "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
                       "ZHmaa gsmaaa Lmaaaa"]
    for i in range(len(input_S)):
        if toGoatLatin(input_S[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', toGoatLatin(input_S[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(toGoatLatin(input_S[-1]))

# 830
def largeGroupPositions(S):
    now = ''
    first_p = 0
    count = 0
    position_nums = []
    for i, c in enumerate(S):
        if c != now:
            # record
            if count >= 3: position_nums.append([first_p, i - 1])
            # reset
            now = c
            count = 1
            first_p = i
        else:
            count += 1
    if count >= 3: position_nums.append([first_p, i])
    return position_nums


def main830():
    input_S = ["abbxxxxzzy", "abc", "abcdddeeeeaabbbcd", "aaa"]
    expected_output = [[[3, 6]], [], [[3, 5], [6, 9], [12, 14]], [[0, 2]]]
    for i in range(len(input_S)):
        if largeGroupPositions(input_S[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', largeGroupPositions(input_S[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")

# 840
def numMagicSquaresInside(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])
    if rows < 3 or cols < 3: return 0
    for r in range(rows-2):
        for c in range(cols-2):

            # origin = (r,c)
            r1 = [grid[r][c], grid[r][c+1], grid[r][c+2]]
            r2 = [grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2]]
            r3 = [grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]]
            c1 = [grid[r][c], grid[r+1][c], grid[r+2][c]]
            c2 = [grid[r][c+1], grid[r+1][c+1], grid[r+2][c+1]]
            c3 = [grid[r][c+2], grid[r+1][c+2], grid[r+2][c+2]]
            d1 = [grid[r][c], grid[r+1][c+1], grid[r+2][c+2]]
            d2 = [grid[r][c+2], grid[r+1][c+1], grid[r+2][c]]

            nums = r1 + r2 + r3
            if len(nums) != len(set(nums)): continue
            if sorted(nums) != [i for i in range(1,10)]: continue
            if sum(r1) != 15 or \
               sum(r2) != 15 or \
               sum(r3) != 15 or \
               sum(c1) != 15 or \
               sum(c2) != 15 or \
               sum(c3) != 15 or \
               sum(d1) != 15 or \
               sum(d2) != 15: continue

            count += 1
    return count

def main840():
    grid = [[4,3,8,4],
                   [9,5,1,9],
                   [2,7,6,2]]
    return numMagicSquaresInside(grid)


# 844
def backspaceCompare(S, T):
    def helper(M):
        res = ''
        cd = 0
        for c in M[::-1]:
            if c == '#':
                cd += 1
            elif cd > 0:
                cd -= 1
            else:
                res = c + res
        return res

    return helper(S) == helper(T)


def main844():
    input_S = ["ab#c", "ab##", "a##c", "a#c"]
    input_T = ["ad#c", "c#d#", "#a#c", "b"]
    expected_output = [True, True, True, False]
    for i in range(len(input_S)):
        if backspaceCompare(input_S[i], input_T[i]) != expected_output[i]:
            print(
            "Wrong!!!", ' Output:', backspaceCompare(input_S[i], input_T[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    print(backspaceCompare(input_S[1], input_T[1]))

# 849
def maxDistToClosest(seats):
    def maxDistance(dist):
        if dist % 2 != 0:
            distNums.append(dist//2 + 1)
        else:
            distNums.append(dist//2)

    firstIndex = seats.index(1)
    lastIndex = len(seats) - 1 - seats[::-1].index(1)
    middle = seats[firstIndex + 1: lastIndex]
    distNums = [firstIndex, seats[::-1].index(1)]
    dist = 0 
    for seat in middle:
        if seat == 1:
            maxDistance(dist)
            dist = 0
        else:
            dist += 1
    if dist != 0: maxDistance(dist)
    return max(distNums)

def main849():
    seats = [1,0,0,0,1,0,0,0,0,0,1]
    return maxDistToClosest(seats)

# 859
def buddyStrings(A, B):
    if set(A) != set(B) or len(A) < 2 or len(B) < 2:
        return False
    if A == B:
        from collections import Counter
        a = Counter(A)
        if a.most_common(1)[0][1] >= 2:
            return True
        return False
    a_b = None
    for a, b in zip(A, B):
        if a != b:
            if a_b:
                if a != a_b[1] or b != a_b[0]:
                    return False
            a_b = (a, b)
    if a_b:
        return True
    else:
        return False


def main859():
    input_A = ["ab", "ab", "aa", "aaaaaaabc", ""]
    input_B = ["ba", "ab", 'aa', "aaaaaaacb", "aa"]
    expected_output = [True, False, True, True, False]
    for i in range(len(input_A)):
        if buddyStrings(input_A[i], input_B[i]) != expected_output[i]:
            print(
            "Wrong!!!", ' Output:', buddyStrings(input_A[i], input_B[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")

# 867
def transpose(A):
    rowNum = len(A)
    colNum = len(A[0])
    # trans = [ [0] * rowNum  ] * colNum
    # trans = [ [] ] * colNum # shallow copy issue
    trans = []
    for i in range(colNum):
        trans.append([])
    for ri in range(rowNum):
        for ci in range(colNum):
            trans[ci].append(A[ri][ci])
    return trans

def main867():
    A = [[1,2,3],[4,5,6],[7,8,9]]
    return transpose(A)

#874
def robotSim(commands, obstacles):
    turnRight = {
        "north": "east",
        "south": "west",
        "east": "south",
        "west": "north"
    }
    turnLeft = {
        "north": "west",
        "south": "east",
        "east": "north",
        "west": "south"
    }
    nowDirection = "north"
    pos = [0,0]
    for command in commands:
        if command == -2: # turn left 90 degrees
            nowDirection = turnLeft[nowDirection]

        elif command == -1: #  turn right 90 degrees
            nowDirection = turnRight[nowDirection]

        else: # 1 <= x <= 9
            steps = float('inf')

            if nowDirection == "north":
                for obstacle in obstacles:
                    if  obstacle[0] == pos[0] and \
                        obstacle[1] > pos[1] and \
                        (obstacle[1]-pos[1] -1) < command and \
                        (obstacle[1]-pos[1] -1) < steps:
                        steps = obstacle[1] - pos[1] -1
                if steps == float('inf'): pos[1] += command
                else : pos[1] +=  steps

            elif nowDirection == "south":
                for obstacle in obstacles:
                    if  obstacle[0] == pos[0] and \
                        obstacle[1] < pos[1] and \
                        (pos[1] - obstacle[1] -1) < command and \
                        (pos[1] - obstacle[1] -1) < steps:
                        steps = pos[1] - obstacle[1] -1
                if steps == float('inf'): pos[1] -=  command
                else : pos[1] -= steps

            elif nowDirection == "east":
                for obstacle in obstacles:
                    if  obstacle[1] == pos[1] and \
                        obstacle[0] > pos[0] and \
                        (obstacle[0]-pos[0] -1) < command and \
                        (obstacle[0]-pos[0] -1) < steps:
                        steps = obstacle[0] - pos[0] -1
                if steps == float('inf'): pos[0] += command
                else : pos[0] += steps

            elif nowDirection == "west":
                for obstacle in obstacles:
                    if  obstacle[1] == pos[1] and \
                        obstacle[0] < pos[0] and \
                        (pos[0] - obstacle[0] -1) < command and \
                        (pos[0] - obstacle[0] -1) < steps:
                        steps = pos[0] - obstacle[0] -1
                if steps == float('inf'): pos[0] -= command
                else : pos[0] -= steps
    
    return pos[0]**2 + pos[1]**2

def main874():
    commands = [[4,-1,4,-2,4], [1,2,-2,5,-1,-2,-1,8,3,-1,9,4,-2,3,2,4,3,9,2,-1,-1,-2,1,3,-2,4,1,4,-1,1,9,-1,-2,5,-1,5,5,-2,6,6,7,7,2,8,9,-1,7,4,6,9,9,9,-1,5,1,3,3,-1,5,9,7,4,8,-1,-2,1,3,2,9,3,-1,-2,8,8,7,5,-2,6,8,4,6,2,7,2,-1,7,-2,3,3,2,-2,6,9,8,1,-2,-1,1,4,7]]
    obstacles = [[[2,4]], [[-57,-58],[-72,91],[-55,35],[-20,29],[51,70],[-61,88],[-62,99],[52,17],[-75,-32],[91,-22],[54,33],[-45,-59],[47,-48],[53,-98],[-91,83],[81,12],[-34,-90],[-79,-82],[-15,-86],[-24,66],[-35,35],[3,31],[87,93],[2,-19],[87,-93],[24,-10],[84,-53],[86,87],[-88,-18],[-51,89],[96,66],[-77,-94],[-39,-1],[89,51],[-23,-72],[27,24],[53,-80],[52,-33],[32,4],[78,-55],[-25,18],[-23,47],[79,-5],[-23,-22],[14,-25],[-11,69],[63,36],[35,-99],[-24,82],[-29,-98],[-50,-70],[72,95],[80,80],[-68,-40],[65,70],[-92,78],[-45,-63],[1,34],[81,50],[14,91],[-77,-54],[13,-88],[24,37],[-12,59],[-48,-62],[57,-22],[-8,85],[48,71],[12,1],[-20,36],[-32,-14],[39,46],[-41,75],[13,-23],[98,10],[-88,64],[50,37],[-95,-32],[46,-91],[10,79],[-11,43],[-94,98],[79,42],[51,71],[4,-30],[2,74],[4,10],[61,98],[57,98],[46,43],[-16,72],[53,-69],[54,-96],[22,0],[-7,92],[-69,80],[68,-73],[-24,-92],[-21,82],[32,-1],[-6,16],[15,-29],[70,-66],[-85,80],[50,-3],[6,13],[-30,-98],[-30,59],[-67,40],[17,72],[79,82],[89,-100],[2,79],[-95,-46],[17,68],[-46,81],[-5,-57],[7,58],[-42,68],[19,-95],[-17,-76],[81,-86],[79,78],[-82,-67],[6,0],[35,-16],[98,83],[-81,100],[-11,46],[-21,-38],[-30,-41],[86,18],[-68,6],[80,75],[-96,-44],[-19,66],[21,84],[-56,-64],[39,-15],[0,45],[-81,-54],[-66,-93],[-4,2],[-42,-67],[-15,-33],[1,-32],[-74,-24],[7,18],[-62,84],[19,61],[39,79],[60,-98],[-76,45],[58,-98],[33,26],[-74,-95],[22,30],[-68,-62],[-59,4],[-62,35],[-78,80],[-82,54],[-42,81],[56,-15],[32,-19],[34,93],[57,-100],[-1,-87],[68,-26],[18,86],[-55,-19],[-68,-99],[-9,47],[24,94],[92,97],[5,67],[97,-71],[63,-57],[-52,-14],[-86,-78],[-17,92],[-61,-83],[-84,-10],[20,13],[-68,-47],[7,28],[66,89],[-41,-17],[-14,-46],[-72,-91],[4,52],[-17,-59],[-85,-46],[-94,-23],[-48,-3],[-64,-37],[2,26],[76,88],[-8,-46],[-19,-68]]]
    expected_output = [65, 5140]
    for i in range(len(commands)):
        if robotSim(commands[1], obstacles[1]) != expected_output[i]:
            print("Wrong!!!", ' Output:', robotSim(commands[i], obstacles[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")

# 917
def reverseOnlyLetters(S):
    i_c = {}
    up = set([chr(x) for x in range(65, 91)])
    low = set([chr(x) for x in range(97, 123)])
    reversed_nums = list()
    for i, c in enumerate(S):
        if c in (up | low):
            reversed_nums.append(c)
        else:
            i_c[i] = c
    reversed_nums.reverse()
    for i in i_c:
        reversed_nums.insert(i, i_c[i])
    reversed_S = ''
    for c in reversed_nums: reversed_S += c
    return reversed_S


def main917():
    input_S = ["ab-cd", "a-bC-dEf-ghIj", "Test1ng-Leet=code-Q!"]
    expected_output = ["dc-ba", "j-Ih-gfE-dCba", "Qedo1ct-eeLg=ntse-T!"]
    for i in range(len(input_S)):
        if reverseOnlyLetters(input_S[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', reverseOnlyLetters(input_S[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(reverseOnlyLetters(input_S[-1]))

# 922
def sortArrayByParityII(A):
    odd = []
    even = []
    for i, c in enumerate(A):
        if (i % 2 == 0) and (c % 2 != 0):
            A[i] = True  # even
            odd.append(c)
        elif (i % 2 == 1) and (c % 2 != 1):
            A[i] = False  # odd
            even.append(c)
    for i, c in enumerate(A):
        if c is False:
            A[i] = odd.pop()
        elif c is True:
            A[i] = even.pop()
    return A


def main922():
    print(sortArrayByParityII([4, 2, 5, 7]))


# 925
def isLongPressedName(name, typed):
    if name == typed: return True
    if set(name) != set(typed): return False
    last = ''
    j = 0
    for i, nc in enumerate(name):
        while j < len(typed):
            if typed[j] == nc:
                j += 1
                break
            elif typed[j] == last:
                j += 1
            else:
                return False
        if i < len(name) and j == len(typed) and typed[j - 1] != nc: return False  #
        last = nc
    rest = set(typed[j:])
    if rest:
        if len(rest) > 1: return False
        return True if last in rest else False
    return True


def main925():
    input_name = ["alex", "saeed", "leelee", "laiden", "kikcxmvzi", "izi"]
    input_typed = ["aaleex", "ssaaedd", "lleeelee", "laiden", "kiikcxxmmvvzz", "izz"]
    expected_output = [True, False, True, True, False, False]
    for i in range(len(input_name)):
        if isLongPressedName(input_name[i], input_typed[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', isLongPressedName(input_name[i], input_typed[i]), '; Expected Output:',
                  expected_output[i])
        else:
            print("Right")


# 	print(isLongPressedName(input_name[-1], input_typed[-1]))

# 929
def numUniqueEmails(emails):
    local_name = ''
    uniqe_emails = set()
    for email in emails:
        for i, c in enumerate(email):
            if c == '.':
                continue
            elif c == '+':
                uniqe_emails.add(local_name + email[email.index('@'):])
                local_name = ''
                break
            elif c == '@':
                uniqe_emails.add(local_name + email[i:])
                local_name = ''
                break
            else:
                local_name += c
    return len(uniqe_emails)


def main929():
    input_emails = [
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]]
    expected_output = [2]
    for i in range(len(input_emails)):
        if numUniqueEmails(input_emails[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', numUniqueEmails(input_emails[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(numUniqueEmails(input_emails[-1]))

# 976
def largestPerimeter(A):
    A.sort(reverse=True)
    for i in range(len(A) - 2):
        if A[i] < A[i + 1] + A[i + 2]:
            return sum(A[i:i + 3])
    return 0


def main976():
    input_A = [[2, 1, 2], [1, 2, 1], [3, 2, 3, 4], [3, 6, 2, 3]]
    expected_output = [5, 0, 10, 8]
    for i in range(len(input_A)):
        if largestPerimeter(input_A[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', largestPerimeter(input_A[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(largestPerimeter(input_A[-1]))

# 1025
def divisorGame(N):
    def helper(M):
        if M == 1: return 1
        devisors = set()
        import math
        for i in range(1, int(math.sqrt(M)) + 1):
            if (i < M) and (M // i != 0) and (M % i == 0):
                devisors.add(i)
                if M // i < M:
                    devisors.add(M // i)
        return M - max(devisors)

    chalkboard = [N]
    while N > 1:
        N = helper(N)
        chalkboard.append(N)
    if chalkboard.index(1) % 2 == 1:
        return False
    return True


def main1025():
    input1 = [1, 2, 3, 4, 5]
    expected_output = [False, True, False, True, False]
    for i in range(len(input1)):
        if divisorGame(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', divisorGame(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    print(divisorGame(input1[1]))


# 1078
def findOcurrences(text, first, second):
    res = []

    t_re = text.split(' ')[::-1]
    if len(t_re) < 3: return res
    for i, w in enumerate(t_re[:-2]):
        if t_re[i + 1] == second and t_re[i + 2] == first:
            res = [w] + res

    return res


def main1078():
    input1 = ["we will we will rock you"]
    input2 = ["we"]
    input3 = ["will"]
    expected_output = [["we", "rock"]]
    for i in range(len(input1)):
        if findOcurrences(input1[i], input2[i], input3[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', findOcurrences(input1[i], input2[i], input3[i]), '; Expected Output:',
                  expected_output[i])
        else:
            print("Right")


# print(findOcurrences(input1[-1], input2[-1], input3[-1]))

# 1122
def relativeSortArray(arr1, arr2):
    arr_front = []
    s1 = set(arr1)
    for c in arr2:
        # if c in arr1:
        arr_front.extend([c] * arr1.count(c))
        s1.remove(c)
    arr_end = []
    for c in s1:
        arr_end.extend([c] * arr1.count(c))
    arr_end.sort()
    return arr_front + arr_end


def main1122():
    input_arr1 = [[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]]
    input_arr2 = [[2, 1, 4, 3, 9, 6]]
    expected_output = [[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]]
    for i in range(len(input_arr1)):
        if relativeSortArray(input_arr1[i], input_arr2[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', relativeSortArray(input_arr1[i], input_arr2[i]), '; Expected Output:',
                  expected_output[i])
        else:
            print("Right")


# print(relativeSortArray(input_arr1[-1], input_arr2[-1]))

# 1337
def kWeakestRows(mat, k):
    row_nums = []
    for row in mat:
        row_nums.append(sum(row))
    row_nums_sort = row_nums.copy()
    row_nums_sort.sort()
    del mat, row
    for i, num in enumerate(row_nums_sort):
        j = row_nums.index(num)
        row_nums_sort[i] = j
        # row_nums[j] = True #####!!!!????
        row_nums[j] = -1
    del i, j, num, row_nums, row_nums_sort[k:]
    return row_nums_sort


def main1337():
    input_mat = [[[1, 1, 0, 0, 0],
                  [1, 1, 1, 1, 0],
                  [1, 0, 0, 0, 0],
                  [1, 1, 0, 0, 0],
                  [1, 1, 1, 1, 1]],
                 [[1, 0, 0, 0],
                  [1, 1, 1, 1],
                  [1, 0, 0, 0],
                  [1, 0, 0, 0]]
                 ]
    input_k = [3, 2]
    expected_output = [[2, 0, 3], [0, 2]]
    for i in range(len(input_mat)):
        if kWeakestRows(input_mat[i], input_k[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', kWeakestRows(input_mat[i], input_k[i]), '; Expected Output:',
                  expected_output[i])
        else:
            print("Right")
    print(kWeakestRows(input_mat[-1], input_k[-1]))


# 1351
def countNegatives(grid):
    count = 0
    row = len(grid[0])
    for col in grid:
        for i, e in enumerate(col):
            if e < 0:
                count += row - i
                break
    return count


def main1351():
    input_grid = [
        [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
        [[3, 2], [1, 0]],
        [[1, -1], [-1, -1]],
        [[-1]]
    ]
    expected_output = [8, 0, 3, 1]
    for i in range(len(input_grid)):
        if countNegatives(input_grid[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', countNegatives(input_grid[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")


# print(countNegatives(input_grid[-1]))

if __name__ == "__main__":
    import time

    t_start = time.time()
    # main532()
    # main599()
    # main633()
    # main645()
    # main720()
    # main728()
    # main748()
    # main811()
    # main821()
    # main840()
    # main844()
    # main849()
    # main867()
    main874()
    # main1025()
    # main1078()
    # main1337()
    # main1351()
    print(time.time() - t_start)


    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

# 504
# print(convertToBase7())

# 507
# print(checkPerfectNumber(28))

# for i in range(1,1000000000):
# 	if checkPerfectNumber(i):
# 		print(i)
