class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if not len(sentence1) == len(sentence2):
            return False
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue

            similar_pair = False
            for j in range(len(similarPairs)):
                if sentence1[i] in similarPairs[j] and sentence2[i] in similarPairs[j]:
                    similar_pair = True
                    break
            
            if not similar_pair:
                return False
        
        return True