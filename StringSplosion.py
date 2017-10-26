# String  splosion
# Given a non-empty string like "Code" return a string like "CCoCodCode".


# stringSplosion("Code") → "CCoCodCode"
# stringSplosion("abc") → "aababc"
# stringSplosion("ab") → "aab"

# public String stringSplosion(String str) {
#   String result="";
#   int length1 = str.length();
#   for(int i=0;i<length1;i++)
#   {
#    result = result+str.substring(0,i+1);
#   }
#   return result;
# }


def string_splosion(str):
  result=""
  for i in range(0,len(str)):
    result=result+str[0:i+1]
  return result

str=raw_input()
result=string_splosion(str)
print result