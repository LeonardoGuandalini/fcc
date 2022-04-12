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
