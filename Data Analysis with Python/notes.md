### Calculator

#### Main points

* An array (list) is not the same as a numpy array. A list can be converted to a numpy array using the np.array() function and a numpy array can be converted to a list using the .tolist() method
* It is possible to conveniently reshape a numpy array with the .reshape(dim, dim) method
* Numpy objects provide convenient functions such as mean, var, std, max, min and sum. It is necessary to specify an axis for it to work according to want is desired. axis=0 ==> lines; axis=1 ==> columns; nothing ==> uses entire array


### Demographic Data Analyzer

#### Main points

* Pandas has two fundamental data structures: DataFrames and Series'. A DataFrame is made up of Series'.
* A Series is a column of a DataFrame and can be accessed through df['name of column'], returning a Series object
* The value_counts() method is very useful, since it retrieves summarized data in a grouped manner. It also returns a Serires object
* The .sum() method can be used with value_counts() to return the total number of something as int64 type. This datatype provides the .round() method, that rounds a decimal to the desired form.
* It is possible to conditionally select data. Use the & (and) or | (or) operators.

### Medical Data Analyzer

#### Main points

* List comprehension can be really useful when adding new columns to a DataFrame, although the process can be quite confusing sometimes
* There also exists Dictionary Comprehension, which is equally useful for repetitive tasks
* pd.melt() transforms a long horizontal table into a very long vertical table according to a column.
* Categorical Data can be understood as data which is represented by a finite set of values (like 1 or 0, for example)
* the DataFrame.drop() method is commonly used to delete columns. However, it can be used to delete specific lines according to some rule by passing the indexes. It will delete all lines which return true to the condition inside the method.
* DataFrames have a method called corr() which will calculate the correlation between the existing variables. 
* The np.triu_indices_from() or np.tril_indices_from() functions are really useful for creating triangular matrices, since they return de indices from the upper or lower triangle, respectivelly.
* The DataFrame.quantile() method returns all values that are withing the determined quantile

#### Useful tools for other projects
* It is possible to get 2 values from a for loop using a function called zip. For instance, when creating a new column that depends on two already existing columns, one can use:

```python
for x, y in zip(column1, column2)
```


