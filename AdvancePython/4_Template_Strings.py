'''
***************TEMPLATE STRING**********************
'''
#need security with format string, dont know the source 

from string import Template

def main():
    #Usual string formatting with format()
    str1 = "You're practising {0} from {1}".format('Python','YouTube')
    print(str1)

    #Create a template with placeholder
    templ=Template("You're practising ${lang} from ${src}")


    #Use the substitution method with keyword arguments
    str2 = templ.substitute(lang="Python",src = "Youtube")
    print(str2)


    #use the substition method with a dictionary 
    data = {
        "lang":"Python",
        "src":"Youtube"
    }
    str3 = templ.substitute(data)
    print(str3)

if __name__ == '__main__':
    main()
