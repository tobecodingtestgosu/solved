import sys


def backtracking(idx,vowel_count,consonant_count):
    if vowel_count >= 1 and consonant_count >= 2 and len(cipher) == L:
        print(''.join(cipher))
        return
    for i in range(idx,len(characters)):
        new_vowel_count = vowel_count
        new_consonant_count = consonant_count
        if characters[i] in vowels:
            new_vowel_count+=1
        else:
            new_consonant_count +=1
        cipher.append(characters[i])
        backtracking(i+1,new_vowel_count,new_consonant_count)
        cipher.pop()

if __name__ == "__main__":
  L, C = map(int,sys.stdin.readline().split())
  characters = sorted(list(sys.stdin.readline().rstrip().split()))

  answer = []
  cipher = []

  vowels = ['a', 'e', 'i', 'o', 'u']
  backtracking(0,0,0)





















