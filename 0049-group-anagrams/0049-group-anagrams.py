from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string and use it as a tuple key
            anagram_map[tuple(sorted(s))].append(s)
            
        return list(anagram_map.values())