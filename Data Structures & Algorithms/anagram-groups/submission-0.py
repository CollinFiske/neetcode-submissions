class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = collections.defaultdict(list)

        for s in strs:
            sortedStr = "".join(sorted(s))
            anagram_map[sortedStr].append(s)

        return list(anagram_map.values())


