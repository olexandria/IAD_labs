import matplotlib.pyplot as plt

def graphic(df, col):
    if col == 'Humidity':
        x = list(df.index.values)
        y = list(df[col])
        df[col].plot.area()
        plt.ylabel(col)
        plt.xticks(rotation=90)
        plt.legend()
        plt.show() 
    elif col == 'Wind' or col == 'Condition':
        x = list(df.index.values)
        y = list(df[col])
        plt.scatter(x,y, label=col)
        plt.xticks(rotation=90)
        plt.ylabel(col)
        plt.legend()
        plt.show()
    elif col == 'Pressure' or col == 'Precip.' or col == 'Precip Accum':
        x = list(df.index.values)
        y = list(df[col])
        df[col].plot.line()
        plt.ylabel(col)
        plt.xticks(rotation=90)
        plt.legend()
        plt.show() 
    else:
        x = list(df.index.values)
        y = list(df[col])
        plt.scatter(x,y, label=col)
        plt.xticks(rotation=90)
        plt.ylabel(col)
        plt.legend()
        plt.show()

def show(df,columns):
    for col in columns:
            graphic(df, col)
