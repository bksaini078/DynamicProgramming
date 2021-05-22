import sys
def MinWindowSubstring(strArr):
  str1= strArr[0]
  str2=strArr[1]
  str_t=str2
  substr=''
  min_len=sys.maxsize
  for i in range(len(str1)):
    str_t=str2
    for j in range(i, len(str1)):
      if str1[j] in str_t:
        str_t=str_t.replace(str1[j],'',1)
        # print(str_t)
      if len(str_t)==0:
        if len(str1[i:j+1])< min_len:
          min_len= len(str1[i:j+1])
          # print(str1[i:j+1])
          substr=(str1[i:j+1])
  return substr
# keep this function call here
if __name__=='__main__':
    strarr=["aaffhkksemckelloe", "fhea"]
    print(MinWindowSubstring(strarr))