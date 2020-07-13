import querys




def relative_freq(username):
    '''
    This function returns a number between 0 and 1 that is named relative frequency. After,  realize a conversion to numbers between 0 and 4 for use in the  heatmap development in ReactJS 
    '''

    total= querys.countIntancesPending(username)[0]
    done = querys.countIntancesDone(username)[0]

    if total == 0:
        return f'No hay registros'
    else:
        score = done / total  

        if score == 0:
            return 0
        elif score > 0 and score <= 0.25:
            return 1
        elif score > 0.25 and score <= 0.5:
            return 2
        elif score > 0.5 and score <= 0.75:
            return 3
        else:
            return 4




def array_score(username):
    '''
    Return elements in a dictionary for use as json object
    '''
    score_list=[]
    tupla_username = querys.allScore(username)
    scale=tupla_username[0]
    date=tupla_username[1].strftime('%Y/%m/%d')

    new_score= {'date': date , 'count': scale}
    score_list.append(new_score)
    return score_list

