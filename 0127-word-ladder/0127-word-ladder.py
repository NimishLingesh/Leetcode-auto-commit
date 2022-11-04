class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        word_dic = defaultdict(list)
        wordList.insert(0, beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i] + "*" + word[i+1:]
                word_dic[tmp].append(word)
        visited = set([beginWord])
        
        q = Deque([beginWord])
        count = 1
        while(q):
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    tmp = word[:i] + "*" + word[i+1:]
                    for sub_word in word_dic[tmp]:
                        if sub_word not in visited:
                            visited.add(sub_word)
                            q.append(sub_word)
            count += 1
        return 0