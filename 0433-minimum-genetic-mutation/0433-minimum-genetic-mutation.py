class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        
        bank.append(start)
        
        gene_dict = defaultdict(list)
        for gene in bank:
            for i in range(len(gene)):
                tmp = gene[:i] + "*" + gene[i+1:]
                gene_dict[tmp].append(gene)
                
        visited = set([start])
        q = Deque([start])
        
        count = 0
        while q:
            for i in range(len(q)):
                gene = q.popleft()
                if gene == end:
                    return count
                
                for i in range(len(gene)):
                    tmp = gene[:i] + "*" + gene[i+1:]
                    for sub_gene in gene_dict[tmp]:
                        if sub_gene not in visited:
                            visited.add(sub_gene)
                            q.append(sub_gene)
                
            count +=1
        return -1