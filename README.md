### Python_recommendation

##### Selects all products from the input table that satisfies all of the given list of conditions.
##### Input: 
Table of products with all the features (products), list of conditions and each of condition contains integer feature index, symbol and feature value (conditions)
##### Output: 
List of all input products that satisfy all the input conditions
##### For example:
- phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],['Galaxy S20', 'Samsung', 6.2, 4000, 1348],['Nova 5T', 'Huawei', 6.26, 3750, 497],['V40 ThinQ', 'LG', 6.4, 3300, 598],['Reno Z', 'Oppo', 6.4, 4035, 397]]
- selection(phones, [(1, '!=', 'Apple')])
[['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Reno Z', 'Oppo', 6.4, 4035, 397]]
- selection(phones, [(4, '<=', 400), (2, '>=', 6.3)])
[['Reno Z', 'Oppo', 6.4, 4035, 397]]
