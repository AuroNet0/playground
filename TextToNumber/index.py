numberByUnits = {
    "zero": 0, "um": 1, "dois": 2, "tres": 3, "quatro": 4, 
    "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9,
}

numbersByDozensAndAssistants = {
    "e": 0, "dez": 10, "onze": 11, "doze": 12, "treze": 13, "quatorze": 14, 
    "quinze": 15, "dezesseis": 16, "dezessete": 17, "dezoito": 18, 
    "dezenove": 19, "vinte": 20, "trinta": 30, "quarenta": 40, 
    "cinquenta": 50, "sessenta": 60, "setenta": 70, "oitenta": 80, "noventa": 90,
}

numberByHundreds = {
    "cento": 100, "cem": 100, "duzentos": 200, "trezentos": 300, 
    "quatrocentos": 400, "quinhentos": 500, "seiscentos": 600, 
    "setecentos": 700, "oitocentos": 800, "novecentos": 900,
}

full_number_map = {
    **numberByUnits,
    **numbersByDozensAndAssistants,
    **numberByHundreds
}


def convertTextToNumber ():
    inputTextValue = str(input("Digite um valor no formato escrito: "));

    if(inputTextValue.count(' ') > 0):
        result = findNumberWithSpace(inputTextValue)
        print("O valor digitado é: ", result)
    else:
        result = findNumberWithoutSpace(inputTextValue)
        print("O valor digitado é: ", result)

def findNumberWithoutSpace (inputTextValue):
    for key,value in full_number_map.items():
        if (key == inputTextValue ):
            return value

def findNumberWithSpace (inputTextValue):
    textNumbersList = inputTextValue.split(' ')
    resultSum = 0
    for number in textNumbersList:
        searchResult = findNumberWithoutSpace(number)
        resultSum += searchResult
    return resultSum

convertTextToNumber()