# Parsing
# Extract domain name from a URL
# url can start with https, www, or simply domain.com/org
# url can have home, different page
#   To get the correct domain name, know where is the start and end condition
#   start parsing after "www." if exists or "/" if it doesn't
#   end parsing after next dot

def domain_name(url)->str:
    if("www." in url):
        domain = url.split("www.")[1]
        print(domain)
        domain = domain.split(".")[0]
        print(domain)
    elif("http" in url):
        domain = url.split("/")[2]
        print(domain)
        domain = domain.split(".")[0]
        print(domain)
    else:
        domain = url.split(".")[0]
        print(domain)
    return domain

#remove all the string after comment marker (!, #)
#any whitespace at the end should also be removed
def strip_comments(strng, markers):
    result = []
    
    for line in strng.splitlines():
        for m in markers:
            line = line.split(m, 1)[0]
        result.append(line.rstrip())
    return "\n".join(result)
