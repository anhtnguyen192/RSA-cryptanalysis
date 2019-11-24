# hasing a text
def hashing(pl):
        a = pl.split(" ")
        hashCode = []
        for x in a:
            count = 0
            sum = 0
            for i in x:
                sum += (ord(i) - ord('a') + 1) * (26 ** (len(x) - count - 1))
                count += 1
            hashCode.append(sum)
        return hashCode

# unhashing 1 word
def unhashing(n):
        str = ''
        i = 0; 
        while(n != 0): 
            temp = 0; 
            temp = n % 26; 
            s = chr(temp + ord('a') - 1);  
            i = i + 1; 
            n = int(n / 26); 
            str += s
        return str[::-1]
    






            

