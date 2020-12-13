import pandas as pd
path = r'I:\Data\Personal Data\graduation project\SACOL\Balloon\2007\UPAR200706.csv'
draw_print = pd.read_csv(path)
print(draw_print)
draw_print.drop(draw_print.index, inplace=True)
print(draw_print)