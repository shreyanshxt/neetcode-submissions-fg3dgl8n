class Solution:
    def mergeAlternately(self,word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)
        list1=list(word1)
        list2=list(word2)
        list3=[]
        if len1==len2:
           
            for i in range(len1):
              list3.append(list1[i])
              list3.append(list2[i])

            print(list3)
            merged_word = "".join(list3)
            return merged_word

            # Method 2: Direct return (simpler)
            return "".join(list3)

        elif len1>len2:
            for i in range(len2):
              list3.append(list1[i])
              list3.append(list2[i])
            list3.extend(list1[len2:])
            print(list3)
            merged_word = "".join(list3)
            return merged_word

            # Method 2: Direct return (simpler)
            return "".join(list3)
        else:
            for i in range(len1):
              list3.append(list1[i])
              list3.append(list2[i])
            list3.extend(list2[len1:])
            print(list3)
            merged_word = "".join(list3)
            return merged_word

            # Method 2: Direct return (simpler)
            return "".join(list3)


        