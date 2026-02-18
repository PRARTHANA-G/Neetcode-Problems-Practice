class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if string t is a valid anagram of string s.
        An anagram must have the exact same characters in the exact same quantities.
        
        Time Complexity: O(N) where N is the length of the strings.
        Space Complexity: O(K) where K is the number of unique characters.
        """
        
        # 1. The Quick Fail
        # If the strings are different lengths, it is physically impossible 
        # for them to be anagrams. We can exit immediately to save time.
        if len(s) != len(t):
            return False
            
        # 2. The Scoreboard
        # We use a dictionary to keep a running tally of character counts.
        freq = {}
        
        # 3. The Tug-of-War
        # We loop through both strings at the exact same time using the index 'i'.
        for i in range(len(s)):
            
            # For string 's', we ADD 1 to the character's score.
            # .get(character, 0) means: "Get the current score, but if the 
            # character isn't in the dictionary yet, start its score at 0."
            freq[s[i]] = freq.get(s[i], 0) + 1
            
            # For string 't', we SUBTRACT 1 from the character's score.
            freq[t[i]] = freq.get(t[i], 0) - 1
            
        # 4. The Verification
        # If the strings are perfect anagrams, every single +1 from 's' 
        # will be perfectly canceled out by a -1 from 't'.
        # We loop through all the final scores in our dictionary.
        for count in freq.values():
            # If we find ANY score that isn't exactly 0, the strings are not anagrams.
            if count != 0:
                return False
                
        # If we made it through the whole loop without finding any non-zero 
        # scores, the strings are perfect anagrams!
        return True

# ==========================================
# Execution Block (For Testing)
# ==========================================
if __name__ == "__main__":
    # Create an instance of our Solution class
    solver = Solution()
    
    # Test Case 1: Standard Anagram (Should be True)
    word1 = "anagram"
    word2 = "nagaram"
    print(f"Are '{word1}' and '{word2}' anagrams? -> {solver.isAnagram(word1, word2)}")
    
    # Test Case 2: Your test case (Should be False)
    word1 = "jam"
    word2 = "jar"
    print(f"Are '{word1}' and '{word2}' anagrams? -> {solver.isAnagram(word1, word2)}")

    # Test Case 3: Different Lengths (Should be False)
    word1 = "apple"
    word2 = "app"
    print(f"Are '{word1}' and '{word2}' anagrams? -> {solver.isAnagram(word1, word2)}")
    
    # Test Case 4: Same letters, different quantities (Should be False)
    word1 = "aacc"
    word2 = "ccac"
    print(f"Are '{word1}' and '{word2}' anagrams? -> {solver.isAnagram(word1, word2)}")