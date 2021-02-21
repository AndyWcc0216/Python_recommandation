def inferred_conditions(pos_ex, neg_ex):
    """
    According to the user feedback on the individual products ('like'/'dislike'), the function will categorise other products as either interesting or not interesting for the same user.

    Input : a list of products(pos_ex)that the user likes, a list of products(neg_ex)that the user dislikes, both based on the same feature columns.
    Output : a list of conditions that contains a range which can include all the user like products(pos_ex) and less dislike products(neg_ex) within this range.

    For example:
    >>> pos_ex = [['iPhone11', 'Apple', 6.1, 3110, 1280],['Nova 5T', 'Huawei', 6.26, 3750, 497],['V40 ThinQ', 'LG', 6.4, 3500, 800]]
    >>> neg_ex = [['Galaxy S20', 'Samsung', 6.46, 3000, 1348],['V40 ThinQ', 'LG', 5.8, 3100, 598],['7T', 'OnePlus', 6.3, 3300, 1200]]
    >>> new_phones = [['Galaxy S9', 'Samsung', 5.8, 3000, 728],['Galaxy Note 9', 'Samsung', 6.3, 3600, 700],['A9 2020', 'Oppo', 6.4, 4000, 355]]
    >>> conds = inferred_conditions(pos_ex, neg_ex)
    >>> conds
    [(2, '>=', 6.1), (3, '>=', 3110), (2, '<=', 6.4)]
    >>> selection(pos_ex, conds)
    [['iPhone11', 'Apple', 6.1, 3110, 1280], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3500, 800]]
    >>> selection(neg_ex, conds)
    [['7T', 'OnePlus', 6.3, 3300, 1200]]
    >>> selection(new_phones, conds)
    [['Galaxy Note 9', 'Samsung', 6.3, 3600, 700], ['A9 2020', 'Oppo', 6.4, 4000, 355]]

    The function solves the problem of finding the condition which include all the products that the user likes, as less as possible(pos_ex) for the products that the user dislike(neg_ex).
    The challenge of this task is to find the x-axis and y-axis of the condition when there is more than two feature at the same time.
    i.e. there are screen size, phone battery and prices in the given example.
    Therefore, the first thing I do is to compare the same feature of different products and find out the maximun value and minimum value for the specific feature.
    After finding all the maximum and minimun of different feature, set the maximun and minimun as a range and find out which two features contain the less dislike products(neg_ex) within this range.
    The two features that contain the less dislike products(neg_ex) will become our x-axis and y-axis.
    After finding the x-axis and y-axis, set the condition by finding the maximun and minimun of these two features which we have done previously.
    Importantly, we have to figure out whether there is a limitation for the range of condition.
    i.e. In the above example, the user likes the battery size from 3110 to 3750, but in the dislike product(neg_ex), he do not mention he does not like the battery size (3000,3100,3300) which is larger than 3750.
    Thus, we cannot assume the range of battery size from 3110-3750 and should be from 3110-unlimited.
    Therefore to solve this problem, we have to set two for-loop to check whether there are features that the user dislikes is larger than the maximun of the user likes.
    If so, the maximun does not change. Else, we set the range to unlimit.

    In my implementation, the first i do is to filter out all the feature other than data(integer or float) and record their integer into the data list by using the for-loop function.
    If there is only two data, we can just set these two features be p1 and p2.
    However, when there is more than two features, we have to filter them until two features remain.
    By using the double for-loop function, the outer for-loop is looping all the features and set 0 into a list called include_neg which is used to calculate how many dislike products(neg_ex) is within the range of like products(pos_ex).
    After that, the first inner for-loop is to find the maximum and minimun of the specific feature and the second inner for-loop is to count for how many dislike products(neg_ex) inside this feature.
    We choose the the two features that contain the less dislike products(neg_ex) to be p1 and p2 and use another two for-loop to find the maximun and minimun of these two features.
    After all, we have to check whether there is limitation for the feature condition.
    i.e. In the above example, the user likes the battery size from 3110 to 3750, but in the dislike product(neg_ex), he do not mention he does not like the battery size (3000,3100,3300) which is larger than 3750.
    Thus, we cannot assume the range of battery size from 3110-3750 and should be from 3110-unlimited.
    To find the limitation, we have to set the different feature(x_Check, y_Check) be True(means no limitation) at the begin and use for-loop to
    check whether there is value of dislike products(neg_ex) of the specific feature is larger than the maximun value of the like product(pos_ex) of this feature.
    If there is value value of dislike products(neg_ex) of the specific feature larger than the maximun value of the like product(pos_ex) of this feature, we turn the check to False.
    Finally, we append the maximum and minimun of the two feature into the result_condition and if the x_Check or y_Check is True, we do not need to append the corresponding maximum of feature into the result_condition.
    Return the conditions by returning the result_condition

    The worst case computational complexity of the function is O(p*f + n*f) where f is the number of features other than string features i.e. brand and phone model, p is the number of products that the user likes(pos_ex)
    and n is the number of products that the user dislikes(neg_ex)
    This complexity is caused by the cheking which of the two features can be the x-axis and y-axis of the graph, and there are two parts to achieve this purpose
    first is to find the maximun and minimun value of each specific features which takes time O(p*f) and checking how many dislike products(neg_ex)inside this range takes time O(n*f).
    The complexity of worst case and best case of this function is the same and with that the worst-case complexity can be stated O(n**2), which is simpler but arguably less informative.
    """
    data=[]

    for i in range(len(pos_ex[0])):
        if isinstance(pos_ex[0][i],int) or isinstance(pos_ex[0][i],float):
            data.append(i)

    p1 = data[0]
    p2 = data[1]

    if len(data)>2:
        include_neg=[]
        
        for i in range(len(data)):
            include_neg.append(0)
            Min = pos_ex[0][data[i]]
            Max = pos_ex[0][data[i]]

            for j in range(1, len(pos_ex)):
                if (pos_ex[j][data[i]] < Min):
                    Min = pos_ex[j][data[i]]
                elif (pos_ex[j][data[i]] > Max):
                    Max = pos_ex[j][data[i]]

            for k in range(len(neg_ex)):
                if neg_ex[k][data[i]] >= Min and neg_ex[k][data[i]] <= Max:
                    include_neg[i]+=1

        p1 = data[include_neg.index(min(include_neg))]
        include_neg[include_neg.index(min(include_neg))]=999999
        p2 = data[include_neg.index(min(include_neg))]

    x1=pos_ex[0][p1]; x2=pos_ex[0][p1]

    y1=pos_ex[0][p2]; y2=pos_ex[0][p2]

    for i in range(1,len(pos_ex)):
        if(pos_ex[i][p1]<x1):
            x1=pos_ex[i][p1]
        elif(pos_ex[i][p1]>x2):
            x2=pos_ex[i][p1]

    for i in range(1,len(pos_ex)):
        if(pos_ex[i][p2]<y1):
            y1=pos_ex[i][p2]
        elif(pos_ex[i][p2]>y2):
            y2=pos_ex[i][p2]
            
    x_Check=True; y_Check=True

    for i in range(len(neg_ex)):
        if(neg_ex[i][p1] >= x2):
            x_Check=False
    for i in range(len(neg_ex)):
        if(neg_ex[i][p2] >= y2):
            y_Check=False

    result_conditions = []

    result_conditions.append((p1,'>=',x1))
    result_conditions.append((p2,'>=',y1))

    if(x_Check is False):
        result_conditions.append((p1,"<=",x2))
    if(y_Check is False):
        result_conditions.append((p2,"<=",y2))

    return result_conditions

def satisfies(product, cond):
    """
    Determines whether a product satisfies an individual condition.

    Input : List with different product features (product), condition with integer feature index, symbol and feature value (cond)
    Output : True if condition holds for the product otherwise False.

    For example:
    >>> satisfies(['Nova 5T', 'Huawei', 6.26, 3750, 497],(4, '<=', 1000))
    True
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280],(2, '>=', 6.3))
    False

    The problem for this task is to find the meaning of the symbol also need find the product features accoding to the given index in the input.
    Therefore, double brackets are needed to find the corresponding index in the product list according to the cond.
    Also if, elif ,else function is needed for finding the meaning of the symbol and undergo the arithmetic operation according to the cooresponding symbol

    In my implementation, I choose to use if,elif and else function to explain the symbol and to determine whether the product is satisfies the condition.
    For finding the index we need of product, I choose to use product to blanket the cond with the first index which is the product index we need.
    I choose Boolean to show whether the product is satisfies the condition.
    This solution allows a comprehensive code which can cope with different conditions.
    """
    if cond[1] == '<=':
        if product[cond[0]] <= cond[-1]:
            return True
        else:
            return False
    
    elif cond[1] == '<':
        if product[cond[0]] < cond[-1]:
            return True
        else:
            return False
    elif cond[1] == '>=':
        if product[cond[0]] >= cond[-1]:
            return True
        else:
            return False
        
    elif cond[1] == '>':
        if product[cond[0]] > cond[-1]:
            return True
        else:
            return False
        
    elif cond[1] == '==':
        if product[cond[0]] == cond[-1]:
            return True
        else:
            return False
        
    elif cond[1] == '!=':
        if product[cond[0]] != cond[-1]:
            return True
        else:
            return False

def selection(products, conditions):
    """
    Selects all products from the input table that satisfies all of the given list of conditions.

    Input : Table of products with all the features (products), list of conditions and each of condition contains integer feature index, symbol and feature value (conditions)
    Output : List of all input products that satisfy all the input conditions

    For example:
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],['Galaxy S20', 'Samsung', 6.2, 4000, 1348],['Nova 5T', 'Huawei', 6.26, 3750, 497],['V40 ThinQ', 'LG', 6.4, 3300, 598],['Reno Z', 'Oppo', 6.4, 4035, 397]]
    >>> selection(phones, [(1, '!=', 'Apple')])
    [['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Reno Z', 'Oppo', 6.4, 4035, 397]]
    >>> selection(phones, [(4, '<=', 400), (2, '>=', 6.3)])
    [['Reno Z', 'Oppo', 6.4, 4035, 397]]

    This is a table processing problem where input table contains unknown types of products.
    This means that a loop is required to iterate over all rows of the table and determine whether types of products meet all the conditions.
    Also, the input list contains unknown types of conditions.
    Thus, a loop is required to iterate over all elements and determine whether types of products meet all the conditions.
    Importantly, according the specification, the result has to show inside a list.
    Therefore, the function has to provide a new list and the output has to be accumulated in the new list.

    In my implementation, I choose to iterate over the input table and input list with a for-loop, for running each row of the products first and the different conditions.
    To test whether the input table can satisfy the conditions, the satisfies function of pervious task can be re-use.
    Therefore, I import the satisfies function from Task1A_satisfies and put the result of each row of product with the conditions by using the append function into a new list called results.
    To check whether the row of product can meet all the conditions, I use if, not and in function to check whether there are any False cases in the results list.
    If all the cases show True, then I will put this row of product into the a new list called final_result by append function.
    This solution allows a comprehensive and concise code which can cope with unknown size of product and condition.
    """
    final_results=[]
    
    for i in range(len(products)):
        results = []
        for j in range(len(conditions)):
            result = satisfies(products[i],conditions[j])
            results.append(result)
        if(False not in results ):
            final_results.append(products[i])

    return final_results

